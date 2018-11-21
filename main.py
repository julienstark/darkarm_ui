"""
Main handler for the Robot Arm UI program.

Usage: python3 main.py
"""

import tkinter as tk

import roboarm_views as rav


def main():
    """Main function for program UI loop."""

    root = tk.Tk()

    main_view = rav.MainView(root)
    main_view.pack(side="top", fill="both", expand=True)

    root.wm_geometry("1100x400")

    root.mainloop()


if __name__ == '__main__':
    main()