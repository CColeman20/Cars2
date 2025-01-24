mport pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

df.fillna({"price": 0, "condition": "unknown", "odometer": 0, "year": 0, "model": "unknown"}, inplace=True)

st.header("Car Price and Condition Dashboard")
if st.checkbox("Show only cars with price > $5,000"):
    df = df[df["price"] > 5000]
    st.subheader("Histogram: Distribution of Car Prices")
fig_hist = px.histogram(df, x="price", title="Car Price Distribution", nbins=30)
st.plotly_chart(fig_hist)

st.subheader("Scatter Plot: Price vs Odometer")
fig_scatter = px.scatter(
    df,
    x="odometer",
    y="price",
    color="condition",
    title="Price vs Odometer by Condition",
    labels={"odometer": "Odometer (miles)", "price": "Price (USD)"},
    hover_data=["model_year", "model"]
)
st.plotly_chart(fig_scatter)

if st.checkbox("Show Raw Dataset"):
    st.write("Dataset Preview", df.head()) 


