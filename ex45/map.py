from scenes import *

class Map(object):

    scenes = {
        'entrance': Entrance(),
        'hall': Hall(),
        'kitchen': Kitchen(),
        'bedroom': Bedroom(),
        'laundry': Laundry(),
        'finish': Finish(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = self.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
