from uav import UAV
from environment import Environment
from control_systems import ControlSystem
from aerodynamics import Aerodynamics
from simulate import Simulation

def run_graphical_simulation():
    # Environment parameters
    air_density = 1.225  # Typical value at sea level in kg/m^3

    # UAV Parameters
    initial_position = (0, 0, 0)
    initial_velocity = (1, 1, 1) # Magnitude and Direction
    initial_thrust = 0
    mass = 5.0  # 5 kg

    # Aerodynamic parameters
    lift_coefficient = 0.5
    drag_coefficient = 0.02
    wing_area = 0.5  # square meters
    airframe_drag_coefficient = 0.01  # A small drag for the entire UAV structure

    # Control Setpoints
    desired_altitude = 1  # meters
    desired_heading = 90  # degrees

    # Create instances of our classes
    aerodynamics = Aerodynamics(
        lift_coefficient=lift_coefficient,
        drag_coefficient=drag_coefficient,
        wing_area=wing_area,
        airframe_drag_coefficient=airframe_drag_coefficient
    )

    environment = Environment(air_density=air_density, wind_speed=(0, 0, 0))  # Introducing a 3D wind vector
    uav = UAV(aerodynamics, environment, position=initial_position, velocity=initial_velocity, thrust=initial_thrust, mass=mass)
    control_system = ControlSystem(altitude_set_point=desired_altitude, heading_set_point=desired_heading)
    
    # Set any desired initial conditions, setpoints, or parameters
    control_system.set_altitude_setpoint(desired_altitude)
    control_system.set_heading_setpoint(desired_heading)

    # Create the Simulation instance and run the graphical simulation
    simulation = Simulation(uav, control_system)
    simulation.run(total_time=50)

# Run the graphical simulation
run_graphical_simulation()