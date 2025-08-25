export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand; // Use underscore-prefixed properties for public access
    this._motor = motor;
    this._color = color;
  }

  // Clone the car by creating a new instance with undefined properties
  cloneCar() {
    const clonedCar = new this.constructor(); // Create a new instance of the same class
    clonedCar._brand = undefined;
    clonedCar._motor = undefined;
    clonedCar._color = undefined;
    return clonedCar;
  }

  // Getter methods to access the properties
  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }
}
