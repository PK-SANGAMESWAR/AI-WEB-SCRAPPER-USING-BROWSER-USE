import asyncio
from bubus.helpers import P
from dotenv import load_dotenv
from browser_use.llm import ChatGoogle
from browser_use import Agent, BrowserSession,Controller
from pydantic import BaseModel
from typing import List

# Load API key from .env
load_dotenv()

# Initialize the model
llm = ChatGoogle(model='gemini-2.0-flash-exp')

class Post(BaseModel):
    caption:str
    url:str

class Posts(BaseModel):
    posts:List[Post]

controller = Controller(output_model=Posts)


async def main():
    # Start a browser session (Chromium or Chrome)
    browser = await BrowserSession.create(
        executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'  # Optional
    )

    agent = Agent(
    task="Go to sangameswar_ instagram post and grab the most recent post captions",
    llm=llm,
    browser=browser,  # Added comma here
    controller=controller
)


    result = await agent.run()
    print(result.final_result)

    await browser.close()

# Run the async main
asyncio.run(main())
