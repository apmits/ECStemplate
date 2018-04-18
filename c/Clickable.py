class Clickable:
    def __init__(self, to_function=None, is_selectable=False):
        """ Signifies that linked entity (that is either renderable or clickable; see ClickProcessor for impl details)
            can be clicked.
            Left clicking results in calling function: to_function.
        """
        self.to_function = to_function
        self.is_selectable = is_selectable
        if self.is_selectable:
            self.selected = False
