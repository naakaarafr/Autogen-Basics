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


    task = """Write a concise but engaging blogpost about Meta."""

    writer = autogen.AssistantAgent(
        name="Writer",
        llm_config=llm_config,
        system_message="""
        You are a professional writer, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.
        You should improve the quality of the content based on the feedback from the user.
        """,
    )

    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
        code_execution_config={
            "last_n_messages": 1,
            "work_dir": "my_code",
            "use_docker": False,
        }
    )

    critic = autogen.AssistantAgent(
        name="Critic",
        llm_config=llm_config,
        system_message="""
        You are a critic, known for your thoroughness and commitment to standards.
        Your task is to scrutinize content for any harmful elements or regulatory violations, ensuring
        all materials align with required guidelines.
        For code
        """,
    )


    def reflection_message(recipient, messages, sender, config):
        print("Reflecting...")
        return f"Reflect and provide critique on the following writing. \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"


    user_proxy.register_nested_chats(
        [
            {
                "recipient": critic,
                "message": reflection_message,
                "summary_method": "last_msg",
                "max_turns": 1
            }
        ],
        trigger=writer
    )

    user_proxy.initiate_chat(recipient=writer, message=task, max_turns=2, summary_method="last_msg")

if __name__ == "__main__":
    main()