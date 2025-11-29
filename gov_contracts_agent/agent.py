from google.adk.agents.llm_agent import Agent
from .prompt import COORDINATOR_INSTRUCTION
from .sub_agents.search_specialist.agent import search_specialist_agent
from .sub_agents.contract_analyst.agent import contract_analyst_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='LicitationCoordinator',
    description='Coordinador principal del sistema de licitaciones.',
    instruction=COORDINATOR_INSTRUCTION,
    sub_agents=[search_specialist_agent, contract_analyst_agent],
)
