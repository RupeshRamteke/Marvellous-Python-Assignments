import pandas as pd
import numpy as np

def main():

    Data = {"Marks" : [45,67,88,32,76]}
    df = pd.DataFrame(Data)

    df["Marks"] = np.where(df["Marks"] <= 50, "Fail", df["Marks"])

    print("\nDatframe after repalcing less than 50 with fail:")
    print(df)

if __name__=="__main__":
    main()

