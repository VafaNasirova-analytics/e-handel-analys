import pandas as pd

data = pd.read_csv("data/ecommerce_sales.csv")

data["date"] = pd.to_datetime(data["date"])

data["månad"] = data["date"].dt.month

def månadsförsäljning(data):
    return data.groupby("månad")["revenue"].sum()

def månadsförsäljning_kategori(data):
    return data.groupby(["category", "månad"])["revenue"].sum()

def månadsförsäljning_stad(data):
    return data.groupby(["city", "månad"])["revenue"].sum()

def antal_enheter_månad(data):
    return data.groupby("månad")["units"].sum()

def antal_unika_order_månad(data):
    return data.groupby("månad")["order_id"].nunique()





