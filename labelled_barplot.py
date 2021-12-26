# Libraries to help with reading and maintaining data
import numpy as np
import pandas as pd

def labelled_barplot(data, feature, perc=False, n=None):
    """
    Barplot with percentage at the top

    data: Dataframe
    feature: datafrmae column
    perc: Wether to display percentage instead of counts ( Default is false)
    n: Display the top n category, levels (default is None, i.e display al levels.)
    """
    # Get length of the column
    total = len(data[feature])
    count = data[feature].nunique()
    if n is None:
        plt.figure(figsize=(count + 1, 5))
    else:
        plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=5)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n].sort_values(),
    )
    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # Percentage of each class of teh category
        else:
            label = p.get_height()  # Count of each level of teh category

    x = p.get_x() + p.get_width() / 2  # Width of teh plot
    y = p.get_height()  # Height of the plot

    ax.annotate(
        label,
        (x, y),
        ha="center",
        va="center",
        size=12,
        xytext=(0, 5),
        textcoords="offset points",
    )  # Annotate the percentage


plt.show()  # Show the plot


# function to create labeled barplots
