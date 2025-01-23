const { spawn } = require('child_process');

describe('1-stdin.js', () => {
  it(
    'should handle manual input correctly',
    (done) => {
      const child = spawn('node', ['1-stdin.js']);
      let output = '';
      let inputWritten = false;

      // Capture stdout and write input when ready
      child.stdout.on('data', (data) => {
        output += data.toString();

        if (!inputWritten && output.includes('Welcome to Holberton School, what is your name?')) {
          child.stdin.write('Bob\n'); // Simulate user input
          inputWritten = true;
        }
      });

      // Handle process closure
      child.on('close', () => {
        // Assertions
        expect(output).toContain('Welcome to Holberton School, what is your name?');
        expect(output).toContain('Your name is: Bob');
        expect(output).toContain('This important software is now closing');
        done();
      });
    },
    10000 // Set timeout to 10 seconds
  );

  it(
    'should handle piped input correctly',
    (done) => {
      // Simulate piped input
      const child = spawn('echo', ['John | node 1-stdin.js'], { shell: true });
      let output = '';

      // Capture stdout
      child.stdout.on('data', (data) => {
        output += data.toString();
      });

      // Handle process closure
      child.on('close', () => {
        // Assertions
        expect(output).toContain('Welcome to Holberton School, what is your name?');
        expect(output).toContain('Your name is: John');
        expect(output).toContain('This important software is now closing');
        done();
      });
    },
    10000 // Set timeout to 10 seconds
  );
});
