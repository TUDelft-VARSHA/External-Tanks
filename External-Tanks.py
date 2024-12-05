import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')  # Use a backend suitable for rendering plots


class ParabolicTankPlotter:
    def __init__(self):
        self.tanks = []
        self.y_offset = 0  # Tracks cumulative length to position tanks end-to-end

    def add_parabolic_tank(self, height, width, length):
        """
        Add a parabolic tank.
        :param height: Height of the tank (z-axis).
        :param width: Width of the tank (x-axis).
        :param length: Length of the tank (y-axis).
        """
        self.tanks.append({
            'height': height,
            'width': width,
            'length': length,
            'y_offset': self.y_offset
        })
        self.y_offset += length  # Update y_offset for the next tank

    def calculate_total_volume(self):
        """
        Calculate the total volume of all parabolic tanks.
        :return: Total volume.
        """
        total_volume = 0
        for tank in self.tanks:
            height = tank['height']
            width = tank['width']
            length = tank['length']
            # Volume of a parabolic tank
            volume = (2 / 3) * width * length * height
            total_volume += volume
        return total_volume

    def plot_tanks(self):
        """
        Create a 3D plot of all the tanks aligned end-to-end with equal axis scaling.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        max_x = max_y = max_z = 0

        for idx, tank in enumerate(self.tanks):
            height = tank['height']
            width = tank['width']
            length = tank['length']
            y_offset = tank['y_offset']

            # Calculate the curvature coefficient 'a' for the parabolic profile
            a = height / (width / 2) ** 2

            # Create a grid for the parabolic profile
            x = np.linspace(-width / 2, width / 2, 100)
            z = a * x ** 2  # Parabola equation
            y = np.linspace(0, length, 100) + y_offset
            X, Y = np.meshgrid(x, y)

            # Extrude the parabola along the y-axis (length)
            Z = a * X ** 2

            # Plot the tank
            ax.plot_surface(X, Y, Z, alpha=0.5, edgecolor='none')

            # Update maximum dimensions for scaling
            max_x = max(max_x, width / 2)
            max_y = max(max_y, y_offset + length)
            max_z = max(max_z, height)

        # Set equal scaling
        ax.set_box_aspect([max_x, max_y, max_z])  # Match aspect ratio
        ax.set_xlim(-max_x, max_x)
        ax.set_ylim(0, max_y)
        ax.set_zlim(0, max_z)

        ax.set_xlabel('Width (X)')
        ax.set_ylabel('Length (Y)')
        ax.set_zlabel('Height (Z)')
        plt.title("End-to-End Aligned Parabolic Tanks with Equal Scaling")
        plt.show()

    def plot_front_view(self):
        """
        Create a 2D front view of all the tanks with equally spaced axes,
        aligning the tops of the tanks to z = 0.
        """
        fig, ax_front = plt.subplots(figsize=(10, 6))

        max_x = max_z = 0

        for idx, tank in enumerate(self.tanks):
            height = tank['height']
            width = tank['width']

            # Calculate the curvature coefficient 'a' for the parabolic profile
            a = height / (width / 2) ** 2

            # Create the parabolic profile, aligning the top of the tank to z = 0
            x = np.linspace(-width / 2, width / 2, 100)
            z = a * x ** 2 - height  # Align tops to z = 0

            # Plot the front view (z vs x)
            ax_front.plot(x, z, label=f'Tank {idx + 1}')

            # Update maximum dimensions for scaling
            max_x = max(max_x, width / 2)
            max_z = max(max_z, height)

        # Set equal scaling for the front view
        ax_front.set_aspect('equal', adjustable='datalim')
        ax_front.set_xlim(-max_x, max_x)
        ax_front.set_ylim(-max_z, 0)  # Align top to z = 0

        ax_front.set_xlabel('Width (X)')
        ax_front.set_ylabel('Height (Z)')
        ax_front.set_title('Front View (Tops Aligned)')
        ax_front.legend()

        plt.grid(True)
        plt.tight_layout()
        plt.show()


# Example Usage
if __name__ == "__main__":
    plotter = ParabolicTankPlotter()

    # Add parabolic tanks with different dimensions
    plotter.add_parabolic_tank(height=1.6, width=3, length=14)
    plotter.add_parabolic_tank(height=1.2, width=5.26, length=10)
    plotter.add_parabolic_tank(height=1.2, width=2.75, length=7)

    # Calculate and print total volume
    total_volume = plotter.calculate_total_volume()
    print(f"Total Volume of Tanks: {total_volume:.2f} cubic units")

    # Plot the tanks
    plotter.plot_tanks()

    # Plot the front view
    plotter.plot_front_view()
