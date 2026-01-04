# Asteroids Arcade Clone
### Object-Oriented Game Development Project

<img width="1280" height="718" alt="image" src="https://github.com/user-attachments/assets/47832853-d8a7-4f53-88be-959428dba100" />

# Project Overview

The Asteroids Arcade Clone is a modern reimagining of the classic 1979 arcade game, built from scratch using Python and the Pygame-ce library. This project was designed to master complex software engineering concepts such as Object-Oriented Programming (OOP), vector mathematics, and real-time game loop management.

# Key Features

    Vector-Based Physics: Implements 2D vector mathematics for smooth, momentum-based player movement and projectile trajectories.

Dynamic Asteroid Splitting: Features a recursive-style spawning system where large asteroids break into smaller, faster fragments upon impact.

Collision Detection System: Utilizes a sophisticated circular hit-box system to manage interactions between the player, projectiles, and asteroids.

Encapsulated Game Objects: Every game element (Player, Asteroid, Shot) is a discrete class inheriting from a base CircleShape to ensure modularity and code reuse.

# Technical Architecture

The game engine is built on a robust architectural foundation:

    Game Loop Management: A centralized main.py handles the clock speed (FPS), delta-time calculations for frame-rate independence, and the rendering pipeline.

Inheritance & Polymorphism: A core CircleShape class provides the foundation for position, velocity, and collision logic, which is then extended by specialized classes.

Sprite Grouping: Leverages Pygame's Group containers to efficiently update and draw multiple objects (like asteroid fields or bullet volleys) simultaneously.

Input Handling: Implements responsive keyboard mapping for rotation, acceleration, and a cooldown-based shooting system.

# Technical Deep Dive

    Collision Logic: Implements a distance-based collision algorithm (distance <= radius1 + radius2) to provide precise interaction detection without the overhead of per-pixel masks.

Delta Time (dt): All movement and rotations are multiplied by a dt variable, ensuring the game runs at the same speed regardless of the hardware's processing power.

Constants Management: Centralizes all game parameters (screen dimensions, player speed, asteroid sizes) in a constants.py file for easy tuning and balancing.

# Installation 

  Clone the Repository:
    
    Bash
    git clone https://github.com/tstokes22/asteroids_game.git

Install Dependencies:
  
    Bash
    pip install -r requirements.txt

Run the Game:

    Bash
    python main.py
