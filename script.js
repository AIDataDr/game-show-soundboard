const audio = {
  correct: document.getElementById('correct'),
  finished: document.getElementById('finished'),
  wrong: document.getElementById('wrong')
};

const buttons = [...document.querySelectorAll('.sound-button')];
const stopButton = document.getElementById('stopButton');
const volume = document.getElementById('volume');
const volumeValue = document.getElementById('volumeValue');
const status = document.getElementById('status');

function stopAll() {
  Object.values(audio).forEach(sound => {
    sound.pause();
    sound.currentTime = 0;
  });
  buttons.forEach(button => button.classList.remove('playing'));
  status.textContent = 'Stopped';
}

function playSound(name) {
  stopAll();
  const sound = audio[name];
  const button = document.querySelector(`[data-sound="${name}"]`);
  sound.volume = Number(volume.value);
  sound.currentTime = 0;
  sound.play().then(() => {
    button.classList.add('playing');
    status.textContent = `Playing: ${button.querySelector('span:nth-child(2)').textContent}`;
  }).catch(() => {
    status.textContent = 'Your browser blocked playback. Click a sound button to try again.';
  });
}

buttons.forEach(button => {
  button.addEventListener('click', () => playSound(button.dataset.sound));
});

Object.entries(audio).forEach(([name, sound]) => {
  sound.addEventListener('ended', () => {
    document.querySelector(`[data-sound="${name}"]`).classList.remove('playing');
    status.textContent = 'Ready';
  });
});

stopButton.addEventListener('click', stopAll);

volume.addEventListener('input', () => {
  const level = Number(volume.value);
  Object.values(audio).forEach(sound => sound.volume = level);
  volumeValue.value = `${Math.round(level * 100)}%`;
});

document.addEventListener('keydown', event => {
  if (event.target.matches('input, button')) return;
  if (event.code === 'Digit1') playSound('correct');
  if (event.code === 'Digit2') playSound('finished');
  if (event.code === 'Digit3') playSound('wrong');
  if (event.code === 'Space') {
    event.preventDefault();
    stopAll();
  }
});
