import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Constants
NUM_USERS = 10
NUM_SESSIONS_PER_USER = 5
MAX_CONTENT_PER_SESSION = 10
CONTENT_IDS = [f"movie_{i}" for i in range(1, 21)]

def generate_user_watch_data():
    records = []

    for user_id in range(1, NUM_USERS + 1):
        for session_id in range(1, NUM_SESSIONS_PER_USER + 1):
            start_time = datetime.now() - timedelta(days=random.randint(0, 30))
            num_contents = random.randint(1, MAX_CONTENT_PER_SESSION)
            for _ in range(num_contents):
                duration = random.randint(10, 90)  # minutes
                content_id = random.choice(CONTENT_IDS)
                records.append({
                    "user_id": f"user_{user_id}",
                    "session_id": session_id,
                    "timestamp": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "content_id": content_id,
                    "duration_minutes": duration
                })
                # Add some time between watch events
                start_time += timedelta(minutes=duration + random.randint(1, 5))

    return pd.DataFrame(records)

def main():
    df = generate_user_watch_data()

    # Create 'data/' folder if it doesn't exist
    output_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "synthetic_watch_data.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Synthetic watch history data created at: {output_path}")

if __name__ == "__main__":
    main()
