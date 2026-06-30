
SKILL_METADATA = {
    "name": "agent_warmup.context_loader",
    "description": "Inyecta contexto de dominio especializado en agentes LLM. Soporta ecotoxicología.",
    "input": "domain: str",
    "output": "dict con system_context, messages, domain",
    "domain": ["research", "engineering", "ecotoxicology_nanomaterials"],
    "version": "1.0.0"
}

DOMAIN_CONTEXTS = {
    "research": "Eres un asistente de investigación científica...",
    "engineering": "Eres un ingeniero de software senior...",
    "ecotoxicology_nanomaterials": """Eres un experto mundial en ecotoxicología de nanomateriales.
1. Evalúa de forma sistemática parámetros fisicoquímicos (tamaño, solubilidad) y su efecto en toxicidad.
2. Clasifica el riesgo basándote en la evidencia de toxicidad para organismos modelo estandarizados.
3. Cita explícitamente pautas de regulación (ej. OECD Test Guidelines para nanomateriales).
4. Mantén un estricto rigor científico, proporcionando recomendaciones conservadoras basadas en evidencia."""
}

def list_available_domains(): return list(DOMAIN_CONTEXTS.keys())

def warm_up(domain: str, custom_config=None):
    from langchain_core.messages import SystemMessage
    context = DOMAIN_CONTEXTS.get(domain, f"Eres un experto en {domain}")
    return {"domain": domain, "system_context": context, "messages": [SystemMessage(content=context)]}

def warm_up_agent(domain: str): return warm_up(domain)["system_context"]
