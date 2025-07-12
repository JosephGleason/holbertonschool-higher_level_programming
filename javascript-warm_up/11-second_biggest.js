#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(function (arg) {
    return parseInt(arg);
  });

  const sortedNumbers = numbers.sort(function (a, b) {
    return b - a;
  });

  const uniqueNumbers = [];

  for (let i = 0; i < sortedNumbers.length; i++) {
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
