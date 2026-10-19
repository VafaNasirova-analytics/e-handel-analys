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