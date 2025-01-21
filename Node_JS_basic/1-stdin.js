// Display the initial prompt
console.log("Welcome to Holberton School, what is your name?");

process.stdin.on('data', (data) => {
  // Read user input and remove the newline character
  const name = data.toString().trim();

  // Display the user's name
  console.log(`Your name is: ${name}`);

  // Exit the process
  console.log("This important software is now closing");
  process.exit();
});
