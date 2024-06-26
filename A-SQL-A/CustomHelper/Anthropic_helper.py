from typing import Sequence, Tuple, List
from langchain_core.agents import AgentAction
from langchain_core.messages import AIMessage, ToolMessage, BaseMessage

from CustomHelper.Custom_AnthropicAgentOutputParser import AnthropicAgentAction



# WE can use basically same as LangChain OpenAI's 'format_to_openai_tool_message', but little bit custom is there
def _create_tool_message(
    agent_action: AnthropicAgentAction, observation: str
) -> ToolMessage:
    """ This is basically same as LangChain's '_create_tool_message' function
    Convert agent action and observation into a function message.
    Args:
        agent_action: the tool invocation request from the agent
        observation: the result of the tool invocation
    Returns:
        FunctionMessage that corresponds to the original tool invocation
    """
    if not isinstance(observation, str):
        try:
            import json
            content = json.dumps(observation, ensure_ascii=False)
        except Exception:
            content = str(observation)
    else:
        content = observation
    return ToolMessage(
        tool_call_id=agent_action.tool_call_id,
        content=content,
        additional_kwargs={"name": agent_action.tool},
    )


def format_to_anthropic_tool_messages(
    intermediate_steps: Sequence[Tuple[AgentAction, str]],
) -> List[BaseMessage]:
    """Convert (AgentAction, tool output) tuples into FunctionMessages.

    Args:
        intermediate_steps: Steps the LLM has taken to date, along with observations

    Returns:
        list of messages to send to the LLM for the next prediction

    Basically use LangChain's format_to_openai_tool_messages()
    """
    messages = []
    for agent_action, observation in intermediate_steps:
        if isinstance(agent_action, AnthropicAgentAction):
            new_messages = list(agent_action.message_log) + [
                _create_tool_message(agent_action, observation)
            ]
            messages.extend([new for new in new_messages if new not in messages])
        else:
            messages.append(AIMessage(content=agent_action.log))
    return messages



def convert_tools(tools: list):
    return "\n".join(
        [
            f"""Tool {index+1}:
Name: {tool.name}
Description: {tool.description}
Parameter: {tool.args}""" for index, tool in enumerate(tools)
        ]
    )