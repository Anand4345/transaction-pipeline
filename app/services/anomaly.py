def detect_anomalies(df):

    df["is_anomaly"] = False

    for acc in df["account_id"].unique():
        median = df[df["account_id"] == acc]["amount"].median()

        df.loc[
            (df["account_id"] == acc) &
            (df["amount"] > 3 * median),
            "is_anomaly"
        ] = True

    return df