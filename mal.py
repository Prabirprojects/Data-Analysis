import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # this is used for the plot the graph 
import seaborn as sns # used for plot interactive graph.
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import warnings
warnings.filterwarnings('ignore')
from pylab import rcParams
# figure size in inches

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


df_country = pd.read_csv("C:\Data Analysis and Visualization of Malnutrition\country-wise-average.csv")
print(df_country)
print("--------------------1")
df_world = pd.read_csv("C:\Data Analysis and Visualization of Malnutrition\World_Malnutrition_Data.csv")
print(df_world)
print("--------------------2")
df_region = pd.read_csv("C:\Data Analysis and Visualization of Malnutrition\Region_Data.csv")
print(df_region)
print("--------------------3")

print(df_country.head())
print("--------------------4")
print(df_region.head())
print("--------------------5")
print(df_world.head())
print("--------------------6")

# Income classification is a category and can be converted to int
df_country["Income Classification"] =  df_country["Income Classification"].astype("int32")
print(df_country["Severe Wasting"].describe())
print("--------------------7")

plt.figure(figsize=(16, 8))
sns.set(style="whitegrid")
cols = ["Income Classification","Severe Wasting","Wasting","Overweight","Stunting","Underweight" ]
sns.pairplot(df_country[cols], height = 2.5 )
plt.show();

plt.figure(figsize=(16, 8))
x = df_country.groupby(["Income Classification"])["Severe Wasting"].mean()
print(x)
print("--------------------7.1")
sns.set(style="whitegrid")
ax = sns.barplot(x=x.index, y=x.values)
ax.set_title('Severe Wasting')
ax.set_ylabel('% Severe Wasting')
ax.set_xlabel('Income Classification')
plt.xticks(rotation = 90)

#Plotting on the WorldMap using plotly
x = df_country.groupby(["Country"])["Severe Wasting"].mean()
print(x)
print("--------------------7.2")
data = dict(type = 'choropleth',
            locations = x.index,
            locationmode = 'country names',
            colorscale= 'Portland',
            text= x.index,
            z=x,
            colorbar = {'title':'Severe Wasting %', 'len':200,'lenmode':'pixels' })
layout = dict(geo = {'scope':'world'},title="Severe Wasting % around the world")
print(layout)
print("--------------------7.2.1")
col_map = go.Figure(data = [data],layout = layout)
col_map.show()

plt.figure(figsize=(16, 8))
x = df_country.groupby(["Income Classification"])["Wasting"].mean()
print(x)
print("--------------------7.3")
sns.set(style="whitegrid")
ax = sns.barplot(x=x.index, y=x.values)
ax.set_title('Wasting')
ax.set_ylabel('% Wasting')
ax.set_xlabel('Income Classification')
plt.xticks(rotation = 90)

#Plotting on the WorldMap using plotly
x = df_country.groupby(["Country"])["Wasting"].mean()
print(x)
print("--------------------7.4")
data = dict(type = 'choropleth',
            locations = x.index,
            locationmode = 'country names',
            colorscale= 'Portland',
            text= x.index,
            z=x,
            colorbar = {'title':'Wasting %', 'len':200,'lenmode':'pixels' })
layout = dict(geo = {'scope':'world'},title="Wasting % around the world")
print(layout)
print("--------------------7.4.1")
col_map = go.Figure(data = [data],layout = layout)
col_map.show()
plt.show()

df_world.rename(columns = {"TIME_PERIOD" : "Year", "OBS_VALUE" : "value"}, inplace =True)
df_world_mort = df_world[df_world["Indicator"] == "Under-five mortality rate"]
print(df_world_mort)
print("--------------------7.4.2")
df_world_stunting = df_world[df_world.Indicator == "Height-for-age <-2 SD (stunting)"]
print(df_world_stunting)
print("--------------------7.4.3")
df_world_underwt = df_world[df_world.Indicator == "Weight-for-age <-2 SD (Underweight)"]
print(df_world_underwt)
print("--------------------7.4.4")
df_world_mort.drop(["Indicator"],axis="columns",inplace = True)
print(df_world_mort.Year.unique())
print("--------------------8")




plt.figure(figsize=(16, 8))
x = df_world_mort[(df_world_mort["Sex"] == "Total") & (df_world_mort["Year"] == 2018) ].sort_values(by="value", ascending=False).head(20)
print(x)
print("--------------------8.1")
sns.set(style="darkgrid")
ax = sns.barplot(x=x["Country"].index, y=x["value"].values)
ax.set_title('Mortality Rate Childs/1000 Births in 2018')
ax.set_ylabel('Number of deaths')
ax.set_xlabel('Country')
plt.xticks(rotation = 90)
plt.show()

print(df_world_mort.head())
print("--------------------9")


plt.figure(figsize=(16, 8))
sns.set(style="darkgrid")
cols = ["Male","Female"]
for col in cols:
    x = df_world_mort[df_world_mort["Sex"] == col].groupby("Year")["value"].mean()
    print(x)
    print("--------------------9.1")
    ax = sns.barplot(x=x.index,y= x.values, label=col)
ax.set_title('World Wide mortality Rate of Infants / 1000 births')
ax.set_ylabel('Number of deaths / 1000 births')
ax.set_xlabel('Year')
ax.legend()
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(16, 8))
x = df_world_stunting[(df_world_stunting["Sex"] == "Total") & (df_world_stunting["Year"] == 2018) ].sort_values(by="value", ascending=False).head(20)
print(x)
print("--------------------9.2")
sns.set(style="darkgrid")
ax = sns.barplot(x=x["Country"].index, y=x["value"].values)
ax.set_title('Height-for-age <-2 SD (stunting) in 2018 in percentage')
ax.set_ylabel('Percentage')
ax.set_xlabel('Country')
plt.xticks(rotation = 90)

plt.show()

plt.figure(figsize=(16, 8))
sns.set(style="darkgrid")
cols = ["Male","Female"]
for col in cols:
    x = df_world_stunting[df_world_stunting["Sex"] == col].groupby("Year")["value"].mean()
    print(x)
    print("--------------------9.3")
    ax = sns.barplot(x=x.index, y=x.values, label=col)
ax.set_title('World Wide Height-for-age <-2 SD (stunting)')
ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.legend()
plt.xticks(rotation = 90)

plt.show()

plt.figure(figsize=(16, 8))
x = df_world_underwt[(df_world_underwt["Sex"] == "Total") & (df_world_underwt["Year"] == 2018) ].sort_values(by="value", ascending=False).head(20)
print(x)
print("--------------------9.4")
sns.set(style="darkgrid")
ax = sns.barplot(x=x["Country"].index, y=x["value"].values)
ax.set_title('Weight-for-age <-2 SD (Underweight) in 2018 in percentage')
ax.set_ylabel('Percentage')
ax.set_xlabel('Country')
plt.xticks(rotation = 90)

plt.show()

plt.figure(figsize=(16, 8))
sns.set(style="darkgrid")
cols = ["Male","Female"]
for col in cols:
    x = df_world_underwt[df_world_underwt["Sex"] == col].groupby("Year")["value"].mean()
    print(x)
    print("--------------------9.5")
    ax = sns.barplot(x=x.index, y=x.values, label=col)
ax.set_title('World Wide Weight-for-age <-2 SD (Underweight)')
ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.legend()
plt.xticks(rotation = 90)
plt.show()

print(df_region.head())
print("--------------------10")

print(df_region["Indicator"].unique())
print("--------------------11")
print(df_region["Geographic Area"].unique())
print("--------------------12")


continents = ['Asia','Africa','Australia and New Zealand','South America','North America']
plt.figure(figsize=(16, 8))
sns.set(style="darkgrid")
for col in continents:
    x = df_region[(df_region["Geographic Area"] == col) &  (df_region["Indicator"] == "Height-for-age <-2 SD (stunting)")].groupby("TIME_PERIOD")["OBS_VALUE"].mean()
    print(x)
    print("--------------------9.6")
    ax = sns.barplot(x=x.index, y=x.values, label=col)
ax.set_title('World Wide Height-for-age <-2 SD (stunting)')
ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.legend()
plt.xticks(rotation = 90)
plt.show()

continents = ['Asia','Africa','Australia and New Zealand','South America','North America']
plt.figure(figsize=(16, 8))
sns.set(style="darkgrid")
for col in continents:
    x = df_region[(df_region["Geographic Area"] == col) &  (df_region["Indicator"] == "Weight-for-age <-2 SD (Underweight)")].groupby("TIME_PERIOD")["OBS_VALUE"].mean()
    print(x)
    print("--------------------9.7")
    ax = sns.barplot(x=x.index, y=x.values, label=col)
ax.set_title('World Wide Weight-for-age <-2 SD (Underweight)')
ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.legend()
plt.xticks(rotation = 90)
plt.show()

