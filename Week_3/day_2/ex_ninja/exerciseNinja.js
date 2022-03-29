// 5 >= 1 is true

// 0 === 1 is false

//4 < = 1  is false

//1 != 1 false

// 'A' > 'B'  false

// "B" < "C" true

// "a" > "A" true

// "b" < "A" false

// true === false false

// true != true false

// Exercise 2

let userInput = prompt('Enter 2 numbers separated by a comma');
let idx = userInput.indexOf(',');
let num1 = userInput.substring(0, idx);
let num2 = userInput.substring(idx + 1);

// let setee = userInput.split(/[ ,]+/);
// let myvar = userInput.replace(/,/g, '+');
// console.log(Number(myvar));
// console.log(myvar * 1);

num1 = Number(num1);
num2 = Number(num2);

let sum = num1 + num2;

console.log(sum);

// Exercise 3 Find Nemo

let mySentence = 'I love the movie named Nemo';

let newS = mySentence.split(' ');
console.log(newS);

let pos = newS.indexOf('Nemo');

console.log(pos);
console.log(`I found the word ${newS[5]} at position ${pos}`);

// Exercise 4 BOOM

let user = prompt('enter a number');
user = Number(user);

// if (user < 2) {
//   alert('boom');
// } else if (user > 2 && user % 2 !== 0 && user % 5 !== 0) {
//   alert('B' + 'o'.repeat(user) + 'm');
// } else if (user > 2 && user % 2 === 0 && user % 5 !== 0) {
//   alert('B' + 'o'.repeat(user) + 'm!');
// } else if (user > 2 && user % 2 !== 0 && user % 5 === 0) {
//   alert(('B' + 'o'.repeat(user) + 'm').toUpperCase());
// } else if (user > 2 && user % 2 === 0 && user % 5 === 0) {
//   alert(('B' + 'o'.repeat(user) + 'm!').toUpperCase());
// }
// confirm('do you want to play again ?');

if (user < 2) {
  alert('boom');
} else {
  let nuser = 'B' + 'o'.repeat(user) + 'm';
  if (user % 2 === 0 && user % 5 !== 0) {
    alert(`${nuser}!`);
  } else if (user % 2 !== 0 && user % 5 === 0) {
    alert(`${nuser}`.toUpperCase());
  } else if (user % 2 === 0 && user % 5 === 0) {
    alert(`${nuser}!`.toUpperCase());
  }
}
