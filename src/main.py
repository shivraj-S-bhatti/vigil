# src/main.py
import argparse
import threading
from pathlib import Path

from dataio import load_time_series
from pipeline import run_stream

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="assets/sample_logs.csv")
    parser.add_argument("--threshold", type=float, default=3.0)
    args = parser.parse_args()

    # import Tk UI only when needed (avoids tk issues in headless)
    from ui import App

    selected_file = None
    stop_flag = {"stop": False}

    def on_file_selected(path: str):
        nonlocal selected_file
        selected_file = path
        app.show_alert(f"[info] Loaded file: {path}")

    def on_start(thresh: float):
        if not selected_file:
            app.show_alert("[warn] Select a CSV first.")
            return
        df = load_time_series(selected_file)
        stop_flag["stop"] = False
        threading.Thread(
            target=run_stream,
            args=(df, float(thresh), app.show_alert, stop_flag),
            daemon=True,
        ).start()

    def on_stop():
        stop_flag["stop"] = True
        app.show_alert("[info] Stopped.")

    # construct UI
    app = App(on_file_selected, on_start, on_stop)

    # bring window to front on macOS (and others)
    app.after(50, lambda: app.lift())
    app.after(60, lambda: app.focus_force())
    app.after(70, lambda: app.attributes("-topmost", True))
    app.after(200, lambda: app.attributes("-topmost", False))

    # autoload sample if present
    default_path = Path(args.file)
    if default_path.exists():
        on_file_selected(str(default_path))
    app.show_alert("[info] UI ready. Click Start to begin.")
    app.mainloop()

if __name__ == "__main__":
    main()
