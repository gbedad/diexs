/**Create a variable called billAmount that fetches the value of the input, which id is billAmt (check the HTML file) –> It’s the amount of the bill.
 */
let totalTipDisp = document.querySelector('#totalTip');
totalTipDisp.style.display = 'none';

let calculateTip = () => {
  let billAmount = Number(document.querySelector('#billamt').value);

  let serviceQuality = Number(document.querySelector('#serviceQual').value);

  let numberOfPeople = Number(document.querySelector('#peopleamt').value);
  console.log(serviceQuality);

  if (serviceQuality === 0 || billAmount === '') {
    alert('You have to enter an amount and/or service');
  }
  if (numberOfPeople === 0) {
    numberOfPeople = 1;
    document.querySelector('#peopleamt').value = 1;
  }
  let total = (billAmount * (1 + serviceQuality)) / numberOfPeople;
  total = total.toFixed(2);
  if (totalTipDisp.style.display === 'none') {
    totalTipDisp.style.display = 'block';
  } else {
    totalTipDisp.style.display = 'none';
  }
  let tipEach = totalTipDisp.querySelector('#tip');
  tipEach.textContent = total;
  return total;
};

let buttonCalculate = document.querySelector('#calculate');
buttonCalculate.addEventListener('click', calculateTip);
/*
Create a variable called serviceQuality that fetches the value of the input, which id is serviceQual (check the HTML file) –> It’s the quality of the service.

Create a variable called numberOfPeople that fetches the value of the input, which id is numOfPeople (check the HTML file) –> It’s the number of people sitting at the table.

Create a condition :
If serviceQuality is equal to zero, or billAmount is empty, alert the user to enter these values.

Create another condition after the first one :
If the input numberOfPeople is empty or is smaller than 1, set a default value of 1 to numberOfPeople and make sure that the tag which id is each, is not displayed (check the end of the HTML file).

Create a variable named total: the value should be ( billAmount * serviceQuality ) / numberOfPeople (the outcome is the average tip each person should pay)

Use the toFixed method to round total to two decimal points.

Add the CSS property “display:block” to the tag which id is totalTip.

Display the variable total in the tag which id is tip. */
const coor = document.querySelector('#coordinates');
coor.style.display = 'none';

const description = document.querySelectorAll('#coordinates  p');
description.forEach((desc) => {
  desc.style.color = 'red';
});
// description.style.color = 'red';
function geoFindMe() {
  const status = document.querySelector('#status');
  const mapLink = document.querySelector('#map-link');

  const lat = document.querySelector('#lattitude');
  const long = document.querySelector('#longitude');
  lat.style.color = 'green';
  long.style.color = 'green';

  mapLink.href = '';
  mapLink.textContent = '';

  function success(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    status.textContent = '';
    mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
    // mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
    if (coor.style.display === 'none') {
      coor.style.display = 'block';
    } else {
      coor.style.display = 'none';
    }

    lat.textContent = `${latitude} °`;
    long.textContent = `${longitude} °`;
  }

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }

  if (!navigator.geolocation) {
    status.textContent = 'Geolocation is not supported by your browser';
  } else {
    status.textContent = 'Locating…';
    navigator.geolocation.getCurrentPosition(success, error);
  }
}

document.querySelector('#find-me').addEventListener('click', geoFindMe);

//! Exercise check the email

const mydiv = document.querySelector('#checkEmail');
const myForm = document.createElement('form');
const myEmail = document.createElement('input');
mydiv.appendChild(myForm);
myForm.appendChild(myEmail);
myEmail.classList.add('email');
const checkButton1 = document.createElement('button');
const checkButton2 = document.createElement('button');
checkButton1.textContent = 'Check email regex';
myForm.appendChild(checkButton2);
checkButton2.textContent = 'Check email';
myForm.appendChild(checkButton1);
myForm.appendChild(checkButton2);
const display = document.createElement('p');
mydiv.appendChild(display);
display.textContent = '';

const validRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

const validEmail = (email) => {
  if (
    email.length > 0 &&
    email.includes('@') &&
    email.includes('.') &&
    email.indexOf('@') > 2 &&
    email.indexOf('.') >= email.indexOf('@') + 2 &&
    email.indexOf('.') < email.length - 2
  ) {
    return true;
  } else return false;
};

const checkEmail = (e) => {
  e.preventDefault();
  let email = document.querySelector('.email').value;
  //   console.log(email);
  let checkIsValid = validRegex.test(email);

  if (checkIsValid) {
    display.textContent = 'The email is valid';
  } else {
    display.textContent = 'The email is not valid';
  }
};

const checkEmail2 = (e) => {
  e.preventDefault();
  let email = document.querySelector('.email').value;
  //   console.log(email);
  let checkIsValid = validEmail(email);

  if (checkIsValid) {
    display.textContent = 'The email is valid';
  } else {
    display.textContent = 'The email is not valid';
  }
};

checkButton1.addEventListener('click', checkEmail);

checkButton2.addEventListener('click', checkEmail2);
// console.log(validRegex.test(email));
