# 🎉 Game Show Soundboard

A lightweight browser-based soundboard for quizzes, games, classrooms, presentations, family game nights, or anywhere you need instant **Correct!**, **Finished!**, and **Wrong!** sound effects.

The project uses only **HTML, CSS, and vanilla JavaScript**. There are no frameworks, packages, build tools, or server-side dependencies.

## 🔊 Sounds

| Button | Sound | Keyboard |
| --- | --- | --- |
| ✅ **Correct!** | Short winner/correct bell | `1` |
| ❌ **Wrong!** | Wrong-answer buzzer | `2` |
| ⭐ **Finished!** | Longer victory fanfare | `3` |
| ⏹ **Stop** | Stops and resets the current sound | `Space` |

The soundboard also includes a volume slider and an animated visual response while a sound is playing.

## 🚀 Run It Locally

No installation is required. Clone or download the repository and open `index.html` in a modern web browser.

```bash
git clone https://github.com/YOUR-USERNAME/game-show-soundboard.git
cd game-show-soundboard
```

Then open `index.html`.

> Tip: Browser audio works best after the page has received a user interaction, such as clicking one of the sound buttons.

## 🌐 Publish with GitHub Pages

1. Push this project to a GitHub repository.
2. Open the repository's **Settings**.
3. Select **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select your main branch and the `/ (root)` folder.
6. Save the settings.

GitHub will provide a public URL for the soundboard after deployment.

Once published, you can replace this line with your live link:

**[▶ Launch the Game Show Soundboard](https://AIDataDr.github.io/game-show-soundboard/)**

## 📁 Project Structure

```text
game-show-soundboard/
├── index.html
├── style.css
├── script.js
├── README.md
└── sounds/
    ├── correct_winner.wav
    ├── finished.wav
    └── wrong_answer_buzzer.wav
```

## ✨ Features

- Three large, color-coded sound buttons
- One-click sound playback
- Stop/reset button
- Volume control
- Playing animation
- Keyboard shortcuts (`1`, `2`, `3`, and `Space`)
- Responsive layout for desktop, tablet, and phone
- Reduced-motion accessibility support
- No external libraries or dependencies
- Ready for GitHub Pages

## 🛠 Customize It

The audio files are stored in the `sounds` folder. To replace a sound, either keep the existing filename or update the matching `<audio>` element in `index.html`.

Button appearance and animations are controlled by `style.css`. Playback behavior and keyboard shortcuts are controlled by `script.js`.

