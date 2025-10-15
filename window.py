import tkinter as tk
from helpers import make_draggable

def create_main_window(on_close_callback, open_settings_callback):
    root = tk.Tk()
    root.title("Sticky Note")
    root.geometry("350x350")
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.resizable(True, True)

    # header
    header = tk.Frame(root, bg="#ffef70", height=28)
    header.pack(fill="x", side="top")
    title = tk.Label(header, text="Sticky Note", bg="#ffef70", fg="#000", font=("Segoe UI", 10, "bold"))
    title.pack(side="left", padx=10, pady=4)
    close_btn = tk.Label(header, text="✕", bg="#ffef70", fg="#000", font=("Segoe UI", 10, "bold"), cursor="hand2")
    close_btn.pack(side="right", padx=5)
    close_btn.bind("<Button-1>", lambda e: on_close_callback())
    settings_btn = tk.Label(header, text="⚙", bg="#ffef70", fg="#000", font=("Segoe UI", 10, "bold"), cursor="hand2")
    settings_btn.pack(side="right", padx=5)
    settings_btn.bind("<Button-1>", lambda e: open_settings_callback())

    make_draggable(header, root)

    # text area
    text = tk.Text(root, wrap="word", font=("Segoe UI", 11), bg="#fff48c", fg="#202020", bd=0, highlightthickness=0, insertbackground="#000000")
    text.pack(expand=True, fill="both")
    return root, text
