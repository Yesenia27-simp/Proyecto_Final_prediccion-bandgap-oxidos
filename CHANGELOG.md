# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] - 2026-04-11

### Added

- **U5_04_GOOGLE_ADK_A2A_COMP_GEMMA4.ipynb** — Notebook Unit 5, Leccion 4: Google ADK 1.0 con protocolo A2A y Gemma4. Incluye: LlmAgent, SequentialAgent, ParallelAgent, LoopAgent, BuiltInCodeExecutor, BaseTool con Pydantic, checkpoints de sesion, AgentCard A2A, cliente cross-framework con Bearer token, y fallbacks locales para cuota agotada.

---

## [1.0.0] - 2026-04-08

### Added

- **Unidad 1** — Introduccion a IA y simulacion molecular (notebooks + README)
- **Unidad 2** — Machine Learning para prediccion de propiedades de materiales
- **Unidad 3** — Redes neuronales: fundamentos y arquitecturas (FUNDAMENTOS + PARTE2)
- **Unidad 4** — Modelos avanzados y transfer learning en nanotecnologia
- **Unidad 5** — Sistemas multi-agente: LangChain, CrewAI, Google ADK, SmolaAgents
- **Unidad 6** — DevOps/Cloud para IA cientifica: despliegue, monitoreo, CI/CD
- `external_skills/` — 9 modulos reutilizables: `context_loader`, `task_classifier`, `output_scorer`, `episodic_retriever`, `trace_annotator`, `token_budget_guard`, `toxicity_predictor`, `librarian_rag`, `socratic_debugger`
- `pyproject.toml` — proyecto instalable con `pip install -e ".[dev]"`
- GitHub Actions CI workflow — ejecuta 83 tests en cada push a `main`
- 83 tests automatizados cubriendo `external_skills` y logica de unidades
- `CONTRIBUTING.md`, `GOVERNANCE.md`, `SKILLS_ATTRIBUTION.md`
- `.gitignore` completo: artefactos `.onnx`, carpetas `tmp/`, scripts de desarrollo

### Fixed

- Encoding UTF-8 en `UNIDAD_3_FUNDAMENTOS_REDES_NEURONALES.ipynb` (caracteres en espanol)
- CI ahora usa `pip install -e ".[dev]"` en lugar de dependencias manuales

### Notes

- Los modulos `toxicity_predictor`, `librarian_rag` y `socratic_debugger` son implementaciones
  educativas/mock; no requieren APIs externas.
- `unit_05/requirements.txt` contiene versiones validadas en marzo 2026.

[1.0.0]: https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core/releases/tag/v1.0.0
