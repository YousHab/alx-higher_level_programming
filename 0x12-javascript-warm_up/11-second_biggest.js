#!/usr/bin/node
// fin the biggest number

const n = process.argv.length;
if (n <= 3){
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
