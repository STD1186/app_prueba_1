import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta

# Funciones auxiliares
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso", "#FF6B6B", "💪"
    elif imc < 25:
        return "Peso normal", "#4ECDC4", "✅"
    elif imc < 30:
        return "Sobrepeso", "#FFA726", "⚠️"
    else:
        return "Obesidad", "#EF5350", "🚨"

def calcular_meta(imc):
    if imc < 18.5:
        return "Ganar peso saludablemente"
    elif imc < 25:
        return "Mantener peso actual"
    elif imc < 30:
        return "Perder 5-10% de peso"
    else:
        return "Perder 10-15% de peso"
