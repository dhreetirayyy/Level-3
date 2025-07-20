import os
import sys

def shutdown_windows(time_in_seconds=0, force=False):
    """
    Initiates a shutdown on Windows.

    Args:
        time_in_seconds (int): Delay in seconds before shutdown. Default is 0 (immediate).
        force (bool): Forces applications to close.
    """
    command = "shutdown /s"
    if time_in_seconds > 0:
        command += f" /t {time_in_seconds}"
    if force:
        command += " /f"

    print(f"Executing command: {command}")
    try:
        os.system(command)
        print("Shutdown command sent to Windows.")
    except Exception as e:
        print(f"Error executing shutdown command: {e}")
        print("Please ensure your script has the necessary permissions.")

if __name__ == '__main__':
    if sys.platform == "win32":
        print("Attempting to schedule a Windows shutdown in 30 seconds (forced)...")
        shutdown_windows(time_in_seconds=30, force=True)
        print("\nTo cancel a scheduled shutdown on Windows, open Command Prompt and type 'shutdown /a'")
    else:
        print("This Windows shutdown function is not applicable to your operating system.")