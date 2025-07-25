import pandas as pd


def main():

    Data = {"Grade" : ["A+","B","A","C","B+"]}
    df = pd.DataFrame(Data)

    df["Grade"] = df["Grade"].map({"A+":"Excellent", "A":"Very Good", "B+": "Good", "B": "Average", "C": "Poor"})

    print(df)

if __name__=="__main__":
    main()

