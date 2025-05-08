from basic_agent import ask_gemini

def analyse_kpi(kpi_name: str, value: float):
    prompt= f"""Analyse this KPI for an aesthetic clinic:
    - KPI: {kpi_name}
    - Value: {value}
    Compare to industry standards and suggest one actionable improvement."""
    return ask_gemini(prompt)

print(analyse_kpi("Repeat Client Rate",0.25))