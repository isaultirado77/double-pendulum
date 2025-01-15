import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)

class DoublePendulum:
    def __init__(self, m1, m2, l1, l2, theta1, theta2, omega1=0.0, omega2=0.0):
        self.m1 = m1  # Mass of the first pendulum
        self.m2 = m2  # Mass of the second pendulum
        self.l1 = l1  # Length of the first pendulum
        self.l2 = l2  # Length of the second pendulum
        self.theta1 = theta1  # Initial angle for the first pendulum (rad)
        self.theta2 = theta2  # Initial angle for the second pendulum (rad)
        self.omega1 = omega1  # Initial angular velocity for the first pendulum
        self.omega2 = omega2  # Initial angular velocity for the second pendulum

    def derivatives(self):
        """Returns the derivatives for theta1, theta2, omega1, omega2."""
        delta = self.theta2 - self.theta1

        denom1 = (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * delta))
        domega1_dt = (
            -g * (2 * self.m1 + self.m2) * np.sin(self.theta1)
            - self.m2 * g * np.sin(self.theta1 - 2 * self.theta2)
            - 2 * np.sin(delta) * self.m2 * (
                self.omega2 ** 2 * self.l2 + self.omega1 ** 2 * self.l1 * np.cos(delta)
            )
        ) / (self.l1 * denom1)

        denom2 = (self.l2 * denom1)
        domega2_dt = (
            2 * np.sin(delta) * (
                self.omega1 ** 2 * self.l1 * (self.m1 + self.m2)
                + g * (self.m1 + self.m2) * np.cos(self.theta1)
                + self.omega2 ** 2 * self.l2 * self.m2 * np.cos(delta)
            )
        ) / denom2

        return self.omega1, self.omega2, domega1_dt, domega2_dt

    def step(self, dt):
        """Update the system using the RK4 method."""
        k1_omega1, k1_omega2, k1_domega1, k1_domega2 = self.derivatives()

        theta1_k2 = self.theta1 + 0.5 * dt * k1_omega1
        theta2_k2 = self.theta2 + 0.5 * dt * k1_omega2
        omega1_k2 = self.omega1 + 0.5 * dt * k1_domega1
        omega2_k2 = self.omega2 + 0.5 * dt * k1_domega2

        k2_omega1, k2_omega2, k2_domega1, k2_domega2 = self.derivatives()

        self.theta1 += dt * k2_omega1
        self.theta2 += dt * k2_omega2
        self.omega1 += dt * k2_domega1
        self.omega2 += dt * k2_domega2

    def simulate(self, total_time, dt):
        """Simulate the system for a given total time and time step."""
        steps = int(total_time / dt)
        trajectory = []

        for _ in range(steps):
            trajectory.append((self.theta1, self.theta2, self.omega1, self.omega2))
            self.step(dt)

        return np.array(trajectory)

# Parameters
m1, m2 = 1.5, 1.5  # masses (kg)
l1, l2 = 1.3, 1.3  # lengths (m)
theta1, theta2 = np.pi / 2, np.pi / 2  # initial angles (rad)
total_time, dt = 100, 0.04  # simulation time (s) and time step (s)

# Initialize and run the simulation
double_pendulum = DoublePendulum(m1, m2, l1, l2, theta1, theta2)
trajectory = double_pendulum.simulate(total_time, dt)

# Plot results
plt.figure(figsize=(10, 6))
time = np.arange(0, total_time, dt)
plt.plot(time, trajectory[:, 0], label="Theta1 (rad)")
plt.plot(time, trajectory[:, 1], label="Theta2 (rad)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.title("Double Pendulum Simulation")
plt.grid()
plt.show()
