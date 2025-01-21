const displayMessage = require('./0-console');

describe('displayMessage', () => {
  it('should log the correct message to the console', () => {
    console.log = jest.fn();
    displayMessage('Hello NodeJS!');
    expect(console.log).toHaveBeenCalledWith('Hello NodeJS!');
  });
});
