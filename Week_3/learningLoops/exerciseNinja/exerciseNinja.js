//? Exercise 1 : Checking the BMI

john = {
  fullname: 'John Doe',
  mass: 78,
  height: 179,
  bmi() {
    return (john.height / john.mass).toFixed(2);
  },
};

james = {
  fullname: 'James DCavendish',
  mass: 87,
  height: 167,
  bmi() {
    return (james.height / james.mass).toFixed(2);
  },
};

let johnBMI = john.bmi();
let jamesBMI = james.bmi();

if (johnBMI > jamesBMI) {
  console.log(`John BMI (${johnBMI}) is higher than James BMI (${jamesBMI}).`);
} else if (johnBMI < jamesBMI) {
  console.log(`James BMI (${jamesBMI}) is higher than John BMI (${johnBMI}).`);
} else {
  console.log('Same BMI');
}

//? Exercise 2 : Grade Average
function findAvg(gradesList) {
  let grades = 0;
  const gradesLength = gradesList.length;
  for (let i = 0; i < gradesList.length; i++) {
    grades += gradesList[i];
  }
  let gradesAvg = grades / gradesLength;
  console.log(gradesAvg);
  return gradesAvg;
}

function isPassed(gradesAvg) {
  if (gradesAvg > 65) {
    console.log('Gongratulations, you have passed your exam');
  } else {
    console.log(
      'Your average grade is not sufficient to pqss, you must repeat the course'
    );
  }
}

let grades = [45, 58, 67, 56, 90];

findAvg(grades);
isPassed(findAvg(grades));
