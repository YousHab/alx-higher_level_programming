#!/usr/bin/node
// find the biggest number

const args = process.argv.slice(2).map(Number);
const n = args.length;

if (n <= 1) {
  console.log(0);
} else {
  const biggest = Math.max(...args);
  const secondBiggest = Math.max(...args.filter(num => num !== biggest));
  console.log(secondBiggest);
}
