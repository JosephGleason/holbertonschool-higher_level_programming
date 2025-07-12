#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all args to integers
  const numbers = args.map(function (arg) {
    return parseInt(arg);
  });

  // Sort numbers in descending order
  const sortedNumbers = numbers.sort(function (a, b) {
    return b - a;
  });

  // Create a new array for unique numbers
  var uniqueNumbers = [];

  for (var i = 0; i < sortedNumbers.length; i++) {
    if (uniqueNumbers.indexOf(sortedNumbers[i]) === -1) {
      uniqueNumbers.push(sortedNumbers[i]);
    }
  }

  if (uniqueNumbers.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueNumbers[1]);
  }
}
