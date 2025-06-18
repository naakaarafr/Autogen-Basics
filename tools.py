import autogen
from typing import Annotated
import datetime

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
gemini_api_key = os.getenv('GEMINI_API_KEY')


config_list = [
    {
        'model': 'gemini-2.0-flash',
        'api_key': gemini_api_key,
        'api_type': 'google'
    }
]

llm_config = {
    "config_list": config_list, 
    "seed": 42,
    "temperature": 0.7,
    "timeout": 60
}
def get_weather(location: Annotated[str, "The location"]) -> str:
    if location == "Florida":
        return "It's hot in Florida!"
    elif location == "Maine":
        return "It's cold in Maine"
    else:
        return f"I don't know this place {location}"


def get_time(timezone: Annotated[str, "The timezone we are in"]) -> str:
    now = datetime.datetime.now()

    # Get the time with timezone information
    current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")

    return f"Current time in your {timezone}: {current_time}"


# Let's first define the assistant agent that suggests tool calls.
assistant = autogen.ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
                   "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = autogen.ConversableAgent(
    name="User",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
assistant.register_for_llm(name="get_weather", description="Get the current weather for a specific location")(get_weather)
assistant.register_for_llm(name="get_time", description="The IANA time zone name, e.g. America/Los_Angeles")(get_time)


# Register the tool function with the user proxy agent.
user_proxy.register_for_execution(name="get_weather")(get_weather)
user_proxy.register_for_execution(name="get_time")(get_time)

user_proxy.initiate_chat(
    assistant,
    message="What time is it in Florida?"
)
