from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together and return the result."""
    return a + b

def main():
    model = ChatOpenAI(temperature=0)
    tools = [add_numbers]
    agent_executor = create_agent(model, tools)

    print("I am your AI assistant. Type q to exit.")
    print("Now I can perform simple calculations or chat with you.")

    Flag = True

    while Flag:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "q":
            Flag = False
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()

if __name__ == "__main__":
    main()



 

