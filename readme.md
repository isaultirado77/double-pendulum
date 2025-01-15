# Simulación de Oscilador Doble

Este proyecto simula el movimiento de un péndulo doble utilizando el método Ralston-Rabinowitz (RK) para resolver las ecuaciones de movimiento. El objetivo es simular el sistema, calcular su dinámica y generar resultados como las trayectorias y energías de los osciladores.

## Descripción

El sistema tiene dos masas conectadas por sus respectivos péndulos. La primera masa está conectada al pivote, y la segunda está unida a la primera masa. La simulación utiliza el método RK, actualizando la posición y la velocidad de las masas paso a paso.

### Detalles del Sistema
- **Péndulo 1**:
  - Masa: \(m1 = 0.5 \text{kg}\).
  - Longitud del péndulo: \(l1 = 1.3 \text{m}\).
  - Masa del segundo péndulo: \(m2 = 1.5 \text{kg}\).

- **Péndulo 2**:
  - Longitud del péndulo: \(l2 = 1.5 \text{m}\).
  - Condiciones iniciales: Las posiciones angulares iniciales (\(\theta1\), \(\theta2\)) y las velocidades angulares (\(\dot{x}1\), \(\dot{x}2\)) se establecen en 0.15 radianes y \(\dot{X}\) en 3000 m/s.

### Resultados de la Simulación
1. **Trayectorias**: Simulación de la posición de las masas en el péndulo.
2. **Dinámica de Energía**: Cálculo de las energías totales del sistema, que incluye las energías cinética y potencial del sistema.

## Requisitos

- **Python 3.7** o superior.
- Bibliotecas requeridas:
  - Numpy.
  - Matplotlib

Instalar las bibliotecas requeridas con:
```bash
pip install numpy
pip install matplotlib 
```

## Pasos de la Simulación

1. Simular el movimiento del electrón bajo la influencia del campo eléctrico (script principal).
2. La solución se calcula utilizando el método RK4, asegurándose de implementar las ecuaciones de movimiento para cada péndulo.

3. Las posiciones/velocidades actualizadas de los péndulos se proporcionan en un arreglo.

---