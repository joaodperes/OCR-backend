from enum import Enum

class RoundState(Enum):
    SETUP = 0
    COUNTDOWN = 1
    PLAYING = 2
    ENDING = 3