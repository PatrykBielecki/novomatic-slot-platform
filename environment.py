import os
import sys

# make src/ importable
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from application.controllers import GameController

def before_all(context):
    context.controller = GameController()

def before_scenario(context, scenario):
    context.player = None
    context.last_spin = None
    context.error = None
    context.memory = {}
