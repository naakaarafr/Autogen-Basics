import autogen
import os
from dotenv import load_dotenv
from typing_extensions import Annotated

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
gemini_api_key = os.getenv('GEMINI_API_KEY')

def main():
    # Check if API key exists
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    config_list = [
        {
            'model': 'gemini-1.5-flash',  # Use gemini-1.5-flash instead of 2.0
            'api_key': gemini_api_key,
            'api_type': 'google'
        }
    ]

    llm_config = {
        "config_list": config_list, 
        "seed": 42,
        "temperature": 0.1,  # Lower temperature for more consistent function calling
        "timeout": 120,
        "max_tokens": 1000
    }

    # Define the exchange rate function
    def exchange_rate(base_currency: str, quote_currency: str) -> float:
        """Get exchange rate between two currencies"""
        if base_currency == quote_currency:
            return 1.0
        elif base_currency == "USD" and quote_currency == "EUR":
            return 0.92  # 1 USD = 0.92 EUR (approximate)
        elif base_currency == "EUR" and quote_currency == "USD":
            return 1.09  # 1 EUR = 1.09 USD (approximate)
        else:
            raise ValueError(f"Unsupported currency pair: {base_currency} to {quote_currency}")

    # Define the currency calculator function
    def currency_calculator(
        base_amount: Annotated[float, "Amount of currency in base_currency"],
        base_currency: Annotated[str, "Base currency (USD or EUR)"] = "USD",
        quote_currency: Annotated[str, "Quote currency (USD or EUR)"] = "EUR"
    ) -> str:
        """Convert currency from base to quote currency"""
        # Validate currency inputs
        valid_currencies = ["USD", "EUR"]
        if base_currency not in valid_currencies or quote_currency not in valid_currencies:
            return f"Error: Only {valid_currencies} are supported. You provided: {base_currency} and {quote_currency}"
        
        try:
            rate = exchange_rate(base_currency, quote_currency)
            quote_amount = rate * base_amount
            return f"{base_amount} {base_currency} = {quote_amount:.2f} {quote_currency} (rate: {rate})"
        except ValueError as e:
            return f"Error: {str(e)}"

    # Create user proxy with simpler configuration
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=3,  # Reduced to avoid loops
        code_execution_config=False,
        system_message="You are a user proxy. Execute function calls and terminate when done."
    )

    # Create currency bot with simpler system message
    currency_bot = autogen.AssistantAgent(
        name="currency_bot",
        system_message=(
            "You are a currency exchange assistant. "
            "Use the currency_calculator function to convert between USD and EUR. "
            "Always respond with TERMINATE after completing the conversion."
        ),
        llm_config=llm_config
    )

    # Register the function for both execution and LLM calling
    autogen.register_function(
        currency_calculator,
        caller=currency_bot,
        executor=user_proxy,
        name="currency_calculator",
        description="Convert currency between USD and EUR"
    )

    # Start the conversation
    try:
        result = user_proxy.initiate_chat(
            currency_bot,
            message="Convert 100 USD to EUR",
            max_turns=5
        )
        print("Chat completed successfully!")
        
    except Exception as e:
        print(f"Error during chat: {e}")
        # Try a simpler approach without function calling
        print("Trying without function calling...")
        
        simple_bot = autogen.AssistantAgent(
            name="simple_currency_bot",
            system_message=(
                "You are a currency converter. "
                "Use these rates: 1 USD = 0.92 EUR, 1 EUR = 1.09 USD. "
                "Convert currencies manually and show your calculation."
            ),
            llm_config=llm_config
        )
        
        simple_proxy = autogen.UserProxyAgent(
            name="simple_proxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=1,
            code_execution_config=False
        )
        
        simple_proxy.initiate_chat(
            simple_bot,
            message="Convert 100 USD to EUR using the rate 1 USD = 0.92 EUR"
        )

if __name__ == "__main__":
    main()