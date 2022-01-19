from lib.components.resistor import Resistor
from lib.components.ground import Ground

INTERSECTION_COLOR = "red"
END_COLOR = "blue"

CORNER_COLOR = "yellow"
COMPONENT_COLOR = "green"
CONNECTION_COLOR = "pink"
OTHER_NODE_COLOR = "white"

OTHER_EDGE_COLOR = "green"

FOREGROUND = 0
BACKGROUND = 255

CLASS_NAMES = ['capacitor', 'ground', 'inductor', 'resistor', 'up', 'down', 'left', 'right']
CLASS_OBJECT_NAMES = {"cap":'capacitor', "gnd":'ground', "ind":'inductor', "res":'resistor'}
CLASS_OBJECTS = {"resistor":Resistor(),"ground":Ground()}

POSSIBLE_ROTATIONS = [0,90,180,270]

INTERSECTION_COMBINATION_DIST = 3
