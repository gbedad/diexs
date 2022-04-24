const composeA = [
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
];
const composeB = [
  [0, 1, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 0, 0],
];
const composeS = [
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 0, 1, 1, 1, 0, 0],
];

let checkStar = (value) => {
  switch (value) {
    case 0:
      return ' ';
    case 1:
      return '*';
  }
};

const matrix = document.querySelector('.grid-container');

const writingLetter = (arrayOfLetter) => {
  for (let i = 0; i < arrayOfLetter.length; i++) {
    // let line = '';

    for (let j = 0; j < arrayOfLetter[i].length; j++) {
      // let div = document.createElement('div');
      let cell = document.createElement('div');
      matrix.appendChild(cell);
      cell.classList.add('grid-item');
      cell.textContent = checkStar(arrayOfLetter[i][j]);
    }
  }
};

// writingLetter(composeA);
writingLetter(composeB);
// writingLetter(composeS);
