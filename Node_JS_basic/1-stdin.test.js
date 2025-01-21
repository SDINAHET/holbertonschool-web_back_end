const { spawn } = require('child_process');

describe('1-stdin.js', () => {
  it('should handle manual input correctly', (done) => {
    const child = spawn('node', ['1-stdin.js']);

    let output = '';
    child.stdout.on('data', (data) => {
      output += data.toString();
    });

    child.stdin.write('Alice\n');

    child.on('close', () => {
      expect(output).toContain('Welcome to Holberton School, what is your name?');
      expect(output).toContain('Your name is: Alice');
      expect(output).toContain('This important software is now closing');
      done();
    });
  });

  it('should handle piped input correctly', (done) => {
    const child = spawn('node', ['1-stdin.js']);

    let output = '';
    child.stdout.on('data', (data) => {
      output += data.toString();
    });

    child.stdin.end('John\n');

    child.on('close', () => {
      expect(output).toContain('Welcome to Holberton School, what is your name?');
      expect(output).toContain('Your name is: John');
      expect(output).toContain('This important software is now closing');
      done();
    });
  });
});
