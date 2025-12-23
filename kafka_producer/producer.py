
from kafka import KafkaProducer
import json
from utils.config import KAFKA_TOPIC

class VitalsProducer:
    def __init__(self, kafka_bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def publish_vitals(self, vitals_batch):
        for vitals in vitals_batch:
            self.producer.send(KAFKA_TOPIC, value=vitals)
        self.producer.flush()
