import pandas as pd 

def parser(file):
    i_csv = pd.read_csv(file)

    label_col = i_csv["species"]
    filename = i_csv["filename"]

    species = ["bewickii", "polyglottos", "migratorius", "melodia", "cardinalis"]
    species_label = {species[i]: i for i in range(len(species))}

    df = [[str, str] for _ in range(len(label_col))]
    for i in range (len(label_col)):
        df[i] = [species_label[label_col[i]], filename[i]]

    i2_csv = pd.DataFrame(df)

    o_csv = i2_csv.sample(frac=1).reset_index(drop=True)

    o_csv.to_csv("data.csv", index=False)
