import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def Salespredictor(dataset):

    df = pd.read_csv(dataset)
    print("Data is as follow:")
    print(df)

    df.drop(columns= ["Unnamed: 0"], inplace=True)

    print("After removing unwanted columns")
    print(df.head())

    x= df.drop(columns=["sales"])
    y = df["sales"]

    X_Train, X_Test, Y_Train, Y_Test = train_test_split(x,y,test_size=0.5, random_state=42)

    model = LinearRegression()
    model.fit(X_Train,Y_Train)
    y_pred = model.predict(X_Test)

    plt.scatter(Y_Test,y_pred, color = "blue", label = "Predicted")
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("linear Regression : Actual vs, Predictor")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():

    Salespredictor("Advertising.csv")

if __name__=="__main__":
    main()   