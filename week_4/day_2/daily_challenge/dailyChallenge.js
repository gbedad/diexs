//? Words in the stars

let userInput = prompt('Enter several words separated by commas');

userInput = userInput.split(',');

//*find the higher length
function higherLength(arr) {
  let m = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > m) {
      m = arr[i];
    }
  }
  return m;
}
let userInputL = userInput.length;

console.log(userInput);
let len = [];
for (let i = 0; i < userInputL; i++) {
  len[i] = userInput[i].length;
  len.push(userInput[i].length);
  console.log(len[i]);
}
let higherL = higherLength(len);
// console.log(higherLength(len));
console.log(`${'*'.repeat(higherL + 4)}`);
for (let i = 0; i < userInputL; i++) {
  console.log(
    `* ${userInput[i]}${' '.repeat(higherL - userInput[i].length)} *`
  );
}
console.log(`${'*'.repeat(higherL + 4)}`);
