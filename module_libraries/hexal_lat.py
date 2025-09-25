def generate_hexagonal_lattice(n_cols, n_rows, LX, LY, perturbation_level=0.0):
    """
    Generate a hexagonal lattice with optional perturbation.
    :param n_cols: Number of cells in a row.
    :param n_rows: Number of rows of cells.
    :param LX: Width of the lattice.
    :param LY: Height of the lattice.
    :param perturbation_level: Level of randomness in cell positions (0 = regular hexagons).
    :return: x, y coordinates of cell centers and Voronoi diagram.
    """
    lN = LX / n_cols  # Size of unit hexagon (horizontal spacing)
    e1 = lN  # Horizontal spacing
    e2 = 0.5 * lN + 1j * lN * np.sin(np.pi / 3)  # Vertical spacing

    x_coords = []
    y_coords = []
    # Generate lattice points
    lattice_points = []
    for i in range(n_rows + 4):  # Add buffer rows for Voronoi edges
        for j in range(n_cols + 4):  # Add buffer columns for Voronoi edges
            x = j * e1 + (i % 2) * 0.5 * e1
            y = i * np.sqrt(3) / 2 * lN

            # Add perturbation
            x += perturbation_level * lN * np.random.uniform(-1, 1)
            y += perturbation_level * lN * np.random.uniform(-1, 1)

            x_coords.append(x)
            y_coords.append(y)
            lattice_points.append([x, y])

    lattice_points = np.array(lattice_points)
    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)
    # Filter points within bounds
    mask = (lattice_points[:, 0] > -0.01 * LX) & (lattice_points[:, 0] < 1.01 * LX) & \
           (lattice_points[:, 1] > -0.01 * LY) & (lattice_points[:, 1] < LY)
    filtered_points = lattice_points[mask]

    return x_coords[mask], y_coords[mask], filtered_points