# UAV Simulation Project

## Overview
This project simulates the flight of an Unmanned Aerial Vehicle (UAV) by integrating various aspects such as aerodynamics, control systems, and environmental factors. The simulation includes a graphical representation of the UAV in motion, showcasing its response to control inputs and environmental conditions.

## Modules

### 1. Aerodynamics (`aerodynamics.py`)
This module defines the aerodynamic properties of the UAV, including lift and drag coefficients, wing area, and airframe drag. It is essential for calculating the UAV's flight dynamics.

### 2. Control Systems (`control_systems.py`)
Implements a control system for the UAV, managing altitude and heading. It includes proportional and derivative gains for precise control over the UAV's flight path.

### 3. Environment (`environment.py`)
Describes the flight environment, including air density, wind speed, and gravity. It plays a critical role in determining the UAV's interaction with external conditions.

### 4. UAV (`uav.py`)
Defines the UAV's characteristics, including its aerodynamics, environmental interactions, position, velocity, thrust, and mass. This is the central module that integrates various aspects of the UAV's behavior.

### 5. Simulation (`simulate.py`)
Handles the graphical representation and simulation loop. It uses OpenGL for rendering the UAV and its flight path, providing a visual feedback of the simulation.

### 6. Run Simulation (`run_simulation.py`)
Acts as the entry point for running the simulation. It sets up the environment, UAV parameters, and aerodynamics, and initializes the simulation process.

## Installation

To set up this project, clone the repository and ensure you have Python installed. Dependencies include OpenGL and GLFW for the simulation graphics.

```bash
git clone https://github.com/torparawell/uav_flight_dynamics/
cd uav_flight_dynamics
# Install dependencies
pip install pyopengl glfw
```

## Usage

Run the simulation using the following command:

```bash
python run_simulation.py
```

This will start the graphical simulation of the UAV, reflecting the dynamics as per the defined parameters and environmental conditions.

## Contributing

Contributions to enhance or extend the functionality of this simulation are welcome. Please follow the standard procedures for submitting pull requests.
