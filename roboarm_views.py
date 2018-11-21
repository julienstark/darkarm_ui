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


class JogJointScreen(rau.Screen):
    """Screen displaying the Jog joint options and controls for
    the Robot Arm.

    Attributes:
        header_canvas: Canvas containing the screen title.
        header_message: Message containing the screen title text.
        servobar: Checkbar instance representing the servo tab bar.
        rot_tree: Tree instance representing the rotation measure array.
        content_canvas: Canvas acting as the main screen container.
        inc_canvas: Canvas containing the increment objects.
        jog_inc: Message containing the Jog Increment text.
        inc_entry_canvas: Canvas containing the entry text and arrow for
        the increment.
        arrowleft: Left arrow button.
        entry_field = Entry widget for increment.
        arrowright: Right arrow button.
        grip_canvas: Canvas containing the grip button widgets.
    """

    def __init__(self, *args, **kwargs):
        """Default JogJointScreen builder."""

        rau.Screen.__init__(self, *args, **kwargs)

        header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
        header_canvas.pack(fill=tk.BOTH, pady=25)

        header_message = tk.Message(header_canvas,
                                    text="Jog Joint",
                                    width=200)
        header_message.config(anchor='n',
                              font=("times", 24, "bold"),
                              pady=5)
        header_message.pack(side=tk.TOP, expand=True)

        servobar = rau.Checkbar(self,
                                [
                                 'Servo 1',
                                 'Servo 2',
                                 'Servo 3',
                                 'Servo 4',
                                 'Servo 5',
                                 'Servo 6',
                                ])
        servobar.pack(fill=tk.X)
        servobar.config(relief=tk.GROOVE, bd=2)

        rot_tree = ttk.Treeview(self)
        rot_tree["columns"]=("value")
        rot_tree.column("value", width=100)
        rot_tree.heading("value", text="Measure")

        rot_tree.insert("", 0, text="Angle 6", values=("180"))
        rot_tree.insert("", 0, text="Angle 5", values=("180"))
        rot_tree.insert("", 0, text="Angle 4", values=("180"))
        rot_tree.insert("", 0, text="Angle 3", values=("180"))
        rot_tree.insert("", 0, text="Angle 2", values=("180"))
        rot_tree.insert("", 0, text="Angle 1", values=("180"))

        rot_tree.pack(side=tk.LEFT, expand=False)

        content_canvas = tk.Frame(self)
        content_canvas.pack(fill=tk.X, expand=True)

        inc_canvas = tk.Frame(content_canvas)
        inc_canvas.pack(fill=tk.X, expand=True)

        jog_inc = tk.Message(inc_canvas,
                             text="Jog Increment",
                             width=300)
        jog_inc.pack(fill=tk.BOTH, expand=True)
        
        inc_entry_canvas = tk.Frame(inc_canvas)
        inc_entry_canvas.pack()

        arrowleft = tk.Button(inc_entry_canvas, text="<")
        arrowleft.pack(side=tk.LEFT)

        entry_field = tk.Entry(inc_entry_canvas,
                               justify=tk.CENTER)
        entry_field.pack(side=tk.LEFT)

        arrowright = tk.Button(inc_entry_canvas, text=">")
        arrowright.pack(side=tk.LEFT)

        grip_canvas = tk.Frame(content_canvas)
        grip_canvas.pack(fill=tk.BOTH, expand=True)

        tk.Button(grip_canvas,
                  text="Open Grip").pack(anchor="s",
                                         side=tk.LEFT,
                                         expand=True)
        tk.Button(grip_canvas,
                  text="Close Grip").pack(anchor="s",
                                          side=tk.LEFT,
                                          expand=True)


class JogLinearScreen(rau.Screen):
    """Screen displaying the Jog linear options and controls
    for the Robot Arm.

    Attributes:
        header_canvas: Canvas containing the screen title.
        header_message: Message containing the screen title text.
        servobar: Checkbar instance representing the servo tab bar.
        tree_canvas: Canvas including the Tree widgets.
        rot_tree: Tree instance representing the rotation measure array.
        transl_tree: Tree instance representing the translation measure array.
        content_canvas: Canvas acting as the main screen container.
        inc_canvas: Canvas containing the increment objects.
        jog_inc: Message containing the Jog Increment text.
        inc_entry_canvas: Canvas containing the entry text and arrow for
        the increment.
        arrowleft: Left arrow button.
        entry_field = Entry widget for increment.
        arrowright: Right arrow button.
        grip_canvas: Canvas containing the grip button widgets.
    """

    def __init__(self, *args, **kwargs):
        """Default JogLinearScreen builder."""

        rau.Screen.__init__(self, *args, **kwargs)

        header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
        header_canvas.pack(fill=tk.BOTH, pady=25)

        header_message = tk.Message(header_canvas,
                                    text="Jog Linear",
                                    width=200)
        header_message.config(anchor='n',
                              font=("times", 24, "bold"),
                              pady=5)
        header_message.pack(side=tk.TOP, expand=True)

        servobar = rau.Checkbar(self,
                                [
                                 'Servo 1',
                                 'Servo 2',
                                 'Servo 3',
                                 'Servo 4',
                                 'Servo 5',
                                 'Servo 6',
                                ])
        servobar.pack(fill=tk.X)
        servobar.config(relief=tk.GROOVE, bd=2)

        tree_canvas = tk.Frame(self)
        tree_canvas.pack(side=tk.LEFT)

        rot_tree = ttk.Treeview(tree_canvas)
        rot_tree["columns"]=("value")
        rot_tree.column("value", width=100)
        rot_tree.heading("value", text="Measure")

        rot_tree.insert("", 0, text="Angle 6", values=("180"))
        rot_tree.insert("", 0, text="Angle 5", values=("180"))
        rot_tree.insert("", 0, text="Angle 4", values=("180"))
        rot_tree.insert("", 0, text="Angle 3", values=("180"))
        rot_tree.insert("", 0, text="Angle 2", values=("180"))
        rot_tree.insert("", 0, text="Angle 1", values=("180"))

        rot_tree.pack(side=tk.LEFT)

        transl_tree = ttk.Treeview(tree_canvas)
        transl_tree["columns"]=("value")
        transl_tree.column("value", width=100)
        transl_tree.heading("value", text="Measure")

        transl_tree.insert("", 0, text="Z6_Rot", values=("0.00"))
        transl_tree.insert("", 0, text="Y6_Rot", values=("0.00"))
        transl_tree.insert("", 0, text="X6_Rot", values=("0.00"))
        transl_tree.insert("", 0, text="Z", values=("200"))
        transl_tree.insert("", 0, text="Y", values=("250"))
        transl_tree.insert("", 0, text="X", values=("0"))

        transl_tree.pack(side=tk.LEFT)

        content_canvas = tk.Frame(self)
        content_canvas.pack(fill=tk.X, expand=True)

        inc_canvas = tk.Frame(content_canvas)
        inc_canvas.pack(fill=tk.X, expand=True)

        jog_inc = tk.Message(inc_canvas,
                             text="Jog Increment",
                             width=300)
        jog_inc.pack(fill=tk.BOTH, expand=True)
        
        inc_entry_canvas = tk.Frame(inc_canvas)
        inc_entry_canvas.pack()

        arrowleft = tk.Button(inc_entry_canvas, text="<")
        arrowleft.pack(side=tk.LEFT)

        entry_field = tk.Entry(inc_entry_canvas,
                               justify=tk.CENTER)
        entry_field.pack(side=tk.LEFT)

        arrowright = tk.Button(inc_entry_canvas, text=">")
        arrowright.pack(side=tk.LEFT)

        grip_canvas = tk.Frame(content_canvas)
        grip_canvas.pack(fill=tk.BOTH, expand=True)

        tk.Button(grip_canvas,
                  text="Open Grip").pack(anchor="s",
                                         side=tk.LEFT,
                                         expand=True)
        tk.Button(grip_canvas,
                  text="Close Grip").pack(anchor="s",
                                          side=tk.LEFT,
                                          expand=True)