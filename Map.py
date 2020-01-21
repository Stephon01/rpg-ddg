# Course: CS 30
# Period: 1
# Date created: 20/01/21
# Date last modified: 20/01/21
# Name: Stephon Murray
# Description: Maps and Modules
class MapTile:
    def __init__(user, x, y):
        user.x = x
        user.y = y

    def intro_text(user):

        class StartTile(MapTile):
            def intro_text(user):
                raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(user):
        return """ stuck in the dark shadows of death, u naturally become to see in the dark """

class BoringTile(MapTile):
    def intro_text(user):
        return """ boring part of the krypt """

class VictoryTile(MapTile):
    def intro_text(user):
        return """ to the end of the hallway you see ermacs orb"""
world_map = [
    [None,StartTile(1,0),None],
    [None,BoringTile(1,1),None],
    [None,VictoryTile(1,3),None]
]

def tile_at(x, y):
 if x < 0 or y < 0:
     return None
