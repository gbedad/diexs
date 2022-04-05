// Prompt the number of  bottles

const userInput = Number(prompt('Enter a number of bottles'));

const substractBottles = (number) => {
  let bottles = number;
  for (let i = number; i > 0; i--) {
    let take = number - i + 1;
    let remain = bottles - take;
    if (take === 1) {
      console.log(`${bottles} bottles of beer on the wall
    ${bottles} bottle of beer
    Take ${take} down, pass it around
    ${remain} bottles of beer on the wall`);
    } else if (take >= bottles) {
      console.log(`${bottles} bottles of beer on the wall
        ${bottles} bottles of beer
        Take them down, pass them around
        No bottle of beer on the wall`);
      break;
    } else {
      console.log(`${bottles} bottles of beer on the wall
        ${bottles} bottles of beer
        Take ${take} down, pass them around
        ${remain} bottles of beer on the wall`);
    }
    bottles = remain;
  }
};
let test = substractBottles(userInput);
console.log(test);
