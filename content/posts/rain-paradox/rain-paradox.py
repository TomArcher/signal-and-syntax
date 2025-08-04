from typing import List
import matplotlib.pyplot as plt

def simulate_wetness(speed_ft_s: float, distance_ft: float, rain_density:int = 1000) -> float:
    """
    Calculates total 'wetness' (raindrops hitting the body) for a given speed.

    Parameters:
    - speed_ft_s: speed in feet per second
    - distance_ft: distance to shelter in feet
    - rain_density: raindrops per square foot per second

    Returns:
    - total number of raindrops that hit the body
    """
    # Approximate body dimensions (in feet).
    height = 70 / 12     # 5 ft 10 in tall
    width = 20 / 12      # 20 inches wide
    depth = 12 / 12      # 12 inches deep

    # Time exposed to rain (in seconds).
    time_in_rain = distance_ft / speed_ft_s

    # Surface areas exposed.
    top_area = width * depth     # Head and shoulders.
    front_area = height * width  # Chest and legs.

    # Calculate rain impact.
    rain_from_above = rain_density * top_area * time_in_rain
    rain_from_front = rain_density * front_area * distance_ft

    # Total wetness from above and front.
    return rain_from_above + rain_from_front


def plot_wetness_vs_speed(speeds: List[float], wetness_values: List[float]) -> None:
    """
    Plots wetness vs. speed using matplotlib.

    Parameters:
    - speeds: list of speeds (in feet/second)
    - wetness_values: list of corresponding wetness values
    """
    # Create a new figure with a specified size (width=8", height=5").
    plt.figure(figsize=(8, 5))

    # Plot speed vs. wetness as a blue line with circular markers.
    plt.plot(speeds, wetness_values, marker='o', linestyle='-', color='blue')

    # Add a title to the chart.
    plt.title("Wetness vs. Speed in Rain")

    # Label the x-axis and y-axis.
    plt.xlabel("Speed (feet per second)")
    plt.ylabel("Total Raindrops Hit")

    # Add a grid for better readability.
    plt.grid(True)

    # Use the actual speed values as x-axis ticks.
    plt.xticks(speeds)

    # Automatically adjust layout to prevent clipping.
    plt.tight_layout()

    # Display the plot window.
    plt.show()

if __name__ == '__main__':
    # Define a list of speeds in feet per second.
    speeds: List[float] = [3.3, 5.5, 8.8, 13.2]
    distance: int = 328  # Arbritrary value to test with.

    # Compute wetness values for each speed
    wetness_values: List[float] = [simulate_wetness(speed, distance) for speed in speeds]

    # Iterate over speeds and their corresponding wetness values.
    for speed, wetness in zip(speeds, wetness_values):
        # Print the speed and its associated wetness.
        print(f"Speed: {speed:.1f} ft/s -> Wetness: {int(wetness)} drops")

    # Plot the data.
    plot_wetness_vs_speed(speeds, wetness_values)
