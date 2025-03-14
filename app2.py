import pandas as pd
import numpy as np

import warnings 
warnings.filterwarnings("ignore") # To supress warnings

import seaborn as sns
import matplotlib.pyplot as plt

from plotly.offline import init_notebook_mode
import plotly.express as px


import streamlit as st

data=pd.read_csv("Ad_campaign_cl.csv")

st.title("Technical Trainings, Placements & Services.")
st.subheader("Paid Ad Campaigns To generate leads ")
st.subheader(" - Design of Ads")

colx, coly= st.columns([2,2])
with colx:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1brUXID3tDARgG-kAOtoqWMlA8iou9BctLiL_C0sWoSnr232wSc0M6cZlMjOtGWIQunA&usqp=CAU")
with coly:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1-v53IoAzrPwYPXB5ijHh1ZXQ5ns43ltTw3yOIr3Z0lEPTk09IvTejyUNPuKHma4lkRU&usqp=CAU")

st.dataframe(data)
st.subheader("from above dataset given below Exploratory Data Analysis :")
st.subheader("Uni-variate EDA:")
st.write(" ")

cola, colb= st.columns([2,2])
with cola:
    index = data["Platform"].value_counts().sort_values(ascending=False)[0:10].index
    vals = data["Platform"].value_counts().sort_values(ascending=False)[0:10].values
    fig = px.pie(names=index, values=vals, width=700, height=400)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False)
    st.write("Platform Distribution Pie Chart")
    st.plotly_chart(fig)
with colb:
    index = data["Content_Type"].value_counts().sort_values(ascending=False)[0:10].index
    vals = data["Content_Type"].value_counts().sort_values(ascending=False)[0:10].values
    fig = px.pie(names=index, values=vals, width=700, height=400)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False)
    st.write("Content_Type Distribution Pie Chart")
    st.plotly_chart(fig)


colc, cold = st.columns([2,2])
with colc:
    index = data["Target_Gender"].value_counts().sort_values(ascending=False)[0:10].index
    vals = data["Target_Gender"].value_counts().sort_values(ascending=False)[0:10].values
    fig = px.pie(names=index, values=vals, width=700, height=400)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False)
    st.write("Target_Gender Distribution Pie Chart")
    st.plotly_chart(fig)
with cold:
    index = data["Region"].value_counts().sort_values(ascending=False)[0:10].index
    vals = data["Region"].value_counts().sort_values(ascending=False)[0:10].values
    fig = px.pie(names=index, values=vals, width=700, height=400)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False)
    st.write("Region Distribution Pie Chart")
    st.plotly_chart(fig)
    
 
cole, colf = st.columns([2,2])
with cole:
    sns.set_style("darkgrid", {"axes.facecolor": "black"})
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.histplot(data["Success"], kde=True, ax=ax) 
    st.write("Success Distribution Histogram")
    st.pyplot(fig)
with colf:
    sns.set_style("darkgrid", {"axes.facecolor": "black"})
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.histplot(data["Clicks"], kde=True, ax=ax , color="cyan")
    st.write("Clicks Distribution Histogram")
    st.pyplot(fig)   

st.subheader("bi-variate EDA:")

colg, colh = st.columns([2,2])
with colg:
    st.write("Target_Gender vs Clicks:")
    classes = round(data.groupby('Target_Gender')['Clicks'].sum().sort_values(ascending=False), 2).index
    vals = round(data.groupby('Target_Gender')['Clicks'].sum().sort_values(ascending=False), 2).values

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(classes, vals, color="cyan")  # Bar chart with cyan bars for contrast

    # Add labels and title
    ax.set_title("Target_Gender vs Clicks", color="white")
    ax.set_ylabel("Clicks", color="white")
    ax.set_xlabel("Target Gender", color="white")
    ax.tick_params(colors="white")
    st.pyplot(fig)
with colh:
    st.write("Region vs Clicks:")
    classes = round(data.groupby('Region')['Clicks'].sum().sort_values(ascending=False), 2).index
    vals = round(data.groupby('Region')['Clicks'].sum().sort_values(ascending=False), 2).values

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(classes, vals, color="cyan")  # Bar chart with cyan bars for contrast

    # Add labels and title
    ax.set_title("Region vs Clicks", color="white")
    ax.set_ylabel("Clicks", color="white")
    ax.set_xlabel("Region", color="white")
    ax.tick_params(colors="white")
    st.pyplot(fig)
    
coli, colj = st.columns([2,2])
with coli:
    st.write("Content_Type vs Clicks:")
    classes = round(data.groupby('Content_Type')['Clicks'].sum().sort_values(ascending=False), 2).index
    vals = round(data.groupby('Content_Type')['Clicks'].sum().sort_values(ascending=False), 2).values

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(classes, vals, color="cyan")  # Bar chart with cyan bars for contrast

    # Add labels and title
    ax.set_title("Content_Type vs Clicks", color="white")
    ax.set_ylabel("Clicks", color="white")
    ax.set_xlabel("Content_Type", color="white")
    ax.tick_params(colors="white")
    st.pyplot(fig)
with colj:
    st.write("Platform vs Clicks:")
    classes = round(data.groupby('Platform')['Clicks'].sum().sort_values(ascending=False), 2).index
    vals = round(data.groupby('Platform')['Clicks'].sum().sort_values(ascending=False), 2).values

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(classes, vals, color="cyan")  # Bar chart with cyan bars for contrast

    # Add labels and title
    ax.set_title("Platform vs Clicks", color="white")
    ax.set_ylabel("Clicks", color="white")
    ax.set_xlabel("Platform", color="white")
    ax.tick_params(colors="white")
    st.pyplot(fig)

st.subheader("Multi-variate EDA:")

corr_matrix = data.corr(numeric_only=True)

# Create mask for upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Set up figure
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', mask=mask, ax=ax)

# Display in Streamlit
st.title("Correlation Heatmap")
st.pyplot(fig)

st.write("Sunbrust  diagram")
fig = px.sunburst(
    data,
    path=['Platform', "Content_Type"],  # Hierarchy of categories
    values='Clicks',
    color='Clicks',  # Optional: Color by Clicks
    color_continuous_scale='darkmint'  # A dark-compatible color scale
)
# Apply Dark Theme
fig.update_layout(
    paper_bgcolor="black",  # Background of the figure
    plot_bgcolor="black",   # Background of the plot
    font=dict(color="white")  # Text color for readability
)
# Streamlit App
st.write("Sunburst Chart: Platform vs Content Type")
st.plotly_chart(fig)  # Display Sunburst chart in Streamlit


round(data.groupby(['Region', 'Target_Gender','Target_Age'])[['Clicks', 'CTR','Success']].mean(), 2)
# Create the bar chart
fig = px.bar(
    data,
    x="Conversion_Rate",
    y="Region",
    color="Target_Gender",
    hover_data=["Clicks", "CTR"],
    height=300,
    title="Ads Analysis"
)

# Display the chart in Streamlit
st.plotly_chart(fig)

round(data.groupby(['Region','Platform', 'Content_Type'])[['CTR', 'CPC','Success']].mean(), 2)
fig= px.bar(data,
       x="Clicks",
       y="Content_Type",
       color='Platform',
       hover_data=["CTR",'CPC', 'Success'],
       height=400,
       title='Content_Type and platform vs conversion rate')
st.plotly_chart(fig)