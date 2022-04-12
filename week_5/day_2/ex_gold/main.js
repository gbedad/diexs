//! Exercise 1

let musicGenre = document.querySelector('#genres');

let button = document.querySelector('#display');

let setColor = () => {
  let genre = musicGenre.value;
  document.querySelector('#color').textContent = genre;
};

button.addEventListener('click', setColor);

//! Exercise 2

/**Add a click event listener to the <input type="button">. When clicked on, it should call a function named : removecolor() that removes the selected color from the dropdown list. */
let selectedElement = document.querySelector('#colorSelect');

let removecolor = () => {
  let selected = selectedElement.selectedIndex;
  //   console.log(selected);
  selectedElement.remove(selected);
};

let buttonRemove = document.querySelector('input');

buttonRemove.addEventListener('click', removecolor);

//! Exercise 3 : Create A Shopping List
/**Create an empty array. For example: let shoppingList=[].
Create a form containing : a text input field and an “AddItem” button. Add this form to the DOM.
Type what you need to buy in the text input field, then add the new item to the array as soon as you click on the “AddItem” button (Hint: create a function named addItem()).
Add a “ClearAll” button to the DOM, that when clicked on, should call the clearAll() function (see below).
Create a function named clearAll() that should clear out all the items in the shopping list. */

let shoppingList = [];

let form = document.createElement('form');
let myDiv = document.querySelector('#root');
myDiv.appendChild(form);
let item = document.createElement('input');
form.appendChild(item);
let buttonAdd = document.createElement('button');
form.appendChild(buttonAdd);
buttonAdd.classList.add('addItem');
buttonAdd.textContent = 'AddItem';
let buttonClear = document.createElement('button');
form.appendChild(buttonClear);
buttonClear.classList.add('clearAll');
buttonClear.textContent = 'clearAll';

let addItem = (e) => {
  e.preventDefault();
  shoppingList.push(item.value);
  item.value = '';
  console.log(shoppingList);
};

let clearAll = (arr) => {
  let len = arr.length;
  arr.splice(0, len);
};

console.log(shoppingList);

buttonAdd.addEventListener('click', addItem);
buttonClear.addEventListener('click', clearAll);
