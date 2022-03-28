// Exercise 1

let sentence = ['my', 'favorite', 'color', 'is', 'blue'];

let mySentence = sentence.join(' ');

console.log(mySentence);

// Exercise 2

let str1 = 'mix';
let str2 = 'pod';

let extrac1 = str1.substring(0, 2);
let extrac2 = str2.substring(0, 2);

let newStr1 = str2.substring(0, 2) + str1.substring(2);

let newStr2 = str1.substring(0, 2) + str2.substring(2);
let newWord = `${newStr1} ${newStr2}`;

console.log(newWord);

// Exercise 3

let num1 = prompt('Enter your first number');
let num2 = prompt('Enter the second number');
num1 = Number(num1);
num2 = Number(num2);
let sum = num1 + num2;
let substract = num1 - num2;
let multiply = num1 * num2;
let divide = num1 / num2;
alert(
  `the sum of ${num1} and ${num2} is ${sum}, ${num1} minus ${num2} is equal to ${substract}, ${num1} multiplied by ${num2} is ${multiply} and ${num1} divided by ${num2} is ${divide}`
);
