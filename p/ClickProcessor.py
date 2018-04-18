import esper
import w
import c


class ClickProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        #
        # This Processor will iterate over every Entity that has the 'Renderable' + 'Clickable' Components,
        #   and ...
        for ent, (rend, click) in self.world.get_components(c.Renderable, c.Clickable):
            # Debug:
            # print('Entity: {} , rend: {} , click: {}'.format(str(ent), str(rend), str(click)))
            # print('--rend.x: {}'.format(rend.x))
            # print('--rend.y: {}'.format(rend.y))
            # print('--rend.w: {}'.format(rend.w))
            # print('--rend.h: {}'.format(rend.h))
            # print('--rend.depth: {}'.format(rend.depth))
            # print('--rend.image: {}'.format(rend.image))
            # print('--click.to_function: {}'.format(click.to_function))
            if rend.x < w.mouse.x < rend.x + rend.w and rend.y < w.mouse.y < rend.y + rend.h and w.mouse.clicked_L:
                print('Entity {} is clicked!, points to: {}'.format(str(ent), str(click.to_function)))

                # Debug
                print('>>> click.is_selectable: {}'.format(click.is_selectable))
                if click.is_selectable:
                    print('>>> click.is_selectable evaluated True.   click.selected: {}'.format(click.selected))
                    if not click.selected:
                        # add the selector box.
                        # get the "global" selector, and set its .x, .y
                        
                        pass

        #
        # This Processor will iterate over every Entity that has the 'Printable' + 'Clickable' Components,
        #   and ...
        for ent, (txt, click) in self.world.get_components(c.Printable, c.Clickable):
            # Debug:
            # print('Entity: {} , txt: {} , click: {}'.format(str(ent), str(txt), str(click)))
            # print('--click.to_function: {}'.format(click.to_function))
            if txt.x < w.mouse.x < txt.x + txt.w and txt.y < w.mouse.y < txt.y + txt.h and w.mouse.clicked_L:
                print('Entity {} is clicked!, points to: {}'.format(str(ent), str(click.to_function)))
