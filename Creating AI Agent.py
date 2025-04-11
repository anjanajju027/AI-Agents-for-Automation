import os

import asyncio
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel

print("govindha")

class loginpage(BaseModel):
    login_status:str
    submit_button:str
    confirmation_message:str
    logged_out:str


controller = Controller(output_model=loginpage)
async def validation():
     os.environ["Gemini_api_key"]="use gemini api key here"

     task =('important: i am Automation Tester validating the Automation tasks'
       'open the page https://practicetestautomation.com/practice-test-login/'
       'login with username and password and details are given the same page'
       'After clicking submit Check Logged in Successfully message'
        'Then click on Logout button'
       )
     api_key = os.environ["Gemini_api_key"]
     llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
     agent = Agent(task=task,llm=llm,controller=controller,use_vision=True)
     history = await agent.run()
     text = history.final_result()
     print(text)


asyncio.run(validation())



'''
while creating the AI agent we need to install some packages
langchai-openAI,pydantic,googlegenerativiai,browser-use
agent takes 2 aruguments 1 is task and 2 is intellgence
we need to give exact task to perform 
why we use pydantic- to see the results in json so that we can start asssert validations
api_key will need to take different intellgence models like openAI,Gemini,ollama,claude
'''