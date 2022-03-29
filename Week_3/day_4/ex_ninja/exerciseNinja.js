// Exercise 1

const person1Year = prompt('Enter the year of birth person 1');

const person2Year = prompt('Enter the year of birth person 2');

let today = new Date().getFullYear();

let person1Age = today - Number(person1Year);
let person2Age = today - Number(person2Year);
// console.log(person1Age, person2Age);

let younger = 0;
let older = 0;
let youngerYear = 0;
let date = 0;

if (person1Age > person2Age) {
  younger = person2Age;
  older = person1Age;
  youngerYear = Number(person2Year);
  olderYear = Number(person1Year);
} else {
  younger = person1Age;
  older = person2Age;
  youngerYear = Number(person1Year);
  olderYear = Number(person2Year);
}
let ageToTwice = 2 * (older / 2 - younger);
// let ageGapToReach = younger + ageToTwice;
// date = youngerYear + ageGapToReach;
// console.log(younger + ageToTwice);
console.log(youngerYear + younger + ageToTwice);
date = youngerYear + younger + ageToTwice;
console.log(date);

console.log(
  ` The date when the younger one is exactly half the age of the older is ${date} `
);

// console.log(2 * (person1Age / 2 - person2Age));
// console.log(today - 2 * (older / 2 - younger));

// annee1 = y + age2/2   age2 = annee2 - y
// annee2 = y + age2   annee1 = y + (annee2 -y)/2 => y/2 = annee1 - annee2/2 => y = 2*annee1 - annee2

// Exercise 2

// Version with regex
//_____________________________
/* A variable that is assigned to a value. */
let zipcode = prompt('Enter your zipcode');

const regex = /^([0-9]{5})$/gm;

let checkCode = regex.test(zipcode);
console.log(checkCode);
if (checkCode === true) {
  console.log('Success');
} else {
  console.log('zipcode incorrect');
}

// Version without regex

if (
  zipcode[0] != NaN &&
  zipcode[1] != NaN &&
  zipcode[2] != NaN &&
  zipcode[3] != NaN &&
  zipcode[4] != NaN
) {
  console.log('Success2');
} else {
  console.log('Error 2');
}
console.log(zipcode[0] != NaN);

//********* */
// Exercise 3 : Secret Word

let userWord = prompt('Enter your secret word');

const noVowels = userWord.replace(/[aeiouy]/g, '');

console.log(noVowels);

let replaced = userWord
  .replace(/[a]/g, '1')
  .replace(/[e]/g, '2')
  .replace(/[i]/g, '3')
  .replace(/[o]/g, '4')
  .replace(/[u]/g, '5');
// replaced = userWord.replace(/[e]/g, '2');
//

console.log(replaced);
//******************** */

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer',
};

for (const property in details) {
  console.log(`${property} ${details[property]}`);
}
