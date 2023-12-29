from tools import create_updated_tools
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
## ConversationSummaryMemory,
from langchain.prompts import MessagesPlaceholder

llm = AzureChatOpenAI( 
    openai_api_key="<<open-ai-key>>",
    azure_endpoint="<<azure-endpoint>>", 
    deployment_name="<<azure-deployment-name>>", 
    openai_api_version="<<api-version>>", 
    openai_api_type="azure"
)

memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
## ConversationSummaryMemory(llm=llm, return_messages=True, memory_key="memory")

agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
}

async def create_custom_agent():
    updated_tools = await create_updated_tools()
    return initialize_agent(
        updated_tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        memory=memory,
        agent_kwargs=agent_kwargs
    )
