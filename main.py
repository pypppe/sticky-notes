from window import create_main_window
from settings import open_settings
from helpers import save_text, load_text

# globals
BG_COLOR = "#fff48c"
CURRENT_FONT = ("Segoe UI", 11)

def set_bg_color(col):
    global BG_COLOR
    BG_COLOR = col
    text.config(bg=BG_COLOR)
    save_text(text, BG_COLOR, CURRENT_FONT)

def set_font(font_name):
    global CURRENT_FONT
    CURRENT_FONT = (font_name, CURRENT_FONT[1])
    text.config(font=CURRENT_FONT)
    save_text(text, BG_COLOR, CURRENT_FONT)

def on_close():
    save_text(text, BG_COLOR, CURRENT_FONT)
    root.destroy()

# --- create window ---
root, text = create_main_window(on_close, lambda: open_settings(root, text, BG_COLOR, CURRENT_FONT, set_bg_color, set_font))

# --- load saved content properly ---
saved_bg, saved_font = load_text(text)
BG_COLOR = saved_bg
CURRENT_FONT = saved_font
text.config(bg=BG_COLOR, font=CURRENT_FONT)  # update text widget with loaded values

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
