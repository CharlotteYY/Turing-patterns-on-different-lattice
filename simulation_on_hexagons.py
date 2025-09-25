import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from model_librareis.hexal_lat import generate_hexagonal_lattice
from model_librareis.gray_scott_hexal import simulate_gray_scott_on_hexagons


# Main function to run the simulation
if __name__ == "__main__":
    
    # Parameters
    n_rows = 1150
    n_cols = 1000
    LX = 1000
    LY = 1000
    f_values = [0.039]
    k_values = [0.058]
    
    perturbation_level = 0

    for f in f_values:
        for k in k_values:
            simulate_gray_scott_on_hexagons(n_rows=n_rows,
                                            n_cols=n_cols,
                                            LX=LX,
                                            LY=LY,
                                            f=f,
                                            k=k,
                                            perturbation_level=perturbation_level,
                                            stoptime=400)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])