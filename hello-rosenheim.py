import streamlit as st

st.write("Hello Rosenheim!!!")


import pandas as pd

# Example data
data = {
    "Indicator": ["Tourism", "Happiness Index", "Inflation", "GDP"],
    "Sri Lanka": [2.3, 4.3, 7.5, 84],  # Replace with real values
    "Germany": [35.6, 7.1, 2.2, 4500],  # Replace with real values
}

df = pd.DataFrame(data)

import pandas as pd
import plotly.express as px
import streamlit as st

# Example Data
data = {
    "Indicator": ["Tourism", "Happiness Index", "Inflation", "GDP"],
    "Sri Lanka": [2.3, 4.3, 7.5, 84],  # Replace with real values
    "Germany": [35.6, 7.1, 2.2, 4500],  # Replace with real values
}
df = pd.DataFrame(data)

# Create interactive graphs with Plotly
fig_tourism = px.bar(df, x="Indicator", y=["Sri Lanka", "Germany"], title="Tourism Comparison")
fig_happiness = px.bar(df, x="Indicator", y=["Sri Lanka", "Germany"], title="Happiness Index Comparison")
fig_inflation = px.bar(df, x="Indicator", y=["Sri Lanka", "Germany"], title="Inflation Comparison")
fig_gdp = px.bar(df, x="Indicator", y=["Sri Lanka", "Germany"], title="GDP Comparison")

# Streamlit App Layout
st.title("Sri Lanka vs Germany - Economic & Social Indicators")

# Grid Layout
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_tourism, use_container_width=True)
    st.plotly_chart(fig_inflation, use_container_width=True)

with col2:
    st.plotly_chart(fig_happiness, use_container_width=True)
    st.plotly_chart(fig_gdp, use_container_width=True)


