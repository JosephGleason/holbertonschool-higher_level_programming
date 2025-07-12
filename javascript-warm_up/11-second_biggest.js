#!/usr/bin/node

const args = process.argv;
const length = args.length - 2;

if (length < 2) {
  console.log(0);
} else {
  let max = parseInt(args[2]);
  let secondMax = 0;

  for (let i = 3; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > max) {
      max = num;
    }
  }

  secondMax = parseInt(args[2]);
  for (let i = 3; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  if (secondMax === max || secondMax === parseInt(args[2])) {
    console.log(0);
  } else {
    console.log(secondMax);
  }
}
