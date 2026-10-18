# Python Calculator

A simple Python calculator application built with a
modular backend architecture.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation
- Error handling
- Unit tests

## Project Structure

- backend/calculator.py: Mathematical operations
- backend/exceptions.py: Custom exceptions
- backend/main.py: Command-line interface
- tests/test_calculator.py: Unit tests

## Requirements

- Python 3.10 or later

## Setup

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

## Run the Application

python -m backend.main

## Run Tests

python -m unittest discover -s tests -v