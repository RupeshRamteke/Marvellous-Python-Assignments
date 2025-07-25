import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():

    Data = {"City" : ["Pune", "Mumbai", "Delhi", "Pune", "Delhi"]}

    df = pd.DataFrame(Data)
    le = LabelEncoder()

    df["Category Encoder"] = le.fit_transform(df["City"])
    print("Data after label Encoding")
    print(df)


if __name__=="__main__":
    main()

