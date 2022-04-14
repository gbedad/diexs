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
const writingLetter = (arrayOfLetter) => {
  for (let i = 0; i < arrayOfLetter.length; i++) {
    let line = '';
    for (let j = 0; j < arrayOfLetter[i].length; j++) {
      line = line + checkStar(arrayOfLetter[i][j]);
    }
    console.log(line);
  }
};

writingLetter(composeA);
writingLetter(composeB);
writingLetter(composeS);
