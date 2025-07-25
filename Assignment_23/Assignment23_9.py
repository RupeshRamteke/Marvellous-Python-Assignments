import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt
import numpy as np

def GetMaxScoreinSci():

        Data = {
                "Name" : ["Amit", "Sagar", "Pooja"],
                "Math" : [85,90,78],
                "Science" : [92,88,80],
                "English" : [75,85,82]
        }

        df = pd.DataFrame(Data)

        print(df)

        df.fillna(df.mean(numeric_only= True), inplace=True)

        print(df)

def main():

        GetMaxScoreinSci()
    

if __name__=="__main__":
    main()


