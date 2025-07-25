import pandas as pd

def main():

    Data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
        }

    df = pd.DataFrame(Data)
    df.insert(4, "Gender", ["Male", "Male", "Female"])

    grouped_data = df.groupby("Gender")

    for x, y in grouped_data:
        print(f'{x}\n{y}\n')

    print("Average Data of group by values")
    Avg_data = grouped_data[["Math","Science","English"]].mean()    
    print(Avg_data)

if __name__=="__main__":
    main()

