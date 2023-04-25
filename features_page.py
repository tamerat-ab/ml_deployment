import streamlit as st  
import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle
import sys
sys.tracebacklimit=0




with open('numeric_dtype_features.pickle', 'rb') as f:
    numeric_features = pickle.load(f)

with open('object_dtype_features.pickle', 'rb') as f:
    object_features = pickle.load(f)


cols=[ {'object':object_features},{'int':numeric_features}]
dct={}
def features():
        s=[]
        dct={}
        x= {
            "object": st.sidebar.multiselect(
                'Select The Qualitative Data', cols[0]['object']#.unique()
            ),
            "int": st.sidebar.multiselect(
                'Select The Quantitative Data', cols[1]['int']#.unique()
            )
        }
       

        if x['object']:
            for i in  x['object']:


                s.append(i[:3])
                for j in s:
                    if s.count(j)>1:
                        st.write(f'You Selected "{i}" Criterion {s.count(j)} times!!!, only one criterion is permitted')
                        st.stop()

                        # raise Exception (f'You Selected "{i}" Criterion {s.count(j)} times!!!, only one criterion is permitted')


                dct[i]=1
        else:
            dct=dct
        if x['int']:
            for i in  x['int']:
                y=st.number_input(i)
                dct[i]=y
        else:
            dct=dct
        return dct


with open('train_data_features_col.pickle', 'rb') as f:
    train_data_features_col = pickle.load(f)

def dictionaries(dct_1):
    dct_2={}
    # dct_1=features()
    dict_kyes_list=list(dct_1.keys())
    set_dict = set(dict_kyes_list)
    set_col = set(train_data_features_col)
    diff_col=set_col.difference(set_dict)
    diff_col=list(diff_col)
    for j in diff_col:
        dct_2[j]=0
    dct_2
    merged_dict= {**dct_1,**dct_2}
    return merged_dict

def df(dct):

    df=pd.DataFrame([dct])
    # df.columns =train_data_features_col
    df=df[train_data_features_col]
    # df=pd.DataFrame([dct])
    return df

def category(df):
    col_higher_magnitude=[]
    col_lower_magnitude=[]
    col=df.columns
    for i in col:
        if any(df[i]>10):
            col_higher_magnitude.append(i)
        else:
            col_lower_magnitude.append(i)
    return (col_higher_magnitude, col_lower_magnitude)


def min_max(df,col_higher_magnitude,col_lower_magnitude):
    min_max_scaler = preprocessing.MinMaxScaler(feature_range =(0, 1))
    min_max_scaler_after = min_max_scaler.fit_transform(df[col_higher_magnitude])
    df_higher=pd.DataFrame(min_max_scaler_after,columns=col_higher_magnitude)
    df=pd.concat([df_higher,df[col_lower_magnitude]],axis=1)
    df=df[train_data_features_col]
    return df


def main():

    dct_1=features()
    dct=dictionaries(dct_1)
    df_1=df(dct)
    st.write(df_1)
    values=category(df_1)
    col_higher_magnitude,col_lower_magnitude=values
  
    with open('GradientBoostingRegressor.pickle','rb') as f:
            model=pickle.load(f)

    if st.button('Predict'):

        try:
            with open('GradientBoostingRegressor.pickle','rb') as f:
                model=pickle.load(f)
            df_2=min_max(df_1,col_higher_magnitude,col_lower_magnitude)
            df_pred=model.predict(df_2)
            df_pred=round(df_pred[0],2)
            return st.write(f'The Predicted Price,{df_pred} $')
        except:
            st.write('Please Insert At Least One Value For Both The Numeric and Object Datatype')
if __name__=='__main__':
    main()


