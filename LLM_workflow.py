from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class LLMChat(TypedDict):
    question : str
    answer : str


def llm_qa(state:LLMChat)->LLMChat:
    question = state['question']
    
    prompt = f'answer the follwing questions, {question}'

    answer = model.invoke(prompt).content

    state['answer'] = answer

    return state


graph = StateGraph(LLMChat)


graph.add_node('llm_qa', llm_qa)



graph.add_edge(START,"llm_qa")
graph.add_edge('llm_qa', END)


workflow = graph.compile()



initial_state = {'question': 'how far is moon from earth'}

final_state = workflow.invoke(initial_state)

print(final_state['answer'])