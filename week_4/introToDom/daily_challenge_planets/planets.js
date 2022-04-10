let planets = [
  'jupyter',
  'neptune',
  'saturn',
  'venus',
  'mercury',
  'mars',
  'uranus',
  'pluton',
  'earth',
  'moon',
  'sun',
];
let newPlanets = [
  {
    plName: 'sun',
    moons: [],
  },

  {
    plName: 'mercury',
    color: 'grey',
    dimension: ['40px', '40px'],
  },

  {
    plName: 'venus',
    color: 'orange',
    dimension: ['50px', '50px'],
  },

  {
    plName: 'earth',
    color: 'cyan',
    dimension: ['50px', '50px'],
    moons: [{ mname: 'moon', position: ['50px', '60px'] }],
  },

  {
    plName: 'mars',
    color: 'red',
    dimension: ['50px', '50px'],
    moons: [
      { mname: 'phobos', position: ['-40px', '30px'] },
      { mname: 'deimos', position: ['100px', '50px'] },
    ],
  },
  {
    plName: 'jupyter',
    color: 'magenta',
    dimension: ['100px', '100px'],
    moons: [
      { mname: 'io', position: ['-40px', '30px'] },
      { mname: 'europe', position: ['160px', '30px'] },
      { mname: 'ganymede', position: ['-100px', '30px'] },
      { mname: 'callisto', position: ['110px', '50px'] },
    ],
  },
  {
    plName: 'saturn',
    color: 'orangered',
    dimension: ['90px', '90px'],
    moons: [
      { mname: 'nimas', position: ['-40px', '30px'] },
      { mname: 'encelade', position: ['60px', '-30px'] },
      { mname: 'thetis', position: ['-40px', '30px'] },
      { mname: 'dione', position: ['-60px', '70px'] },
      { mname: 'rhea', position: ['-40px', '30px'] },
      { mname: 'titan', position: ['100px', '-40px'] },
      { mname: 'japet', position: ['-40px', '-30px'] },
      { mname: 'phoebe', position: ['80px', '30px'] },
    ],
  },
  {
    plName: 'uranus',
    color: 'pink',
    dimension: ['60px', '60px'],
    moons: [
      { mname: 'pick', position: ['-40px', '30px'] },
      { mname: 'miranda', position: ['120px', '-40px'] },
      { mname: 'ariel', position: ['-40px', '-60px'] },
      { mname: 'umbriel', position: ['50px', '-30px'] },
      { mname: 'titania', position: ['-100px', '80px'] },
      { mname: 'uberon', position: ['70px', '30px'] },
    ],
  },

  {
    plName: 'neptune',
    color: 'blue',
    dimension: ['60px', '60px'],
    moons: [
      { mname: 'triton', position: ['-40px', '30px'] },
      { mname: 'nereide', position: ['60px', '-30px'] },
    ],
  },
];

// let planetColor = (planetName) => {
//   switch (planetName) {
//     case 'sun':
//       return 'yellow';
//     case 'mars':
//       return 'red';
//     case 'jupyter':
//       return 'magenta';
//     case 'neptune':
//       return 'green';
//     case 'saturn':
//       return 'purple';
//     case 'pluton':
//       return 'blue';
//     case 'earth':
//       return 'cyan';
//     case 'uranus':
//       return 'orange';
//     case 'venus':
//       return 'pink';
//     case 'mercury':
//       return 'grey';
//   }
// };

let planetList = document.querySelector('.listPlanets');
console.log(planetList);
// planets.forEach((planet) => {
//   let divElem = document.createElement('div');
//   let planetDetail = planetList.appendChild(divElem);
//   if (planet === 'sun') {
//     planetDetail.classList.add('sun');
//     planetDetail.innerText = 'Sun';
//   } else if (planet === 'moon') {
//     planetDetail.classList.add('moon');
//     planetDetail.innerText = 'Moon';
//   } else {
//     planetDetail.classList.add('planet', planet);
//     planetDetail.setAttribute('style', `background:${planetColor(planet)}`);
//     planetDetail.innerText = planet;
//   }
// });
planetList.setAttribute(
  'style',
  'display:flex; justify-content: space-between; align-items:center'
);
newPlanets.forEach((planet) => {
  let divElem = document.createElement('div');
  let planetDetail = planetList.appendChild(divElem);

  if (planet.plName === 'sun') {
    planetDetail.classList.add('sun');
    planetDetail.innerText = 'Sun';
    //   } else if (planet.plName === 'moon') {
    //     planetDetail.classList.add('moon');
    //     planetDetail.innerText = 'Moon';
    //   } else {
  } else {
    planetDetail.classList.add('planet', planet.plName);
    planetDetail.setAttribute(
      'style',
      `background:${planet.color}; width:${planet.dimension[0]}; height: ${planet.dimension[1]}`
    );
    planetDetail.innerText = planet.plName;
    let moonsList = document.querySelectorAll(`.${planet.plName}`)[0];
    // console.log(moonsList);

    if (planet.moons) {
      planet.moons.forEach((moon) => {
        let moonDiv = document.createElement('div');
        let moonsDetail = moonsList.appendChild(moonDiv);
        moonsDetail.classList.add('moon', `${moon.mname}`);
        moonsDetail.setAttribute(
          'style',
          `top:${moon.position[0]}; left: ${moon.position[1]};border-color:${planet.color}`
        );
      });

      //   }
    }
  }
});
