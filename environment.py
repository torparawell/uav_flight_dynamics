'''
Environment Class:
Properties:
- airDensity: Current air density (which can change with altitude).
- windSpeed: Vector representing wind conditions the UAV might experience.
- gravity: Gravitational acceleration (typically a constant like 9.81 m/s²).
Methods:
- getAirDensity(): Return current air density based on altitude.
- getWindSpeed(): Return current wind conditions.
'''
# make the environment update with aerodynamics
class Environment:
    def __init__(self, air_density, wind_speed, gravity=9.81, temperature=20) -> None:
        self.air_density = air_density
        self.wind_speed = wind_speed
        self.gravity = gravity
        self.temperature = temperature
    
    def get_air_density(self, uav_altitude):
        # A simple placeholder formula; you might replace this with a more accurate model
        self.air_density = uav_altitude + (120 * (self.temperature - 59))
        return self.air_density
    
    def get_wind_speed(self):
        return self.wind_speed
    
    def get_gravity(self):
        return self.gravity
    
    def set_wind_speed(self, new_speed):
        self.wind_speed = new_speed
    
    def set_temperature(self, new_temp):
        self.temperature = new_temp

    