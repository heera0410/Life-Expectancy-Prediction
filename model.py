#import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# load data
url = "./Life_Expectancy_Data.csv"
data = pd.read_csv(url,sep=',')
# drop the null values if any from all rows
data.dropna(axis=0, how='any', inplace=True)
# replace the status variable as binary input
data.replace({'Status':{'Developed':0,'Developing':1}},inplace=True)

# Input features in x and target variable in y
x=data[['Year','Status','Adult Mortality','infant deaths','Alcohol','percentage expenditure','Hepatitis B','Measles', 'BMI' ,'under-five deaths' ,'Polio','Total expenditure','Diphtheria' , 'HIV/AIDS','GDP','Population','thinness 1-19 years','thinness 5-9 years','Income composition of resources','Schooling']]
y=data[['Life expectancy']]
# Split data 80% for training and 20% for testing
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size =0.2)

# Instantiate linear regression class
regression=LinearRegression()

# Train the model by providing 80% of training data
fit = regression.fit(x_train,y_train)

# predict the target variable using test data
regression.predict(x_test)
# print accuracy metric which is 83%
print(regression.score(x_test,y_test))
# dump the trained model to load it in app.py file
pickle.dump(fit,open('model.pkl','wb'))

