from langgraph.graph import StateGraph,START,END
from typing import TypedDict

#define state
class BMIState(TypedDict):
    weight_kg : float
    height_mt : float
    bmi : float
    category: str


def calculate_bmi(state: BMIState) -> BMIState:

    weight = state['weight_kg']
    height = state['height_mt']
    
    bmi = weight/(height**2)

    state['bmi'] = round(bmi, 2)

    return state


def label_bmi(sate:BMIState)-> BMIState:
    bmi = sate['bmi']
    if bmi < 18.5 :
         sate['category'] = 'underweight'
    elif 18.5 <= bmi < 25:
        sate['category'] = 'normal'
    elif 25 <= bmi < 30:
        sate['category'] = 'overweight'
    else:
        sate['category'] = 'obese'

    return sate        



#define graph
graph = StateGraph(BMIState)




#add nodes to your gragh
graph.add_node('calculate_bmi', calculate_bmi)
graph.add_node('label_bmi', label_bmi)


#add edges to your graph
graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', 'label_bmi')
graph.add_edge('label_bmi',END)


#compile the graph
workflow = graph.compile()


#execute the node
inital_state = {'weight_kg':80, 'height_mt': 1.3}
final_state = workflow.invoke(inital_state)

print(final_state)