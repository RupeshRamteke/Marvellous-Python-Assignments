import pandas as pd 
import DataFrameModule

def Namechange():

    df = DataFrameModule.GetDataFrame()
    print("Updated Name in Column:")

    
    df["Name"].replace("Pooja", "Puja", inplace=True)
    print(df.head())

def main():

    Namechange()    

if __name__=="__main__":
    main()


