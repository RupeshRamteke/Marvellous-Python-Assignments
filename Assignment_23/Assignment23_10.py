import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt
import numpy as np


def DataDescripton():

        df = DataFrameModule.GetDataFrame()
        df.drop(columns= ["English"], inplace=True)
        print("Drop col English")
        print(df.head())

def main():

        DataDescripton()

if __name__=="__main__":
    main()


