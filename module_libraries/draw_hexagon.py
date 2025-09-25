def draw_hexagon(ax, x_center, y_center, size, color):
    """
    Draw a single hexagon.
    :param ax: Matplotlib axis object.
    :param x_center: X-coordinate of the hexagon center.
    :param y_center: Y-coordinate of the hexagon center.
    :param size: Size of the hexagon (radius).
    :param color: Color of the hexagon.
    """
    angles = np.linspace(0, 2 * np.pi, 7)  # Six vertices + closing point
    x_hex = x_center + size * np.cos(angles)
    y_hex = y_center + size * np.sin(angles)
    ax.fill(x_hex, y_hex, color=color)