import asyncio
import chainlit as cl
import os
from dotenv import find_dotenv,load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,RunConfig,Runner,set_tracing_disabled

set_tracing_disabled(True)

#setting API Key
load_dotenv(find_dotenv())
gemini_key = os.environ.get("GEMINI_API_KEY")

#setting provider
external_client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

#setting model of provider
model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client=external_client
    ) 

#setting configuration 
config = RunConfig(
    model=model,
    model_provider=external_client
    )

@cl.on_message
async def main(message : cl.Message):
    agent = Agent(
        name = "Assistant",
        instructions= "You are an assistant of jewellery designer",
        model= model
        )
    res=await Runner.run(agent,input=message.content,run_config = config)
    await cl.Message(content=res.final_output).send()
    # print(res.final_output)


if __name__ == "__main__":
    asyncio.run(main())
