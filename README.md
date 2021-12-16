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
	
How to run project:
	python tetris_game.py
	
Control:
	Press Left_Key to move figure left
	Press Right_Key to move figure right
	Press Down_key to move figure down faster
	Press Space to instantly move figure down
	Press Up_Key to rotate figure
	Press Escape to start new game

__Release version:__ ![version](https://img.shields.io/badge/version-1.0-blue) 
