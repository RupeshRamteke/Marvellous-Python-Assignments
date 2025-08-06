import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score, roc_curve, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier


def BankTermDeposit(dataset):

    df = pd.read_csv(dataset, sep=";", header=0)

    print(df)

    # split data set in x & y
    x1 = df.drop(columns=["y"])
    y1 = df["y"]

    #repalce unknow value with nan
    x1.replace("unknown", np.nan, inplace=True)
    print(x1)

    #get mena value

    mean_value = df.fillna(df.mean(numeric_only=True))

    #replace nan value with mean
    x1.fillna(mean_value, inplace=True)

    print(df.describe())

    for col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        print(df)

    #feature scalar using standardscalar
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    print("\nScalad data (Mean=0, std Dev=1 fro each feature):")
    print(scaled_data)

    x = df.drop(columns=["y"])
    y = df["y"]

    ###################################################################################################################

    ##Train data using logistic regression
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 42)

    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("Logistic regression accuracy is :", accuracy)

    #confussion Matrix logistic regression
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Classification report for logistic regression

    class_report = classification_report(y_test, y_pred, target_names=["Yes","No"])
    print("Classification Report:")
    print(class_report)

    # ROC Score for logistic regression
    auc_score = roc_auc_score(y_test, y_pred)
    print(auc_score)


    # Visual of Confusion matrix for logistic regression
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Logistic regression confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    # Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Guess (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

    print(f"AUC Score: {auc_score:.2f}")

    #########################################################################################################################

    #Train data using KNeighborsClassifier


    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("KNeighborsClassifier accuracy is :", accuracy)

    #confussion Matrix for KNeighborsClassifier
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Classification report for KNeighborsClassifier

    class_report = classification_report(y_test, y_pred, target_names=["Yes","No"])
    print("Classification Report:")
    print(class_report)

    # ROC Score for KNeighborsClassifier
    auc_score = roc_auc_score(y_test, y_pred)
    print(auc_score)

    # Visual of Confusion matrix for KNeighborsClassifier
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("KNeighborsClassifier confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    # Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Guess (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

    print(f"AUC Score: {auc_score:.2f}")

    ###################################################################################################################

    #Train data using Random Forest Classifier

    model =RandomForestClassifier(n_estimators=150, max_depth=7, random_state=42)

    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)*100

    print("Random Forest Classifier accuracy is :",accuracy)    

    #confussion Matrix Random Forest Classifier
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Classification report for Random Forest Classifier

    class_report = classification_report(y_test, y_pred, target_names=["Yes","No"])
    print("Classification Report:")
    print(class_report)

    # ROC Score for Random Forest Classifier
    auc_score = roc_auc_score(y_test, y_pred)
    print(auc_score)

    # Visual of Confusion matrix for Random Forest Classifier
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Random Forest Classifier confusion matrix")
    plt.xlabel("Predicted value")
    plt.ylabel("Actual value")
    plt.show()

    #Calculate False Positive Rate (FPR), True Positive Rate (TPR), and thresholds
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    #Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % auc_score)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Guess (AUC = 0.50)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

    print(f"AUC Score: {auc_score:.2f}")


def main():

    BankTermDeposit("bank-full.csv")

if __name__=="__main__":
    main()
    