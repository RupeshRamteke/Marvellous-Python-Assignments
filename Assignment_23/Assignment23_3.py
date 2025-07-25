import pandas as pd 
import DataFrameModule

def AddTotalColumn():

    df = DataFrameModule.GetDataFrame()
    print("Add Total col in Dataframe:")
    #df.insert(4,"Total" , df["Math"] + df["Science"] + df["English"])

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print(df)
    #print(df.head())

def main():

    AddTotalColumn()    

if __name__=="__main__":
    main()


