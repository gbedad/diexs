let userInput = prompt('Which language do you want to speak ?');

userInput = userInput.toLowerCase();

switch (userInput) {
  case 'french':
    console.log('Bonjour');
    break;
  case 'english':
    console.log('Hello');
    break;
  case 'hebrew':
    console.log('Shalom');
    break;
  default:
    console.log('01110011 01101111 01110010 01110010 01111001');
}

// Exercise 2 : The Grade Assigner

let userGrade = prompt('Please enter your grade');

userGrade = Number(userGrade);

if (userGrade > 90) {
  console.log('A');
} else if (userGrade > 80 && userGrade <= 90) {
  console.log('B');
} else if (userGrade > 70 && userGrade <= 80) {
  console.log('C');
} else if (userGrade <= 70) {
  console.log('D');
} else {
  console.log('Your input is not valid');
}

// Exercise 3 : Verbing

let userVerb = prompt('Enter a verb');

let verbLength = userVerb.length;

if (
  verbLength >= 3 &&
  userVerb.substring(verbLength - 3, verbLength) !== 'ing'
) {
  console.log(`${userVerb}ing`);
} else if (
  verbLength >= 3 &&
  userVerb.substring(verbLength - 3, verbLength) === 'ing'
) {
  console.log(`${userVerb}ly`);
} else {
  console.log(userVerb);
}
