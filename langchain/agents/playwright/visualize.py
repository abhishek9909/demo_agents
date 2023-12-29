### visualize the langchain execution of a given chain (https://python.langchain.com/docs/modules/chains/).

import langchain_visualizer
import asyncio
from custom_lcel_agent import create_custom_agent

async def custom_agent_demo():
    custom_agent = await create_custom_agent()
    _ = await custom_agent.arun("Extract cookies from twitch site")
    _ = await custom_agent.arun("Get all the hyperlinks there")
    return None

langchain_visualizer.visualize(custom_agent_demo)