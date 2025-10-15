import tkinter as tk
from tkinter import ttk
from helpers import save_text

def open_settings(root, text_widget, bg_color, current_font, set_bg_callback, set_font_callback):
    settings_window = tk.Toplevel(root)
    settings_window.overrideredirect(True)
    settings_window.attributes("-topmost", True)
    settings_window.geometry("240x200")
    settings_window.config(bg="#eee8d5")

    from helpers import make_draggable
    make_draggable(settings_window, settings_window)

    close_btn = tk.Label(settings_window, text="✕", bg="#eee8d5", fg="#000", font=("Segoe UI", 10, "bold"), cursor="hand2")
    close_btn.pack(side="top", anchor="ne", padx=5, pady=5)
    close_btn.bind("<Button-1>", lambda e: settings_window.destroy())

    tk.Label(settings_window, text="Colors:", bg="#eee8d5", font=("Segoe UI", 10, "bold")).pack(pady=(10,0))
    color_frame = tk.Frame(settings_window, bg="#eee8d5")
    color_frame.pack(pady=5)
    colors = ["#fff48c", "#ffb3b3", "#b3ffb3", "#b3d9ff", "#ffdfb3"]
    for c in colors:
        btn = tk.Button(color_frame, bg=c, width=3, height=1, bd=0, command=lambda col=c: set_bg_callback(col))
        btn.pack(side="left", padx=3)

    tk.Label(settings_window, text="Font:", bg="#eee8d5", font=("Segoe UI", 10, "bold")).pack(pady=(10,0))
    font_options = ["Segoe UI", "Arial", "Calibri", "Verdana", "Comic Sans MS"]
    font_var = tk.StringVar(value=current_font[0])
    font_dropdown = ttk.Combobox(settings_window, values=font_options, textvariable=font_var, state="readonly")
    font_dropdown.pack(pady=5)
    font_dropdown.bind("<<ComboboxSelected>>", lambda e: set_font_callback(font_var.get()))

