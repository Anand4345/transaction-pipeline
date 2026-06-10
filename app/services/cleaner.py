def clean_data(df):

    df.columns = df.columns.str.lower()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df["amount"] = df["amount"].replace(r"[$,]", "", regex=True).astype(float)

    df["status"] = df["status"].str.upper()

    df["category"] = df["category"].fillna("Uncategorised")

    df = df.drop_duplicates()

    return df