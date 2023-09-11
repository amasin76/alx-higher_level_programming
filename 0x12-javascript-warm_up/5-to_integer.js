#!/usr/bin/node
const num = Number(process.argv[2]) | 0;
console.log(Number.isNaN(num) ? 'Not a number' : `My number: ${num}`);
