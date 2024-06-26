import sys
import os
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from src.game.engine import TicTacToe
from src.game.players import RandomComputerPlayer, MinimaxComputerPlayer
from src.logic.models import Mark

from console.renderers import ConsoleRenderer
from console.players import ConsolePlayer

player1 = ConsolePlayer(Mark("X"))
# player2 = RandomComputerPlayer(Mark("X"))
player2 = MinimaxComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()