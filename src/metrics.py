def calc_aov(df):
    """
    Calculate the Average Order Value (AOV) for a given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing order data.

    Returns:
    float: The calculated AOV.
    """
    return df["revenue"].mean().round(2)

