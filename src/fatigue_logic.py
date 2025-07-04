import pandas as pd
import os

def load_data(filepath="data/synthetic_watch_data.csv"):
    return pd.read_csv(filepath)

def analyze_fatigue(df):
    fatigue_scores = []

    grouped = df.groupby(["user_id", "session_id"])

    for (user, session), group in grouped:
        total_duration = group["duration_minutes"].sum()
        avg_duration = group["duration_minutes"].mean()
        content_count = group.shape[0]

        # Detect late night watching
        timestamps = pd.to_datetime(group["timestamp"])
        late_night_watches = timestamps.apply(lambda t: t.hour >= 23 or t.hour <= 4).sum()

        # Simple rule-based fatigue score
        score = 0
        if total_duration > 180: score += 2
        if content_count >= 5: score += 1
        if late_night_watches > 0: score += 1

        fatigue_scores.append({
            "user_id": user,
            "session_id": session,
            "total_duration": total_duration,
            "content_count": content_count,
            "late_night_views": late_night_watches,
            "fatigue_score": score
        })

    return pd.DataFrame(fatigue_scores)

def save_results(fatigue_df, output_path="data/fatigue_results.csv"):
    fatigue_df.to_csv(output_path, index=False)
    print(f"✅ Fatigue scores saved at: {output_path}")

if __name__ == "__main__":
    df = load_data()
    fatigue_df = analyze_fatigue(df)
    save_results(fatigue_df)


