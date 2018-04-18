class Velocity:
    def __init__(self, x=0.0, y=0.0):
        """
        Signifies that the linked entity (that is renderable, see MovementProcessor)
        has a velocity that allows it to move in the window.

        :param x: x velocity
        :param y: y velocity
        """
        self.x = x
        self.y = y
