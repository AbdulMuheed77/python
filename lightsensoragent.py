# Python ka datetime module import kar rahe hain
from datetime import datetime

# LightSensorAgent naam ka class define kar rahe hain
class LightSensorAgent:
    
    # Constructor function (__init__) hai jo agent ko initialize karta hai
    def __init__(self):
        # Light ka initial status "OFF" set kiya gaya hai
        self.light_status = "OFF"
    
    # Perceive and Act ka method jo light decision leta hai
    def perceive_and_act(self):
        # Hum current hour ko get kar rahe hain (0 se 23 ke beech)
        current_hour = datetime.now().hour  # datetime se current hour le rahe hain
        
        # Decision block: Agar current hour 6 AM se pehle ya 6 PM ke baad ho
        if current_hour < 6 or current_hour >= 18:
            # Agar time raat ka ya shaam ka hai, to light ko ON kar do
            self.light_status = "ON"
        else:
            # Agar time din ka hai, to light ko OFF kar do
            self.light_status = "OFF"
        
        # Return statement: Time aur light status ko return karte hain
        return f"Time: {current_hour}:00 → Light: {self.light_status}"

# Performance measure: Din ke waqt energy save karna aur raat mein light provide karna
# Agent ka object banate hain
agent = LightSensorAgent()

# Agent ka action perform karte hain aur result print karte hain
print(agent.perceive_and_act())
