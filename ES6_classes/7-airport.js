// 7-airport.js

class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Override toString method to return the airport code in the required format
  toString() {
    return `[object ${this._code}]`;
  }
}

export default Airport;
