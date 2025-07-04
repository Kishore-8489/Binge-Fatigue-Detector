import pandas as pd # type: ignore
from src.fatigue_detector import calculate_fatigue_score
from src.recommender import recommend_watch_time

log_path = 'data/sample_viewing_logs.csv'
df = pd.read_csv(log_path)

score = calculate_fatigue_score(df)
recommendation = recommend_watch_time()

print(f"Fatigue Score: {score}")
print(f"Recommendation: {recommendation}")
