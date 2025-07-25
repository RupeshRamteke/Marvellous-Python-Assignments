import pandas as pd

def main():

    Data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
        }

    df = pd.DataFrame(Data)
    df.insert(4, "Gender", ["Male", "Male", "Female"])
    print("Data before encoding")
    print(df)

    df["Gender"] = df["Gender"].map({"Female" : 0, "Male" :1})
    print("Data after encoding")
    print(df)    


if __name__=="__main__":
    main()

