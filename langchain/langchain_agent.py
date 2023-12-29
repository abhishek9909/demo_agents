from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import AzureChatOpenAI
llm = AzureChatOpenAI( 
    openai_api_key="<<open_ai_key>>",
    azure_endpoint="<<azure_endpoint>>", 
    deployment_name="<<deployment_name>>", 
    openai_api_version="<<api_version>>", 
    openai_api_type="azure")

from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.tools.playwright.utils import (
    create_sync_playwright_browser
)

sync_browser = create_sync_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
tools = toolkit.get_tools()
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,    
)

def main():
    while True:
        user_input = input("Please enter ask (use 'exit' to end conversation)")
        if user_input.lower() == 'exit':
            print("Exiting the program")
            break
        result = agent_chain.run(user_input)
        print("result: ", end = " ")
        print(result)

if __name__ == "__main__":
    main()