# Simulación de Péndulo Doble

Este proyecto simula el movimiento de un péndulo doble utilizando el método de Runge-Kutta (RK) para resolver las ecuaciones de movimiento. Se pueden visualizar trayectorias, espacio fase y energía del sistema, comparando escenarios de pequeñas oscilaciones y movimiento caótico.


## Análisis y Resultados
Los resultados, incluyendo trayectorias, espacio fase y energía, se encuentran en el notebook:

[![Ver Análisis en Jupyter](https://nbviewer.jupyter.org/github/usuario/repositorio/blob/main/double_pendulum_analysis.ipynb)](https://nbviewer.jupyter.org/github/isaultirado77/double-pendulum/blob/main/double_pendulum_analysis.ipynb)

## Ejecución de la Simulación

La simulación puede ejecutarse con valores predefinidos o personalizarse mediante `argparse`:

### 1. Uso con valores predefinidos:
```python
m1, l1, theta1_init, omega1_init = 1.0, 1.0, 1.5, 0.0
m2, l2, theta2_init, omega2_init = 1.0, 1.0, 1.5, 0.0
dt = 0.01
t_max = 10.0

system = System(m1, l1, theta1_init, omega1_init, m2, l2, theta2_init, omega2_init)
system.simulate(t_max, dt)
```

### 2. Uso con `argparse`:
```bash
python main.py --m1 1.0 --l1 1.0 --theta1 1.5 --omega1 0.0 \
               --m2 1.0 --l2 1.0 --theta2 1.5 --omega2 0.0 \
               --dt 0.01 --t_max 10.0 --ndata data.dat

## Requisitos
- **Python 3.7** o superior.
- Bibliotecas necesarias:
  ```bash
  pip install numpy matplotlib
  ```