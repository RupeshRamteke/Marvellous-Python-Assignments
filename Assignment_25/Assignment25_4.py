import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():

    Data = {"Department" : ["HR", "IT", "Finance", "HR", "IT"]}

    df = pd.DataFrame(Data)
    x = df[["Department"]]
    encoder = OneHotEncoder(handle_unknown= "ignore", sparse_output=False)

    drop_enc = encoder.fit_transform(x)

    encoded_df = pd.DataFrame(drop_enc, columns=encoder.get_feature_names_out(["Department"]))

    df_encoded = pd.concat([df.drop("Department", axis = 1), encoded_df], axis=1)

    print(df_encoded)

if __name__=="__main__":
    main()

