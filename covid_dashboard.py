
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="COVID-19 Dashboard", page_icon="🦠", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ff4444;'>🦠 COVID-19 Dashboard</h1>", unsafe_allow_html=True)

@st.cache_data
@st.cache_data
def load_data():
    c = pd.read_csv("country_wise_latest.csv")
    d = pd.read_csv("covid_19_clean_complete.csv")
    w = pd.read_csv("day_wise.csv")
    c["CFR"] = (c["Deaths"] / c["Confirmed"] * 100).round(2)
    d["Date"] = pd.to_datetime(d["Date"])
    w["Date"] = pd.to_datetime(w["Date"])

    # Fix for pandas 2.x — only fill numeric columns with 0
    num_cols_c = c.select_dtypes(include="number").columns
    num_cols_d = d.select_dtypes(include="number").columns
    c[num_cols_c] = c[num_cols_c].fillna(0)
    d[num_cols_d] = d[num_cols_d].fillna(0)

    return c, d, w

country_latest, covid_complete, day_wise = load_data()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Confirmed",  f"{country_latest['Confirmed'].sum():,.0f}")
k2.metric("Total Deaths",     f"{country_latest['Deaths'].sum():,.0f}")
k3.metric("Total Recovered",  f"{country_latest['Recovered'].sum():,.0f}")
k4.metric("Global CFR",       f"{(country_latest['Deaths'].sum()/country_latest['Confirmed'].sum()*100):.2f}%")

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    st.subheader("Global Trend")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=day_wise["Date"], y=day_wise["Confirmed"], name="Confirmed", line=dict(color="#4da6ff")))
    fig.add_trace(go.Scatter(x=day_wise["Date"], y=day_wise["Deaths"],    name="Deaths",    line=dict(color="#ff4444")))
    fig.add_trace(go.Scatter(x=day_wise["Date"], y=day_wise["Recovered"], name="Recovered", line=dict(color="#00cc66")))
    fig.update_layout(height=350, margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Top 10 Countries")
    top10 = country_latest.nlargest(10, "Confirmed")
    fig = px.bar(top10, x="Confirmed", y="Country/Region", orientation="h", color="Confirmed", color_continuous_scale="Reds")
    fig.update_layout(height=350, yaxis=dict(autorange="reversed"), margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("World Map")
fig = px.choropleth(country_latest, locations="Country/Region", locationmode="country names",
                    color="Confirmed", hover_name="Country/Region",
                    hover_data=["Deaths","Recovered","CFR"], color_continuous_scale="Reds")
fig.update_layout(height=450, margin=dict(t=20))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Compare Countries")
all_countries = sorted(covid_complete["Country/Region"].unique().tolist())
selected = st.multiselect("Select Countries:", all_countries, default=["India","US","Brazil","Russia","United Kingdom"])
if selected:
    ts = covid_complete[covid_complete["Country/Region"].isin(selected)]
    ts = ts.groupby(["Date","Country/Region"])["Confirmed"].sum().reset_index()
    fig = px.line(ts, x="Date", y="Confirmed", color="Country/Region")
    fig.update_layout(height=380, margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
c3, c4 = st.columns(2)
with c3:
    st.subheader("Case Fatality Rate")
    top_cfr = country_latest[country_latest["Confirmed"] > 1000].nlargest(15, "CFR")
    fig = px.bar(top_cfr, x="CFR", y="Country/Region", orientation="h", color="CFR", color_continuous_scale="Oranges")
    fig.update_layout(height=420, yaxis=dict(autorange="reversed"), margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

with c4:
    st.subheader("Correlation Heatmap")
    cols = ["Confirmed","Deaths","Recovered","Active","New cases","New deaths","Deaths / 100 Cases","Recovered / 100 Cases"]
    corr = country_latest[cols].corr()
    fig = go.Figure(go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns,
                               colorscale="RdBu", zmid=0, text=corr.round(2).values, texttemplate="%{text}"))
    fig.update_layout(height=420, margin=dict(t=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("India Deep Dive")
india = covid_complete[covid_complete["Country/Region"] == "India"]
india = india.groupby("Date")["Confirmed"].sum().reset_index()
india["Daily_new"] = india["Confirmed"].diff().fillna(0)
india["Rolling_7"] = india["Daily_new"].rolling(7).mean()
fig = make_subplots(rows=1, cols=2, subplot_titles=("Total Cases", "Daily New + 7-Day Avg"))
fig.add_trace(go.Scatter(x=india["Date"], y=india["Confirmed"], fill="tozeroy", name="Total", line=dict(color="#4da6ff")), row=1, col=1)
fig.add_trace(go.Bar(x=india["Date"], y=india["Daily_new"], marker_color="rgba(255,68,68,0.4)", name="Daily"), row=1, col=2)
fig.add_trace(go.Scatter(x=india["Date"], y=india["Rolling_7"], line=dict(color="#ffcc00", width=2), name="7-day avg"), row=1, col=2)
fig.update_layout(height=380, margin=dict(t=30))
st.plotly_chart(fig, use_container_width=True)
