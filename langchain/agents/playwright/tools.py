from typing import cast, List, Type
from pydantic import Field, BaseModel, validator
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.tools.playwright.base import BaseBrowserTool
from langchain_core.tools import BaseTool
from langchain_community.tools.playwright.utils import get_current_page, aget_current_page
from axe_core_python.sync_playwright import Axe
from axe_core_python.async_playwright import Axe as AAxe

def create_sync_playwright_browser():
    browser = sync_playwright().start()
    return browser.chromium.launch(headless=True)

async def create_async_playwright_browser():
    browser = await async_playwright().start()
    launched = await browser.chromium.launch(headless=True)
    return launched

### A new tool to run accessibility checks.
class RunAccessibility(BaseBrowserTool):
    name: str = "accessibility_test"
    description: str = "Conduct accessibility tests for a website using axe tools"
    args_schema: Type[BaseModel] = BaseModel
    
    def _run(self):
        axe = Axe()
        page = get_current_page(self.sync_browser)
        
        ## Run accessiblity checks on a given page.
        results = axe.run(page)
        
        return f"Found {[f'{key}: {value}' for key, value in results.items() if 'violations' in key]} on the site: {page.url}"        
        
    async def _arun(self):
        axe = AAxe()
        page = await aget_current_page(self.async_browser)
        
        ## Run accessibility checks on a given page.
        results = await axe.run(page)
        return f"Found {[f'{key}: {value}' for key, value in results.items() if 'violations' in key]} on the site: {page.url}"
    
### A new tool to extract cookies from a site.
class ExtractCookies(BaseBrowserTool):
    
    name: str = "extract_cookies"
    description: str = "Extract cookies for the current page"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self):
        page = get_current_page(self.sync_browser)
        
        ## cookies present in the site.
        cookies = page.context.cookies()
        
        ## return the list of cookies.
        return f'List of cookies extracted: {", ".join([f"""name: {cookie["name"]}, domain: {cookie["domain"]}""" for cookie in cookies])}'

    
    async def _arun(self):
        page = await aget_current_page(self.async_browser)
        
        ## cookies present in the site.
        cookies = await page.context.cookies()
        
        ## return the list of cookies.
        return f'List of cookies extracted: {", ".join([f"""name: {cookie["name"]}, domain: {cookie["domain"]}""" for cookie in cookies])}'


async def create_updated_tools():
    async_browser = await create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    default_tools = toolkit.get_tools()
    default_tools.extend(cast(List[BaseTool], 
            [tool_cls.from_browser(sync_browser=None, async_browser=async_browser) 
            for tool_cls in [RunAccessibility, ExtractCookies]]))
    return default_tools
