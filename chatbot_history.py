import asyncio
import chainlit as cl
import os
from dotenv import find_dotenv,load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,RunConfig,Runner

#setting API Key
load_dotenv(find_dotenv())
gemini_key = os.environ.get("GEMINI_API_KEY")

#provider
provider = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

#model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
    )

#config
agent_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
    )

# setting up agent with chainlit
agent1=Agent(
        name="chatot",
        instructions="You are an assistant who knows each and every thing ",
        model=model
        )

@cl.on_chat_start 
async def startup(): 
    #creating history
    cl.user_session.set("history",[])
    await cl.Message(content = "Hello I'm a Custom Made Support agent.How may I help You?").send()
    # print("Application is starting!") # Initialize resources here

@cl.on_message
async def messaging(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({
        "role":"user",
        "content" : message.content
        })
    
    result1= await Runner.run(
        agent1,
        input=message.content,
        run_config=agent_config
        )
    history.append({
            "role":"assistant",
            "content": result1.final_output
            })
    cl.user_session.set("history",history)
    await cl.Message(content=result1.final_output).send()
    print(history )