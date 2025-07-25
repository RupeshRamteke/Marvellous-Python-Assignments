import pandas as pd 
import DataFrameModule

def DataDescription():

    df = DataFrameModule.GetDataFrame()
    print("Data Description is as Follows:")
    print(df.describe())

def main():

    DataDescription()    

if __name__=="__main__":
    main()


