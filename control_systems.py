class ControlSystem:
    def __init__(self, altitude_set_point=0, heading_set_point=0):
        self.altitude_set_point = altitude_set_point
        self.heading_set_point = heading_set_point
        self.current_error_altitude = 0
        self.previous_error_altitude = 0
        self.current_error_heading = 0
        self.previous_error_heading = 0
        self.Kp_altitude = 1  # Proportional gain for altitude control
        self.Kd_altitude = 0.1  # Derivative gain for altitude control
        self.Kp_heading = 1  # Proportional gain for heading control
        self.Kd_heading = 0.1  # Derivative gain for heading control

    def set_altitude_setpoint(self, altitude_set_point):
        self.altitude_set_point = altitude_set_point

    def set_heading_setpoint(self, heading_set_point):
        self.heading_set_point = heading_set_point

    def calculateControlOutput(self, current_altitude, current_heading):
        # Altitude control
        self.current_error_altitude = self.altitude_set_point - current_altitude
        dErrorAltitude = self.current_error_altitude - self.previous_error_altitude
        altitude_output = self.Kp_altitude * self.current_error_altitude + self.Kd_altitude * dErrorAltitude
        self.previous_error_altitude = self.current_error_altitude
        
        # Heading control
        self.current_error_heading = self.heading_set_point - current_heading
        dErrorHeading = self.current_error_heading - self.previous_error_heading
        heading_output = self.Kp_heading * self.current_error_heading + self.Kd_heading * dErrorHeading
        self.previous_error_heading = self.current_error_heading
        
        return altitude_output, heading_output

    def get_inputs(self, uav):
        current_altitude = uav.get_altitude()
        current_heading = uav.get_heading()
        altitude_output, heading_output = self.calculateControlOutput(current_altitude, current_heading)
        return altitude_output, heading_output
