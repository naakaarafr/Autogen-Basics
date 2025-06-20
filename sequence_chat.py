import autogen
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
gemini_api_key = os.getenv('GEMINI_API_KEY')

def main():
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


    assistant_quote1 = autogen.AssistantAgent(
        name="assistant1",
        system_message="You are an assistant agent who gives quotes.  Return 'TERMINATE' when the task is done.",
        llm_config=llm_config,
    )

    assistant_quote2 = autogen.AssistantAgent(
        name="assistant2",
        system_message="You are another assistant agent who gives quotes.  Return 'TERMINATE' when the task is done.",
        llm_config=llm_config,
        max_consecutive_auto_reply=1
    )

    assistant_create_new = autogen.AssistantAgent(
        name="assistant3",
        system_message="You will create a new quote based on others.  Return 'TERMINATE' when the task is done.",
        llm_config=llm_config,
        max_consecutive_auto_reply=1
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config=False
    )

    user_proxy.initiate_chats(
        [
            {
                "recipient": assistant_quote1,
                "message": "give a quote from a famous author",
                "clear_history": True,
                "silent": False,
                "summary_method": "reflection_with_llm"
            },
            {
                "recipient": assistant_quote2,
                "message": "give another quote from a famous author",
                "clear_history": True,
                "silent": False,
                "summary_method": "reflection_with_llm"
            },
            {
                "recipient": assistant_create_new,
                "message": "based on the previous quotes, come up with your own!",
                "clear_history": True,
                "silent": False,
                "summary_method": "reflection_with_llm"
            }
        ]
    )

if __name__ == "__main__":
    main()