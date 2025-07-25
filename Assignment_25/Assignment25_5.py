import pandas as pd
from sklearn.model_selection import train_test_split

def main():

    Data = {"Age" : ["22","25","47","52","46","56"], "Purchase" : [0,1,1,0,1,0]}

    df = pd.DataFrame(Data)

    x = df["Age"]
    y = df["Purchase"]

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.5, random_state= 42)

    print("Data split in train/test is as follow:")
    print("X_Train :", X_train)
    print("X_Test :", X_test)
    print("Y_Train :", Y_train)
    print("Y_Test :", Y_test)

if __name__=="__main__":
    main()

