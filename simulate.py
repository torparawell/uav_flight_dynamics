import glfw
from OpenGL.GL import *

class Simulation:
    def __init__(self, uav, control_system, delta_time=0.01):
        self.uav = uav
        self.control_system = control_system
        self.delta_time = delta_time
        self.current_time = 0.0
        self.uav_trail = []  # Stores past positions of the UAV for drawing the trail
        self.init_window()

    def init_window(self):
        if not glfw.init():
            return

        self.window = glfw.create_window(640, 480, "UAV Simulation", None, None)
        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)
        glEnable(GL_DEPTH_TEST)

    def step(self):
        control_inputs = self.control_system.get_inputs(self.uav)
        self.uav.update_state(self.delta_time)
        self.current_time += self.delta_time
        
        # Store the UAV's current position for the trail
        self.uav_trail.append(self.uav.get_position())
        
        self.update_visualization()

    def update_visualization(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw ground plane, axes, altitude lines, UAV trail, and UAV state info
        self.draw_ground_plane()
        self.draw_axes()
        self.draw_altitude_lines()
        self.draw_uav_trail()
        self.draw_uav_info()

        x, y, z = self.uav.get_position()
        glPointSize(10.0)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POINTS)
        glVertex3f(x, y, z)
        glEnd()
        
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def draw_uav_trail(self):
        """Draw the UAV's past trajectory."""
        glColor3f(0.7, 0.9, 0.7)  # Light green for the trail
        glPointSize(3.0)
        glBegin(GL_POINTS)
        for pos in self.uav_trail:
            glVertex3f(*pos)
        glEnd()

    def draw_uav_info(self):
        """Display the UAV's current state information."""
        x, y, z = self.uav.get_position()
        info_str = f"Time: {self.current_time:.2f}s | Position: ({x:.2f}, {y:.2f}, {z:.2f})"
        # This is a placeholder and will need a method to render text in OpenGL.

    def draw_ground_plane(self, base_size=100):
        x, _, z = self.uav.get_position()
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_LINES)
        for i in range(-base_size, base_size+1, 10):
            glVertex3f(x - base_size, 0, z + i)
            glVertex3f(x + base_size, 0, z + i)
            glVertex3f(x + i, 0, z - base_size)
            glVertex3f(x + i, 0, z + base_size)
        glEnd()

    def draw_axes(self, size=10):
        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(size, 0, 0)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, size, 0)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, size)
        glEnd()

    def draw_altitude_lines(self, altitude_interval=100):
        x, y, z = self.uav.get_position()
    
        # Round to the nearest integer to ensure valid range values
        min_altitude = max(0, round(y - 5 * altitude_interval))  # 5 lines below current altitude
        max_altitude = round(y + 5 * altitude_interval)  # 5 lines above current altitude

        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_LINES)
        for altitude in range(min_altitude, max_altitude + 1, altitude_interval):
            glVertex3f(x - 10, altitude, z)
            glVertex3f(x + 10, altitude, z)
        glEnd()

    def run(self, total_time):
        while not glfw.window_should_close(self.window) and self.current_time < total_time:
            self.step()

    def reset(self):
        self.current_time = 0.0
        self.uav.reset_state()

    def terminate(self):
        glfw.terminate()
