import pandas as pd

def main():

    Data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
        }

    df = pd.DataFrame(Data)
    df ["Normalized values"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())

    #normalized funtion
    #(x-xmin)/(xmax-xmin)
    #(85-78)/(90-78) = 7/12 = 0.5833
    #(90-78)/(90-78) = 12/12 =1 
    #(78-78)/(90-78) =0/12 = 0
    print(df["Normalized values"])


if __name__=="__main__":
    main()

