<<<<<<< HEAD
(your local content)
=======
(remote content)
>>>>>>> (commit hash)
# Mood-Based-Song-Recommender-Python-Only-Backend
A Python-only CLI app that suggests songs based on your mood. It pulls songs from a local JSON file and opens matching YouTube links in your browser. Optional voice feedback with pyttsx3 adds interactivity. Fully offline except for opening links—just fun, clean Python logic.
=======
# 🎧 Mood-Based Song Recommender

![Mood Music Banner](https://images.unsplash.com/photo-1511376777868-611b54f68947?auto=format&fit=crop&w=1350&q=80)

## 💡 About the Project

**Mood-Based Song Recommender** is a fun Python project that takes how you're feeling and matches it with songs tailored to your mood. Whether you're feeling 💃 happy, 😞 sad, 🧘 calm, or 🔥 pumped — this program suggests songs that *vibe* with you.

> All song data is stored locally in a `songs.json` file. No internet or APIs needed.

---

## 🔥 Features

✨ Takes user mood as input  
🎶 Recommends songs based on emotional tone  
🗣️ Optional voice output with `pyttsx3`  
📁 Simple JSON file for easy customization  
📊 CLI-based and beginner-friendly

---

## 🖼️ Demo Animation

![Demo GIF](https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif)

---

## 🛠️ Built With

- Python 3
- `pyttsx3` – Text-to-Speech (optional)
- `json` – For song storage
- `random` – To shuffle results

---

## 📁 Project Structure

mood-changer/
│
├── data/
│   └── songs.json
├── src/
│   └── mood_recommender.py
└── README.md

---

## 🧪 Example `songs.json`

```json
{
  "happy": ["Happy - Pharrell Williams", "Best Day of My Life - American Authors"],
  "sad": ["Fix You - Coldplay", "Someone Like You - Adele"],
  "calm": ["Weightless - Marconi Union", "River Flows in You - Yiruma"]
}
```

---

## 🖥️ How to Run

```bash
git clone https://github.com/yourusername/mood-song-recommender.git
cd mood-song-recommender
pip install pyttsx3
python src/mood_recommender.py
```

### 🎤 Optional: Enable Voice Output
To have the songs read aloud, make sure pyttsx3 is installed:

```bash
pip install pyttsx3
```

---

## 🧠 How It Works

1. You type in your current mood.
2. The program fetches a matching song list.
3. It shows 3–5 random suggestions.
4. Optionally, the titles are read aloud.

---

## 🚀 Future Ideas
- Add YouTube/Spotify links
- Add GUI with Tkinter or Streamlit
- Save favorite songs locally

---

## 🤝 Contributing
Pull requests are welcome! Feel free to suggest improvements or new moods.

---

## 📸 Screenshots
| Mood Input | Recommendations |
|------------|-----------------|
| happy      | 🎵 Happy, 🎵 Can't Stop the Feeling |
| sad        | 🎵 Someone Like You, 🎵 Fix You      |

---

## 📜 License
This project is open source and available under the MIT License. ❤️ Made with love and Python by [uncannystranger]
>>>>>>> 3bea245 (Initial commit: Mood-Based Song Recommender)
