import pandas as pd


def main():

    Data = {"Age" : [18,22,25,30,35]}
    df = pd.DataFrame(Data)

    df ["Normalized values"] = (df["Age"] - df["Age"].min()) / (df["Age"].max() - df["Age"].min())

    print(df["Normalized values"])

if __name__=="__main__":
    main()

