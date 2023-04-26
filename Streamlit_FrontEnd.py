import streamlit as st
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
from sklearn.ensemble import GradientBoostingRegressor
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,\
    mean_squared_error, mean_absolute_percentage_error
import missingno as msno 
import warnings
from features_page import  features,main ,df
from explore import visualization , correlation



st.title("House Price Prediction Application")
st.image("house.jpeg",width=700)

num_dict={}
obj_dict={}
page = st.sidebar.selectbox("Explore Or Predict", ("features", "explore"))


if page == "features":

    # features()
    # df()
    main()

    with open('data_description.txt', 'r') as f:
        data_description =f.readlines()
    st.sidebar.write('|Please Click The Arrows Below To Find out What The Acronyms In The Feature Stand For|',data_description)

if page == "explore":
    st.title('The visualization and Correlation Parts are Used only for having insight of The Model Training dataset')
    exp=st.sidebar.selectbox('correlation or visualization',('correlation','visualization'))
    if exp=='visualization':
        visualization()
    if exp=='correlation':
        correlation()
# if page == "Acronym and description":
#     with open('data_description.txt', 'r') as f:
#         data_description =f.readlines()
#         st.write('click on the arrows',data_description)











