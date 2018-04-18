import esper
import pygame
import c


class PrintProcessor(esper.Processor):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def process(self):
        # Font initialisation (required).
        pygame.font.init()  # The .font(..) module must be initialized before any other functions will work.
        #                     It is safe to call the init function more than once.
        # How to use:         https://www.pygame.org/docs/ref/font.html

        # This will iterate over every Entity that has this Component, and "blit" the surface to the frame-buffer.
        for ent, txt in self.world.get_component(c.Printable):
            myfont = pygame.font.Font('dina10px.ttf', 18)  # uses the font from project dir.
            textsurface = myfont.render(txt.text, False, (0, 128, 0))  # RGB, GREEN

            # SET (update) the proper component values, of given entities.
            txt.w, txt.h = myfont.size(txt.text)

            self.window.blit(textsurface, (txt.x, txt.y))  # POSITION

        # Flip the frame-buffers (Update the contents of the entire display.)
        pygame.display.flip()  # maybe move this to main() for efficiency?
