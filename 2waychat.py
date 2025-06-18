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
            'model': 'gemini-1.5-flash',
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
    
    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config=llm_config
    )
    
    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",  # This will pause for your input after each agent response
        max_consecutive_auto_reply=0,  # Set to 0 when using "ALWAYS"
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )
    
    user_proxy.initiate_chat(
        assistant, 
        message="Plot a chart of META and TESLA stock price change"
    )

if __name__ == "__main__":
    main()