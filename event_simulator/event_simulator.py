
import time
from data_generator.vitals_generator import VitalsGenerator
from kafka_producer.producer import VitalsProducer
from utils.config import NUM_PATIENTS, KAFKA_BROKER_URLS, EVENT_SIMULATION_INTERVAL

def main():
    vitals_generator = VitalsGenerator(NUM_PATIENTS)
    vitals_producer = VitalsProducer(KAFKA_BROKER_URLS)

    while True:
        vitals_batch = vitals_generator.generate_vitals_batch()
        vitals_producer.publish_vitals(vitals_batch)

        #Simulate events periodically
        if time.time() % EVENT_SIMULATION_INTERVAL < 1: #Check if the current time modulo the interval is less than 1 second
            vitals_generator.simulate_event()

        time.sleep(1)

if __name__ == "__main__":
    main()
