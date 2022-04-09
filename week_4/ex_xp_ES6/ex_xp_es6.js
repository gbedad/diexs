/* Create a global variable that save the amount of money you have in your account
Create a variable that saves the amount of VAT
Create a variable that saves the amout of all the expenses and revenu you did /received for the past last month
Create a JS code that multiplies of the expenses by the VAT
Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenu.
Display it */
// let account = {
//     amount : 20000,
//     vat : 0.,
//     totalAmout(){
//        return amount*vat
//     }
// }

let vatAmount = 0;
let totalAmount = 20000;
let expRev;

let totalIncludingVat = totalAmount * vatAmount;

let expenseRevenue = (value, type) => {
  switch (type) {
    case 'e':
      totalAmount -= value;
      return totalAmount;
    case 'r':
      totalAmount += value;
      return totalAmount;
  }
};
expRev = expenseRevenue(3000, 'r') * (1 + vatAmount);

totalIncludingVat = expRev;

console.log(totalIncludingVat);
