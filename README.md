# cstd-rudavskyiivan-2122

_Subject_: Computer systems design theory
_Group_: KI-48
_Developer_: Ivan Rudavskyi
_Student Number_: 15

_Project Game_: Tetris
_HW interface_ - I2C
_Data driven format_ - BINARY

_Play modes_:
    # Man vs AI
    # Man vs Man
    # AI vs AI

_AI supports next complexity levels_:
    # Random move
    # Win strategy

_Actions_:
    # New
    # Save
    # Load

_The proposal for data driven approach: configuration (saved in configuration file or DB)_:
    # board size
    # distance
    # tool size
    # win statement
    # lose statement
    # AI parameters

To run project need to set up python virtual environment:
	Run virtual environment by: `pipenv shell`

_Run project_:
	`python tetris_game.py`
_Run tests_:
	`python -m unittest tetris_test`

_Config_:
    Change config file to choose whether AI will play the game or change the user_name

_Control_:
	Press Left_Key to move figure left
	Press Right_Key to move figure right
	Press Down_key to move figure down faster
	Press Space to instantly move figure down
	Press Up_Key to rotate figure
	Press Escape to start new game
    Press CTRL + S to save a game

__Release version:__ ![version](https://img.shields.io/badge/version-3.0-blue)
