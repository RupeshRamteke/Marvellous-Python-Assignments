import pandas as pd 
import DataFrameModule
import matplotlib.pyplot as plt
import numpy as np

def BarDiagramofStudent():

    df = DataFrameModule.GetDataFrame()

    x = np.array(["Math", "Science", "English"])
    marks = df[df["Name"] == "Amit"][["Math", "Science", "English"]].values.flatten()


    plt.plot(x,marks,marker = "o")

    
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Amit Line Plot")
    plt.grid(True)
    plt.show()


def main():

    BarDiagramofStudent()    

if __name__=="__main__":
    main()


