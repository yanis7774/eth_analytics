base = 100
base2=100
base3=100
daily_return = .0055095
day = []
daily_value = []
daily_noncompounding_value = []
non_compounding = 0
x = 1095
y = 0
while y < x:
    base=(base*daily_return) + base
    daily_value.append(base)
    y+=1
    day.append(y)
    non_compounding=(base2*daily_return)
    base2=100
    base3=base3+non_compounding
    daily_noncompounding_value.append(base3)
print(daily_value)
print(len(daily_value))
print(len(day))
print(base3)


import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=day, y=daily_value,
                    mode='lines',
                    name='lines',
                    ))
fig.add_trace(go.Scatter(x=day, y=daily_noncompounding_value,
                    mode='lines',
                    name='lines',
                    ))

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
            color='blue',
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