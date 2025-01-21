// 1-stdin.js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

rl.on('line', (name) => {
  console.log(`Your name is: ${name}`);
  rl.close();
});

rl.on('close', () => {
  console.log('This important software is now closing');
  process.exit(0); // Explicitly exit the process
});
