import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def PlayPredictor(dataset):

    df = pd.read_csv(dataset)
    df.drop(columns= ["Unnamed: 0"], inplace=True)
    #print(df)

    le = LabelEncoder()

    df["Whether"] = le.fit_transform(df["Whether"])
    df["Temperature"] = le.fit_transform(df["Temperature"])

    #print(df)

    x= df.drop(columns=["Play"])
    y = df["Play"]

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(x,y,test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_Train,Y_Train)
    y_pred = model.predict(X_Test)


    new_data_point = [[0,1]]
    predicted_class = model.predict(new_data_point)
    print("Predicted class for new data point", predicted_class)

    new_data_point = [[2,1]]
    predicted_class = model.predict(new_data_point)
    print("Predicted class for new data point", predicted_class)

    new_data_point = [[1,0]]
    predicted_class = model.predict(new_data_point)
    print("Predicted class for new data point", predicted_class)    

    accuracy= accuracy_score(Y_Test,y_pred)*100
    print(accuracy)

    for i in range (2,8):
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X_Train,Y_Train)
        y_pred = model.predict(X_Test)
        accuracy = accuracy_score(Y_Test,y_pred)*100
        print(accuracy)


def main():

    PlayPredictor("PlayPredictor.csv")

if __name__=="__main__":
    main()