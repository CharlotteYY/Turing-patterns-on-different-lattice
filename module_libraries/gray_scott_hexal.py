# Reaction-diffusion simulation function
def simulate_gray_scott_on_hexagons(n_rows, n_cols, LX, LY, f=0.039, k=0.058,
                                    da=1.5, db=0.5,
                                    dt=0.25, stoptime=10000.0,
                                    perturbation_level=0.0):
    """
    Simulate Gray-Scott reaction-diffusion dynamics on a hexagonal lattice.
    :param n_rows: Number of rows in the lattice.
    :param n_cols: Number of columns in the lattice.
    :param LX: Width of the lattice.
    :param LY: Height of the lattice.
    :param f: Feed rate.
    :param k: Kill rate.
    :param da: Diffusion rate for activator A.
    :param db: Diffusion rate for inhibitor B.
    :param dt: Time step size.
    :param stoptime: Total simulation time.
    :param perturbation_level: Perturbation level for irregularity in hexagons.
    """
    # Generate hexagonal lattice
    x_coords, y_coords, hex_points = generate_hexagonal_lattice(n_rows=n_rows,
                                                    n_cols=n_cols,
                                                    LX=LX,
                                                    LY=LY,
                                                    perturbation_level=perturbation_level)
    # Initialize activator (A) and inhibitor (B)
    n_cells = len(hex_points)
    #print(n_cells)
    A = np.ones(n_cells)
    B = np.zeros(n_cells)

    # Seed initial patterns for B
    seed_indices = np.random.choice(n_cells, int(0.1 * n_cells), replace=False)
    B[seed_indices] = 1

        # Simulation loop
    t = 0
    lN = LX / n_cols
    calcu = -1
    while t < stoptime:
        # Reaction-diffusion dynamics (simplified for discrete cells)
        dA = da * (np.roll(A, 1) + np.roll(A, -1) - 2 * A) - A * (B ** 2) + f * (1 - A)
        dB = db * (np.roll(B, 1) + np.roll(B, -1) - 2 * B) + A * (B ** 2) - (k + f) * B

        A += dA * dt
        B += dB * dt

        A = np.clip(A, 0, 1)
        B = np.clip(B, 0, 1)

        t += dt

        # Visualization at specific intervals
        if int(t) % int(stoptime / 5) == 0 and int(t) / int(stoptime / 5) != calcu:

            plot_hexagonal_reaction_diffusion(points = hex_points, x_coords=x_coords, y_coords=y_coords, lN = lN, LX = LX, LY = LY, B = A, t = int(t))
        
        calcu = int(t) / int(stoptime / 5)