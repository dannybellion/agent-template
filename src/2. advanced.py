from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from functions import client, load_context
import nest_asyncio

nest_asyncio.apply()

model = OpenAIModel("gpt-4o", openai_client=client())

### Setup the main agent ###

context = load_context()

main_system_prompt = """
You are a helpful assistant that will help users 
"""

main_agent = Agent(model, system_prompt=main_system_prompt)

### Setup the code agent ###

code_agent_system_prompt = f"""
You are a code generator. 

Here is some context:
{context}
"""

### Setup the code agent ###


@main_agent.tool
def code_generator(ctx: RunContext, text: str):
    """ "
    A tool that will generate code from a text.

    Args:
        text: The text to generate code from.
    """
    code_agent_system_prompt = f"""
You are a code generator. 

Here is some context:
{context}
"""
    code_agent = Agent(model, system_prompt=code_agent_system_prompt)
    return code_agent.run_sync(text).data


### run the user query ###
def run_chat():
    while True:
        print("---------Your Message---------")

        user_input = input()
        if user_input == "\n":
            break

        response = main_agent.run_sync(user_input)

        print("------------------------")
        print("---------Model Working---------")
        print(response.all_messages())
        print("------------------------")
        print("---------Response---------")
        print(response.data)
        print("------------------------")

    print("---------Ended---------")


# Run the chat
run_chat()
