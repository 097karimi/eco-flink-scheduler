# workload-generator/producer.py
import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer


TOPIC = "eco-workload"
BOOTSTRAP_SERVERS = "localhost:9092"


def build_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def generate_event() -> dict:
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_id": random.randint(1000, 9999),
        "load": round(random.uniform(0.1, 1.0), 3),
        "source": "workload-generator",
    }


def main() -> None:
    producer = build_producer()
    print(f"Producing events to topic: {TOPIC}")

    while True:
        event = generate_event()
        producer.send(TOPIC, event)
        producer.flush()
        print(f"Sent: {event}")
        time.sleep(1)


if __name__ == "__main__":
    main()
