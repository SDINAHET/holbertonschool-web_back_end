const displayMessage = require('./0-console');

describe('displayMessage', () => {
  it('logs the correct message to the console', () => {
    // Mock console.log
    console.log = jest.fn();

    // Call the function
    displayMessage('Hello NodeJS!');

    // Assert that console.log was called with the correct message
    expect(console.log).toHaveBeenCalledWith('Hello NodeJS!');
  });
});
