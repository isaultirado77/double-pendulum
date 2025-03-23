import numpy as np
import os

class Mass:
    def __init__(self, mass, length, theta, omega):
        """
        Inicializa una masa de un péndulo doble.
        :param mass: Masa del péndulo.
        :param length: Longitud del brazo.
        :param theta: Ángulo inicial (en radianes).
        :param omega: Velocidad angular inicial (en rad/s).
        """
        self.mass = mass
        self.length = length
        self.theta = theta
        self.omega = omega  # Velocidad angular

class System:
    def __init__(self, m1, l1, theta1, omega1, m2, l2, theta2, omega2, g=9.81):
        """
        Inicializa el sistema del péndulo doble.
        :param m1, m2: Masas de los péndulos.
        :param l1, l2: Longitudes de los péndulos.
        :param theta1, theta2: Ángulos iniciales en radianes.
        :param omega1, omega2: Velocidades angulares iniciales.
        :param g: Aceleración gravitacional.
        """
        self.g = g
        self.mass1 = Mass(m1, l1, theta1, omega1)
        self.mass2 = Mass(m2, l2, theta2, omega2)

        # Crear carpeta para guardar datos
        os.makedirs("data", exist_ok=True)

    def equations_of_motion(self, state):
        """Devuelve las derivadas de theta1, theta2, omega1, omega2 usando las ecuaciones del péndulo doble."""
        theta1, omega1, theta2, omega2 = state
        m1, m2 = self.mass1.mass, self.mass2.mass
        l1, l2 = self.mass1.length, self.mass2.length
        g = self.g

        delta_theta = theta2 - theta1
        den1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta_theta)**2
        den2 = (l2 / l1) * den1

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        domega1_dt = (
            m2 * l1 * omega1**2 * np.sin(delta_theta) * np.cos(delta_theta) +
            m2 * g * np.sin(theta2) * np.cos(delta_theta) +
            m2 * l2 * omega2**2 * np.sin(delta_theta) -
            (m1 + m2) * g * np.sin(theta1)
        ) / den1

        domega2_dt = (
            -l2 * omega2**2 * np.sin(delta_theta) * np.cos(delta_theta) +
            (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta) -
            (m1 + m2) * l1 * omega1**2 * np.sin(delta_theta) -
            (m1 + m2) * g * np.sin(theta2)
        ) / den2

        return np.array([dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt])

    def runge_kutta_step(self, state, dt):
        """Calcula el siguiente estado usando el método de Runge-Kutta de 4º orden."""
        k1 = dt * self.equations_of_motion(state)
        k2 = dt * self.equations_of_motion(state + 0.5 * k1)
        k3 = dt * self.equations_of_motion(state + 0.5 * k2)
        k4 = dt * self.equations_of_motion(state + k3)
        return state + (k1 + 2*k2 + 2*k3 + k4) / 6

    def kinetic_energy(self, theta1, omega1, theta2, omega2):
        """Calcula la energía cinética del sistema."""
        m1, m2 = self.mass1.mass, self.mass2.mass
        l1, l2 = self.mass1.length, self.mass2.length
        v1 = l1 * omega1
        v2 = np.sqrt((l1 * omega1 * np.cos(theta1) + l2 * omega2 * np.cos(theta2))**2 +
                     (l1 * omega1 * np.sin(theta1) + l2 * omega2 * np.sin(theta2))**2)
        return 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2

    def potential_energy(self, theta1, theta2):
        """Calcula la energía potencial del sistema."""
        m1, m2 = self.mass1.mass, self.mass2.mass
        l1, l2 = self.mass1.length, self.mass2.length
        g = self.g
        y1 = -l1 * np.cos(theta1)
        y2 = y1 - l2 * np.cos(theta2)
        return m1 * g * y1 + m2 * g * y2

    def simulate(self, t_max, dt):
        """Ejecuta la simulación y guarda los datos en 'data/data.dat'."""
        steps = int(t_max / dt)
        state = np.array([self.mass1.theta, self.mass1.omega, self.mass2.theta, self.mass2.omega])

        with open("data/data.dat", "w") as file:
            file.write("# t theta1 omega1 theta2 omega2 E_kin E_pot E_total\n")

            time = 0.0
            for _ in range(steps):
                theta1, omega1, theta2, omega2 = state

                E_kin = self.kinetic_energy(theta1, omega1, theta2, omega2)
                E_pot = self.potential_energy(theta1, theta2)
                E_total = E_kin + E_pot

                data_str = f"{time:.5f} {theta1:.5f} {omega1:.5f} {theta2:.5f} {omega2:.5f} {E_kin:.5f} {E_pot:.5f} {E_total:.5f}\n"
                file.write(data_str)

                state = self.runge_kutta_step(state, dt)
                time += dt

if __name__ == "__main__":
    # Parámetros del péndulo doble
    m1, l1, theta1, omega1 = 1.0, 1.0, np.pi / 2, 0.0
    m2, l2, theta2, omega2 = 1.0, 1.0, np.pi / 2, 0.0
    dt = 0.01
    t_max = 10.0

    system = System(m1, l1, theta1, omega1, m2, l2, theta2, omega2)
    system.simulate(t_max, dt)
    print("Simulación completada. Datos guardados en 'data/data.dat'.")

