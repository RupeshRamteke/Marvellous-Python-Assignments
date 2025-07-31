import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def DiabeticPredictor(dataset):

    df = pd.read_csv(dataset)

    print("First five rows are :")
    print(df.head())

    print("Display information of column")
    print(df.info)

    print("Data types of columns")
    print(df.dtypes)

    print("Check fo null value")
    print(df.isnull().any().any())

    print("Display basic statics of data")
    print(df.describe())

    df["Outcome"].hist(bins= 30)
    plt.title("Distribution of Target Variable")
    plt.xlabel("Target Variable value")
    plt.ylabel("Frequency")
    plt.show()

    plt.boxplot(df)
    plt.title("Basic Boxplot")
    plt.ylabel("Values")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Paiplot ", y = 1.02)
    plt.show()

    x = df.drop(columns=["Outcome"])
    y = df["Outcome"]

    x.replace(0, np.nan, inplace=True)
    mean_value = x.mean()
    x.fillna(mean_value, inplace=True)

    print(x)

    scalar = StandardScaler()
    scaled_data = scalar.fit_transform(df)

    print(scaled_data)

    print("\nMean of each feature:", scalar.mean_)
    print("Standard Deviation of each feature :", np.sqrt(scalar.var_))

    #Train data using logistic regression

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 42)

    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("Logistic regression accuracy is :", accuracy)

    #confussion Matrix logistic regression
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Logistic regression confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Precision Matrix for Logistic Regression
    precision = precision_score(y_test, y_pred, average="weighted")
    print("Logistic Regression for precision matrix  :", precision)

    #Recall score for Logistic Regression
    recall = recall_score(y_test,y_pred)
    print("Logistic Regression for recall score  :", recall)

    #F1 score for Logistic Regression
    f1_LogReg = f1_score(y_test,y_pred, average="weighted")
    print("Logistic Regression for F1 Score  :", f1_LogReg)

    #Moving data in CSV file
    LogReg_Pred= y_pred

    #Train data using KNeighborsClassifier

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("KNeighborsClassifier accuracy is :", accuracy)

    #confussion Matrix for KNeighborsClassifier
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(" KNeighborsClassifier confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Precision Matrix for KNeighborsClassifier
    precision = precision_score(y_test, y_pred, average="weighted")
    print("KNeighborsClassifier for precision matrix :", precision)

    #Recall score for KNeighborsClassifier
    recall = recall_score(y_test,y_pred)
    print("KNeighborsClassifier for recall score  :", recall)

    #F1 score for KNeighborsClassifier
    f1_KNN = f1_score(y_test,y_pred, average="weighted")
    print("Logistic Regression for F1 Score  :", f1_KNN)

    #Moving data in CSV file
    KNN_Pred= y_pred

    #Train data using Decision Tree

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("Decision Tree accuracy is :", accuracy)

    #confussion Matrix for Decision Tree
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Decision Tree confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Precision Matrix for Decision Tree
    precision = precision_score(y_test, y_pred, average="weighted")
    print("Decision Tree for precision matrix  :", precision)

    #Recall score for Decision Tree
    recall = recall_score(y_test,y_pred)
    print("Decision Tree for recall score  :", recall)

    #F1 score for Decision Tree
    f1_DecTree = f1_score(y_test,y_pred, average="weighted")
    print("Logistic Regression for F1 Score  :", f1_DecTree)

    #Moving data in CSV file
    DecTree_Pred= y_pred

    #Define mapping dictionary
    mapping = {0: "Diabetic", 1: "Non-Diabetic"}

    #Apply the mapping to convert numeric prediction to string
    LR_Str = [mapping[pred] for pred in LogReg_Pred]
    KNN_Str = [mapping[pred] for pred in KNN_Pred]
    DT_Str = [mapping[pred] for pred in DecTree_Pred]

    data = {
        "Sr.no" : range(len(DecTree_Pred)),
        "Liner Regression" : LR_Str,
        "Knn" : KNN_Str,
        "Decision Tree" : DT_Str
    }

    df = pd.DataFrame(data)
    df.to_csv("Prediction_of_All_Algorithm.csv", index=False)

def main():
    DiabeticPredictor("diabetes.csv")

if __name__=="__main__":
    main()