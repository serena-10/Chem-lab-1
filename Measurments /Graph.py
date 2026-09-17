#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import numpy as np

# Measurements from the lab
volume = [10.0, 18.0, 27.0, 35.0, 43.0]
mass = [52.522, 61.485, 70.034, 78.752, 86.671]

# Calculate the average mass
average_mass = np.mean(mass)

# Calculate density using the slope of mass vs. volume
density = np.polyfit(volume, mass, 1)[0]

# Create the bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    ["10.0 mL", "18.0 mL", "27.0 mL", "35.0 mL", "43.0 mL"],
    mass,
    label="Mass (g)"
)

# Add average mass line
plt.axhline(
    average_mass,
    linestyle="--",
    label=f"Average Mass = {average_mass:.3f} g"
)

# Add density information to the graph
plt.axhline(
    density * np.mean(volume),
    linestyle=":",
    label=f"Density = {density:.3f} g/mL"
)

# Add the mass values above each bar
for bar, value in zip(bars, mass):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{value:.3f}",
        ha="center"
    )

# Title and axis labels
plt.title("The Density of Water Using a Graduated Cylinder at 21.5°C")
plt.xlabel("Measurements")
plt.ylabel("Mass (g)")

# Add legend
plt.legend()

# Add grid lines
plt.grid(axis="y", linestyle="--", alpha=0.3)

# Display the graph
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Experimental data
volumes = [10.0, 20.0, 30.0, 40.0, 50.0]
masses = [45.314, 55.222, 65.430, 75.067, 84.960]

# Trial labels
measurements = [
    "10.0 mL\n(Trial 1)",
    "20.0 mL\n(Trial 2)",
    "30.0 mL\n(Trial 3)",
    "40.0 mL\n(Trial 4)",
    "50.0 mL\n(Trial 5)"
]

# Calculate average mass
average_mass = np.mean(masses)

# Density of water at 20 degrees Celsius
density = 0.9982  # g/mL

# Create the graph
plt.figure(figsize=(12, 7))

# Create bars
bars = plt.bar(
    measurements,
    masses,
    label="Mass (g)"
)

# Add the mass value above each bar
for bar, mass in zip(bars, masses):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.8,
        f"{mass:.3f}",
        ha="center",
        va="bottom",
        fontsize=11
    )

# Add average line
plt.axhline(
    y=average_mass,
    linestyle=":",
    linewidth=2,
    label=f"Average ({average_mass:.3f} g)"
)

# Add density reference line
# Placed near the average so it can be shown on the mass axis
density_line = density * np.mean(volumes) + 35

plt.axhline(
    y=density_line,
    linestyle="--",
    linewidth=2,
    label=f"Density ({density:.4f} g/mL)"
)

# Graph title
plt.title(
    "The Density of Water Using a Volumetric Pipette\nat 20°C",
    fontsize=18,
    fontweight="bold"
)

# Axis labels
plt.xlabel("Measurements", fontsize=14)
plt.ylabel("Mass (g)", fontsize=14)

# Y-axis range
plt.ylim(30, 100)

# Add legend
plt.legend(fontsize=11)

# Add light horizontal grid lines
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

# Make layout fit nicely
plt.tight_layout()

# Display graph
plt.show()