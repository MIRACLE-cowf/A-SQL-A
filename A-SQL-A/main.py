from langchain.memory import ConversationBufferMemory

from CustomHelper.load_model import get_anthropic_model
from Util.console_controller import clear_console, print_welcome, print_see_you_again
from Util.db_loader import load_db
from basic import load_sql_qa_agent

if __name__ == '__main__':
    db_name = input("Enter database name that conversation with LLM: ")
    db = load_db(db_name)
    if db is None:
        exit(1)

    clear_console()
    print_welcome()
    print(db.get_usable_table_names())

    memory = ConversationBufferMemory(return_messages=True)
    llm = get_anthropic_model()
    agent = load_sql_qa_agent(llm=llm, db=db)

    while True:
        user_input = input(f"What are you looking for in {db_name} database(If you want 'quit' press 'q'): ")

        if user_input.lower() == 'q':
            print_see_you_again()
            break

        agent_result = agent.invoke({
            "input": user_input,
            "chat_history": memory.chat_memory.messages
        })
        agent_response = agent_result['output']
        print(f"LLM:\n{agent_response}")

        memory.save_context(
            {"input": user_input},
            {"output": agent_response}
        )