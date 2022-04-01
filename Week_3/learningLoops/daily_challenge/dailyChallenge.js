//? Part one tree

//* version 1
for (let i = 1; i <= 6; i++) {
  console.log(' *'.repeat(i));
}

//* version 2
let star = ' ';
for (let i = 0; i < 5; i++) {
  for (let j = 1; j < i; j++) {
    star = star + ' *';
    console.log(star);
  }
}

//? Part 2

//* Exercise gold
const numbers = [5, 0, 23, 567, 7, 90, 2, 91, 700, 8];

let new_array = numbers.toString();

console.log(new_array);
new_array = numbers.join('/');

console.log(new_array);

//* Bubble sort

let lower;
let lengthNumbers = numbers.length;
let tempArray = [];

for (let i = 0; i < lengthNumbers; i++) {
  higher = numbers[i];
  for (let j = i; j < lengthNumbers; j++) {
    if (numbers[j] > higher) {
      higher = numbers[j];
      numbers[j] = numbers[i];
      numbers[i] = higher;
    }
    // console.log(higher);
  }
  console.log('higher', higher);
  console.log('Array to check', numbers);
}

console.log(numbers);

// for (let i = 0; i < numbersLenth; i++) {
//   for (let j = 1; j < numbersLenth; j++) {
//     if (numbers[i] < numbers[j]) {
//       lower = numbers[i];
//       numbers[j + 1] = lower;
//     }
//     console.log(numbers[j + 1]);
//   }

//     numbers[numbersLenth - 1] = lower;
//     console.log('posNum', numbers[numbersLenth - 1]);
// }
// console.log(numbers);
// todo : check the code again
