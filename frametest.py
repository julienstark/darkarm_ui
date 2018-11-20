import tkinter as tk
import tkinter.ttk as ttk

class Checkbar(tk.Frame):

    def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.W):
        tk.Frame.__init__(self, parent)
        self.v = tk.IntVar()
        self.v.set(0)
        for val, servo in enumerate(picks):
            _var = tk.IntVar()
            chk = tk.Radiobutton(self,
                                 text=servo,
                                 indicatoron=0,
                                 padx=20,
                                 width=20,
                                 variable=self.v,
                                 value=val)
            chk.pack(side=side, anchor=anchor, expand=tk.YES)

    def state(self):
        return self.v.get()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
       header_canvas.pack(fill=tk.BOTH, pady=25)
       header = tk.Message(header_canvas, text="Robot Arm", width=200)

       header.config(anchor='n',
                   font=("times", 24, "bold"),
                   pady=5)

       header.pack(side=tk.TOP, expand=True)

       new_canvas = tk.Frame(self)
       new_canvas.pack(fill=tk.BOTH, expand=True)

       left_canvas = tk.Frame(new_canvas)
       left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
       right_canvas = tk.Frame(new_canvas, borderwidth=1)
       right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

       tk.Message(left_canvas, text='Placeholder', width=100).pack()

       tk.Message(right_canvas, text='Welcome to the Robot Arm GUI !', width=900).pack()
       tk.Message(right_canvas, text='Access the various command panels with tabs on the top.', width=500).pack(fill=tk.X)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
       header_canvas.pack(fill=tk.BOTH, pady=25)
       header = tk.Message(header_canvas, text="Jog Joint", width=200)

       header.config(anchor='n',
                   font=("times", 24, "bold"),
                   pady=5)

       header.pack(side=tk.TOP, expand=True)

       lng = Checkbar(self, ['Servo 1', 'Servo 2', 'Servo 3', 'Servo 4', 'Servo 5', 'Servo 6'])
       lng.pack(fill=tk.X)
       lng.config(relief=tk.GROOVE, bd=2)

       tree = ttk.Treeview(self)

       tree["columns"]=("value")
       tree.column("value", width=100)
       tree.heading("value", text="Measure")

       tree.insert("" , 0, text="Angle 6",  values=("180"))
       tree.insert("" , 0, text="Angle 5",  values=("180"))
       tree.insert("" , 0, text="Angle 4",  values=("180"))
       tree.insert("" , 0, text="Angle 3",  values=("180"))
       tree.insert("" , 0, text="Angle 2",  values=("180"))
       tree.insert("" , 0, text="Angle 1",  values=("180"))

       tree.pack(side=tk.LEFT, expand=False)

       new_canvas = tk.Frame(self)
       new_canvas.pack(fill=tk.X, expand=True)

       inc_canvas = tk.Frame(new_canvas)
       inc_canvas.pack(fill=tk.X, expand=True)

       jog_inc = tk.Message(inc_canvas, text="Jog Increment", width=300)
       jog_inc.pack(fill=tk.BOTH,  expand=True)

       inc_entry_canvas = tk.Frame(inc_canvas)
       inc_entry_canvas.pack()

       arrowleft = tk.Button(inc_entry_canvas, text="<")
       arrowleft.pack(side=tk.LEFT)

       e1 = tk.Entry(inc_entry_canvas, justify=tk.CENTER)
       e1.pack(side=tk.LEFT)

       arrowright = tk.Button(inc_entry_canvas, text=">")
       arrowright.pack(side=tk.LEFT)

       grip_canvas = tk.Frame(new_canvas)
       grip_canvas.pack(fill=tk.BOTH, expand=True)

       tk.Button(grip_canvas, text='Open Grip').pack(anchor="s", side=tk.LEFT, expand=True)
       tk.Button(grip_canvas, text='Close Grip').pack(anchor='s', side=tk.LEFT, expand=True)

       def allstates():
           print(lng.state())

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
       header_canvas.pack(fill=tk.BOTH, pady=25)
       header = tk.Message(header_canvas, text="Jog Linear", width=200)

       header.config(anchor='n',
                   font=("times", 24, "bold"),
                   pady=5)

       header.pack(side=tk.TOP, expand=True)

       lng = Checkbar(self, ['Servo 1', 'Servo 2', 'Servo 3', 'Servo 4', 'Servo 5', 'Servo 6'])
       lng.pack(fill=tk.X)
       lng.config(relief=tk.GROOVE, bd=2)

       tree_canvas=tk.Frame(self)
       tree_canvas.pack(side=tk.LEFT)

       tree = ttk.Treeview(tree_canvas)

       tree["columns"]=("value")
       tree.column("value", width=100)
       tree.heading("value", text="Measure")

       tree.insert("" , 0, text="Angle 6",  values=("180"))
       tree.insert("" , 0, text="Angle 5",  values=("180"))
       tree.insert("" , 0, text="Angle 4",  values=("180"))
       tree.insert("" , 0, text="Angle 3",  values=("180"))
       tree.insert("" , 0, text="Angle 2",  values=("180"))
       tree.insert("" , 0, text="Angle 1",  values=("180"))

       tree.pack(side=tk.LEFT)

       tree2 = ttk.Treeview(tree_canvas)

       tree2["columns"]=("value")
       tree2.column("value", width=100)
       tree2.heading("value", text="Measure")

       tree2.insert("" , 0, text="Z6_Rot",  values=("0.00"))
       tree2.insert("" , 0, text="Y6_Rot",  values=("0.00"))
       tree2.insert("" , 0, text="X6_Rot",  values=("0.00"))
       tree2.insert("" , 0, text="Z",  values=("200"))
       tree2.insert("" , 0, text="Y",  values=("250"))
       tree2.insert("" , 0, text="X",  values=("0"))

       tree2.pack(side=tk.LEFT)

       new_canvas = tk.Frame(self)
       new_canvas.pack(fill=tk.X, expand=True)

       inc_canvas = tk.Frame(new_canvas)
       inc_canvas.pack(fill=tk.X, expand=True)

       jog_inc = tk.Message(inc_canvas, text="Jog Increment", width=300)
       jog_inc.pack(fill=tk.BOTH, expand=True)

       inc_entry_canvas = tk.Frame(inc_canvas)
       inc_entry_canvas.pack()

       arrowleft = tk.Button(inc_entry_canvas, text="<")
       arrowleft.pack(side=tk.LEFT)

       e1 = tk.Entry(inc_entry_canvas, justify=tk.CENTER)
       e1.pack(side=tk.LEFT)

       arrowright = tk.Button(inc_entry_canvas, text=">")
       arrowright.pack(side=tk.LEFT)

       grip_canvas = tk.Frame(new_canvas)
       grip_canvas.pack(fill=tk.BOTH, expand=True)

       tk.Button(grip_canvas, text='Open Grip').pack(anchor="s", side=tk.LEFT, expand=True)
       tk.Button(grip_canvas, text='Close Grip').pack(anchor='s', side=tk.LEFT, expand=True)

       def allstates():
           print(lng.state())


class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
       header_canvas.pack(fill=tk.BOTH, pady=25)
       header = tk.Message(header_canvas, text="Teach Record", width=200)

       header.config(anchor='n',
                   font=("times", 24, "bold"),
                   pady=5)

       header.pack(side=tk.TOP, expand=True)

       tree_canvas=tk.Frame(self)
       tree_canvas.pack(side=tk.LEFT)

       tree = ttk.Treeview(tree_canvas)

       tree["columns"]=("value")
       tree.column("value", width=100)
       tree.heading("value", text="Measure")

       tree.insert("" , 0, text="Angle 6",  values=("180"))
       tree.insert("" , 0, text="Angle 5",  values=("180"))
       tree.insert("" , 0, text="Angle 4",  values=("180"))
       tree.insert("" , 0, text="Angle 3",  values=("180"))
       tree.insert("" , 0, text="Angle 2",  values=("180"))
       tree.insert("" , 0, text="Angle 1",  values=("180"))

       tree.pack(side=tk.LEFT)

       command_canvas = tk.Frame(self)
       command_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

       button_canvas = tk.Frame(command_canvas)
       button_canvas.pack(fill=tk.BOTH, expand=True)

       play_button = tk.Button(button_canvas, text="Play")
       play_button.pack(side=tk.LEFT, expand=True)

       pause_button = tk.Button(button_canvas, text="Pause")
       pause_button.pack(side=tk.LEFT, expand=True)

       record_button = tk.Button(button_canvas, text="Record")
       record_button.pack(side=tk.LEFT, expand=True)

       clear_button = tk.Button(button_canvas, text="Clear")
       clear_button.pack(side=tk.LEFT, expand=True)

       grip_canvas = tk.Frame(command_canvas)
       grip_canvas.pack(fill=tk.BOTH, expand=True)

       gripper_open_button = tk.Button(grip_canvas, text="Gripper Open")
       gripper_open_button.pack(side=tk.LEFT, expand=True)

       gripper_close_button = tk.Button(grip_canvas, text="Gripper Close")
       gripper_close_button.pack(side=tk.LEFT, expand=True)


class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       header_canvas = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
       header_canvas.pack(fill=tk.BOTH, pady=25)
       header = tk.Message(header_canvas, text="Teach Point", width=200)

       header.config(anchor='n',
                   font=("times", 24, "bold"),
                   pady=5)

       header.pack(side=tk.TOP, expand=True)

       tree_canvas=tk.Frame(self)
       tree_canvas.pack(side=tk.LEFT)

       tree = ttk.Treeview(tree_canvas)

       tree["columns"]=("value")
       tree.column("value", width=100)
       tree.heading("value", text="Measure")

       tree.insert("" , 0, text="Angle 6",  values=("180"))
       tree.insert("" , 0, text="Angle 5",  values=("180"))
       tree.insert("" , 0, text="Angle 4",  values=("180"))
       tree.insert("" , 0, text="Angle 3",  values=("180"))
       tree.insert("" , 0, text="Angle 2",  values=("180"))
       tree.insert("" , 0, text="Angle 1",  values=("180"))

       tree.pack(side=tk.LEFT)

       command_canvas = tk.Frame(self)
       command_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

       button_canvas = tk.Frame(command_canvas)
       button_canvas.pack(fill=tk.BOTH, expand=True)

       play_button = tk.Button(button_canvas, text="Play")
       play_button.pack(side=tk.LEFT, expand=True)

       pause_button = tk.Button(button_canvas, text="Pause")
       pause_button.pack(side=tk.LEFT, expand=True)

       record_button = tk.Button(button_canvas, text="Teach")
       record_button.pack(side=tk.LEFT, expand=True)

       clear_button = tk.Button(button_canvas, text="Clear")
       clear_button.pack(side=tk.LEFT, expand=True)

       points_canvas = tk.Frame(command_canvas)
       points_canvas.pack(fill=tk.BOTH, expand=True)

       tot_points_canvas = tk.Frame(points_canvas)
       tot_points_canvas.pack(side=tk.LEFT, expand=True)
       tot_points_mess = tk.Message(tot_points_canvas, text="Total Points")
       tot_points_mess.pack(expand=True)
       tot_points_entry = tk.Message(tot_points_canvas, text="100")
       tot_points_entry.pack(expand=True)


       teach_points_canvas = tk.Frame(points_canvas)
       teach_points_canvas.pack(side=tk.LEFT, expand=True)
       teach_points_mess = tk.Message(teach_points_canvas, text="Taught Points", width=100)
       teach_points_mess.pack(expand=True)
       teach_points_entry = tk.Message(teach_points_canvas, text="0")
       teach_points_entry.pack(expand=True)

       remain_points_canvas = tk.Frame(points_canvas)
       remain_points_canvas.pack(side=tk.LEFT, expand=True)
       remain_points_mess = tk.Message(remain_points_canvas, text="Remain Points", width=100)
       remain_points_mess.pack(expand=True)
       remain_points_entry = tk.Message(remain_points_canvas, text="100")
       remain_points_entry.pack(expand=True)

       grip_canvas = tk.Frame(command_canvas)
       grip_canvas.pack(fill=tk.BOTH, expand=True)

       gripper_open_button = tk.Button(grip_canvas, text="Gripper Open")
       gripper_open_button.pack(side=tk.LEFT, expand=True)

       gripper_close_button = tk.Button(grip_canvas, text="Gripper Close")
       gripper_close_button.pack(side=tk.LEFT, expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p2 = Page2(self)
        p3 = Page3(self)
        p1 = Page1(self)
        p4 = Page4(self)
        p5 = Page5(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        alerter = tk.Frame(self)
        alerter.pack(side="bottom")

        line_canvas = tk.Canvas(alerter, width=1100, height=20)
        line_canvas.pack()

        line_canvas.create_line(0, 20, 1100, 20)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Jog Joint", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Jog Linear", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Teach Record", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Teach Point", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Stand By Position")
        b7 = tk.Button(buttonframe, text="Go Home")
        b8 = tk.Button(buttonframe, text="Quit", command=self.quit)


        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        b8.pack(side="right")
        b6.pack(side="right")
        b7.pack(side="right")

        position = tk.Message(alerter, text="STAND BY POSITION", width="309", pady="15")
        position.pack(side="bottom", expand=True, fill=tk.BOTH)

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1100x400")
    root.mainloop()