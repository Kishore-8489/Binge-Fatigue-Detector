import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath="data/fatigue_results.csv"):
    return pd.read_csv(filepath)

def preprocess_data(df):
    features = df[["total_duration", "content_count", "late_night_views", "fatigue_score"]]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features

def perform_clustering(scaled_data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(scaled_data)
    return labels

def visualize_clusters(df, labels):
    df["cluster"] = labels
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="total_duration", y="fatigue_score", hue="cluster", palette="Set2")
    plt.title("User Clusters Based on Fatigue Patterns")
    plt.savefig("data/cluster_plot.png")
    plt.close()
    print("✅ Cluster plot saved as data/cluster_plot.png")
    return df

def save_clustered_data(df, path="data/clustered_users.csv"):
    df.to_csv(path, index=False)
    print(f"✅ Clustered user data saved at: {path}")

if __name__ == "__main__":
    df = load_data()
    scaled = preprocess_data(df)
    labels = perform_clustering(scaled)
    clustered_df = visualize_clusters(df, labels)
    save_clustered_data(clustered_df)
