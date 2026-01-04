import json
import time
import random
from datetime import datetime
import os

os.makedirs("input", exist_ok=True)

while True:
    filename = f"input/data_{int(time.time())}.json"

    record = {
        "user_id": random.randint(1, 10),
        "amount": random.randint(100, 1000),
        "event_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(filename, "w") as f:
        json.dump(record, f)

    print(f"Written {filename}")
    time.sleep(2)  # new file every 2 seconds
