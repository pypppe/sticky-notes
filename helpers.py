import json
import os

SAVE_FILE = "sticky_save.json"

def save_text(text_widget, bg_color, current_font):
    data = {
        "text": text_widget.get("1.0", "end-1c"),
        "bg": bg_color,
        "font_family": current_font[0],
        "font_size": current_font[1]
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_text(text_widget):
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", data.get("text", ""))
            return data.get("bg", "#fff48c"), (data.get("font_family", "Segoe UI"), data.get("font_size", 11))
    return "#fff48c", ("Segoe UI", 11)

# --- dragging ---
def make_draggable(widget, target_window):
    widget.bind("<ButtonPress-1>", lambda e: start_move(e, target_window))
    widget.bind("<ButtonRelease-1>", lambda e: stop_move(target_window))
    widget.bind("<B1-Motion>", lambda e: do_move(e, target_window))

def start_move(event, win):
    win.start_x = event.x
    win.start_y = event.y

def stop_move(win):
    win.start_x = None
    win.start_y = None

def do_move(event, win):
    x = win.winfo_x() + (event.x - win.start_x)
    y = win.winfo_y() + (event.y - win.start_y)
    win.geometry(f"+{x}+{y}")
