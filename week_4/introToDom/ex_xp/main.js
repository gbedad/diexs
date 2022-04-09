//* Exercise 1

/**In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method. */
let navbar = document.querySelector('#navBar');
navbar.setAttribute('id', 'socialNetworkNavigation');

console.log(navbar);

/**First, create a new <li> tag (use the createElement method).
Create a new text node with “Logout” as its specified text.
Append the text node to the newly created list node (li).
Finally, append this updated list node to the unordered list above, using the appendChild method. */
let newText = document.createTextNode('Logout');
let getUl = document.querySelector('ul');

let newLi = document.createElement('li');
// newLi.textContent = 'Logout';
newLi.appendChild(newText);
getUl.appendChild(newLi);

/**Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property). */

let first = getUl.firstElementChild;
let last = getUl.lastElementChild;
console.log(first.textContent, last.textContent);

//* Exercise 2

/*In the HTML above change the name “Pete” to “Richard”.
Change each first name of the two <ul>'s to your name.
At the end of each <ul> add a <li> that says “Hey students”.
Delete the name Sarah from the second <ul>.
Bonus
Add a class called student_list to both of the <ul>'s.
Add the classes university and attendance to the first <ul>.*/
let getFirst = document.querySelectorAll('.list')[0];
getFirst.classList.add('university', 'attendance');
console.log(getFirst);
let list = getFirst.getElementsByTagName('li');
console.log(list);

for (let elem of list) {
  let text = elem.textContent;
  console.log(elem.textContent);
  if (text === 'Pete') {
    // check if it ends with "zip"
    elem.textContent = 'Richard';
  }
}

let getUls = document.querySelectorAll('.list');
console.log(getUls);

for (let elem of getUls) {
  elem.classList.add('student_list');
  console.log(elem);
  elem.firstElementChild.textContent = 'Gerald';
  let newLi = document.createElement('li');
  elem.appendChild(newLi);
  newLi.textContent = 'Hey students';
  let lis = elem.children;
  for (let item of lis) {
    if (item.textContent === 'Sarah') {
      elem.removeChild(item);
    }
  }
}

//* Exercise 3

/**For the following exercise use the HTML presented above:

Add a “light blue” background color and some padding to the <div>.
Do not display the first name (John) in the list.
Add a border to the second name (Pete).
Change the font size of the whole body.
Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
 */

let getLastDiv = document.querySelectorAll('div')[2];
getLastDiv.style.background = 'lightblue';
getLastDiv.style.padding = '5px';

let lastUl = document.querySelectorAll('ul')[3];
console.log(lastUl);
let myLi1 = lastUl.querySelectorAll('li')[0];

let myLi2 = lastUl.querySelectorAll('li')[1];

myLi2.setAttribute('style', 'border: 1px solid lightblue; font-size:20px');
myLi1.setAttribute('style', 'display:none;font-size:20px');

let myPage = document.querySelectorAll('div');
console.log(myPage);
for (let elem of myPage) {
  if (elem.style.background === 'lightblue') {
    alert(`Hello ${myLi1.textContent} and ${myLi2.textContent}`);
  }
}
