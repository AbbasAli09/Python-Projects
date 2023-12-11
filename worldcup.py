import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

data = pd.read_csv("t20-world-cup-22.csv")
print(data)


# Number of matches won by each Team in World-Cup-->
figure1 = px.bar(data,
                x=data["winner"],
                title="Number of Matches Won by teams in t20 World Cup")
figure1.show()


# number of matches won by batting first or second in the t20 world cup-->
won_by2 = data["won by"].value_counts()
label2 = won_by2.index
counts2 = won_by2.values
colors2 = ['gold', 'lightgreen']

fig2 = go.Figure(data=go.Pie(labels=label2, values=counts2))
fig2.update_layout(title_text='Number of Matches Won By Runs or Wickets')
fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30, marker=dict(colors=colors2, line=dict(color='black', width=3)))
fig2.show()


# toss decisions by teams in the world cup-->
toss = data["toss decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue', 'yellow']

fig3 = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig3.update_layout(title_text='Toss Decisions in t20 World Cup 2022')
fig3.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig3.show()


# top scorers in the t20 world cup-->
figure4 = px.bar(data,
                x=data["top scorer"],
                y=data["highest score"],
                color=data["highest score"],
                title="Top Scorers in t20 World Cup 2022")
figure4.show()


# number of player of the match awards in the world cup-->
figure5 = px.bar(data,
                x=data["player of the match"],
                title="Player of the Match Awards in t20 World Cup 2022")
figure5.show()


# best bowling figures-->
figure6 = px.bar(data,
                x=data["best bowler"],
                title="Best Bowlers in t20 World Cup 2022")
figure6.show()


# compare the runs scored in the first innings and second innings in every stadium of the t20 world cup-->
fig7 = go.Figure()
fig7.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings score"],
    name='First Innings Runs',
    marker_color='blue'
))
fig7.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings score"],
    name='Second Innings Runs',
    marker_color='red'
))
fig7.update_layout(barmode='group',
                  xaxis_tickangle=-45,
                  title="Best Stadiums to Bat First or Chase")
fig7.show()


# compare the number of wickets lost in the first innings and second innings in every stadium of the t20 world cup-->
fig8 = go.Figure()
fig8.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings wickets"],
    name='First Innings Wickets',
    marker_color='blue'
))
fig8.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings wickets"],
    name='Second Innings Wickets',
    marker_color='red'
))
fig8.update_layout(barmode='group',
                  xaxis_tickangle=-45,
                  title="Best Statiums to Bowl First or Defend")
fig8.show()


# --------------------------------Summary---------------------------------------
# So some highlights of the t20 world cup 2022 we found from our analysis are:

# 1. England won the most number of matches
# 2. Virat Kohli scored highest in the most number of matches
# 3. Sam Curran was the best bowler in the most number of matches
# 4. More teams won by batting first
# 5. More teams decided to bat first
# 6. SCG was the best stadium to bat first
# 7. SCG was the best stadium to defend the target in the World Cup
# 8. The Optus Stadium was the best stadium to bowl first
