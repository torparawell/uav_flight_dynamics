class UAV:
    def __init__(self, aerodynamics, environment, position, velocity, thrust, mass) -> None:
        self.aerodynamics = aerodynamics
        self.environment = environment
        self.position = list(position) 
        self.velocity = list(velocity) # Which is incorporated as a magnitude and direction.
        self.thrust = thrust  # This might be a vector in 3D or a scalar if thrust is only vertical
        self.mass = mass
        self.orientation = {'roll': 0, 'pitch': 0, 'yaw': 0}  # Initial orientation
        
    def get_altitude(self):
        return self.position[2]  # Assuming z-axis is the vertical axis

    def get_heading(self):
        return self.orientation['yaw']  # This is simplifying heading to just the yaw angle

    def get_position(self):
        return self.position
    
    def update_state(self, deltaTime):
        # Gravity only acts on the vertical axis (z-axis)
        net_vertical_force = self.thrust - self.mass * self.environment.gravity
        vertical_acceleration = net_vertical_force / self.mass
        
        # Update position in 3D
        for i in range(3):
            self.position[i] += self.velocity[i] * deltaTime

        # Add the acceleration due to force for vertical axis
        self.position[2] += 0.5 * vertical_acceleration * (deltaTime ** 2)
        
        '''# Update velocity in 3D
        for i in range(3):
            self.velocity[i] += vertical_acceleration * deltaTime if i == 2 else 0  # Only z-axis is affected by gravity'''


        # Calculating both lift and drag from the aerodynamics class (assuming they're scalars)
        lift = self.aerodynamics.calculateLift(self.environment.air_density, self.velocity)
        drag = self.aerodynamics.calculateDrag(self.environment.air_density, self.velocity)
        
        '''# Update velocities based on lift and drag (you might want more detailed physics here)
        self.velocity[2] += lift * deltaTime / self.mass  # Simplified lift application
        for i in range(3):
            self.velocity[i] -= drag * deltaTime / self.mass  # Simplified drag application, affecting all directions equally'''

    def applyControls(self, controlOutputs):
        # Assuming controlOutputs contain values to adjust orientation and thrust
        self.orientation['roll'] += controlOutputs['roll']
        self.orientation['pitch'] += controlOutputs['pitch']
        self.orientation['yaw'] += controlOutputs['yaw']
        
        # Adjusting thrust if present in controlOutputs
        if 'thrust' in controlOutputs:
            self.thrust += controlOutputs['thrust']
