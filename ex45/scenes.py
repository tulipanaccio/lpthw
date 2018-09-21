from sys import exit
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("Not yet configured")
        print("Use a subclass of it and implement its own enter() method.")
        exit(1)


class Entrance(Scene):

    def enter(self):
        print(dedent("""
            You entered in the house.
            """))
        return 'hall'


class Hall(Scene):

    def enter(self):
        print("HALL")
        return 'kitchen'


class Kitchen(Scene):

    def enter(self):
        print("KITCHEN")
        return 'bedroom'


class Bedroom(Scene):

    def enter(self):
        print("BEDROOM")
        return 'laundry'


class Laundry(Scene):

    def enter(self):
        print("LAUNDRY")
        return 'death'


class Finish(Scene):

    def enter(self):
        print("FINISH")
        return 'finish'


class Death(Scene):

    def enter(self):
        print("DEATH")
        return 'finish'
