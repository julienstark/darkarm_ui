import tkinter as tk
import tkinter.ttk as ttk

class Checkbar(tk.Frame):

    def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.W):
        tk.Frame.__init__(self, parent)
        self.v = tk.IntVar()
        self.v.set(0)
        for val, servo in enumerate(picks):
            var = tk.IntVar()
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

def main_window():

    root = tk.Tk()

    header = tk.Message(root, text="Main")

    header.config(anchor='n',
                  font=("times", 24, "bold"),
                  pady=5)

    header.pack(side=tk.TOP)

    new_canvas = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
    new_canvas.pack(fill=tk.BOTH, expand=True)

    top = tk.Frame(new_canvas)
    center = tk.Frame(new_canvas)
    bottom = tk.Frame(new_canvas)

    top.pack(side=tk.TOP)
    center.pack(side=tk.TOP)
    bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    tk.Button(new_canvas, text='Wake Up', command=root.quit).pack(in_=top, side=tk.LEFT, expand=True)
    tk.Button(new_canvas, text='Go Home').pack(in_=top, side=tk.LEFT)

    tk.Button(new_canvas, text='Jog Joint', command=jog_windows).pack(in_=center, side=tk.LEFT)
    tk.Button(new_canvas, text='Jog Linear', command=jog_linear).pack(in_=center, side=tk.LEFT)

    tk.Button(new_canvas, text='Teach Record', command=teach_record).pack(in_=bottom, side=tk.LEFT)
    tk.Button(new_canvas, text='Teach Point', command=teach_point).pack(in_=bottom, side=tk.LEFT)

    bott_canvas = tk.Frame(root)
    bott_canvas.pack(fill=tk.BOTH, expand=True)

    tk.Message(bott_canvas, text="IN STAND BY POSITION", anchor='s').pack(anchor='c', fill=tk.BOTH, expand=True)

    root.mainloop()

def jog_windows():

    root = tk.Tk()

    header = tk.Message(root, text="Jog Joint")

    header.config(anchor='n',
                  font=("times", 24, "bold"),
                  pady=5)

    header.pack(side=tk.TOP)

    lng = Checkbar(root, ['Servo 1', 'Servo 2', 'Servo 3', 'Servo 4'])
    lng.pack(fill=tk.X)
    lng.config(relief=tk.GROOVE, bd=2)

    tree = ttk.Treeview(root)

    tree["columns"]=("value")
    tree.column("value", width=100)
    tree.heading("value", text="Measure")

    tree.insert("" , 0, text="Angle 4",  values=("180"))
    tree.insert("" , 0, text="Angle 3",  values=("180"))
    tree.insert("" , 0, text="Angle 2",  values=("180"))
    tree.insert("" , 0, text="Angle 1",  values=("180"))

    tree.pack(side=tk.LEFT, expand=False)

    new_canvas = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
    new_canvas.pack(fill=tk.BOTH, expand=True)

    jog_dir = tk.Message(new_canvas, text="Jog Direction", anchor='n',
                         font=("times", 12), width=300)
    jog_dir.pack(anchor='n', fill=tk.X,  expand=True)

    inc_canvas = tk.Frame(new_canvas)
    inc_canvas.pack(fill=tk.BOTH, expand=True)

    jog_inc = tk.Message(inc_canvas, text="Jog Increment", anchor='n',
                         font=("times", 8), width=300)
    jog_inc.pack(anchor='n', fill=tk.BOTH,  expand=True)

    arrowleft = tk.Button(inc_canvas, text="<")
    arrowleft.pack(side=tk.LEFT, expand=True)

    e1 = tk.Entry(inc_canvas)
    e1.pack(side=tk.LEFT, expand=True)

    arrowright = tk.Button(inc_canvas, text=">")
    arrowright.pack(side=tk.LEFT, expand=True)

    grip_canvas = tk.Frame(new_canvas)
    grip_canvas.pack(fill=tk.BOTH, expand=True)

    tk.Button(grip_canvas, text='Open Grip', command=root.quit).pack(anchor="s", side=tk.LEFT, expand=True)
    tk.Button(grip_canvas, text='Close Grip').pack(anchor='s', side=tk.LEFT, expand=True)

    def allstates():
        print(lng.state())

    tk.Button(root, text='Back', command=root.quit).pack(anchor="s", side=tk.RIGHT)
    tk.Button(root, text='Stand By Position', command=allstates).pack(anchor='s', side=tk.RIGHT)
    tk.Button(root, text='Go Home', command=allstates).pack(anchor='s', side=tk.RIGHT)

    tk.Message(root, text="IN STAND BY POSITION", anchor='s').pack(anchor='s', side=tk.LEFT)

    root.mainloop()

def jog_linear():

    root = tk.Tk()

    header = tk.Message(root, text="Jog Linear")

    header.config(anchor='n',
                  font=("times", 24, "bold"),
                  pady=5)

    header.pack(side=tk.TOP)

    lng = Checkbar(root, ['Servo 1', 'Servo 2', 'Servo 3', 'Servo 4', 'Servo 4', 'Servo 5', 'Servo 6'])
    lng.pack(fill=tk.X)
    lng.config(relief=tk.GROOVE, bd=2)

    tree_canvas=tk.Frame(root)
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

    new_canvas = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
    new_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    jog_dir = tk.Message(new_canvas, text="Jog Direction", anchor='n',
                         font=("times", 12), width=300)
    jog_dir.pack(anchor='n', fill=tk.X,  expand=True)

    inc_canvas = tk.Frame(new_canvas)
    inc_canvas.pack(fill=tk.BOTH, expand=True)

    jog_inc = tk.Message(inc_canvas, text="Jog Increment", anchor='n',
                         font=("times", 8), width=300)
    jog_inc.pack(anchor='n', fill=tk.BOTH,  expand=True)

    arrowleft = tk.Button(inc_canvas, text="<")
    arrowleft.pack(side=tk.LEFT, expand=True)

    e1 = tk.Entry(inc_canvas)
    e1.pack(side=tk.LEFT, expand=True)

    arrowright = tk.Button(inc_canvas, text=">")
    arrowright.pack(side=tk.LEFT, expand=True)

    grip_canvas = tk.Frame(new_canvas)
    grip_canvas.pack(fill=tk.BOTH, expand=True)

    tk.Button(grip_canvas, text='Open Grip', command=root.quit).pack(anchor="s", side=tk.LEFT, expand=True)
    tk.Button(grip_canvas, text='Close Grip').pack(anchor='s', side=tk.LEFT, expand=True)

    def allstates():
        print(lng.state())

    bott_canvas = tk.Frame(new_canvas)
    bott_canvas.pack(anchor='s', fill=tk.BOTH, expand=True)

    tk.Button(bott_canvas, text='Back', command=root.quit).pack(anchor="s", side=tk.RIGHT)
    tk.Button(bott_canvas, text='Stand By Position', command=allstates).pack(anchor='s', side=tk.RIGHT)
    tk.Button(bott_canvas, text='Go Home', command=allstates).pack(anchor='s', side=tk.RIGHT)

    tk.Message(bott_canvas, text="IN STAND BY POSITION", anchor='s').pack(anchor='s', side=tk.LEFT)

    root.mainloop()

def teach_record():

    root = tk.Tk()

    header = tk.Message(root, text="Teach Record")

    header.config(anchor='n',
                  font=("times", 24, "bold"),
                  pady=5)

    header.pack(side=tk.TOP)

    tree_canvas=tk.Frame(root)
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

    command_canvas = tk.Frame(root)
    command_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    button_canvas = tk.Frame(command_canvas, relief=tk.RAISED, borderwidth=1)
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

    bott_canvas = tk.Frame(root)
    bott_canvas.pack(anchor='s', fill=tk.BOTH, expand=True)

    tk.Button(bott_canvas, text='Back', command=root.quit).pack(anchor="s", side=tk.RIGHT)
    tk.Button(bott_canvas, text='Stand By Position').pack(anchor='s', side=tk.RIGHT)
    tk.Button(bott_canvas, text='Go Home').pack(anchor='s', side=tk.RIGHT)

    tk.Message(bott_canvas, text="IN STAND BY POSITION", anchor='s').pack(anchor='s', side=tk.LEFT)

    root.mainloop()

def teach_point():

    root = tk.Tk()

    header = tk.Message(root, text="Teach Point")

    header.config(anchor='n',
                  font=("times", 24, "bold"),
                  pady=5)

    header.pack(side=tk.TOP)

    tree_canvas=tk.Frame(root)
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

    command_canvas = tk.Frame(root)
    command_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    button_canvas = tk.Frame(command_canvas, relief=tk.RAISED, borderwidth=1)
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
    teach_points_mess = tk.Message(teach_points_canvas, text="Taught Points")
    teach_points_mess.pack(expand=True)
    teach_points_entry = tk.Message(teach_points_canvas, text="0")
    teach_points_entry.pack(expand=True)

    remain_points_canvas = tk.Frame(points_canvas)
    remain_points_canvas.pack(side=tk.LEFT, expand=True)
    remain_points_mess = tk.Message(remain_points_canvas, text="Remain Points")
    remain_points_mess.pack(expand=True)
    remain_points_entry = tk.Message(remain_points_canvas, text="100")
    remain_points_entry.pack(expand=True)

    grip_canvas = tk.Frame(command_canvas)
    grip_canvas.pack(fill=tk.BOTH, expand=True)

    gripper_open_button = tk.Button(grip_canvas, text="Gripper Open")
    gripper_open_button.pack(side=tk.LEFT, expand=True)

    gripper_close_button = tk.Button(grip_canvas, text="Gripper Close")
    gripper_close_button.pack(side=tk.LEFT, expand=True)

    bott_canvas = tk.Frame(root)
    bott_canvas.pack(anchor='s', fill=tk.BOTH, expand=True)

    tk.Button(bott_canvas, text='Back', command=root.quit).pack(anchor="s", side=tk.RIGHT)
    tk.Button(bott_canvas, text='Stand By Position').pack(anchor='s', side=tk.RIGHT)
    tk.Button(bott_canvas, text='Go Home').pack(anchor='s', side=tk.RIGHT)

    tk.Message(bott_canvas, text="IN STAND BY POSITION", anchor='s').pack(anchor='s', side=tk.LEFT)

    root.mainloop()

if __name__ == '__main__':

    main_window()

