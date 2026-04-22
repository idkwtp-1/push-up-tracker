import math
import threading
import winsound

def calculate_angle(a, b, c):
    """Calculate angle between three points (in degrees)"""
    try:
        ang = math.degrees(
            math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
        )
        return abs(ang) if abs(ang) <= 180 else 360 - abs(ang)
    except:
        return 0

def play_beep(frequency, duration, enabled=True):
    if not enabled: return
    def _beep():
        try:
            winsound.Beep(frequency, duration)
        except:
            pass
    threading.Thread(target=_beep, daemon=True).start()
