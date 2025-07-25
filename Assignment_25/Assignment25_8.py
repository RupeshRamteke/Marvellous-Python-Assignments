import pandas as pd
import numpy as np

def main():

    Data = {"Marks" : [85,np.nan,90,np.nan,95]}
    df = pd.DataFrame(Data)

    print("Original Dataframe")
    print(df)

    df_interpolated = df.interpolate()

    print("\nDataFrame after Linear interpolation:")
    print(df_interpolated)


if __name__=="__main__":
    main()

