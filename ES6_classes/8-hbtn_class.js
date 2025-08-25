// 8-hbtn_class.js

class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Override valueOf method to return the size when the class is cast to a Number
  valueOf() {
    return this._size;
  }

  // Override toString method to return the location when the class is cast to a String
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
