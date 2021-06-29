import pandas as pd 
import plotly.graph_objects as go
#import plotly.express as px

# Users over time 
lending_data = pd.read_csv('data/lending_deposits.csv')  
borrow_data = pd.read_csv('data/borrowed.csv')  
print(borrow_data)
#cust_sell = mainDf[mainDf.Type == 'S']
#cust_buy = mainDf[mainDf.Type == 'P']
lending_data = lending_data[lending_data.project != 'MakerDAO']
borrow_data = borrow_data[borrow_data.project != 'MakerDAO']
lending_data = lending_data[lending_data.project != 'Compound']
borrow_data = borrow_data[borrow_data.project != 'Compound']


fig = go.Figure()

fig.add_trace(go.Scatter(x=lending_data['day'], y=lending_data['outstanding_usd_value'], fill='tozeroy',
                    mode='none' # override default markers+lines
                    ))
'''
fig.add_trace(go.Scatter(x=borrow_data['day'], y=borrow_data['outstanding_usd_value'], fill='tozeroy',
                    mode='none' # override default markers+lines
                    ))
'''
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
