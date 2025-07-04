# 🎬 Binge Fatigue Detector 🧠

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/status-actively--developing-success)

> A smart, lightweight system that uses ML + content analysis to detect signs of **binge fatigue** in users — and visualize their fatigue score via a beautiful **Streamlit dashboard**.

---

## 🧠 Demo

![Demo GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDZna3c2N3B5eGJvMXVvZzJubTV1aXpoeWZycWd2aGFwcGV1NWNqZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZVik7pBtu9dNS/giphy.gif)

> _“Watch responsibly!”_ – Your Friendly ML Assistant

---

## 🚀 Features

- 🧮 **ML-based fatigue detection** from watch history
- 🧠 **NLP analysis** of content to identify binge triggers
- 📊 **User clustering** using KMeans
- 📈 **Interactive Streamlit dashboard**
- ☁️ Designed to deploy on Streamlit Cloud or Docker

---

## 🗂️ Project Structure

```
binge-fatigue-detector/
├── src/
│   └── app.py                  # Main Streamlit app
│   └── cluster_users.py        
│   └── data_processing.py
│   └── fatigue_logic.py 
│   └── generate_data.py 
│   └── run_analysis.py 
├── data/                       # Fatigue and cluster CSVs
├── notebooks/
│   └── fatigue_ml_exploration.ipynb
│   └── nlp_content_analysis.ipynb
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## 📊 Fatigue Score Explained

The model generates a **fatigue score (0.0 to 1.0)** based on:
- 🚨 Number of back-to-back watches
- ⏰ Late-night watch sessions
- 🧠 Type and intensity of content

> Scores closer to **1.0** indicate possible **binge fatigue** symptoms.

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/binge-fatigue-detector.git
cd binge-fatigue-detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run src/app.py
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas, Scikit-learn, Seaborn
- NLTK, WordCloud
- Docker (optional)
- GitHub Actions (optional)

---

## 💼 Ideal For

- 📌 Netflix job projects
- 📚 Resume project highlights
- 🎓 Final year ML/DS portfolios
- 🧑‍💻 Hackathons / quick demos

---

## 📌 To-Do

- [x] Build fatigue score logic
- [x] Streamlit UI with filters
- [x] KMeans user clustering
- [x] NLP + WordClouds
- [ ] Dockerize app
- [ ] Streamlit Cloud deployment

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.


---

## 📬 Contact

Made with 💻 by [Kishore S.](https://github.com/yourusername)

Let’s build something binge-worthy — responsibly!
