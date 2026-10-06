<img width="1350" height="700" alt="Figure_1" src="https://github.com/user-attachments/assets/f9136990-4027-49f7-9478-e75b497f9fb8" /># Logistic Map Simulator

A MATLAB-based educational simulator for exploring the behavior of the **logistic map** and its transition from periodic to chaotic dynamics.

The simulator was developed to provide a more quantitative way of studying the logistic map. In addition to visualizing the map's dynamics, it includes tools for calculating and analyzing the **Lyapunov exponent**, **symbolic block entropy**, and **Shannon entropy**.

## Features

- **Logistic Map Simulation**
  - Iterates the logistic map
    \[
    x_{n+1}=rx_n(1-x_n)
    \]
  - Allows the user to vary the control parameter \(r\).
  - Visualizes the resulting time series and dynamical behavior.
 
<img width="715" height="478" alt="comparison1" src="https://github.com/user-attachments/assets/e1b6ccbb-f1ba-4fe9-88d3-38e50d1945d2" />
<img width="800" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/edcf17d3-56a7-4841-a926-70ce96bceb1c" />
<img width="651" height="441" alt="comparison2" src="https://github.com/user-attachments/assets/207045cc-9f76-40c2-8d73-cbd720025e10" />


- **Bifurcation Diagram**
  - Visualizes the transition from stable fixed points to periodic orbits and eventually chaotic behavior as \(r\) increases.
  - Allows the period-doubling route to chaos to be explored interactively.
<img width="1350" height="700" alt="Figure_1" src="https://github.com/user-attachments/assets/f1b4cea9-ac25-489a-9577-bd1ebd141427" />

- **Lyapunov Exponent**
  - Calculates the Lyapunov exponent of the logistic map.
  - Provides a quantitative measure of the sensitivity to initial conditions.
  - Positive values indicate chaotic behavior, while negative values generally correspond to stable dynamics.

- **Symbolic Block Entropy**
  - Converts the logistic-map trajectory into a symbolic sequence using a partition of the state space.
  - Calculates block probabilities for different block lengths.
  - Allows the growth of block entropy to be examined as the block length increases.

- **Shannon Entropy**
  - Calculates the Shannon entropy of the resulting symbolic distribution.
  - Provides an information-theoretic measure of the uncertainty within the system.

## Why This Simulator?

Many basic logistic-map simulators focus primarily on visualizing the trajectory or generating a bifurcation diagram. While these are useful for understanding the qualitative behavior of the system, they provide limited quantitative information about the transition to chaos.

This project was created to combine **dynamical-systems** and **information-theoretic** approaches in a single educational tool.

In particular, the simulator allows the behavior of the logistic map to be investigated through both:

- **Geometric/dynamical measures**, such as the Lyapunov exponent.
- **Information-theoretic measures**, such as Shannon entropy and symbolic block entropy.

This makes it possible to compare different descriptions of the transition from periodic to chaotic behavior.

## The Logistic Map

The logistic map is a discrete dynamical system defined by

\[
x_{n+1}=rx_n(1-x_n)
\]

where:

- \(x_n\) is the state of the system at iteration \(n\).
- \(r\) is the control parameter.
- \(0\leq x_n\leq1\).

Depending on the value of \(r\), the system can exhibit stable fixed points, periodic behavior, period-doubling cascades, and chaotic dynamics.

## Requirements

- MATLAB
- No additional toolboxes are required unless specified by the individual scripts.

## Usage

1. Clone or download this repository.
2. Open the project in MATLAB.
3. Run the main simulation script.
4. Select the desired value of \(r\), initial condition, and number of iterations.
5. Use the available analysis tools to calculate the Lyapunov exponent, symbolic block entropy, and Shannon entropy.

## Project Structure

```text
Logistic-Map-Simulator/
│
├── README.md
├── ...
└── ...
```

The repository may be expanded with additional scripts for individual analyses and visualization.

## Educational Purpose

This project was developed primarily as an **educational and exploratory tool**. It is intended to make concepts from nonlinear dynamics and information theory more accessible through direct experimentation.

Rather than treating the logistic map only as a mathematical equation, the simulator allows users to observe how different quantitative measures respond as the system moves from ordered to chaotic behavior.

## Author

Developed as an independent educational/research project exploring nonlinear dynamics, chaos theory, and information theory.
