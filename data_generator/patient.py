
import random

class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.age = random.randint(18, 85)
        self.initial_health_condition = random.choice(["Good", "Moderate", "Poor"])

    def generate_vitals(self):
        # Simulate vital signs based on age and initial condition
        heart_rate = int(random.normalvariate(70, 10) + (self.age - 50) * 0.5)
        resp_rate = int(random.normalvariate(16, 2) + (self.age - 60) * 0.1)
        temperature = round(random.normalvariate(98.6, 0.3), 1)
        systolic_bp = int(random.normalvariate(120, 15) + (self.age - 40) * 0.8)
        diastolic_bp = int(random.normalvariate(80, 10) + (self.age - 50) * 0.4)
        oxygen_saturation = int(random.normalvariate(97, 1.5))

        # Ensure values are within realistic ranges
        heart_rate = max(50, min(heart_rate, 150))
        resp_rate = max(12, min(resp_rate, 30))
        temperature = max(95, min(temperature, 104))
        systolic_bp = max(80, min(systolic_bp, 200))
        diastolic_bp = max(50, min(diastolic_bp, 120))
        oxygen_saturation = max(85, min(oxygen_saturation, 100))

        vitals = {
            "patient_id": self.patient_id,
            "heart_rate": heart_rate,
            "resp_rate": resp_rate,
            "temperature": temperature,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp,
            "oxygen_saturation": oxygen_saturation,
        }
        return vitals
