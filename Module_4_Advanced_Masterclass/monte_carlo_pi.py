import random

def estimate_pi(num_points: int) -> float:
    """
    Estimates the value of Pi using a Monte Carlo simulation.
    
    Args:
        num_points: The number of random darts to throw.
        
    Returns:
        An estimated float value of Pi.
    """
    points_inside_circle = 0
    
    for _ in range(num_points):
        # Generate random x, y coordinates between 0 and 1
        x = random.random()
        y = random.random()
        
        # Check if point is inside the unit circle (x^2 + y^2 <= 1)
        if (x**2 + y**2) <= 1:
            points_inside_circle += 1
            
    # The ratio of points is Pi/4
    return 4 * (points_inside_circle / num_points)

if __name__ == "__main__":
    n = 100_000
    pi_estimate = estimate_pi(n)
    print(f"Estimated Pi with {n:,} points: {pi_estimate}")
