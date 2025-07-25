import pandas as pd
import matplotlib.pyplot as plt

def main():

    Data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
        }

    df = pd.DataFrame(Data)

    Subject = ["Math", "Science", "English"]
    marks = df[df["Name"] == "Sagar"][["Math", "Science", "English"]].values.flatten()

    plt.pie(marks, labels=Subject)
    plt.title("Marks of Sagar")
    plt.show()


if __name__=="__main__":
    main()

