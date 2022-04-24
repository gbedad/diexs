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
// const div = document.createElement('div');
// let createCell = (i, j) => {
//   let idCell = document.createElement('td');
//   idCell.textContent = checkStar(k);
//   idCell.classList.add('tdCell');
//   // tr.append(idCell);
//   return idCell;
// };
// console.log(createCell(2));

// let cells = [...document.querySelectorAll('.grid-item')];

const writingLetter = (arrayOfLetter) => {
  for (let i = 0; i < arrayOfLetter.length; i++) {
    // let line = '';

    for (let j = 0; j < arrayOfLetter[i].length; j++) {
      // let div = document.createElement('div');
      let cell = document.createElement('div');
      matrix.appendChild(cell);
      cell.classList.add('grid-item');
      cell.textContent = checkStar(arrayOfLetter[i][j]);
      console.log(i, j);
      // let cell = document.createTextNode(createCell(arrayOfLetter[i][j]))

      // cells.classList.add('grid-item');
      // cells.textContent = createCell(arrayOfLetter[i][j]);
      // line = line + checkStar(arrayOfLetter[i][j]);
      // cells[j].createTextNode(checkStar(arrayOfLetter[i][j]));
      // let td = createCell(arrayOfLetter[i][j]);
      // tr.append(td);
    }

    // table.append(tr);
    // console.log(line);
  }
};

writingLetter(composeA);
// writingLetter(composeB);
// writingLetter(composeS);
