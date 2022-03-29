// Exercise 1

let myFavoriteFood = 'scrambled eggs';
let myFavoriteMeal = 'breakfast';

console.log(`I eat ${myFavoriteFood} at every ${myFavoriteMeal}`);

// Exercise 2

let myWatchedSeries = ['black mirror', 'money heist', 'the big bang theory'];

// Variables

let myWatchedSeriesLength = myWatchedSeries.length;
let lastSerie = myWatchedSeries[myWatchedSeriesLength - 1];

let myWatchedSeriesReduced = myWatchedSeries.splice(
  0,
  myWatchedSeriesLength - 1
);
let firstSeries = myWatchedSeriesReduced.join(',');
console.log(firstSeries);

let myWatchedSeriesSentence = `${myWatchedSeries[0]}, ${myWatchedSeries[1]} and ${myWatchedSeries[2]}`;
myWatchedSeriesSentence = `${firstSeries} and ${lastSerie}`;
console.log(myWatchedSeriesSentence);

console.log(
  `I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`
);
console.log(myWatchedSeries);
let posBigBang = myWatchedSeries.indexOf('the big bang theory');
console.log(posBigBang);

myWatchedSeries[posBigBang] = 'friends';

myWatchedSeries.push('happy days');

myWatchedSeries.splice(0, 0, 'the hobbits');

myWatchedSeries.splice(1, 1);

//console.log(myWatchedSeries);
//let pos = myWatchedSeries[1].indexOf('n');
//console.log(pos);

console.log(myWatchedSeries[1].charAt(myWatchedSeries[1].indexOf('n')));

console.log(myWatchedSeries);

// Exercise 3 : The Temperature Converter

let temperatureInCelcius = 23;

let temperatureConvCelciusToFarenheit = (temperatureInCelcius / 5) * 9 + 32;
console.log(
  `${temperatureInCelcius}˚C is ${temperatureConvCelciusToFarenheit} ˚F`
);

// Exercise 4 : Guess the answer
let c;
let a = 34;
let b = 21;

console.log(a + b); //first expression
// Prediction: the sum of 34 + 21 = 55
// Actual: 55

a = 2;

console.log(a + b); //second expression
// Prediction: The new value of a is 2, the sum is 2 + 21 = 23
// Actual: 23
// c is undefined because only declared

// the outcome of console.log(3 + 4 + '5) is 75

console.log(3 + 4 + '5');

// Guess the answer

typeof 15;
// Prediction: 15 is a number
// Actual:

typeof 5.5;
// Prediction: 5.5 is a number
// Actual:

typeof NaN;
// Prediction: NaN is NaN
// Actual:

typeof 'hello';
// Prediction: String
// Actual:

typeof true;
// Prediction: Boolean
// Actual:

typeof (1 != 2);
// Prediction: boolean
// Actual:boolean

'hamburger' + 's';
// Prediction: hamburgers
// Actual:

'hamburgers' - 's';
// Prediction: NaN
// Actual: NaN

'1' + '3';
// Prediction:13
// Actual: 13

'1' - '3';
// Prediction: -2
// Actual: -2

'johnny' + 5;
// Prediction: johnny5
// Actual:Johnny5

'johnny' - 5;
// Prediction: NaN
// Actual: NaN

99 * 'hello';
// Prediction: NaN
// Actual: NaN

1 != 1;
// Prediction: false
// Actual: false

1 == '1';
// Prediction: true
// Actual: true

1 === '1';
// Prediction: false
// Actual: false

// 6 Guess the answer

5 + '34';
// Prediction: 534 concatenate 5 with 34
// Actual: 534

5 - '4';
// Prediction: 1 because it has recognized the type number of the first
// Actual: 1

10 % 5;
// Prediction: the rest of the euclidian division is 0
// Actual: 0

5 % 10;
// Prediction: the rest should be 5
// Actual:

'Java' + 'Script';
// Prediction: Concatenation JavaScript
// Actual:

' ' + ' ';
// Prediction: '    ' concatenate 4 spaces
// Actual:'   '

' ' + 0;
// Prediction: concatenate ' ' +0 = ' 0"
// Actual: ' 0'

true + true;
// Prediction: true is evaluated to 1, answer is 2
// Actual: 2

true + false;
// Prediction: 1 + 0 = 1
// Actual: 1

false + true;
// Prediction: 0 + 1 = 1
// Actual: 1

false - true;
// Prediction: 0 - 1 = -1
// Actual: -1

!true;
// Prediction: not true is false
// Actual:

3 - 4;
// Prediction: -1
// Actual:-

'Bob' - 'bill';
// Prediction:NaN
// Actual: NaN
