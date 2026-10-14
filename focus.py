import argparse
import time
import sys

def timer(minutes):
    seconds = minutes * 60
    print(f"Starting focus session: {minutes} minutes")
    try:
        while seconds > 0:
            m, s = divmod(seconds, 60)
            sys.stdout.write(f"\rTime remaining: {m:02d}:{s:02d} ")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        print("\nFocus session completed! Great job.")
    except KeyboardInterrupt:
        print("\nSession paused.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI focus timer")
    parser.add_argument("--minutes", "-m", type=int, default=25, help="Session duration in minutes (default: 25)")
    args = parser.parse_args()
    timer(args.minutes)
