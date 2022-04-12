/**Get the value of each of the inputs in the HTML file when the button is clicked.
Make sure the values are not empty
Write a story that uses each of the values.
Make sure you check the console for errors when playing the game.
Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly. */

let inputs = document.querySelectorAll('input');
let buttonLib = document.querySelector('#lib-button');
let buttonLibrnd = document.querySelector('#lib-button-rnd');

console.log(inputs);

let getInputs = () => {
  let newArray = [];
  inputs.forEach((input) => {
    if (input.value.length > 0 && isNaN(input.value)) {
      newArray.push(input.value);
    }
  });
  if (newArray.length !== 5) {
    alert('Missing fields or invalid input');
    return;
  }
  return newArray;
};

// let getStory = (arr) => {
//   let myStory = '';
//   for (let item of arr) {
//     console.log(item);
//     myStory += `${item} `;
//   }
//   return myStory.trim();
// };
let getStory = (arr) => {
  let myStory = `Today I went to my favorite restaurant called ${arr[0]}. Unlike most of the times, I was with my friend ${arr[2]}. The best thing I ${arr[3]} a ${arr[1]} jump on the floor. I will never go to a place like: ${arr[4]}!`;

  return myStory;
};

let composeStory = () => {
  let story = document.querySelector('#story');
  let textCompose = getStory(getInputs());
  let text = document.createTextNode(textCompose);
  story.appendChild(text);
};

buttonLib.addEventListener('click', composeStory);

let getRandomStory = (arr) => {
  let myStories = [
    `Today I went to my favorite restaurant called ${arr[0]}. Unlike most of the times, I was with my friend ${arr[2]}. The best thing I ${arr[3]} a ${arr[1]} jump on the floor. I will never go to a place like: ${arr[4]}!`,
    `When I was young, I used to go to ${arr[4]}. At this place, my ${arr[1]} friend ${arr[2]} was living. Everyday the man was ${arr[3]} and singing.`,
    `During summer the sun is ${arr[1]}. People ${arr[3]} like going to ${arr[4]}. But ${arr[2]} doesn't like ${arr[0]}.`,
  ];

  return myStories[Math.floor(Math.random() * 3)];
};

let composeRandomStory = () => {
  let story = document.querySelector('#story');
  story.textContent = '';
  let textCompose = getRandomStory(getInputs());
  //   let text = document.createTextNode(textCompose);
  story.textContent = textCompose;
};

buttonLibrnd.addEventListener('click', composeRandomStory);
