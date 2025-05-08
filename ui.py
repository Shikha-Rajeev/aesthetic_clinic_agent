import gradio as gr
from kpi import analyse_kpi

KPI_OPTIONS=[
    "Repeat Client Rate",
    "Consult-to-Booking Rate",
    "Average Spend per Visit",
    "Patient Satisfaction Score",
    "No-Show Rate"
]

def analyse_kpi_gradio(kpi_name: str, kpi_value: str) -> str:
    try:
        value=float(kpi_value)
        if not 0<=value<=100:
            return "⚠️ Error: Value must be between 0-100"
        result= analyse_kpi(kpi_name, value)
        return f"📊 **Analysis for {kpi_name} ({value}%)**\n\n{result}"
    except ValueError:
        return "⚠️ Error: Please enter valid number"
    except Exception as e:
        return f"⚠️ Error: {str(e)}" 

with gr.Blocks(title="Clinic KPI Analyser") as app:
    gr.Markdown("Aesthetic Clinic KPI Dashboard")
    
    with gr.Row():
        kpi_name=gr.Dropdown(
            KPI_OPTIONS,
            label="Select KPI",
            value="Repeat Client Rate"
        )
        kpi_value=gr.Number(
            label="Enter Value (%)",
            value=25,
            minimum=0,
            maximum=100
        )
    submit_btn=gr.Button("Analyse", variant="primary")
    output=gr.Markdown()
    
    gr.Examples(
        examples=[
            ["Repeat Client Rate", 25],
            ["Consult-to-Booking Rate", 15],
            ["No-Show Rate", 20]
        ],
        inputs=[kpi_name,kpi_value]
    )
    
    submit_btn.click(
        fn=analyse_kpi_gradio,
        inputs=[kpi_name,kpi_value],
        outputs=output
    )
    
app.launch()