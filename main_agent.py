"""
Módulo de inicialización cognitiva del agente.
Define metadatos y el System Prompt para garantizar el rigor científico en la evaluación ecotoxicológica.
"""

# Constante obligatoria para el registro de Skills
SKILL_METADATA = {
    'name': 'EcotoxRiskEvaluator',
    'version': '1.0.0',
    'description': 'Contextualización y evaluación de riesgo ecotoxicológico de nanomateriales basada en guías OCDE.'
}

def warm_up(domain: str) -> str:
    """
    Inicializa el System Prompt forzando al modelo a actuar como un toxicólogo experto.
    
    Args:
        domain (str): Dominio de aplicación (ej. 'Nanotoxinas Acuáticas').
        
    Returns:
        str: System Prompt formateado.
    """
    # OWASP: Sanitización básica de inputs del dominio para evitar inyección de prompt
    clean_domain = domain.strip().replace("{", "").replace("}", "")
    
    return f"""Eres un toxicólogo experto adscrito a las normativas y guías de la OCDE para la evaluación de nanomateriales.
Tu campo de especialización es: {clean_domain}.

En tu análisis debes considerar rigurosamente los siguientes descriptores fisicoquímicos:
1. Área superficial (reactividad)
2. Potencial zeta (estabilidad coloidal)
3. Endpoints toxicológicos (como CL50/LC50)

Todas tus respuestas deben estar fundamentadas científicamente y debes consultar tus herramientas para extraer métricas empíricas antes de generar una conclusión de clasificación de riesgo.
"""


    Returns:
        El mismo agente_instance con el contexto aplicado.
    """
    ctx = warm_up(domain)
    system_context = ctx["system_context"]

    if hasattr(agent_instance, "system_message"):
        agent_instance.system_message = system_context
    elif hasattr(agent_instance, "backstory"):
        current = getattr(agent_instance, "backstory", "")
        agent_instance.backstory = f"{current}\n\n{system_context}".strip()

    return agent_instance
