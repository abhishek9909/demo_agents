from tools import create_updated_tools
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
## ConversationSummaryMemory,
from langchain.prompts import MessagesPlaceholder

llm = AzureChatOpenAI( 
    openai_api_key="6f3ab983d07d4599abe7a52266fbe141",
    azure_endpoint="https://gcs-jobrec-openai-ncus-ppe.openai.azure.com", 
    deployment_name="gpt-35-turbo-16k", 
    openai_api_version="2023-09-01-preview", 
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
