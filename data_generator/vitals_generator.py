
import random
from data_generator.patient import Patient

class VitalsGenerator:
    def __init__(self, num_patients):
        self.num_patients = num_patients
        self.patients = self.create_patients()

    def create_patients(self):
        return [Patient(i) for i in range(self.num_patients)]

    def generate_vitals_batch(self):
        vitals_batch = []
        for patient in self.patients:
            raw_vitals = patient.generate_vitals()
            avg_heart_rate, avg_oxygen_saturation = patient.calculate_rolling_averages()

            # Include rolling averages in the vitals data
            if avg_heart_rate is not None and avg_oxygen_saturation is not None:
                averaged_vitals = {
                    "patient_id": patient.patient_id,
                    "avg_heart_rate": round(avg_heart_rate, 1),
                    "avg_oxygen_saturation": round(avg_oxygen_saturation, 1),
                }
                vitals_batch.append({"raw_vitals": raw_vitals, "averaged_vitals": averaged_vitals})
            else:
                 vitals_batch.append({"raw_vitals": raw_vitals, "averaged_vitals": None})
        return vitals_batch

    def simulate_event(self):
        # Simulate a cardiac or respiratory event for a random subset of patients
        num_affected = random.randint(1, int(0.05 * self.num_patients))
        affected_patients = random.sample(self.patients, num_affected)
        for patient in affected_patients:
            event_type = random.choice(["cardiac_arrest", "respiratory_failure"])
            if event_type == "cardiac_arrest":
                patient.vitals = {
                    "patient_id": patient.patient_id,
                    "heart_rate": 0,
                    "resp_rate": patient.generate_vitals()["resp_rate"],
                    "temperature": patient.generate_vitals()["temperature"],
                    "systolic_bp": 0,
                    "diastolic_bp": 0,
                    "oxygen_saturation": 0,
                    "event": "cardiac_arrest",
                }
            elif event_type == "respiratory_failure":
                patient.vitals = {
                    "patient_id": patient.patient_id,
                    "heart_rate": patient.generate_vitals()["heart_rate"],
                    "resp_rate": 0,
                    "temperature": patient.generate_vitals()["temperature"],
                    "systolic_bp": patient.generate_vitals()["systolic_bp"],
                    "diastolic_bp": patient.generate_vitals()["diastolic_bp"],
                    "oxygen_saturation": 50,
                    "event": "respiratory_failure",
                }

