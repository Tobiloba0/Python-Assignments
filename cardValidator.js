
function convertToArray(cardNumber) {
    let cardArray = [];
    for (let i = 0; i < cardNumber.length; i++) {
        cardArray.push(Number(cardNumber[i]));
    }
    return cardArray;
}


function digitDoubling(cardArray) {
    let sum = 0;

    for (let i = cardArray.length - 2; i >= 0; i -= 2) {
        let number = cardArray[i] * 2;
        if (number > 9) {
            number -= 9;
        }
        sum += number;
    }

    return sum;
}


function oddNumberSum(cardArray) {
    let sum = 0;

    for (let i = cardArray.length - 1; i >= 0; i -= 2) {
        sum += cardArray[i];
    }

    return sum;
}


function isValid(cardArray) {
    let total = oddNumberSum(cardArray) + digitDoubling(cardArray);
    return total % 10 === 0;
}


function creditCardType(cardArray) {
    if (cardArray[0] === 4) return "Visa Card";
    if (cardArray[0] === 5) return "Master Card";
    if (cardArray[0] === 3 && cardArray[1] === 7) return "American Express Card";
    if (cardArray[0] === 6) return "Discover Card";
    
    return "Type not found";
}


const prompt = require("prompt-sync")(); 

let cardNumber = prompt("Enter your Credit Card Number: ");

let cardArray = convertToArray(cardNumber);

console.log("Credit Card Type:", creditCardType(cardArray));
console.log("Credit Card Number:", cardNumber);
console.log("Credit Card Length:", cardArray.length);
console.log("Card validity:", isValid(cardArray) ? "Valid" : "Invalid");

