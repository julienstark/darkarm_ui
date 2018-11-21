"""
Module supporting the main application views of the Robot Arm UI project.

class InfoScreen: Default view of the UI, displaying an informative screen of
the project.

class JogJointScreen: Screen displaying the Jog joint options and controls for
the Robot Arm.

class JogLinearScreen: Screen displaying the Jog linear options and controls
for the Robot Arm.

class TeachRecordScreen: Screen displaying the teach record options for the
Robot Arm.

class TeachPointScreen: Screen displaying the teach points left and teach
options for the Robot Arm.

class ViewManager: The view manager class responsible for displaying and
controlling the different view flows in the UI.
"""


import tkinter as tk
import tkinter.ttk as ttk

import roboarm_utils as rau


class InfoScreen(rau.Screen):
    """Default view of the UI, displaying an informative screen of the
    project.

    Attributes:
        header_canvas: Canvas containing the screen title.
        header_message: Message containing the screen title text.
        content_canvas: Canvas acting as the main screen container.
        left_canvas: Canvas representing the left side of the content.
        right_canvas: Canvas representing the right side of the content.
    """

    def __init__(self, *args, **kwargs):
        """Default InfoScreen builder."""

        rau.Screen.__init__(self, *args, **kwargs)

        header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
        header_canvas.pack(fill=tk.BOTH, pady=25)

        header_message = tk.Message(header_canvas,
                                    text="Robot Arm",
                                    width=200)
        header_message.config(anchor='n',
                              font=("times", 24, "bold"),
                              pady=5)
        header_message.pack(side=tk.TOP, expand=True)

        content_canvas = tk.Frame(self)
        content_canvas.pack(fill=tk.BOTH, expand=True)

        left_canvas = tk.Frame(content_canvas)
        left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right_canvas = tk.Frame(content_canvas, borderwidth=1)
        right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Message(left_canvas,
                   text="Placeholder",
                   width=100).pack()

        tk.Message(right_canvas,
                   text="Welcome to the Robot Arm GUI !",
                   width=500).pack()

        tk.Message(right_canvas,
                   text="Access the command panels with top tabs.",
                   width=500).pack(fill=tk.X)
