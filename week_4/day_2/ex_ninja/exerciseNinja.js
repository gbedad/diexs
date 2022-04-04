//? Exercise 1: Random Number

function evenNumbers() {
  let getRandom = Math.round(Math.random(0, 1) * 100);
  console.log('Random', getRandom);
  for (let i = 2; i <= getRandom; i++) {
    if (i % 2 === 0) {
      console.log(i);
    }
  }
}

console.log(evenNumbers());

//? Exercise 2: Capitalized Letters
/**Create a function that takes a string as an argument.
Have the function return:
The string but all letters in even indexes should be capitalized.
The string but all letters in odd indexes should be capitalized.
Note:

Index 0 will be considered even.
The argument of the function should be a lowercase string with no spaces. */

function capitalize(word) {
  let odd = '';
  let even = '';

  for (letter in word) {
    let charEven;
    let charOdd;
    if (letter % 2 === 0) {
      charEven = word[letter].toUpperCase();
      charOdd = word[letter];
    } else {
      charEven = word[letter];
      charOdd = word[letter].toUpperCase();
    }
    even = even + charEven;
    odd = odd + charOdd;
  }
  console.log(even, odd);
  return [even, odd];
}

capitalize('abcdef');

//? Exercise 3 : Is Palindrome?

function isPalindrome(word) {
  let wordInverted = '';
  for (let i = word.length - 1; i >= 0; i--) {
    wordInverted += word[i];
  }
  if (wordInverted === word) {
    return `${word} is a palindrome`;
  } else {
    return `${word} is not a palindrome`;
  }
}

console.log(isPalindrome('kayak'));

//? Exercise 4 : Biggest Number

/**Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
Note : This function should work with any array;
 */

function biggestNumberInArray(arrayNumber) {
  if (arrayNumber.length === 0) {
    return 0;
  } else {
    for (let item in arrayNumber) {
      if (isNaN(arrayNumber[item])) {
        arrayNumber.splice(item, 1);
      }
    }
    console.log(arrayNumber);
    let max = arrayNumber[0];
    for (let i = 0; i < arrayNumber.length; i++) {
      if (arrayNumber[i] > max) {
        max = arrayNumber[i];
      }
    }
    return max;
  }
}

const array = [-1, 0, 3, 100, 99, 2, 99]; // should return 100
const array2 = ['a', 3, 4, 2]; // should return 4
const array3 = []; // should return 0
console.log(biggestNumberInArray(array));
console.log(biggestNumberInArray(array2));
console.log(biggestNumberInArray(array3));

//? Exercise 5: Unique Elements

function isUnique(array) {
  let newArray = array.slice(0);
  console.log(newArray);

  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] === array[j]) {
        // console.log(array[j]);
        array = array.slice(0, i + 1).concat(array.slice(j + 1));
        // console.log(array);
      }
    }
  }
  return array;
}

const list1 = [1, 2, 3, 3, 3, 3, 4, 5];
const list2 = [1, 2, 1, 2, 3, 3, 4, 5];

console.log(isUnique(list1));
console.log(isUnique(list2));
