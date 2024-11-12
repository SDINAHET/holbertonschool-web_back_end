// 2-hbtn_course.js

class HolbertonCourse {
  constructor(name, length, students) {
    // Type validation for 'name'
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;

    // Type validation for 'length'
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;

    // Type validation for 'students'
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }

  // Getter for 'name'
  get name() {
    return this._name;
  }

  // Setter for 'name'
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter for 'length'
  get length() {
    return this._length;
  }

  // Setter for 'length'
  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Getter for 'students'
  get students() {
    return this._students;
  }

  // Setter for 'students'
  set students(value) {
    if (!Array.isArray(value) || !value.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}

export default HolbertonCourse;
