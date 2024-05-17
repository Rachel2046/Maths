import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(ax, npoints):
    """
    Draw the plane: a+b+c=1, a>0, b>0, c>0
    """
    u = np.linspace(0, 1, num=npoints)
    v = np.linspace(0, 1, num=npoints)
    a, b = np.meshgrid(u, v)

    for i in range(npoints):
        for j in range(npoints):
            if (i + j >= npoints):
                a[i, j] = float("NaN")
                b[i, j] = float("NaN")
    c = 1 - a - b
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('c')
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_zticks([])
    surf = ax.plot_surface(a, b, c, cmap='Wistia', alpha=.8)

def draw_aplane(ax, npoints):
    """
    draw the plane: a=0.5
    """
    m = np.linspace(0,0.5, num=npoints)
    n = np.linspace(0, 0.5, num=npoints)
    y, z = np.meshgrid(m, n)
    x = 0.5
    linex = ax.plot3D(x*np.ones(npoints), 0.5-m, n, color='red', linewidth=2)
    surf = ax.plot_surface(x, y, z, cmap='winter', alpha=.6)

def rotation(ax, altitude=30, azimuth_start=60, azimuth_finish=420):
    """
    Rotate the 3D plot range_angle degrees at azimuth = init_angle
    """
    for angle in range(azimuth_start, azimuth_finish):
        ax.view_init(altitude, angle)
        plt.draw()
        plt.pause(.001)
    plt.show()

if __name__ == "__main__":
    ax = plt.axes(projection='3d')
    npoints = 100
    draw_triangle(ax, npoints)
    draw_aplane(ax, npoints)
    rotation(ax)
