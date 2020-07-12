# Life Expectancy Prediction

[![OpenFaaS](https://img.shields.io/badge/Framework-Flask-darkblue.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Model-LinearRegression-darkgreen.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Language-Python-purple.svg)](https://www.openfaas.com)

## This web app is to predict life expectancy based on input features 

## DATASET
    -- The dataset contains 22 columns and 2938 rows.
    -- Out of which 20 features are used to predict the target variable life expectancy.

## PRE REQUISITES
    -- The file requirements.txt contains all the requisites to be installed.
    -- You can run the following command in the terminal to install all the packages.
    ``` 
        pip install -r requirements.txt 
    ```

## STRUCTURE OF THE APP
    -- static folder contains the required css and image files.
    -- template folder consists of all html files.
    -- model.py is the file where the data for train and test is split and evaluated the performance using accuracy(r2 score) metric.
    -- app.py is the file where the model is loaded and the form inputs given in the web page is collected to make some prediction.

## WORKING
    -- Navigate to the project folder and run
        ``` 
            python3 app.py 
        ```
    -- The server is running at
         ```
             http://127.0.0.1:5000
         ```


