from app import ask
import json

def analyse_kpi(name,value):
    prompt=f"""ANalyse this clinic KPI:
    - Name: {name}
    - Value: {value}
    Compare to industry average and suggest one action."""
    return ask(prompt)
    
def load_data():
    with open("data.json") as f:
        return json.load(f)
    
data=load_data()
for kpi, value in data.items():
    analyse_kpi(kpi,value)

#analyse_kpi("No-Show Rate","15%")