let planets = [
  //   {
  //     plName: 'jupyter',
  //     color: 'magenta',
  //     diameter: '100px',
  //     position: ['100px', '30px'],
  //   },
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
  },

  {
    plName: 'mercury',
    color: 'grey',
    dimension: ['40px', '40px'],
    moons: ['moon1'],
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
    moons: ['moon'],
  },
  {
    plName: 'moon',
  },
  {
    plName: 'mars',
    color: 'red',
    dimension: ['50px', '50px'],
    moons: ['phobos', 'deimos'],
  },
  {
    plName: 'jupyter',
    color: 'magenta',
    dimension: ['100px', '100px'],
    moons: ['io', 'europe', 'ganymede', 'callisto'],
  },
  {
    plName: 'saturn',
    color: 'orangered',
    dimension: ['90px', '90px'],
    moons: [
      'mimas',
      'encelade',
      'thetis',
      'dione',
      'rhea',
      'titan',
      'hyperion',
      'japet',
      'phoebe',
    ],
  },
  {
    plName: 'uranus',
    color: 'pink',
    dimension: ['60px', '60px'],
    moons: ['pick', 'miranda', 'ariel', 'umbriel', 'titania', 'uberon'],
  },

  {
    plName: 'neptune',
    color: 'blue',
    dimension: ['60px', '60px'],
    moons: ['triton', 'nereide'],
  },
];

let planetColor = (planetName) => {
  switch (planetName) {
    case 'sun':
      return 'yellow';
    case 'mars':
      return 'red';
    case 'jupyter':
      return 'magenta';
    case 'neptune':
      return 'green';
    case 'saturn':
      return 'purple';
    case 'pluton':
      return 'blue';
    case 'earth':
      return 'cyan';
    case 'uranus':
      return 'orange';
    case 'venus':
      return 'pink';
    case 'mercury':
      return 'grey';
  }
};

let planetList = document.querySelector('.listPlanets');

planets.forEach((planet) => {
  let divElem = document.createElement('div');
  let planetDetail = planetList.appendChild(divElem);
  if (planet === 'sun') {
    planetDetail.classList.add('sun');
    planetDetail.innerText = 'Sun';
  } else if (planet === 'moon') {
    planetDetail.classList.add('moon');
    planetDetail.innerText = 'Moon';
  } else {
    planetDetail.classList.add('planet', planet);
    planetDetail.setAttribute('style', `background:${planetColor(planet)}`);
    planetDetail.innerText = planet;
  }
});

newPlanets.forEach((planet) => {
  console.log(planet);
  let divElem = document.createElement('div');
  let planetDetail = planetList.appendChild(divElem);
  if (planet.plName === 'sun') {
    planetDetail.classList.add('sun');
    planetDetail.innerText = 'Sun';
  } else if (planet.plName === 'moon') {
    planetDetail.classList.add('moon');
    planetDetail.innerText = 'Moon';
  } else {
    planetDetail.classList.add('planet', planet.plName);
    planetDetail.setAttribute(
      'style',
      `background:${planet.color}; width:${planet.dimension[0]}; height: ${planet.dimension[1]}`
    );
    planetDetail.innerText = planet.plName;
  }
});
