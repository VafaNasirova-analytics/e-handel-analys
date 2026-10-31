def aov_plot(df):
    """
    Create a histogram of order values with AOV.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing order data.
    """
    import matplotlib.pyplot as plt

    aov_total = df["revenue"].mean().round(2)

    plt.hist(df["revenue"], bins=70, color='steelblue', edgecolor='white')
    plt.title("Distribution of Order Values")
    plt.xlabel("Order Value (kr)")
    plt.ylabel("Frequency")
    plt.axvline(aov_total, color='black', linestyle='dashed', linewidth=2, label=f'AOV: {aov_total}kr')
    plt.legend()
    plt.show()


def aov_by_cat_plot(df, category_col="category"):
    """
    Create a bar plot of average order value by category.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing order data.
    category_col (str): The column name for the category variable.
    """
    import matplotlib.pyplot as plt

    aov_by_category = df.groupby(category_col)["revenue"].mean().round(2)

    aov_by_category.plot(kind='bar', color='steelblue')
    plt.title(f'Average Order Value by {category_col.capitalize()}')
    plt.xlabel(category_col.capitalize())
    plt.ylabel("Average Order Value (kr)")
    plt.show()


import matplotlib.pyplot as plt
import pandas as pd

def plot_revenue_by_category(category_revenue):
    """Visar total omsättning per produktkategori"""

    fig,ax = plt.subplots(figsize=(10, 6))

    category_revenue.plot(kind="bar", ax=ax, color="blue")

    ax.set_title("Total omsättning per produktkategori")
    ax.set_xlabel("Produktkategori")
    ax.set_ylabel("Omsättning i kronor")
    ax.yaxis.set_major_formatter(lambda x, pos: f"{x:,.0f}".replace(","," "))

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_units_by_category(category_units):
    """Visar antal sålda enheter per produktkategori"""

    fig, ax = plt.subplots(figsize= (10,6))

    category_units.plot(kind="bar", ax=ax, color="blue")

    ax.set_title("Antal sålda enheter per produktkategori")
    ax.set_xlabel("Produktkategori")
    ax.set_ylabel("Antal sålda enheter")

    ax.yaxis.set_major_formatter(lambda x, pos: f"{x:,.0f}".replace(",", " "))

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_revenue_by_city(city_revenue):
    """Visar total omsättning per stad."""

    fig, ax = plt.subplots(figsize= (10, 6))

    city_revenue.plot(kind="bar", ax = ax, color="blue")

    ax.set_title("Total omsättning per stad")
    ax.set_xlabel("Stad")
    ax.set_ylabel("Omsättning i kronor")

    ax.yaxis.set_major_formatter(
        lambda x, pos: f"{x:,.0f}".replace(",", " ")
    )

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()



def visa_manadsforsaljning_kategori(omsattning_kategori):
    pivot = omsattning_kategori.unstack(level=0, fill_value=0)

    ax = pivot.plot(
        kind="bar",
        stacked=True,
        figsize=(10, 6)
    )

    ax.set_title("Månadsförsäljning per kategori – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"], rotation=45)
    ax.set_ylabel("Omsättning (kr)")
    ax.legend(title="Kategori", loc="upper left", bbox_to_anchor=(1.02, 1))
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    # Totalsummor per månad
    totals = pivot.sum(axis=1)

    # Procent per kategori och månad
    procent = pivot.div(totals, axis=0) * 100

    # Skriv totalsumma ovanför varje stapel
    for i, total in enumerate(totals):
        ax.text(i, total + 5000, f"{int(total):,}".replace(",", " "),
                ha="center", va="bottom", fontsize=10)

    # Skriv procent i varje segment
    for i in range(len(pivot.index)):          # varje månad
        kumulativ = 0
        for kolumn in pivot.columns:           # varje kategori
            värde = pivot.iloc[i][kolumn]
            pct = procent.iloc[i][kolumn]

            if värde > 0 and pct >= 5:  # visa bara om segmentet är tillräckligt stort
                ax.text(
                    i,
                    kumulativ + värde / 2,
                    f"{pct:.0f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

            kumulativ += värde

    plt.tight_layout()
    plt.show()


def visa_electronics_enheter_manad(antal_enheter):
    """Visar antal sålda Electronics-enheter per månad."""

    fig, ax = plt.subplots(figsize=(9, 5))

    staplar = ax.bar(
        antal_enheter.index,
        antal_enheter.values,
        width=0.6,
        color="steelblue"
    )

    ax.set_title("Sålda Electronics-enheter – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Antal sålda enheter")

    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"], rotation=45)

    ax.bar_label(staplar, padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()

def visa_orderutveckling_index(antal_order, ordervarde):
    """Visar utvecklingen av orderantal och ordervärde, januari = 100."""
    tabell = pd.DataFrame({
        "Unika order": antal_order,
        "Ordervärde (kr)": ordervarde
    })

    tabell.index = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]
   

    kolumner = ["Unika order", "Ordervärde (kr)"]

    # Beräkna index med januari som bas
    index = tabell[kolumner].div(tabell[kolumner].iloc[0]) * 100

    fig, ax = plt.subplots(figsize=(11, 6))

    for kolumn in kolumner:
        ax.plot(
            index.index,
            index[kolumn],
            marker="o",
            linewidth=2,
            label=kolumn
        )

        # Visa faktiska värden vid punkterna
        for manad in index.index:
            varde = tabell.loc[manad, kolumn]
            y = index.loc[manad, kolumn]

            if kolumn == "Unika order":
                etikett = f"{varde:.0f} order"
                placering = 12
            else:
                etikett = f"{varde:,.0f} kr".replace(",", " ")
                placering = -18

            ax.annotate(
                etikett,
                (manad, y),
                xytext=(0, placering),
                textcoords="offset points",
                ha="center",
                fontsize=9
            )

    # Referenslinje för januari
    ax.axhline(100, color="gray", linestyle="--", alpha=0.5)

    ax.set_title(
        "Utveckling av unika order och genomsnittligt ordervärde\n"
        "(index, januari = 100)"
    )
    ax.set_xlabel("Månad")
    ax.tick_params(axis="x", labelrotation=45)
    ax.set_ylabel("Index (januari = 100)")

    ax.legend(loc="lower right")
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_ylim(65, 120)

    plt.tight_layout()
    plt.show()



def plot_order_distribution(df):
    """Visar fördelningen av ordervärden."""

    ordervarden = df.groupby("order_id")["revenue"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(ordervarden, bins=30, color="steelblue", edgecolor="white")

    ax.axvline(ordervarden.mean(), color="red",
               linestyle="--", label="Medelvärde")

    ax.axvline(ordervarden.median(), color="green",
               linestyle="--", label="Median")

    ax.set_title("Fördelning av ordervärden")
    ax.set_xlabel("Ordervärde (kr)")
    ax.set_ylabel("Antal beställningar")

    ax.xaxis.set_major_formatter(
        lambda x, pos: f"{x:,.0f}".replace(",", " ")
    )

    ax.legend()
    plt.tight_layout()
    plt.show()