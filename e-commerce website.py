import asyncio
import json
import os

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

print("SHIVA")

class validation_ecoomerce(BaseModel):
    login_status:str
    cart_status:str
    checkout_status:str
    total_update_status:str
    pincode_status:str
    confirmation_message:str

controller = Controller(output_model=validation_ecoomerce)
async def ecommerce():
    os.environ['gemini_api_key'] = 'use api key here with respect to the model'
    task='important:i am automation tester and will perform automation tasks'\
         'open this website it is e-commerce website https://www.saucedemo.com/'\
         'in this page we have different usernames and password are there and use any username and use password to login the page'\
         'after filling  the details click on login button'\
         'after login any pop-up comes click on ok'\
         'Add first 2 products in the cart'\
         'Then click on cart showing in symbol'\
         'Then click on checkout'\
         'Then give first name,last name as username while login,give pincode as 500045'\
         'Then click on continue'\
         'Then click on Finish'\
         'Then verify  Thank you for your order'\
         'Then click on Bach home'
    api_key = os.environ['gemini_api_key']
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=api_key)
    agent = Agent(task=task,llm=llm,controller=controller,use_vision=True)
    history = await agent.run()
    test = history.final_result()
    print(test)

    result_dict = json.loads(test)
    test = validation_ecoomerce(**result_dict)
    print(test)
    assert test.confirmation_message == 'Thank you for your order'

asyncio.run(ecommerce())

