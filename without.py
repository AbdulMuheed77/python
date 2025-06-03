from datetime import datetime

class LightSensorAgent:
    
    def __init__(self):
        self.light_status = "OFF"
    
    def perceive_and_act(self):
        current_hour = datetime.now().hour
        
        if current_hour < 6 or current_hour >= 18:
            self.light_status = "ON"
        else:
            self.light_status = "OFF"
        
        return f"Time: {current_hour}:00 → Light: {self.light_status}"

agent = LightSensorAgent()
print(agent.perceive_and_act())
