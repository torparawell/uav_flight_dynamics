import math

def calculateLift(air_density, velocity):
    lift_coefficient = 0.5
    wing_area = 5  # square meters
    # Calculate the magnitude of the velocity vector
    added_vectors = (velocity[0]**2 + velocity[1]**2 + velocity[2]**2)
    speed = math.sqrt(added_vectors)
    print(speed)
    # Compute lift force
    lift = lift_coefficient * (0.5 * air_density * speed**2) * wing_area
    
    return lift

air_density = 1.225
velocity = [1, 1, 1]
print(calculateLift(air_density, velocity))