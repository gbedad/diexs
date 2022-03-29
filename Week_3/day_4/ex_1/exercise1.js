// Exercise 1

let x = 7;
let y = 7;

if (x > y) {
  console.log(`x(${x}) is biggest number`);
} else if (y > x) {
  console.log(`y(${y}) is the biggest number`);
} else {
  console.log('The 2 numbers should be different!');
}

// Exercise 2 Chihuahua

let newDog = 'Chihuahua';

let lenNewDog = newDog.length;

console.log(`There are ${lenNewDog} letters in ${newDog}`);

console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog === 'Chihuahua') {
  console.log(`I love Chihuahuas, it’s my favorite dog breed`);
} else {
  console.log('I dont care, I prefer cats');
}

// Exercise 3 Even or Odd

let userInput = Number(prompt('Enter a number'));
console.log(typeof userInput);

if (isNaN(userInput)) {
  console.log(`${userInput} is not a number`);
} else if (Number(userInput) === 0) {
  console.log('0 is neither even or odd');
} else if (userInput % 2 === 0) {
  console.log(`${userInput} is an even number`);
} else {
  console.log(`${userInput} is an odd number`);
}

// Exercise 4: Group Chat

let users = [
  'Lea123',
  'Princess45',
  'cat&doglovers',
  'helooo@000',
  'BettyBoop',
];

let numberOnline = users.length;

if (numberOnline === 0) {
  console.log('no one is online');
} else if (numberOnline === 1) {
  console.log(`${users[0]} is online`);
} else if (numberOnline === 2) {
  console.log(`${users[0]} and ${users[1]} are online`);
} else {
  console.log(
    `${users[0]} and ${users[1]} and ${numberOnline - 2} more are online`
  );
}
