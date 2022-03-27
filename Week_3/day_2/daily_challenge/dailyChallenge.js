// Exercise 1

let fruits = ['Banana', 'Apples', 'Oranges', 'Blueberries'];

//1
fruits.shift();

// 2
fruits.sort();

// 3
fruits.push('Kiwi');

// 4
fruits.splice(0, 1);

// 5
fruits.reverse();

//console.log(fruits);

// Exercise 2

let moreFruits = ['Banana', ['Apples', ['Oranges'], 'Blueberries']];

let extracted = moreFruits[1][1][0];

console.log(extracted);
