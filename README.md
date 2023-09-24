# Enigma Machine Simulator

This Python script simulates an Enigma machine, a historical encryption device used during World War II. The Enigma machine consists of various components, including rotors, reflectors, and plugboard settings, which are used to encrypt and decrypt messages.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Running the Tests](#running-the-tests)
- [Rotors and Reflectors](#rotors-and-reflectors)
- [Enigma Settings](#enigma-settings)
- [Functions](#functions)
- [Classes](#classes)
- [Conclusion](#conclusion)

## Overview

The Enigma machine simulator consists of several Python classes and functions that replicate the functionality of the original Enigma machine. The key components include:

- `PlugLead`: Represents a plug lead used in the plugboard to swap pairs of letters.
- `Plugboard`: Simulates the plugboard where plug leads are connected.
- `Rotors`: Models the rotors used for letter substitution.
- `Reflector`: Represents the reflector used to create a reciprocal mapping.

The main `simulator` function is used to encode or decode messages using the Enigma machine. It takes Enigma settings, a message, and rotor/reflectors configurations as input and returns the encoded message.

## Usage

To use this Enigma machine simulator, follow these steps:

1. Ensure you have Python installed on your system.
2. Create a JSON file with rotor and reflector configurations. You can use the existing JSON files (`rotors_Demonstration.json` and `rotors_reflectors.json`) as examples.
3. Modify the Enigma settings and message in the `if __name__ == "__main__":` section of the script.
4. Run the script to see the encoded message.

## Code Structure

The code is organized into several classes, each responsible for a specific part of the Enigma machine. Here's a brief overview of the classes and their responsibilities:

- `PlugLead`: Handles plug lead configurations and letter swapping.
- `Plugboard`: Manages the plugboard and plug lead connections.
- `Rotors`: Models the rotors, rotor notches, and rotor rotations.
- `Reflector`: Represents the reflector used for reciprocal mapping.

The script also includes utility functions for notch settings, rotor functions, and the main simulator.

## Running the Tests

The script includes two test scenarios, each with its Enigma machine settings and messages. To run the tests, follow these steps:

1. Ensure you have the required JSON configuration files (`rotors_Demonstration.json` and `rotors_reflectors.json`) in the same directory as the script.
2. Run the script. The tests will be executed, and the encoded messages will be displayed.

## Rotors and Reflectors

The rotor and reflector configurations are defined in JSON files. You can create your own configurations by following the format used in these JSON files. Each rotor's wiring and reflector mapping can be customized.

## Enigma Settings

In the main section of the script, you can specify the Enigma settings, including plugboard connections, rotor configurations, and the message you want to encode. Ensure you have the correct JSON configuration files and settings for the desired simulation.


## Functions

### `rotor_func(enigma_settings, rotor_reflector, enigma_rotors, char)`

- This function is responsible for the actual encoding or decoding process of a single character.
- It takes the Enigma settings, rotor reflector configuration, the current state of Enigma rotors, and the character to be processed as input.
- It checks for notch positions to determine when to rotate the rotors.
- It performs the character encoding process by passing the character through the rotors (right to left), the reflector, and then back through the rotors (left to right).
- It returns the encoded character.

### `notch_settings(char)`

- A utility function that provides the notch position for a given rotor. It maps rotor identifiers to their respective notch positions.

### `simulator(settings_, msg_, rot_ref='')`

- The main simulation function that orchestrates the entire Enigma machine simulation.
- It takes Enigma settings, an input message, and an optional rotor and reflector configuration.
- It configures the plugboard, rotor positions, and reflector.
- It processes each character in the input message and returns the encoded message.

## Classes

### `PlugLead`

- Represents a plug lead used in the plugboard.
- Checks and enforces conditions for valid plug leads and ensures that paired letters are not the same.

### `Plugboard`

- Simulates the plugboard and manages the connections of plug leads.
- Enforces conditions for adding plug leads, such as the number of pairs and preventing duplicate connections.

### `Rotors`

- Models the rotor components used for character substitution.
- Allows for character encoding in both directions (right to left and left to right).
- Tracks rotor positions, ring settings, and rotor wiring configurations.
- Rotates the rotor when certain conditions (notches) are met.

### `Reflector`

- Represents the reflector, which reflects characters back through the rotors.
- Provides character mappings based on the reflector wiring.

## Conclusion

The Enigma machine simulator project provides a Python implementation of the historical encryption device used during World War II. It can serve as a learning tool to understand the inner workings of the Enigma machine and its cryptographic processes. Additionally, it can be used as a foundation for further exploration of historical encryption methods or as a component in more complex cryptography projects.
