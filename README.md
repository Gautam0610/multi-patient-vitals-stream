# Multi-Patient Vitals Stream

This project simulates realistic vitals for hundreds of patients, publishes them to a Kafka topic, and periodically simulates sudden cardiac or respiratory events for a small subset of patients.

## Usage

1.  **Prerequisites:**
    *   Kafka broker running and accessible.
    *   Docker installed.

2.  **Configuration:**
    *   Update `utils/config.py` with your Kafka broker URLs and topic name.
    *   `NUM_PATIENTS`: Number of patients to simulate.
    *   `KAFKA_BROKER_URLS`: List of Kafka broker URLs.
    *   `KAFKA_TOPIC`: Kafka topic to publish vitals to.
    *   `EVENT_SIMULATION_INTERVAL`: Interval (in seconds) to simulate cardiac/respiratory events.

3.  **Build and Run with Docker:**

    ```bash
    docker build -t multi-patient-vitals-stream .
    docker run multi-patient-vitals-stream
    ```

## Project Structure

```
multi-patient-vitals-stream/
├── data_generator/
│   ├── patient.py       # Defines the Patient class for generating vitals
│   └── vitals_generator.py  # Generates vitals for multiple patients
├── kafka_producer/
│   └── producer.py      # Publishes vitals to Kafka
├── event_simulator/
│   └── event_simulator.py # Simulates cardiac/respiratory events
├── utils/
│   └── config.py        # Configuration file
├── Dockerfile
├── README.md
└── requirements.txt
```
