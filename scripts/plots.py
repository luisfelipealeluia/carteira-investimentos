import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_plots():

    df = pd.read_excel(os.path.join(os.path.dirname(os.getcwd()), "excel", "portfolio.xlsx"))
    df["Total"] = df["Total"].apply(lambda x: round(x, 2))

    plot1 = df.plot.bar(x='Ativo', y='Total').get_figure()
    plt.tight_layout()
    plot1.savefig(os.path.join(os.path.dirname(os.getcwd()), "temp", "barplot.png"))

    plot2 = df.boxplot(column=['Total']).get_figure()
    plt.tight_layout()
    plot2.savefig(os.path.join(os.path.dirname(os.getcwd()), "temp", "boxplot.png"))

    plot3 = df.groupby(['Moeda']).sum().plot.pie(y='Total').get_figure()
    plt.tight_layout()
    plot3.savefig(os.path.join(os.path.dirname(os.getcwd()), "temp", "pieplot.png"))

    df.to_excel(os.path.join(os.path.dirname(os.getcwd()), "excel", "portfolio.xlsx"))
