from google.adk.agents.llm_agent import Agent
from .prompt import CONTRACT_ANALYST_INSTRUCTION

contract_analyst_agent = Agent(
    model='gemini-2.5-flash',
    name='ContractAnalyst',
    description='Analista experto en comparar y evaluar contratos públicos.',
    instruction=CONTRACT_ANALYST_INSTRUCTION,
)
