import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt

def BarDiagramofStudent():

    df = DataFrameModule.GetDataFrame()
    print("Total sorted in descending order:")

    df.insert(4,"Total" , df["Math"] + df["Science"] + df["English"]) # Index 1, Column, values
    
    plt.bar(df["Name"], df["Total"])
    plt.xlabel("Students Name")
    plt.ylabel("Total Marks")
    plt.title("Bar Plot")
    plt.show()


def main():

    BarDiagramofStudent()    

if __name__=="__main__":
    main()


