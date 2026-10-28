import pandas as pd
import matplotlib.pyplot as plt

def visa_manadsforsaljning(omsattning):
    månader = omsattning.index
    värden = omsattning.values
    etiketter = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]

    plt.figure(figsize=(9, 5))
    plt.bar(månader, värden, width=0.6)

    plt.title("Månadsförsäljning – första halvåret 2024")
    plt.xlabel("Månad")
    plt.ylabel("Omsättning (kr)")
    plt.xticks(månader, etiketter)
    plt.grid(axis="y")
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


def visa_manadsforsaljning_stad(omsattning_stad):
    """Visar månadsförsäljning uppdelad per stad som staplat stapeldiagram."""

    pivot = omsattning_stad.unstack(level=0, fill_value=0)

    totals = pivot.sum(axis=1)
    procent = pivot.div(totals, axis=0) * 100

    fig, ax = plt.subplots(figsize=(10, 6))

    pivot.plot(kind="bar", stacked=True, ax=ax)

    ax.set_title("Månadsförsäljning per stad – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Omsättning (kr)")
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"], rotation=45)
    ax.legend(title="Stad", bbox_to_anchor=(1.02, 1), loc="upper left")
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    # Totalsumma ovanför varje stapel
    #for i, total in enumerate(totals):
       # ax.text(i, total + total * 0.01, f"{int(total):,}".replace(",", " "),
               # ha="center", va="bottom", fontsize=10)

    # Procent inne i varje segment
    for i in range(len(pivot.index)):
        kumulativ_hojd = 0
        for kolumn in pivot.columns:
            värde = pivot.loc[pivot.index[i], kolumn]
            proc = procent.loc[pivot.index[i], kolumn]

            if värde > 0:
                y_pos = kumulativ_hojd + värde / 2

                if proc >= 5:   # visa bara om segmentet inte är för litet
                    ax.text(i, y_pos, f"{proc:.0f}%",
                            ha="center", va="center", fontsize=9, color="black")

                kumulativ_hojd += värde

    plt.tight_layout()
    plt.show()

def visa_antal_enheter_manad(antal_enheter):
    """Visar antal sålda enheter per månad."""

    manader = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]

    fig, ax = plt.subplots(figsize=(9, 5))

    staplar = ax.bar(
        antal_enheter.index,
        antal_enheter.values,
        width=0.6,
        color="steelblue"
    )

    ax.set_title("Antal sålda enheter – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Antal sålda enheter")

    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(manader)

    ax.bar_label(staplar, padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()

def visa_antal_order_manad(antal_order):
    """Visar antal unika beställningar per månad."""

    manader = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]

    fig, ax = plt.subplots(figsize=(9, 5))

    staplar = ax.bar(
        antal_order.index,
        antal_order.values,
        width=0.6,
        color="steelblue"
    )

    ax.set_title("Antal unika order – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Antal order")

    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(manader)

    ax.bar_label(staplar, padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()

def visa_medelordervarde_manad(medelordervarde):
    """Visar genomsnittligt ordervärde per månad."""

    manader = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]

    fig, ax = plt.subplots(figsize=(9, 5))

    staplar = ax.bar(
        medelordervarde.index,
        medelordervarde.values,
        width=0.6,
        color="steelblue"
    )

    ax.set_title("Genomsnittligt ordervärde – första halvåret 2024")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Genomsnittligt ordervärde (kr)")

    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_xticklabels(manader)

    ax.bar_label(staplar, fmt="%.0f kr", padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

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

def visa_kategori_och_stad(omsattning_kategori, omsattning_stad):

    kategori = omsattning_kategori.unstack(level=0, fill_value=0)
    stad = omsattning_stad.unstack(level=0, fill_value=0)

    manader = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]

    # Skapa två diagram bredvid varandra
    fig, ax = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Vänster diagram – kategorier
    kategori.plot(kind="bar", stacked=True, ax=ax[0])

    ax[0].set_title("Omsättning per kategori")
    ax[0].set_xlabel("Månad")
    ax[0].set_ylabel("Omsättning (kr)")
    ax[0].set_xticklabels(manader, rotation=45)
    ax[0].legend(title="Kategori", fontsize=8)

    # Höger diagram – städer
    stad.plot(kind="bar", stacked=True, ax=ax[1])

    ax[1].set_title("Omsättning per stad")
    ax[1].set_xlabel("Månad")
    ax[1].set_xticklabels(manader, rotation=45)
    ax[1].legend(title="Stad", fontsize=8)

    plt.tight_layout()
    plt.show()