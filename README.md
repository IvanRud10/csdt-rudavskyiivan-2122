# cstd-rudavskyiivan-2122

Subject: Computer systems design theory
Group: KI-48
Developer: Ivan Rudavskyi
Student Number 15

Project Game: Tetris
HW interface - I2C
Data driven format - BINARY

Play modes:
    # Man vs AI
    # Man vs Man
    # AI vs AI

AI supports next complexity levels:
    # Random move
    # Win strategy

Actions:
    # New
    # Save
    # Load

The proposal for data driven approach: configuration (saved in configuration file or DB):
    # board size
    # distance
    # tool size
    # win statement
    # lose statement
    # AI parameters
    
To run project need to set up python virtual environment:
	Run virtual environment by: pipenv shell
	Then install pygame by: pip install pygame
	
How to run project:
	python tetris.py
	
Control:
	Press Left_Key to move figure left
	Press Right_Key to move figure right
	Press Down_key to move figure down faster
	Press Up_Key to rotate figure
	Press Escape to start new game

Version: 1.0
