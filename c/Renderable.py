import pygame


class Renderable:
    def __init__(self, image, posx=None, posy=None, depth=0):
        """
        Signifies that the linked entity has a renderable image representation in the application window.

        :param image: image to use
        :param posx: x position in window
        :param posy: y position in window
        :param depth: depth
        """
        self.image = pygame.image.load(image)
        self.depth = depth
        self.x = posx
        self.y = posy
        self.w = self.image.get_width()
        self.h = self.image.get_height()
