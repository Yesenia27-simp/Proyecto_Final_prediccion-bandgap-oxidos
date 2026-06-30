import os
import sys
from pathlib import Path
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Ajustar PYTHONPATH para poder importar nuestras herramientas sin problemas
sys.path.append(str(Path(__file__).parent))

from external_skills.tools.tox_tools import calcular_indice_riesgo, consultar_umbral_toxicidad
from external_skills.agent_warmup.context_loader import warm_up

# 4. CONFIGURACIÓN CIENTÍFICA (Hiperparámetros)
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    top_p=0.1,
    max_tokens=512,
    model_kwargs={"seed": 1234} 
)

# 1. Recuperamos y montamos la personalidad científica
contexto_cientifico = warm_up("Ambientes Acuíferos y Nanomateriales Metálicos")

# 3. ORQUESTACIÓN DEL AGENTE (ReAct)
herramientas_agente = [calcular_indice_riesgo, consultar_umbral_toxicidad]

# Definición del Prompt estilo ReAct
prompt_template = f"""{contexto_cientifico}

Tienes acceso a un ecosistema de herramientas experimentales empíricas para ayudarte a dictaminar:

{{tools}}

Para estructurar tu razonamiento deductivo, usa obligatoriamente el siguiente formato:

```
Thought: Tengo que pensar qué paso tomar basado en la evidencia
Action: El nombre de la herramienta a utilizar, el cual debe ser una de [{{tool_names}}]
Action Input: El parámetro(s) de entrada para la herramienta seleccionada
Observation: Los datos matemáticos o base de datos que te arrojó la herramienta
```
(Repite este ciclo Action/Observation hasta estar completamente seguro)

Cuando estés listo para dar un dictamen final (no olvides analizar todo en contexto de Guías OCDE):
```
Thought: Ya tengo toda la información científica necesaria para emitir un fallo toxicológico.
Final Answer: Tu reporte o clasificación final elaborada al usuario.
```

Comenzamos la evaluación:
Pregunta/Caso de estudio: {{input}}
{{agent_scratchpad}}"""

react_prompt = PromptTemplate.from_template(prompt_template)

# Instanciación y ejecución principal
agente = create_react_agent(llm, herramientas_agente, react_prompt)

# Executor con límites contra loops infinitos
agente_executor = AgentExecutor(
    agent=agente, 
    tools=herramientas_agente, 
    verbose=True,           
    max_iterations=5,       
    handle_parsing_errors=True
)

if __name__ == "__main__":
    # CASO DE PRUEBA PRÁCTICO
    caso_estudio = (
        "Analiza el siguiente compuesto artificial: AgNP. "
        "Las medidas empíricas en el laboratorio indican tener un área superficial de 25.5 m2/g "
        "y una solubilidad detectada de 1.2 mg/L. "
        "Aplica tus herramientas para calcular el riesgo e investigar sus umbrales para darme tu dictamen final de toxicidad."
    )
    
    print("=== INICIANDO PIPELINE DE EVALUACIÓN MULTI-AGENTE ===")
    try:
        resultado = agente_executor.invoke({"input": caso_estudio})
        print("\n--- INFORME TOXICOLÓGICO CLASIFICADO ---")
        print(resultado["output"])
    except Exception as e:
         print(f"Error en la ejecución: Asegúrate de tener tu OPENAI_API_KEY configurada. Setup requerido. {e}")
