

def månadsförsäljning(df):
    """Returnerar total omsättning per månad."""
    return df.groupby("månad")["revenue"].sum()

def månadsförsäljning_kategori(df):
    """Returnerar omsättning per produktkategori och månad."""
    return df.groupby(["category", "månad"])["revenue"].sum()

def månadsförsäljning_stad(df):
    """Returnerar omsättning per stad och månad."""
    return df.groupby(["city", "månad"])["revenue"].sum()

def antal_enheter_månad(df):
    """Returnerar antal sålda enheter per månad."""
    return df.groupby("månad")["units"].sum()

def antal_unika_order_månad(df):
    """Returnerar antal unika beställningar per månad."""
    return df.groupby("månad")["order_id"].nunique()

def ordervärde_medel_månad(df):
    """Returnerar genomsnittligt ordervärde per månad."""
    return månadsförsäljning(df) / antal_unika_order_månad(df)

def antal_electronics_manad(df):
    """Returnerar antal sålda Electronics-enheter per månad."""

    electronics = df[df["category"] == "Electronics"]

    return electronics.groupby("månad")["units"].sum()






