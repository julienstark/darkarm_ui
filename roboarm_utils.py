"""
Module supporting various helper functions and classes for the Robot Arm UI project.

class Checkbar: initializes a tkinter widget displaying arbitrary clickable label tabs.

class Screen: base class for the various screens that the application displays
"""


import tkinter as tk


class Checkbar(tk.Frame):
    """This class initializes tkinter widget containing various clickable label tabs.

    Attributes:
        var_id: An int identifying the label being selected.
    """

    def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.W):
        """Checkbar class default builder."""

        tk.Frame.__init__(self, parent)
        self.var_id = tk.IntVar()
        self.var_id.set(0)

        for val, label in enumerate(picks):
            _var = tk.IntVar()
            chk = tk.Radiobutton(self,
                                 text=label,
                                 indicatoron=0,
                                 padx=20,
                                 width=20,
                                 variable=self.var_id,
                                 value=val)
            chk.pack(side=side, anchor=anchor, expand=tk.YES)

    def state(self):
        """Returns the value of the label currently selected.

        Args:
            None

        Returns:
            An int representing the index of the label currently selected.
        """

        return self.var_id.get()


class Screen(tk.Frame):
    """Base class for all screen classes that includes the UI.

    Attributes:
        None
    """

    def __init__(self, *args, **kwargs):
        """Screen class default builder."""

        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        """Invokes the screen on the frontpage of the application.

        Args:
            None

        Returns:
            None
        """

        self.lift()