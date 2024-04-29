#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:31:49 2024

@author: peterasseily
"""

# Define floor buttons and floor indicator
floor_buttons = [False, False, False, False]  # Buttons for floors 1-4
floor_indicator = 1  # Current floor 
emergency_request = False  # Flag for emergency request

# Define motor control functions (replace with actual motor control logic)
def move_up(speed):
  # Move elevator up one floor at the specified speed
  print(f"Moving Up at speed {speed}")
  pass

def move_down(speed):
  # Move elevator down one floor at the specified speed
  print(f"Moving Down at speed {speed}")
  pass

def door_open():
  # Open elevator door
  print("Opening Door")
  pass

def door_close():
  # Close elevator door
  print("Closing Door")
  pass

# Function to handle floor button press
def button_press(floor):
  global floor_buttons
  floor_buttons[floor - 1] = True  # Set button press for specific floor

# Function to handle emergency request
def emergency_button_press():
  global emergency_request,floor
  emergency_request = True  # Set emergency request flag
  floor=1
  print("Emergency Request going back to Floor 1")

# Function to handle elevator movement
def handle_movement():
  global floor_indicator, floor_buttons, emergency_request

  # Check for emergency request
  if emergency_request:
    move_down(1)  # Move directly to floor 1 at maximum speed
    floor_indicator = 1
    door_open()
    door_close()
    emergency_request = False  # Reset emergency request after reaching floor 1
    return

  # Check for button presses on all floors
  for floor in range(1, 5):
    if floor_buttons[floor - 1]:
      # Move elevator to requested floor (considering direction)
      if floor > floor_indicator:
        move_up(0.5)  # Start slow, then increase speed
        move_up(1)  # Maintain cruising speed in the middle
        move_up(0.5)  # Slow down before stopping (ADA compliant)
        floor_indicator = floor - 1
      elif floor < floor_indicator:
        move_down(0.5)  # Start slow, then increase speed
        move_down(1)  # Maintain cruising speed in the middle
        move_down(0.5)  # Slow down before stopping (ADA compliant)
        floor_indicator = floor - 1
      elif floor==floor_indicator:    
        print("You are on the Same Floor")
        floor_indicator=floor
      # Door open at requested floor
      door_open()
      door_close()
      print(f'you are on floor {floor_indicator}')
      floor_buttons[floor - 1] = False  # Reset button press for the floor

  # Check if any button is pressed
  any_button_pressed = any(floor_buttons)

  # If no button is pressed, keep elevator idle
  if not any_button_pressed:
    print("Elevator Idle")

# User Interface (replace with actual user input methods)
def get_user_input():
  while True:
    try:
      floor = int(input("Enter floor number (1-4) or press 0 for emergency: "))
      if 1 <= floor <= 4:
        return floor
      elif floor == 0:
        emergency_button_press()
        return None  # No floor request during emergency
      else:
        print("Invalid input. Please enter a number between 1 and 4 or 0 for emergency.")
    except ValueError:
      print("You can't enter a Letter.Please enter a number between 1 and 4 or 0 for emergency.")

# Main loop
while True:
  # Get user input for floor or emergency
  requested_floor = get_user_input()

  # If not emergency, process floor request
  if requested_floor is not None:
    button_press(requested_floor)

  # Handle elevator movement based on button presses or emergency
  handle_movement()

  # Simulate short delay
  # (replace with actual timer or event loop)
  # time.sleep(1)2
  