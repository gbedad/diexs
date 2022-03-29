let sentence = 'This dinner is bad !';

let wordNot = sentence.indexOf('not');

let wordBad = sentence.indexOf('bad');

console.log(wordNot);
console.log(wordBad);

// console.log(extract);
// let newSentence = sentence.replace(extract, 'good');
// console.log(newSentence);

if (wordBad > wordNot && wordNot !== -1) {
  let extract = sentence.substring(wordNot, wordBad + 3);
  let newSentence = sentence.replace(extract, 'good');
  console.log(newSentence);
} else if (wordNot === -1 || wordNot > wordBad) {
  console.log(sentence);
}
