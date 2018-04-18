import esper
import w
import c


class SelectProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        #
        # This Processor will iterate over every Entity that has the 'Selectable' Components,
        #   and ...
        for ent, (rend, click) in self.world.get_components(c.Selectable):
            pass
