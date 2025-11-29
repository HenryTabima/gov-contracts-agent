from google.adk.agents.llm_agent import Agent
from .tools import search_contracts
from .prompt import SEARCH_SPECIALIST_INSTRUCTION

search_specialist_agent = Agent(
    model='gemini-2.5-flash',
    name='SearchSpecialist',
    description='Especialista en buscar contratos públicos en SECOP II.',
    instruction=SEARCH_SPECIALIST_INSTRUCTION,
    tools=[search_contracts],
)
