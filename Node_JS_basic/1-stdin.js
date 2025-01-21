// 1-stdin.js
const readline = require('readline');

const ui = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

ui.question('', (name) => {
  console.log(`Your name is: ${name}`);
  ui.close();
});

ui.on('close', () => {
  console.log('This important software is now closing');
  process.exit(0); // Explicitly exit the process
});
