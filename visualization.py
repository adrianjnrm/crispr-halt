# visualization.py
# Description: Visualize simulation result
import matplotlib.pyplot as plt

def plot_hiv_clearance(value):
    fig, ax = plt.subplots()
    ax.bar(["HIV Remaining"], [value], color="crimson")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Fraction of HIV Provirus Remaining")
    ax.set_title("CRISPR/Cas9 HIV Eradication Simulation")
    return fig