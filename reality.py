import pint, time
from sympy import Rational

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

class Entity(object):
    def __init__(self, name, color=None, children_items=(), features=(), dimensions=(), position={}):
        self.name = name
        self.color = color
        self.items = children_items
        self.features = features
        self.dimensions = dimensions
        self.position = position

class Character(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class Dialogue(object):
    def __init__(self, character_name, dialogue):
        self.character = character_name
        self.dialogue = dialogue

class Action(object):
    def __init__(self, character, description, subject=None, quantity=None, features=()):
        self.character = character
        self.description = description
        self.subject = subject
        self.quantity = quantity
        self.features = features

class Pause(object):
    def __init__(self, pause_seconds):
        self.pause_length = pause_seconds

class Act(object):
    def __init__(self, act_num, act_name, scenes=()):
        self.no = act_num
        self.name = act_name
        self.scenes = scenes

class Scene(object):
    def __init__(self, scene_num, scene_name, scene_time, scene_remaining_hours, scene_remaining_minutes, scene_items=()):
        self.no = scene_num
        self.name = scene_name
        self.date = time.strptime(scene_time, '%B %d, %Y at %I:%M %p %Z')
        self.remaining_hrs = scene_remaining_hours
        self.remaining_mins = scene_remaining_minutes
        self.items = scene_items

class Color(object):
    def __init__(self, color_code: str):
        # Ulillillia uses ARGB so we'll go with that
        self.opacity, self.red, self.green, self.blue = [int(color_code[i:i+2], base=16) for i in range(0, 8, 2)]

def Quantity(number, unit):
    return Q_(number, unit)
