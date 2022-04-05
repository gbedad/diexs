const playTheGame = () => {
  let computerNumber;
  let userNumber;
  let userInput = confirm('Do you want to play the guess the number game ?');
  if (userInput === false) {
    alert('No problem, GoodBye');
  } else {
    userNumber = Number(prompt('Enter a number between 0 and 10'));
    while (userNumber > 10 || isNaN(userNumber)) {
      if (userNumber > 10 || userNumber < 0) {
        //   alert('Sorry it is not a good number, GoodBye');
        userNumber = Number(prompt('Enter a number between 0 and 10'));
      } else if (isNaN(userNumber)) {
        //   alert('Sorry, not a number, GoodBye');
        userNumber = Number(prompt('Enter a number between 0 and 10'));
      }
    }
    //  else {
    computerNumber = Math.round(Math.random(0, 1) * 10);
    // }
  }
  return { userNumber, computerNumber };
};

const test = (userNumber, computerNumber) => {
  let count = 1;

  while (count <= 3) {
    console.log(count);
    while (userNumber > 10 || isNaN(userNumber)) {
      if (userNumber > 10 || userNumber < 0) {
        //   alert('Sorry it is not a good number, GoodBye');
        userNumber = Number(prompt('Enter a number between 0 and 10'));
      } else if (isNaN(userNumber)) {
        //   alert('Sorry, not a number, GoodBye');
        userNumber = Number(prompt('Enter a number between 0 and 10'));
      }
    }
    if (userNumber === computerNumber) {
      alert(`WINNER in ${count} guess(es)`);
      break;
    } else if (count === 3) {
      alert('You are out of chances, GoodBye');
      break;
    } else if (userNumber == null) {
      alert('GoodBye');
      return;
    } else if (userNumber > computerNumber) {
      alert("Your number is bigger than computer's, guess again");
      userNumber = Number(prompt('Guess again'));

      console.log(userNumber, computerNumber);
    } else if (userNumber < computerNumber) {
      alert("Your number is lower than computer's, guess again");
      userNumber = Number(prompt('Guess again'));

      console.log(userNumber, computerNumber);
    }
    count++;
  }
};
function play() {
  let playAgain = true;
  while (playAgain === true) {
    let { userNumber, computerNumber } = playTheGame();
    test(userNumber, computerNumber);
    playAgain = confirm('Do you want to play again ?');
    if (playAgain === false) {
      alert('No problem, GoodBye');
      break;
    }
  }
}
