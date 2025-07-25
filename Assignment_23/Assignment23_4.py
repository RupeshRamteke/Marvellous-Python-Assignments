import pandas as pd 
import DataFrameModule

def MaxScoreInSCi():

    df = DataFrameModule.GetDataFrame()
    print("Student who scores more than 85 in science are:")
    
    print(df[df("Science") > 85])

    #filtered_df = df.loc[df["Science"] > 85]
    #print(filtered_df)

def main():

    MaxScoreInSCi()    

if __name__=="__main__":
    main()


