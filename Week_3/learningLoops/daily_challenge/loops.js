function myTriangle() {
  let plus = '';
  for (let i = 0; i < 6; i++) {
    plus = plus + '* ';
    console.log(plus);
  }
}
myTriangle();

// Exercise 7 loops
//____________________________________
function secretGroup(arr) {
  let secret = '';
  arr.sort();
  arr.forEach((element) => {
    let first = element[0];
    secret += first;
  });
  return secret;
}

let names = ['Jack', 'Philip', 'Sarah', 'Amanda', 'Bernard', 'Kyle'];

let answer = secretGroup(names);
console.log(answer);

// Writing an A in *
let l1 = '  ***  ';
let l2 = ' ***** ';
let l3 = ' *   * ';

console.log(l1);
for (let i = 0; i < 2; i++) {
  console.log(l3);
}
console.log(l2);
for (let i = 0; i < 3; i++) {
  console.log(l3);
}

//   for (let x = 0; x < 6; x++) {
//     console.log('x');
//   }
