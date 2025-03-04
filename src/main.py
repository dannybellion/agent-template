from pydantic_ai import Agent
from pydantic import BaseModel
from functions import load_prompt, get_model
from snowflake import SnowflakeConnection
from hubspot import HubspotClient
import nest_asyncio

nest_asyncio.apply()


# Setup the main agent


class ModelResponse(BaseModel):
    BDM: str
    Reasoning: str


system_prompt = "You are a sales attribution specialist"

model = get_model("gpt-4o")

agent = Agent(model, system_prompt=system_prompt, result_type=ModelResponse)

# Get the data from the database

snowflake = SnowflakeConnection()

query = """
SELECT * FROM XXX
"""

camelot_data = snowflake.fetch_query(query)

# Get the data from the Hubspot API

hubspot = HubspotClient()

hubspot_data = hubspot.get_recent_calls(limit=3)

# Run the prompt

prompt = load_prompt(hubspot=hubspot_data, camelot=camelot_data)

response = agent.run_sync(user_prompt=prompt)

response.data
