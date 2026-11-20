"""Mycelium Base: opens the game in a native window (Windows, macOS, Linux)."""
import os
import sys

import webview


def resource(name):
    # PyInstaller unpacks bundled files to _MEIPASS; otherwise use this folder.
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


if __name__ == "__main__":
    webview.create_window(
        "Mycelium Base",
        resource("index.html"),
        width=1280,
        height=820,
        min_size=(960, 640),
        background_color="#070b0c",
    )
    webview.start()
