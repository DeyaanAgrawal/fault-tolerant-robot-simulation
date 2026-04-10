# FAULT-TOLERANT AUTONOMOUS ROBOT SYSTEM

## OVERVIEW
This project focuses on building a fault-tolerant autonomous robot capable of navigating environments, detecting obstacles, and handling sensor failures intelligently.

The system follows a simulation-first engineering approach, combining:

1. Python-based logic simulation
2. Unreal Engine environment simulation (planned)
3. AI-based decision-making (planned)
4. Real-world deployment on Raspberry Pi 4

## CORE OBJECTIVES
1. Develop autonomous navigation logic
2. Simulate real-world sensor behavior
3. Detect and handle sensor failures
4. Implement intelligent fallback strategies
5. Transition seamlessly from simulation → hardware

## SIMULATION LAYERS

### Python Simulation (Current Stage)
1. Simulated sensors using random values
2. Fault injection (None, noisy readings)
3. Rule-based navigation logic

### Unreal Engine Simulation (Planned)
1. 3D environment testing
2. Realistic obstacle layouts
3. Physics-based movement
4. Visual debugging of robot decisions

### AI Integration (Planned)
1. Adaptive decision-making
2. Learning-based navigation improvements
3. Handling complex and uncertain environments

## System Architecture
Sensors → Failure Detection → Decision Engine → Action
