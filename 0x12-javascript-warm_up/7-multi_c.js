#!/usr/bin/node
// Script that prints x times "C is fun"

if (isNaN(process.argv[2])){
  console.log('Missing number of occurences');
} else {
  let i=0;
  while (i < parseInt(process.argv[2])){
    console.log('C is fun');
    i++;
  }
}
