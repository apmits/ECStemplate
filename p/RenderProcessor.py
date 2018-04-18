import esper
import pygame
import c


class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        # Clear the window:
        self.window.fill(self.clear_color)
        # This will iterate over every Entity that has this Component, and blit it (paint it):
        for ent, rend in self.world.get_component(c.Renderable):
            if rend.x is not None and rend.y is not None:
                # /\_ the None check is for cases where .x and .y are initialised as None,
                #     e.g. a Selector, which is not required to be rendered immediately.
                self.window.blit(rend.image, (rend.x, rend.y))

        # Flip the frame-buffers (Update the contents of the entire display.)
        pygame.display.flip()  # maybe move this to main() for efficiency?
