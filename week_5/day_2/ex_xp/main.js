//! Exercise 1
//*Using a DOM property, retrieve the h1 and console.log it.

function retrieveElement(elem) {
  let elementToRetrieve = document.querySelectorAll(elem);

  console.log(elementToRetrieve);
  return elementToRetrieve;
}
let elementH1 = retrieveElement('h1')[0];
console.log(elementH1.textContent);

//* Using DOM methods, remove the last paragraph in the <article> tag.

let lastP = document.querySelectorAll('article > p:last-child')[0];
// console.log(lastP);
lastP.remove();

//* Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

function changeBackground() {
  elementH2.style.background = 'red';
}
let elementH2 = retrieveElement('h2')[0];
elementH2.addEventListener('click', changeBackground);

//* Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

function hideElement() {
  elementH3.style.display = 'none';
}

let elementH3 = retrieveElement('h3')[0];

elementH3.addEventListener('click', hideElement);

//* Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

let button = retrieveElement('#textBold')[0];

button.addEventListener('click', changeToBold);

function changeToBold() {
  let elements = retrieveElement('p');
  elements.forEach((elem) => {
    elem.style.fontWeight = 'bold';
  });
}

//* BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

//* BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

function onHoverH1() {
  elementH1.style.fontSize = `${Math.random() * 100}px`;
}

elementH1.addEventListener('mouseover', onHoverH1);

function fadeOut() {
  secondParagraph.style.visibility = 'hidden';
  secondParagraph.style.opacity = 0;
  secondParagraph.style.transition = 'visibility 0s 2s, opacity 2s linear';
}

let secondParagraph = retrieveElement('article > p:nth-of-type(2)')[0];

// console.log(secondParagraph);

secondParagraph.addEventListener('mouseover', fadeOut);

//! Exercise 2 : Work With Forms

/**Retrieve the form and console.log it.

Retrieve the inputs by their id and console.log them.

Retrieve the inputs by their name attribute and console.log them.

When the user submits the form (ie. submit event listener)
get the values of the input tags,
make sure that they are not empty,
create an li per input value,
then append them to a the <ul class="usersAnswer"></ul>, below the form. */

let formRetrieve = retrieveElement('form')[0];
console.log(formRetrieve);

let inputs = formRetrieve.querySelectorAll('input');
// console.log(inputs);

// console.log(inputs[0].getAttribute('name'));
inputs.forEach((input) => {
  let attributeName = input.getAttribute('name');
  if (attributeName) {
    console.log(attributeName);
    return attributeName;
  }
});

// let submit = inputs[2];
console.log(submit, fname, lname);
let submitButton = document.querySelector('#submit');
let ul = document.querySelector('.usersAnswer');
console.log(submitButton);
console.log(ul);

// fname.addEventListener();
let inputValue = (input) => {
  let li = document.createElement('li');
  if (input.value.length > 0) {
    let value = document.createTextNode(input.value);
    li.appendChild(value);
    ul.appendChild(li);
    input.value = '';
  }
};

let addElement = (event) => {
  event.preventDefault();
  if (fname.value.length > 0 && lname.value.length > 0) {
    inputValue(fname);
    inputValue(lname);
  }
};

submitButton.addEventListener('click', addElement);

//! Exercise 3 : Transform The Sentence

/**Create a global variable named allBoldItems.

Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

Create a function called highlight() that changes the color of all the bold text to blue.

Create a function called return_normal() that changes the color of all the bold text back to black.

Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example */

let allBoldItems;

let getBold_items = () => {
  allBoldItems = document.querySelectorAll('strong');
  return allBoldItems;
};
console.log(getBold_items());

let highlight = () => {
  let elements = getBold_items();
  elements.forEach((elem) => {
    elem.style.color = 'blue';
  });
};

let return_normal = () => {
  let elements = getBold_items();
  elements.forEach((elem) => {
    elem.style.color = 'black';
  });
};
// console.log(document.querySelectorAll('strong'));

let paragraph = document.querySelectorAll('#exercise3 > p')[0];

paragraph.addEventListener('mouseover', highlight);
paragraph.addEventListener('mouseout', return_normal);

//! Exercise 4 : Volume Of A Sphere
let formSubmit = document.querySelector('#MyForm');

let calculate = (r) => {
  let volume = (4 / 3) * Math.PI * r ** 3;
  return volume;
};

let getRadius = () => {
  let radius = document.querySelectorAll('#radius')[0].value;
  return radius;
};

let calculateVolume = () => {
  let volumeDisplay = document.querySelector('#volume');
  let radius = getRadius();
  volumeDisplay.value = calculate(radius);
};

// console.log(calculateButton);

formSubmit.addEventListener('click', (e) => {
  e.preventDefault();
  calculateVolume();
});

//! Bonus Exercise 5 : Event Listeners
/**Add as many events listeners as possible to one element on your webpage. Each listener should do a different thing, for instance- change position x, change position y, change color, change the font size… and more. */

const parags = document.querySelectorAll('p');
parags.forEach((p) => {
  p.addEventListener('click', () => {
    p.style.color = 'green';
  });
});

submitButton.addEventListener('mouseover', () => {
  submitButton.style.backgroundColor = 'yellow';
  submitButton.style.color = 'purple';
});
submitButton.addEventListener('mouseout', () => {
  submitButton.style.backgroundColor = 'green';
  submitButton.style.color = 'white';
});
