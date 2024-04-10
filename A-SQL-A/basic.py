from langchain import hub
from langchain.agents import AgentExecutor
from langchain_anthropic import ChatAnthropic
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase

from CustomHelper.Anthropic_helper import format_to_anthropic_tool_messages, convert_tools
from CustomHelper.Custom_AnthropicAgentOutputParser import AnthropicAgentOutputParser_beta
from CustomHelper.load_model import get_anthropic_model

online_prompt = hub.pull("miracle/anthropic_sql_query_agent")


def load_sql_qa_agent(llm: ChatAnthropic, db: SQLDatabase) -> AgentExecutor:
    sql_tool_kit = SQLDatabaseToolkit(llm=llm, db=db)
    sql_tools = sql_tool_kit.get_tools()

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_anthropic_tool_messages(x['intermediate_steps']),
            "chat_history": lambda x: x["chat_history"]
        }
        | online_prompt.partial(tools=convert_tools(tools=sql_tools))
        | llm.bind_tools(tools=sql_tools)
        | AnthropicAgentOutputParser_beta()
    )

    return AgentExecutor(agent=agent, tools=sql_tools)