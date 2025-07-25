import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def main():

    Data = {"Age" : [25,30,45,35,22], "Salary" : [50000,60000,80000,65000,45000],"Purchased" : [1,0,1,0,1]}

    df = pd.DataFrame(Data)

    x = df.drop("Purchased", axis=1)
    y = df["Purchased"]

    X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size= 0.2, random_state=42)

    print("X_Train Data:")
    print(X_train)
    print("Y_Train Data:")
    print(Y_train)

    print("X_Test Data:") 
    print(X_test)
    print("X_Test Data:")
    print(Y_test)



if __name__=="__main__":
    main()

