from agents import Runner,OpenAIChatCompletionsModel,AsyncOpenAI, RunConfig,Agent
from dotenv import load_dotenv,find_dotenv
import os
import chainlit as cl

load_dotenv(find_dotenv())

# setting up gemini key
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
#runtime configuration
runtime_config = RunConfig(
    model = model,
    model_provider=provider,
    tracing_disabled=True
    )

agent = Agent(
    name = "Assistant",
    instructions="You are a helpful assistant",
    model=model
        )

# result =Runner.run_sync(agent,"Who is the founder of Pakistan",run_config = runtime_config)
# print(result.final_output)

@cl.on_chat_start
async def main():
    """Set up the chat session when a user connects."""
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])
    #set configuration in session
    cl.user_session.set("config", runtime_config)
    # set agent 
    cl.user_session.set("agent", agent)
    # automatic first message of assistant
    await cl.Message(content="Hy I am Amna's AI Assistant! How can I help you today?").send()

@cl.on_message
async def handle_message(message : cl.Message):
    # creating history 
    history = cl.user_session.get("chat_history")
    #storing question of user in a variable
    msg = cl.Message(content="")
    await msg.send()
    #adding user's questions in session 
    history.append({"role":"user","content":message.content})

    #setting runtime configuration 
    result = Runner.run_streamed(
        agent,
        input = history,
        run_config=runtime_config
        )
    #looping events of a responce to get answer
    async for e in result.stream_events():
        if e.type == "raw_response_event" and hasattr(e.data, 'delta'):
            await msg.stream_token(e.data.delta)
    
    #storring agents responce in session history
    history.append({"role":"assistant","content":result.final_output})
    #getting final history
    cl.user_session.get("chat_history",history)



