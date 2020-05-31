import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

# data = pd.read_csv("crop_production.csv")

user_input = {
    # "State_Name":"Uttar Pradesh",
    # "Season":"Kharif",
    # "Crop":"Maize",
    # "Area":229,
}


def pre_process(df):
#     data = data.drop(["District_Name","Crop_Year"], axis=1)

    def label_encoding(dataset,data_colounm):
        label = LabelEncoder()
        dataset[data_colounm] = label.fit_transform(dataset[data_colounm])

    label_encoding(df,"State_Name")
    label_encoding(df,"Season")
    label_encoding(df,"Crop")

    return df


def prediction(df):
    data = pre_process(df)
    model = joblib.load("ML/crop_model.pkl")
    result = model.predict(data)
    return result


def getData(context):
    user_input = context
    user_input = pd.DataFrame(user_input, index=[0])

    #print(user_input)
    x = prediction(user_input)
    print(x[0])
    return int(x[0])
