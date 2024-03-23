#!/usr/bin/node
// fin the biggest number

const n = process.argv.length;
if (n <= 3){
  console.log(0);
} else {
  let max = process.argv[0];
  for (let i = 3; i < n; i++){
    if (process.argv[i] > max){
      max = process.argv[i];
    }
  }
  console.log(max);
}
