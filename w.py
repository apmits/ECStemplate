import esper


# "globals" could go in here:

world = esper.World()

# only need it because I moved the mouse processing
#     from ClickProcessor, to the main loop, for speed reasons.


class Mouse:
    def __init__(self, x=0, y=0, clicked_l=False):  # Default values are required, but also good for debug.
        self.x = x
        self.y = y
        self.clicked_L = clicked_l


mouse = Mouse()  # instanciate here, (in w) so 'mouse.' is "globally" accessible.
