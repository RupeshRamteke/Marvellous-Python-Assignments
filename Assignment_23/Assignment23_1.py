import pandas as pd 
import DataFrameModule

def DataframeInfo():

    df = DataFrameModule.GetDataFrame()

    print("Basic information of data :")
    print("Dimension of data is :", df.shape)
    print("Columns name is :",df.columns)
    print("Datatype is :",df.dtypes)
    #print(df["Name"].dtype)
    #print(df["Math"].dtype)
    #print(df["Science"].dtype)
    #print(df["English"].dtype)

def main():

    DataframeInfo()    

if __name__=="__main__":
    main()


