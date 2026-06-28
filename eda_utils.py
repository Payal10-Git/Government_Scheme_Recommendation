import os
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
sns.set_palette("Set2")


def create_graph_folder():

    os.makedirs("../reports/graphs", exist_ok=True)


def save_plot(name):

    plt.tight_layout()

    plt.savefig(

        f"../reports/graphs/{name}.png",

        dpi=300,

        bbox_inches="tight"

    )

    plt.show()