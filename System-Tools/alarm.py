import time
import winsound
from win10toast import ToastNotifier

def timer(message, minutes):
    # Windows Notification Instantiator
    notificator = ToastNotifier()
    # Notification Details
    notificator.show_toast("Alarm",
        f"Alarm wil go off in {minutes} minutes..",
        duration=50)
    # Pause Script
    time.sleep(minutes * 60)
    # Alarm Sound
    winsound.Beep(frequency=2500, duration=1000)
    # Show Notification
    notificator.show_toast(f"Alarm", message, duration=50)

if __name__ == "__main__":
    message = "Post on github!"
    minutes = 20
    timer(message, minutes)
