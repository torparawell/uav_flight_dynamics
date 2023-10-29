'''
Aerodynamics Class:
Properties:
- liftCoefficient: Lift coefficient based on the UAV's current angle of attack.
- dragCoefficient: Drag coefficient based on the UAV's current angle of attack and other factors.
- wingArea: Surface area of the UAV's wings (important for lift calculations).
- airframeDragCoefficient: A coefficient that accounts for the drag due to the UAV's shape and design.
(Any other aerodynamic-related properties like aspect ratio, zero-lift drag coefficient, etc.)
Methods:
- calculateLift(airDensity, velocity): Determine lift force based on air density, velocity, and lift coefficient.
- calculateDrag(airDensity, velocity): Determine drag force based on air density, velocity, and drag coefficient.
- updateCoefficients(angleOfAttack): Adjust aerodynamic coefficients based on the UAV's current angle of attack and possibly other variables.
'''
import math

class Aerodynamics:
    def __init__(self, lift_coefficient, drag_coefficient, wing_area, airframe_drag_coefficient) -> None:
        self.lift_coefficient = lift_coefficient
        self.drag_coefficient = drag_coefficient
        self.wing_area = wing_area
        self.airframe_drag_coefficient = airframe_drag_coefficient
    
    def calculateLift(self, air_density, velocity):
        # Calculate the magnitude of the velocity vector
        speed = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)
        # Compute lift force
        lift = self.lift_coefficient * (0.5 * air_density * speed**2) * self.wing_area
        
        return lift

    def calculateDrag(self, air_density, velocity):
        # Calculate the magnitude of the velocity vector
        speed = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)
        
        # Compute drag force
        drag = self.drag_coefficient * (0.5 * air_density * speed**2) * self.wing_area
        
        return drag