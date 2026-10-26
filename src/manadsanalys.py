import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")   # Läs in försäljningsdata från CSV-filen

df_manad = df.copy()   # Skapa en kopia för månadsanalysen utan att ändra originaldata

df_manad["date"] = pd.to_datetime(df_manad["date"])   # Omvandla datumkolumnen från sträng till datetime

df_manad["månad"] = df_manad["date"].dt.month   # Skapa en ny kolumn med månadsnummer (1–12) från datumet

def månadsförsäljning(df):
    return df.groupby("månad")["revenue"].sum()

def månadsförsäljning_kategori(df):
    return df.groupby(["category", "månad"])["revenue"].sum()

def månadsförsäljning_stad(df):
    return df.groupby(["city", "månad"])["revenue"].sum()

def antal_enheter_månad(df):
    return df.groupby("månad")["units"].sum()

def antal_unika_order_månad(df):
    return df.groupby("månad")["order_id"].nunique()





