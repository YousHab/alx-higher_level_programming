#!/usr/bin/node
// Prints a message depending of the number of arguments passed.

const nArgs = process.argv.length;

if (nArgs === 2) {
    console.log('No arguments');
} else if (nArgs === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
