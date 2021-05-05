import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def cm_to_inch(value):
    """To change from cm to inch"""

    return value/2.54


def histogram_figure(x, y, x_label, y_label, rooth_path, name_fig, ylim1=None, ylim2=None):
    """Creating an histogram """

    # Creating the figure
    sns.set()
    plt.figure(figsize=(cm_to_inch(25),cm_to_inch(15)))
    plt.bar(x=x, height=y, facecolor='#3d4248')

    # Labels
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")
    if ylim1 != None:
        plt.ylim(ylim1, ylim2)

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()


def linediagram_figure(x, y, x_label, y_label, rooth_path, name_fig):
    """ Creating a line diagram """

    # Creating the figure
    sns.set()
    plt.figure(figsize=(cm_to_inch(25),cm_to_inch(15)))
    plt.plot(x, y, color='#3d4248', marker=".", markersize=15, linewidth= 3, label="Year")

    # Labels
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()


def correlation_matrix(df):
    """ Creating a correlation matrix """
    
    # Creating the figure
    plt.figure(figsize=(cm_to_inch(30),cm_to_inch(20)))

    correlation_ = df.corr()
    heatmap_ = sns.heatmap(correlation_, cmap="bone",annot=True)
    fig_cor_ = heatmap_.get_figure()

    # Labels
    plt.yticks(va="center", rotation = 0)


def piechart_figure_6labels(labels, name_fig, rooth_path, x1=None, x2=None, x3=None, x4=None, x5=None, x6=None, x7=None):
    """ Creating a pie chart from 7 to 2 pies """

    # Creating the figure
    sns.set()
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(20)))

    if x7 != None:
        colors = ["#3d4248", "#525960", "#6a727c", "#838b95", "#9fa5ad", "#babfc4", "#d6d9dc"]
        plt.pie([x1, x2, x3, x4, x5, x6, x7], labels = labels, colors=colors, autopct="%.1f %%")

    elif x6 != None:
        colors = ["#3d4248", "#525960", "#6a727c", "#838b95", "#9fa5ad", "#babfc4"]
        plt.pie([x1, x2, x3, x4, x5, x6], labels = labels, colors=colors, autopct="%.1f %%")

    elif x5 != None:
        colors = ["#3d4248", "#525960", "#6a727c", "#838b95", "#9fa5ad"]
        plt.pie([x1, x2, x3, x4, x5], labels = labels, colors=colors, autopct="%.1f %%")

    elif x4 != None:
        colors = ["#6a727c", "#9fa5ad", "#babfc4", "#d6d9dc"]
        plt.pie([x1, x2, x3, x4], labels = labels, colors=colors, autopct="%.1f %%")
    
    elif x3 != None:
        colors = ["#6a727c", "#9fa5ad", "#d6d9dc"]
        plt.pie([x1, x2, x3], labels = labels, colors=colors, autopct="%.1f %%")

    elif x2 != None:
        colors = ["#3d4248", "#9fa5ad"]
        plt.pie([x1, x2], labels = labels, colors=colors, autopct="%.1f %%")    

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()


def checking_outliers_boxplot(x, Values):

    """Checking outliers"""

    # Boxplot
    sns.set_style('darkgrid')
    plt.boxplot(x, sym='.')
    plt.title('Boxplot')
    plt.xlabel(Values)