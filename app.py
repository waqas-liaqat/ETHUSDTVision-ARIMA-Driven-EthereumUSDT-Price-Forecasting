# eth_forecast_app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
import json
from datetime import datetime, timedelta
import os

# App config
st.set_page_config(page_title="ETH Forecast", layout="wide")
st.title("📈 Ethereum Price Forecast")

# Fix path issues for different operating systems
def fix_path(path):
    return os.path.normpath(path)

# Load model and data
@st.cache_resource
def load_model():
    try:
        model_path = fix_path("Artifacts\model_eth.pkl")
        meta_path = fix_path("Artifacts\model_metadata.json")
        model = joblib.load(model_path)
        with open(meta_path) as f:
            meta = json.load(f)
        return model, meta
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        return None, None

model, meta = load_model()

# Load historical data
@st.cache_data
def load_data():
    try:
        data_path = fix_path("Data\eth_usdt_data.csv")
        df = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
        return df['Close']
    except Exception as e:
        st.warning(f"Historical data not found: {str(e)}")
        return None

series = load_data()

# Sidebar controls
st.sidebar.header("Settings")
days = st.sidebar.slider("Forecast days", 7, 90, 30)
show_conf = st.sidebar.checkbox("Show confidence", True)

# Main content
if model and meta and series is not None:
    # Model info cards
    st.subheader("Model Performance")
    cols = st.columns(4)
    cols[0].metric("Model", f"{meta['model_type']}{meta['order']}")
    cols[1].metric("Seasonality", str(meta['seasonal_order']) if meta['seasonal_order'] else "None")
    cols[2].metric("RMSE", f"{meta['rmse']:.2f}")
    cols[3].metric("MAPE", f"{meta['mape']*100:.2f}%")
    
    # Generate forecast
    try:
        forecast = model.get_forecast(steps=days)
        pred_mean = forecast.predicted_mean
        conf_int = forecast.conf_int() if show_conf else None
        
        # Create date range
        last_date = series.index[-1]
        pred_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days)
        
        # Create Plotly figure
        fig = go.Figure()
        
        # Historical data (last 100 days)
        hist_dates = series.index[-100:]
        hist_prices = series[-100:]
        
        # Add traces
        fig.add_trace(go.Scatter(
            x=hist_dates,
            y=hist_prices,
            name="Historical",
            line=dict(color='#636EFA'),
            mode='lines'
        ))
        
        # Connecting line (last historical point to first forecast)
        fig.add_trace(go.Scatter(
            x=[last_date, pred_dates[0]],
            y=[hist_prices[-1], pred_mean.iloc[0]],
            line=dict(color='gray', dash='dot'),
            mode='lines',
            showlegend=False
        ))
        
        # Forecast
        fig.add_trace(go.Scatter(
            x=pred_dates,
            y=pred_mean,
            name="Forecast",
            line=dict(color='#FFA15A'),
            mode='lines+markers'
        ))
        
        # Confidence interval
        if show_conf and conf_int is not None:
            fig.add_trace(go.Scatter(
                x=np.concatenate([pred_dates, pred_dates[::-1]]),
                y=np.concatenate([conf_int.iloc[:, 0], conf_int.iloc[:, 1][::-1]]),
                fill='toself',
                fillcolor='rgba(255,161,90,0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                name="95% Confidence",
                hoverinfo="skip"
            ))
        
        # Layout
        fig.update_layout(
            title=f"ETH/USD {days}-Day Forecast",
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            hovermode="x unified",
            height=600,
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast table with proper date handling
        st.subheader("Forecast Details")
        
        # Create DataFrame with properly formatted dates
        forecast_df = pd.DataFrame({
            "Date": pred_dates.strftime('%Y-%m-%d'),  # Format as clean date strings
            "Predicted": pred_mean.values,  # Use .values to get numpy array
            "Lower": conf_int.iloc[:, 0].values if show_conf else [None] * len(pred_dates),
            "Upper": conf_int.iloc[:, 1].values if show_conf else [None] * len(pred_dates)
        })
        
        # Display formatted table
        st.dataframe(
            forecast_df.set_index('Date').style.format({
                "Predicted": "{:.2f}",
                "Lower": "{:.2f}",
                "Upper": "{:.2f}"
            }),
            use_container_width=True
        )
        
    except Exception as e:
        st.error(f"Forecast generation failed: {str(e)}")

else:
    st.warning("""
    Required files missing. Please ensure you have:
    - `Artifacts/model_eth.pkl`
    - `Artifacts/model_metadata.json`
    - `Data/eth_usdt_data.csv`
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption(f"Last trained: {meta['last_training_date'] if (meta and 'last_training_date' in meta) else 'N/A'}")