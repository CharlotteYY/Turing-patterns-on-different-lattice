def plot_hexagonal_grid(points, LX, LY):
    """
    Plot a hexagonal grid using Voronoi tessellation.
    :param points: Array of points representing cell centers.
    :param LX: Width of the lattice.
    :param LY: Height of the lattice.
    """
    vor = Voronoi(points)

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot each Voronoi region as a patch
    for region in vor.regions:
        if not -1 in region and len(region) > 0:  # Ignore regions with infinite vertices
            polygon = [vor.vertices[i] for i in region]
            ax.fill(*zip(*polygon), edgecolor='black', facecolor='orange', alpha=0.6)

    ax.set_xlim(0, LX)
    ax.set_ylim(0, LY)
    ax.set_aspect('equal')
    
    plt.title("Hexagonal Grid")
    plt.show()