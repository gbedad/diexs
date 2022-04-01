// Exercise 1 divisible by 3
let numbers = [123, 8409, 100053, 333333333, 7];

for (let div in numbers) {
  if (div % 3 === 0) {
    console.log(true, div % 3);
  } else {
    console.log(false);
  }
}

// Exercise 2 Attendance

let guestList = {
  randy: 'Germany',
  karla: 'France',
  wendy: 'Japan',
  norman: 'England',
  sam: 'Argentina',
};

userInput = prompt('Enter your name');
userInput = userInput.toLowerCase();

if (userInput in guestList) {
  console.log(`Hi! I'm ${userInput}, and I'm from ${guestList[userInput]}.`);
} else {
  console.log("Hi! I'm a guest.");
}

// Exercise 3 : Playing With Numbers

let age = [20, 5, 12, 43, 98, 55];

let sum = 0;

for (let i = 0; i < age.length; i++) {
  sum = sum + age[i];
}
console.log(sum);

let len = age.length;
let max = age[0];
for (let i = 0; i < len; i++) {
  if (age[i] > max) {
    max = age[i];
  }
}
console.log(max);
