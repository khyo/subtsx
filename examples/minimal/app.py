#!/usr/bin/env python3
import sys, logging, time
from subtsx import TsxElectron


def main():
    print(f"Launched app.py via {sys.executable}: {sys.version}")
    # logging.basicConfig(level=logging.INFO)
    
    te = TsxElectron("TsxMinimal", "./gui.tsx")

    # Register some event handlers before we launch.
    te.on('js-sourced-event', lambda e, arg: print(f"JS sent an event:", e, arg))
    te.on('ping-python', lambda e, arg: f"python-pong-response")

    def delayed_response(event, arg: float):
        time.sleep(arg)
        return f"done with {event}"
    
    te.on('delayed-response', delayed_response)

    # Launch a new browser window. If Electron isn't available yet, it will be downloaded.
    te.launch()

    # Ask many synchronous requests of Javascript as needed.
    while True:
        arg = input("long-process>")
        if arg == "q":
            break
        if not arg.strip():
            continue
        try:
            delay = float(arg)
            resp = te.ask("long-process",delay)
            print("JS responded with:", resp)
        except:
            pass

    # We can close the browser, or if not it will close when Python exits.
    te.close()


if __name__ == "__main__":
    main()
