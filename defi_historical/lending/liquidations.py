import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#import plotly.express as px

# Users over time 
aave_liquidations = pd.read_csv('data/aave_liquidations.csv')  
compound_liquidations = pd.read_csv('data/compound_liquidations.csv')  

aave_liquidations = aave_liquidations.head(7)
compound_liquidations = compound_liquidations.head(7)
print(aave_liquidations)

compound_sum_liquidations = compound_liquidations['number_of_liquidations'].sum()
aave_sum_liquidations = aave_liquidations['number_of_liquidations'].sum()
aave_sum_collateral = aave_liquidations['collateral_liquidated_usd'].sum()
print(aave_sum_collateral)
#fig = px.line(aave_liquidations, x="day", y="number_of_liquidations")
fig = make_subplots(specs=[[{"secondary_y": True}]])


fig.add_trace(go.Bar(x=aave_liquidations['day'], y=aave_liquidations['collateral_liquidated_usd']))
fig.add_trace(go.Scatter(x=aave_liquidations['day'], y=aave_liquidations['number_of_liquidations'],
                    mode='lines',
                    name='lines'),secondary_y=True)
fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        zeroline=True,
        linecolor='#F4F4F4',
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=21,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=21,
            color='grey',
        ),
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    autosize=True,

    plot_bgcolor='white'
)

'''
fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="stretch",
        opacity=0.5,
        layer="below")
)
'''
fig.show()
