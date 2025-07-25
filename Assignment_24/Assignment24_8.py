import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

    Data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
        }

    df = pd.DataFrame(Data)

    df.insert(4,"Total", df["Math"]+df["Science"]+df["English"])

    conditional_series = np.where(df["Total"] >= 250, "Pass", "Fail")
    df.insert(5, "Status", conditional_series)

    X = df["Name"]
    Y = df["Math"]

    plt.hist(Y, bins = 100, color = "skyblue", edgecolor = "black")

    plt.xlabel("Maths Marks")
    plt.ylabel("Frequency")
    plt.title("Histogram of Maths Marks for all Students")

    plt.show()
    
if __name__=="__main__":
    main()

