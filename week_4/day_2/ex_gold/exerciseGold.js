//? Exercise 1 Is_Blank

function isBlank(word) {
  if (word === '') {
    return true;
  } else if (word.length > 0 && isNaN(word)) {
    return false;
  } else {
    return 'This is not a string';
  }
}

console.log(isBlank(''));
console.log(isBlank('abc'));

//? Exercise 2 Abbrev_name

function abbrevName(name) {
  name = name.split(' ');
  console.log(name);
  if (name.length > 1) {
    return `${name[0]} ${name[1][0]}.`;
  } else {
    return name[0];
  }
}

console.log(abbrevName('Robin Singh'));

//? Exercise 3 : SwapCase

function swapCase(sentence) {
  //   let sentenceToArray = sentence.split(' ');
  let newSentence = '';
  for (let char of sentence) {
    if (char === char.toUpperCase()) {
      char = char.toLowerCase();
      newSentence += char;
    } else if (char === char.toLowerCase()) {
      char = char.toUpperCase();
      newSentence += char;
    }
  }
  return newSentence;
}

console.log(swapCase('The Quick Brown Fox'));

//? Exercise 4 : Omnipresent Value

/**Create a function that determines whether an argument is omnipresent for a given array.
A value is omnipresent if it exists in every subarray inside the main array.
To illustrate:

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.

*/

function isOmniPresent(array, num) {
  let len = array.length;
  let trueArray = [];
  for (let i = 0; i < len; i++) {
    // console.log(array[i]);
    if (array[i].indexOf(num) !== -1) {
      trueArray.push(array[i]);
    }
  }
  if (trueArray.length === len) {
    return true;
  } else {
    return false;
  }
}

console.log(
  isOmniPresent(
    [
      [1, 1],
      [1, 3],
      [5, 1],
      [6, 1],
    ],
    1
  )
);
console.log(
  isOmniPresent(
    [
      [1, 1],
      [1, 3],
      [5, 1],
      [6, 1],
    ],
    6
  )
);
