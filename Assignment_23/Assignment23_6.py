import pandas as pd 
import DataFrameModule

def DescendingOrder():

    df = DataFrameModule.GetDataFrame()
    print("Total sorted in descending order:")


    df.insert(4,"Total" , df["Math"] + df["Science"] + df["English"]) # Index 1, Column, values
    
    sorted_df = df.sort_values(by= ["Total"], ascending=False)
    print(sorted_df)

def main():

    DescendingOrder()    

if __name__=="__main__":
    main()


