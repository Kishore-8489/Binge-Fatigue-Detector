import pandas as pd # type: ignore
from datetime import datetime

def calculate_fatigue_score(df):
    fatigue_score = 0
    for _, row in df.iterrows():
        start = pd.to_datetime(row['start_time'])
        end = pd.to_datetime(row['end_time'])
        watch_duration = (end - start).total_seconds() / 3600  # hours
        if start.hour >= 22 or end.hour <= 6:
            fatigue_score += watch_duration
    return round(fatigue_score, 2)
