class Printable:
    def __init__(self, text='', x=0, y=0):
        """
        Signifies that the linked entity has a printable text representation in the application window.

        :param text: text to be printed
        :param x: x pos in window
        :param y: y pos in window
        """
        self.text = text
        self.x = x
        self.y = y
        self.w = 0  # Default value; proper value is SET in the PrintProcessor.
        self.h = 0  # Default value; proper value is SET in the PrintProcessor.
