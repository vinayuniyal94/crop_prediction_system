import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

# Dictionary as an input to machine learning model
user_input = {
    # "State_Name":"Uttar Pradesh",
    # "Season":"Kharif",
    # "Crop":"Maize",
    # "Area":229,
}


# data preprocessing function
def pre_process(df):

    def label_encoding(dataset,data_colounm):
        label = LabelEncoder()
        dataset[data_colounm] = label.fit_transform(dataset[data_colounm])

    label_encoding(df,"State_Name")
    label_encoding(df,"Season")
    label_encoding(df,"Crop")

    return df


# calling data preprocessing funtion then calling the model for correct prediction
def prediction(df):
    data = pre_process(df)
    model = joblib.load("ML/crop_model.pkl")
    result = model.predict(data)
    return result


def getData(context):
    # context dictionary assiging to user_input dictionary
    user_input = context
    user_input = pd.DataFrame(user_input, index=[0])

    # calling prediction method with user_input dictionary as input
    x = prediction(user_input)

    return int(x[0])
