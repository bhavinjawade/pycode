# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 12:05:47 2020

@author: Samyak
"""

#==============================================================================
#  REGRESSION MODEL - PREDICTING PRICE OF PRE OWNED CARS
#==============================================================================
import numpy as np
import pandas as pd
import seaborn as sns

#setting graph size
sns.set(rc = {"figure.figsize": (10, 8)})

# Reading Data and getting info about data
data_price = pd.read_csv("cars_sampled.csv")
cars = data_price.copy()
cars.info()

cars.describe()

# To set float values upto 3 decimal places
pd.set_option("display.float_format", lambda x: "%.3f" % x)
cars.describe()

# Dropping unwanted columns
cols = ["name", "dateCrawled", "dateCreated", "postalCode", "lastSeen"]
cars = cars.drop(columns = cols, axis =1)

#Removing duplicates from the data
cars.drop_duplicates(keep="first", inplace=True)

cars.isnull().sum()

# varialbe Yearof Registration
yearwise = cars["yearOfRegistration"].value_counts().sort_index()
cars["yearOfRegistration"].describe()
sum(cars["yearOfRegistration"] > 2018)
sum(cars["yearOfRegistration"] < 1950)
sns.regplot(x="yearOfRegistration", y="price", scatter=True, fit_reg=False, data=cars)

# Removing Null values
cars = cars.dropna(axis = 0)
cars.isnull().sum()

# varialbe price
price_count = cars["price"].value_counts().sort_index()
cars["price"].describe()
sum(cars["price"] > 150000)
sum(cars["price"] < 100)
sns.distplot(cars["price"])

# varialbe PowerPS
power_count = cars["powerPS"].value_counts().sort_index()
cars["powerPS"].describe()
sum(cars["powerPS"] > 500)
sum(cars["powerPS"] < 10)
sns.boxplot(cars["powerPS"])
sns.regplot(x="powerPS", y="price", scatter=True, fit_reg=False, data=cars)

#Ranging the data to make it more usefull
cars = cars[
    (cars.yearOfRegistration >= 1950)
    & (cars.yearOfRegistration <= 2018)
    & (cars.price <= 150000)
    & (cars.price >= 100)
    & (cars.powerPS <= 500)
    & (cars.powerPS >= 10)
]

cars["monthOfRegistration"] /= 12

#Adding Age
cars["Age"] = (2018-cars["yearOfRegistration"])+cars["monthOfRegistration"]
cars["Age"] = round(cars["Age"], 2)
cars["Age"].describe()
#Since age is deployed therefor removing
cols1 = ["yearOfRegistration", "monthOfRegistration"]
cars = cars.drop(columns = cols1, axis = 1)
cars1 = cars.copy()

#Vissualizing Parameters after narrowing the range form dataframe
#Age
sns.distplot(cars["Age"])
sns.boxplot(y=cars["Age"])
sns.regplot(x="Age", y="price", scatter=True, fit_reg=False, data=cars1)

#price
sns.distplot(cars["price"])
sns.boxplot(y=cars["price"])

#poweerPS
sns.distplot(cars["powerPS"])
sns.boxplot(y=cars["powerPS"])
sns.regplot(x="powerPS", y="price", scatter=True, fit_reg=False, data=cars1)

#=============================================================================
#Comparing and Analyzing each and every varaible with price
#And removing Insignificant columns
#=============================================================================

#seller
cars["seller"].value_counts()
pd.crosstab(cars["seller"], columns="count", normalize=True)
sns.countplot(x="seller", data=cars1)
sns.boxplot(x="seller", y="price", data=cars1)
#Fewer cars have commercial which is innsignificant
#does not affect price as seen in boxplot
cars1 = cars1.drop(columns=["seller"], axis=1)

#offerType
cars["offerType"].value_counts()
pd.crosstab(cars["offerType"], columns="count", normalize=True)
sns.countplot(x="offerType", data=cars1)
sns.boxplot(x="offerType", y="price", data=cars1)
#does not affect price as seen in boxplot
cars1 = cars1.drop(columns=["offerType"], axis=1)

#abtest
cars["abtest"].value_counts()
pd.crosstab(cars["abtest"], columns="count", normalize=True)
sns.countplot(x="abtest", data=cars1)
sns.boxplot(x="abtest", y="price", data=cars1)
#does not affect price as seen in boxplot
cars1 = cars1.drop(columns=["abtest"], axis=1)

#vehicleType
cars["vehicleType"].value_counts()
pd.crosstab(cars["vehicleType"], columns="count", normalize=True)
sns.countplot(x="vehicleType", data=cars1)
sns.boxplot(x="vehicleType", y="price", data=cars1)
#affecting the price

#gearbox
cars["gearbox"].value_counts()
pd.crosstab(cars["gearbox"], columns="count", normalize=True)
sns.countplot(x="gearbox", data=cars1)
sns.boxplot(x="gearbox", y="price", data=cars1)
#affecting the price

#model
cars["model"].value_counts()
pd.crosstab(cars["model"], columns="count", normalize=True)
#affecting the price

#kilometer
cars["kilometer"].value_counts()
pd.crosstab(cars["kilometer"], columns="count", normalize=True)
sns.countplot(x="kilometer", data=cars1)
sns.boxplot(x="kilometer", y="price", data=cars1)
#affecting the price

#fuelType
cars["fuelType"].value_counts()
pd.crosstab(cars["fuelType"], columns="count", normalize=True)
sns.countplot(x="fuelType", data=cars1)
sns.boxplot(x="fuelType", y="price", data=cars1)
#affecting the price

#brand
cars["brand"].value_counts()
pd.crosstab(cars["brand"], columns="count", normalize=True)
sns.countplot(x="brand", data=cars1)
sns.boxplot(x="price", y="brand", data=cars1)
#affecting the price

#notRepairedDamage
cars["notRepairedDamage"].value_counts()
pd.crosstab(cars["notRepairedDamage"], columns="count", normalize=True)
sns.countplot(x="notRepairedDamage", data=cars1)
sns.boxplot(x="notRepairedDamage", y="price", data=cars1)
#cars wihich have repaired their damage have significantly more value

#============================================================================
#  CORRELATION
#===========================================================================


cars_select = cars.select_dtypes(exclude=[object])
corelation = cars_select.corr()
round(corelation, 3)
cars_select.corr().loc[:, "price"].abs().sort_values(ascending=False)[1:]
# powerPS have some decent affect on the price i.e 58%

cars1.describe()
#==============================================================================
# BUILDING ML MODEL
#==============================================================================

cars2 = cars1.copy()
#converting categorical variable in 0/1 format or dummy format
cars2 = pd.get_dummies(cars1, drop_first=True)

#==============================IMPORTING LIBRARIES=============================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

#Seprating the values for Linear Regression Model
x1 = cars2.drop(["price"], axis = "columns", inplace = False )
y1 = cars2["price"]

#plotting  the variable price
prices = pd.DataFrame({"1. Before": y1, "2. After":np.log(y1)})
prices.hist()

#Transforming file as a loarithmic value
y1 = np.log(y1)

#splittting the training and testing data
x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = 0.3, random_state=0)

#findin mean value on test data
test_mean = np.mean(y_test)
print(test_mean)
test_mean = np.repeat(test_mean, len(y_test))
print(test_mean)


#Root mean squared value error
rmse = np.sqrt(mean_squared_error(y_test, test_mean))
print(rmse)

linear_reg = LinearRegression(fit_intercept = True)

model_fit = linear_reg.fit(x_train, y_train)

cars_prediction = linear_reg.predict(x_test)

#MSE and RMSE for predictive values
mse1 = mean_squared_error(y_test, cars_prediction)
rmse1 = np.sqrt(mse1)
print(mse1)
print(rmse1)

#  R SQUARED VALUE
r2_test = model_fit.score(x_test, y_test)
r2_train = model_fit.score(x_train, y_train)

print(r2_test, r2_train)

#Regression Diaagnostic - Residual plot analysis
reiduals = y_test - cars_prediction
sns.regplot(x=cars_prediction, y=reiduals, fit_reg=False, scatter=True)
reiduals.describe()

#=============================================================================
# RANDOM FOREST MODEL
#=============================================================================

rf = RandomForestRegressor(n_estimators=100, max_features="auto",
                           max_depth=100, min_samples_split=10,
                           min_samples_leaf=4, random_state=1)

model_rf = rf.fit(x_train, y_train)

rf_prediction = rf.predict(x_test)


#MSE and RMSE for predictive values
mse1 = mean_squared_error(y_test, rf_prediction)
rmse1 = np.sqrt(mse1)
print(mse1)
print(rmse1)

#  R SQUARED VALUE
r2_test = model_rf.score(x_test, y_test)
r2_train = model_rf.score(x_train, y_train)

print(r2_test, r2_train)

# END



