"""external_skills/memory/graph_memory.py
Memoria en grafo para agentes: Graphiti (Zep) con fallback en memoria.
"""
from __future__ import annotations

import os
from typing import Any

SKILL_METADATA = {
    "name": "graph_memory",
    "domain": "memory",
    "description": "Memoria en grafo temporal usando Graphiti/Zep. Fallback en memoria si no disponible.",
    "version": "1.0.0",
    "input": "content: str, episode_id: str, group_id: str",
    "output": "list[dict] con content, episode_id, group_id, score",
    "dependencies": [],
}

# Almacén en memoria cuando Graphiti/Neo4j no está disponible
_IN_MEMORY_STORE: list[dict[str, Any]] = []

# Estado del cliente Graphiti (lazy init)
_graphiti_client = None
_graphiti_available = False
_init_attempted = False


def _get_graphiti_client():
    """Intenta inicializar el cliente Graphiti una sola vez."""
    global _graphiti_client, _graphiti_available, _init_attempted
    if _init_attempted:
        return _graphiti_client

    _init_attempted = True
    try:
        from graphiti_core import Graphiti  # type: ignore

        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_password = os.environ.get("NEO4J_PASSWORD", "")

        if neo4j_password:
            _graphiti_client = Graphiti(
                neo4j_uri=neo4j_uri,
                neo4j_user=neo4j_user,
                neo4j_password=neo4j_password,
            )
            _graphiti_available = True
    except ImportError:
        _graphiti_available = False
    except Exception:
        _graphiti_available = False

    return _graphiti_client


async def warm_up() -> dict[str, str]:
    """
    Inicializa la conexión con Graphiti/Neo4j.

    Returns:
        dict con {status, message}.
    """
    client = _get_graphiti_client()
    if _graphiti_available and client:
        try:
            await client.build_indices_and_constraints()
            return {
                "status": "ok",
                "message": "Graphiti conectado y listo.",
            }
        except Exception as exc:
            return {
                "status": "warning",
                "message": f"Graphiti conectado pero error al inicializar: {exc}",
            }

    return {
        "status": "fallback",
        "message": (
            "Graphiti/Neo4j no disponible. Usando almacén en memoria. "
            "Configura NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD para activar persistencia."
        ),
    }


async def add_episode(
    content: str,
    episode_id: str,
    group_id: str,
) -> None:
    """
    Agrega un episodio al grafo de memoria.

    Args:
        content: Contenido textual del episodio.
        episode_id: Identificador único del episodio.
        group_id: Grupo/sesión al que pertenece.
    """
    client = _get_graphiti_client()
    if _graphiti_available and client:
        try:
            from graphiti_core.nodes import EpisodeType  # type: ignore

            await client.add_episode(
                name=episode_id,
                episode_body=content,
                source=EpisodeType.text,
                group_id=group_id,
            )
            return
        except Exception:
            pass  # Fallback a memoria

    # Fallback: almacén en memoria
    _IN_MEMORY_STORE.append({
        "content": content,
        "episode_id": episode_id,
        "group_id": group_id,
    })


async def search(
    query: str,
    group_ids: list[str] | None = None,
) -> list[dict]:
    """
    Busca episodios relevantes en el grafo de memoria.

    Args:
        query: Query de búsqueda.
        group_ids: Lista de grupos en los que buscar (None = todos).

    Returns:
        Lista de dicts con content, episode_id, group_id, score.
    """
    client = _get_graphiti_client()
    if _graphiti_available and client:
        try:
            results = await client.search(query=query, group_ids=group_ids)
            return [
                {
                    "content": r.fact if hasattr(r, "fact") else str(r),
                    "episode_id": getattr(r, "uuid", ""),
                    "group_id": getattr(r, "group_id", ""),
                    "score": getattr(r, "score", 0.5),
                }
                for r in results
            ]
        except Exception:
            pass  # Fallback a memoria

    # Fallback: búsqueda lineal en almacén en memoria
    query_words = set(query.lower().split())
    results = []
    for ep in _IN_MEMORY_STORE:
        if group_ids and ep.get("group_id") not in group_ids:
            continue
        ep_words = set(ep["content"].lower().split())
        overlap = len(query_words & ep_words)
        score = overlap / max(len(query_words), 1)
        if score > 0:
            results.append({
                "content": ep["content"],
                "episode_id": ep["episode_id"],
                "group_id": ep["group_id"],
                "score": round(score, 3),
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
