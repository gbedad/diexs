//?Exercise 1 : Information
//todo : Create a function called infoAboutMe() that takes no parameter.
//todo :The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
//todo : Call the function.

//* part 1 : function with no parameters

function infoAboutMe() {
  console.log(
    'My name is Jonathan, I am 30 years old and I like playing violin.'
  );
  alert('My name is Jonathan, I am 30 years old and I like playing piano.');
}
//Call the function
infoAboutMe();

//* part 2 : function with parameters
/* Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
Call the function twice with the following arguments:
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")*/

function infoAboutPerson(personName, personAge, personFavoriteColor) {
  let message = `Your name is ${personName}, you are ${personAge} old and your favorite color is ${personFavoriteColor}.`;
  console.log(message);
  alert(message);
}
//Call the function
infoAboutPerson('David', 45, 'blue');
infoAboutPerson('Josh', 12, 'yellow');

//? Exercise 2 : Tips

/*John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

Create a function named calculateTip() that takes no parameter.

Inside the function, ask John for the amount of the bill.

Here are the rules
If the bill is less than $50, tip 20%.
If the bill is between $50 and $200, tip 15%.
If the bill is more than $200, tip 10%.

Console.log the tip amount and the final bill (bill + tip).

Call the calculateTip() function.*/

function calculateTip() {
  let bill = null;
  let tip;
  let tipPercent;
  let totalBill;
  //   bill = Number(prompt('Enter the amount of the bill.'));
  while (isNaN(bill) || bill === 0 || bill === null) {
    if (isNaN(bill) || bill === 0 || bill === null) {
      bill = Number(prompt('John, the amount be an integer > 0'));
    }
  }
  //   amount = Number(prompt('Enter the amount of the bill.'));
  //console.log(bill);
  if (bill < 50) {
    tipPercent = 0.2;
  } else if (bill >= 50 && bill < 200) {
    tipPercent = 0.15;
  } else if (bill >= 200) {
    tipPercent = 0.1;
  }
  tip = bill * tipPercent;
  totalBill = (bill + tip).toFixed(2);
  console.log(`Bill : $${bill} \nTip : $${tip} \nTotal Bill : $${totalBill}`);
}
calculateTip();

//? Exercise 3 : Find The Numbers Divisible By 23
/* Create a function call isDivisible() that takes no parameter.
In the function, loop through numbers 0 to 500.
Console.log all the numbers divisible by 23.
At the end, console.log the sum of all numbers that are divisible by 23.*/

function isDivisible() {
  let sum = 0;
  let array23 = [];
  for (let i = 0; i < 500; i++) {
    if (i % 23 === 0) {
      console.log(i);
      array23.push(i);
      sum = sum + i;
    }
  }
  //   console.log('divisible by 23', i);
  console.log('array23', array23);
  console.log('Sum', sum);
}
isDivisible();

/**isDivisible(divisor)
Example:
isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
isDivisible(45) : Console.log all the numbers divisible by 45, and their sum */

function isDivisible(divisor) {
  let sum = 0;
  let arrayDivisor = [];
  for (let i = 0; i < 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      arrayDivisor.push(i);
      sum = sum + i;
    }
  }
  console.log('array divisor', arrayDivisor);
  console.log('Sum', sum);
}

isDivisible(45);

//? Exercise 4 : Shopping List

let stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

let prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};
/**Add the stock and prices objects to your js file.
Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
Create a function called myBill() that takes no parameters.
The function should return the total price of your shoppingList. In order to do this you must follow these rules:
The item must be in stock.
If the item is in stock find out the price in the prices object.
Call the myBill() function.

Bonus: If the item is in stock, decrease the item’s stock by 1 */

let shoppingList = ['banana', 'orange', 'apple'];

function myBill() {
  let myCart = 0;
  for (let item of shoppingList) {
    if (stock[item] !== 0) {
      stock[item] = stock[item] - 1;

      myCart = myCart + prices[item];
      console.log(item, prices[item]);
    }
  }
  console.log('my cart', myCart);
  console.log(' new stock', stock);
}

myBill();

//? Exercise 5 : What’s In My Wallet ?
/**Note: Read the illustration (point 4), while reading the instructions
Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
an item price
and an array representing the amount of change in your pocket.
In the function, determine whether or not you can afford the item.
If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false
Change will always be represented in the following order: quarters, dimes, nickels, pennies.
A quarters is 0.25
A dimes is 0.10
A nickel is 0.05
A penny is 0.01
4. To illustrate:
After you created the function, invoke it like this:
changeEnough(4.25, [25, 20, 5, 0])
The value 4.25 represents the item’s price
The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
Examples
changeEnough(14.11, [2,100,0,0]) => returns false
changeEnough(0.75, [0,0,20,5]) => returns true */

function changeEnough(itemPrice, amountOfChange) {
  let change =
    amountOfChange[0] * 0.25 +
    amountOfChange[1] * 0.1 +
    amountOfChange[2] * 0.05 +
    amountOfChange[3] * 0.01;
  if (change > itemPrice) {
    return true;
  } else {
    return false;
  }
}
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));

//? Exercise 6 : Vacations Costs

/*Let’s create functions that calculate your vacation’s costs:

Define a function called hotelCost().
It should ask the user for the number of nights they would like to stay in the hotel.
If the user doesn’t answer or if the answer is not a number, ask again.
The hotel costs $140 per night. The function should return the total price of the hotel.*/
function hotelCost() {
  let numberOfNights;
  const costPerNight = 140;
  let totalCost;
  while (
    isNaN(numberOfNights) ||
    numberOfNights === 0 ||
    numberOfNights === null
  ) {
    if (
      isNaN(numberOfNights) ||
      numberOfNights === 0 ||
      numberOfNights === null
    ) {
      numberOfNights = Number(
        prompt('Dear customer, how many nights do you want to book ?')
      );
    }
  }
  totalCost = numberOfNights * costPerNight;
  return `The total cost for the hotel is ${totalCost} dollars`;
}

console.log(hotelCost());

/**Define a function called planeRideCost().
It should ask the user for their destination.
If the user doesn’t answer or if the answer is not a string, ask again.
The function should return a different price depending on the location.
“London”: 183$
“Paris” : 220$
All other destination : 300$ */

function planeRideCost() {
  let cost;
  let destination = '';
  while (typeof destination == 'number' || destination === '') {
    destination = prompt('Enter your destination ');
  }
  destination = destination.toLowerCase();
  destination = destination.charAt(0).toUpperCase() + destination.slice(1);
  console.log(destination);

  switch (destination) {
    case 'London':
      cost = 183;

      break;
    case 'Paris':
      cost = 220;

      break;

    default:
      cost = 300;
      break;
  }
  console.log(`The price for ${destination} is ${cost}$`);
  return `The price for ${destination} is ${cost}$`;
}
planeRideCost();

/**Define a function called rentalCarCost().
It should ask the user for the number of days they would like to rent the car.
If the user doesn’t answer or if the answer is not a number, ask again.
Calculate the cost to rent the car. The car costs $40 everyday.
If the user rents a car for more than 10 days, they get a 5% discount.
The function should return the total price of the car rental.
 */
function rentalCarCost() {
  let numberOfDays;
  const carRentalPerDay = 40;
  let totalCost;
  const discount = 0.05;
  let totalDiscount;

  while (isNaN(numberOfDays) || numberOfDays === 0 || numberOfDays === null) {
    if (isNaN(numberOfDays) || numberOfDays === 0 || numberOfDays === null) {
      numberOfDays = Number(
        prompt('Dear customer, how many days do you want to rent ?')
      );
    }
  }
  totalCost = carRentalPerDay * numberOfDays;
  if (numberOfDays > 10) {
    totalDiscount = totalCost * discount;
    totalCost = totalCost - totalDiscount;
  }
  return `The total cost for the car for ${numberOfDays} days is ${totalCost}$. `;
}
console.log(rentalCarCost());

/**Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost(). */

function totalVacationCost() {
  console.log(hotelCost(), planeRideCost(), rentalCarCost());
}

totalVacationCost();

/**Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.
 */

function hotelCost(numberOfNights) {
  const costPerNight = 140;
  let totalCost;

  totalCost = numberOfNights * costPerNight;
  return `The total cost for the hotel is ${totalCost} dollars`;
}

function planeRideCost(destination) {
  let cost;

  switch (destination) {
    case 'London':
      cost = 183;

      break;
    case 'Paris':
      cost = 220;

      break;

    default:
      cost = 300;
      break;
  }
  console.log(`The price for ${destination} is ${cost}$`);
  return `The price for ${destination} is ${cost}$`;
}

function rentalCarCost(numberOfDays) {
  const carRentalPerDay = 40;
  let totalCost;
  const discount = 0.05;
  let totalDiscount;

  totalCost = carRentalPerDay * numberOfDays;
  if (numberOfDays > 10) {
    totalDiscount = totalCost * discount;
    totalCost = totalCost - totalDiscount;
  }
  return `The total cost for the car for ${numberOfDays} days is ${totalCost}$. `;
}

function totalVacationCost() {
  let numberOfNights;
  let destination = '';
  let numberOfDays;

  while (
    isNaN(numberOfNights) ||
    numberOfNights === 0 ||
    numberOfNights === null
  ) {
    if (
      isNaN(numberOfNights) ||
      numberOfNights === 0 ||
      numberOfNights === null
    ) {
      numberOfNights = Number(
        prompt('Dear customer, how many nights do you want to book ?')
      );
    }
  }
  while (typeof destination == 'number' || destination === '') {
    destination = prompt('Enter your destination ');
  }
  destination = destination.toLowerCase();
  destination = destination.charAt(0).toUpperCase() + destination.slice(1);
  console.log(destination);

  while (isNaN(numberOfDays) || numberOfDays === 0 || numberOfDays === null) {
    if (isNaN(numberOfDays) || numberOfDays === 0 || numberOfDays === null) {
      numberOfDays = Number(
        prompt('Dear customer, how many days do you want to rent ?')
      );
    }
  }
  console.log(
    hotelCost(numberOfNights),
    planeRideCost(destination),
    rentalCarCost(numberOfDays)
  );
}

totalVacationCost();
