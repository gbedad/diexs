/** Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
At this point continuously prompt player 2 for a letter.
If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
If player 1 wins, display a message that says CONGRATS YOU WIN.*/

let stars = [];

const show = (word) => {
  let len = word.length;
  let wordHidden = '*'.repeat(len);
  start = wordHidden.split('');
  let first = '*'.repeat(len);
  console.log('*'.repeat(len));
  return first;
};

const checkLetter = (word, letter) => {
  let arr = word.split('');
  // console.log(arr);
  for (let char in arr) {
    // console.log(arr[char]);
    if (letter === arr[char]) {
      let idx = char;
      start.splice(idx, 1, letter);
    }
  }
  let wordReplaced = start.join('');
  console.log(wordReplaced);
  return wordReplaced;
  //   arr.forEach((element) => {
  //     console.log(element);
  //     if (element === letter) {
  //       console.log(arr.indexOf(element));
  //       let idx = arr.indexOf(element);
  //       //   start.slice(0,idx, 1, letter);
  //     }
  //     console.log(start);
  //   });
};
// while (player1Input !== player2Input) {

let checkIfLetter = (letter) => {
  if (letter.length > 1 || !isNaN(letter)) {
    alert('Should be a letter and only one');
  }
  return false;
};

let playHangman = () => {
  let player1Input = prompt('Enter a word with at least 8 characters');
  show(player1Input);
  let myGuess;
  let count = 0;
  let letters = [];
  while (myGuess !== player1Input && count <= 10) {
    let player2Input = prompt('Enter a letter');

    count += 1;
    if (!letters.includes(player2Input)) {
      letters.push(player2Input);
    } else {
      alert('letter already proposed');
    }
    console.log(count, letters);
    myGuess = checkLetter(player1Input, player2Input);
    if (player1Input === myGuess) {
      let message = `You have guessed the word "${player1Input}" in ${count} guesses`;
      return message;
    }
  }
  let message = `You lose, the correct word was : ${player1Input}`;
  return message;
};
