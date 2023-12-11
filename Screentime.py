import pandas as pd
import plotly.express as px



data = pd.read_csv("Screentime-App-Details.csv")
print(data)


# if the dataset has any null values or not--->
print(data.isnull().sum())


# Now let’s have a look at the descriptive statistics of the data--->
print(data.describe())


# Amount of usage of the Apps--->
figure1 = px.bar(data_frame=data,
                x="Date",
                y="Usage",
                color="App",
                title="Usage")
figure1.show()


# number of notifications from the apps--->
figure2 = px.bar(data_frame=data,
                x="Date",
                y="Notifications",
                color="App",
                title="Notifications")
figure2.show()


# Number of times the apps opened--->
figure3 = px.bar(data_frame=data,
                x="Date",
                y="Times opened",
                color="App",
                title="Times opened")
figure3.show()


# relationship between the number of notifications and the amount of usage--->
figure4 = px.scatter(data_frame=data,
                    x="Notifications",
                    y="Usage",
                    size="Notifications",
                    trendline="ols",
                    title="Relationship Between Number of Notifications and Usage")
figure4.show()


# ----------------------------------------Summary------------------------------------------------------------------
# So this is how we can analyze the screen time of a user using the Python programming language. Screen Time
# Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for
# how much time.
