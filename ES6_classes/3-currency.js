// 3-currency.js

class Currency {
  constructor(code, name) {
    // Assigning the constructor parameters to private attributes
    this._code = code;
    this._name = name;
  }

  // Getter for 'code'
  get code() {
    return this._code;
  }

  // Setter for 'code'
  set code(value) {
    this._code = value;
  }

  // Getter for 'name'
  get name() {
    return this._name;
  }

  // Setter for 'name'
  set name(value) {
    this._name = value;
  }

  // Method to display full currency as 'name (code)'
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

export default Currency;
