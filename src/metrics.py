def calc_aov(df):
    
    """Beräknar genomsnittligt ordervärde (AOV)."""

    antal_order = df["order_id"].nunique()

    if antal_order == 0:
        return 0.0

    return round(df["revenue"].sum() / antal_order, 2)


def calc_total_revenue(df):
    """Beräknar företagets totala intäkt."""
    return round(df["revenue"].sum(),2)

def calc_total_units(df):
    """Beräknar total antal sålda enheter"""
    return df["units"].sum()

def calc_total_orders(df):
    """Beräknar antalet unika beställningar."""
    return df["order_id"].nunique()

def revenue_by_category(df):
    """Beräknar total intäkt per produktkategori."""
    return round(df.groupby("category")["revenue"].sum().sort_values(ascending=False),2)

def units_by_category(df):
    """Beräknar antal sålda enheter per produktkategori"""
    return df.groupby("category")["units"].sum().sort_values(ascending=False)

def revenue_per_unit_by_category(df):
    """Beräknar genomsnittlig intäkt per såld enhet och produktkategori."""

    intakter = df.groupby("category")["revenue"].sum()
    enheter = df.groupby("category")["units"].sum()

    intakt_per_enhet = intakter.div(enheter.replace(0, float("nan")))

    return intakt_per_enhet.round(2).sort_values(ascending=False)


def revenue_by_city(df):
    """Beräknar total omsättning per stad."""
    return df.groupby("city")["revenue"].sum().sort_values(ascending=False)

def månadsförsäljning(df):
    """Returnerar total omsättning per månad."""
    return df.groupby("månad")["revenue"].sum().sort_index()

def månadsförsäljning_kategori(df):
    """Returnerar omsättning per produktkategori och månad."""
    return df.groupby(["category", "månad"])["revenue"].sum().sort_index()

def månadsförsäljning_stad(df):
    """Returnerar omsättning per stad och månad."""
    return df.groupby(["city", "månad"])["revenue"].sum().sort_index()

def antal_enheter_månad(df):
    """Returnerar antal sålda enheter per månad."""
    return df.groupby("månad")["units"].sum().sort_index()

def antal_unika_order_månad(df):
    """Returnerar antal unika beställningar per månad."""
    return df.groupby("månad")["order_id"].nunique().sort_index()

def ordervärde_medel_månad(df):
    """Returnerar genomsnittligt ordervärde per månad."""
    return månadsförsäljning(df) / antal_unika_order_månad(df)

def antal_electronics_manad(df):
    """Returnerar antal sålda Electronics-enheter per månad."""

    electronics = df[df["category"] == "Electronics"]

    return electronics.groupby("månad")["units"].sum().sort_index()


def order_statistics(df):
    """Beräknar statistik över ordervärden."""

    ordervarden = df.groupby("order_id")["revenue"].sum()

    return ordervarden.describe().round(2)


def order_outliers(df, return_limits=False):
    """Identifierar avvikande ordervärden med IQR-metoden."""

    ordervarden = df.groupby("order_id")["revenue"].sum()

    q1 = ordervarden.quantile(0.25)
    q3 = ordervarden.quantile(0.75)

    iqr = q3 - q1

    nedre_grans = q1 - 1.5 * iqr
    ovre_grans = q3 + 1.5 * iqr

    avvikande = ordervarden[
        (ordervarden < nedre_grans) |
        (ordervarden > ovre_grans)
    ]

    avvikande = avvikande.sort_values(ascending=False)

    if return_limits:
        return avvikande, q1, q3, iqr, nedre_grans, ovre_grans

    return avvikande