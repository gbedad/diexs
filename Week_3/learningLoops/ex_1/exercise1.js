// Exercise 1

// Part I
let people = ['Greg', 'Mary', 'Devon', 'James'];

// remove "Greg" from the list
for (let i = 0; i < people.length; i++) {
  if (people[i] === 'Greg') {
    let idxGreg = i;
    console.log(idxGreg);
    people.splice(idxGreg, 1);
  }
}
for (let i = 0; i < people.length; i++) {
  if (people[i] === 'James') {
    let idxJames = i;
    console.log(idxJames);
    people[idxJames] = 'Jason';
  }
}
people.push('Gerald');

let newPeople = people.slice(1);

console.log(newPeople);
console.log(people);

for (let i = 0; i < people.length; i++) {
  console.log(
    `The index of Foo is ${people.indexOf(
      'Foo'
    )} because it is not in the array`
  );
}

// Part II

let last = people.slice(people.length - 1);
console.log('last', last);

for (const i in people) {
  console.log(people[i]);
}

for (const i in people) {
  console.log(people[i]);
  if (people[i] === 'Jason') break;
}
//*****End exercise 1 */

// Exercise 2 Your Favorite Colors

let myFavoriteColors = ['purple', 'blue', 'green', 'orange', 'magenta'];

let sentence = '';
for (let i = 0; i < myFavoriteColors.length; i++) {
  sentence = sentence + `My #${i + 1} choice is ${myFavoriteColors[i]},`;
}
console.log(sentence);

// Bonus
// V1
let sentence2 = '';
let pos = '';
for (let i = 0; i < myFavoriteColors.length; i++) {
  switch (i) {
    case 0:
      pos = '1st';
    case 1:
      pos = '2nd';
    case 2:
      pos = '3rd';
    case 3:
      pos = '4th';
    case 4:
      pos = '5th';
  }

  sentence2 = sentence2 + `My ${pos} choice is ${myFavoriteColors[i]},`;
}
console.log(sentence2);

// V2
let sentence3 = '';

let array_pos = ['1st', '2nd', '3rd', '4th', '5th'];
for (let i = 0; i < myFavoriteColors.length; i++) {
  sentence3 =
    sentence3 + `My ${array_pos[i]} choice is ${myFavoriteColors[i]},`;
}
console.log(sentence3);

// Exercise 3

// V1
// let userInput = prompt('Enter a number');
// userInput = Number(userInput);

// do {
//   userInput = prompt('Enter a number');
// } while (userInput < 10);

// V2
let userInput = 0;
while (userInput < 10) {
  userInput = prompt('Enter a number');
  console.log(userInput);
}

// *********** End  exercise 3

// Exercise 4 Building Management
let building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ['Sarah', 'Dan', 'David'],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

console.log('number of floors', building.numberOfFloors);

console.log(
  building.numberOfAptByFloor.firstFloor,
  building.numberOfAptByFloor.thirdFloor
);
console.log(building.nameOfTenants[1]);
console.log(
  building.numberOfRoomsAndRent[building.nameOfTenants[1].toLowerCase()][0]
);

let sumSarah = building.numberOfRoomsAndRent['sarah'][1];
let sumDavid = building.numberOfRoomsAndRent['david'][1];
let sumDan = building.numberOfRoomsAndRent['dan'][1];

if (sumSarah + sumDavid > sumDan) {
  building.numberOfRoomsAndRent['dan'][1] = 1200;
}

console.log(building);
//*********End exercise 4 */

// Exercise 5 : Family

let family = {
  firstname: 'Gerald',
  lastname: 'Berrebi',
  spouse: 'Emmanuelle',
  country: 'France',
  children: [
    { lastname: 'Jonathan', age: 11 },
    { lastname: 'Sephora', age: 9 },
  ],
  hasCar: true,
};

for (const key in family) {
  console.log(key);
}

for (const key in family) {
  console.log(family[key]);
}

// Exercise 6

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer',
};

for (const property in details) {
  console.log(`${property} ${details[property]}`);
}

// Exercise 7 loops secret groups
//____________________________________
function secretGroup(arr) {
  let secret = '';
  arr.sort();
  arr.forEach((element) => {
    let first = element[0];
    secret += first;
  });
  return secret;
}

let names = ['Jack', 'Philip', 'Sarah', 'Amanda', 'Bernard', 'Kyle'];

let answer = secretGroup(names);
console.log(answer);
