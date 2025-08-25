# ES6 classes

![Project badge](https://img.shields.io/badge/Progress-100%25-green)
- **Your score will be updated as you progress.**

## Resources
- Read or watch:

	- `Classes` https://intranet.hbtn.io/rltoken/AJdJxuoO8o3hwpybQaFSDQ

	- `Metaprogramming` https://intranet.hbtn.io/rltoken/jF42Fw5HNIPnFWKmDzVg1g

Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:

How to define a Class
How to add methods to a class
Why and how to add a static method to a class
How to extend a class from another
Metaprogramming and symbols

### describe ressource to learn
In JavaScript, defining and working with `classes` in ES6 and beyond is straightforward. Here’s an overview of how to work with classes, add methods (including static methods), extend classes, and understand metaprogramming with symbols:

1. Defining a Class
To define a class in ES6, use the `class` keyword followed by the class name. Inside the class, a `constructor` method is often used to initialize object properties.

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}
```
This `Person class` has a `constructor` that sets `name` and `age` properties when a `new Person` instance is created.

2. Adding Methods to a Class
You can add methods directly inside the class definition. They don’t need the function keyword.

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    return `Hello, my name is ${this.name}.`;
  }
}
```
Here, the `greet method` is added to the `Person class`. When you create an instance, you can call `personInstance.greet()`.

3. Adding a Static Method to a Class
A static method is a method that belongs to the class itself, not to instances of the class. You define a static method using the static keyword.

```js
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(5, 10)); // Outputs: 15
```
The add method is called on the `MathUtils` class itself, not on an instance of `MathUtils`.

Why Use Static Methods?
Static methods are useful when you want to create utility functions that do not depend on instance properties. They’re often used for functionality that’s relevant to all instances or that doesn’t rely on instance-specific data.

4. Extending a Class from Another
To extend a class, use the extends keyword. This allows you to create a subclass that inherits the properties and methods of the parent class.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} barks.`;
  }
}

const myDog = new Dog('Rex');
console.log(myDog.speak()); // Outputs: "Rex barks."
```
The `Dog class` extends `Animal`, inheriting its properties and methods. The `speak` method in `Dog` overrides the `speak` method in `Animal`.

5. Metaprogramming and Symbols
Symbols are a unique and immutable data type introduced in ES6. They can be used as keys for object properties to avoid naming conflicts, and they’re also useful in metaprogramming.

```js
const uniqueID = Symbol('id');
class User {
  constructor(name) {
    this.name = name;
    this[uniqueID] = Math.random();
  }
}

const user = new User('Alice');
console.log(user); // Outputs: User { name: 'Alice', [Symbol(id)]: 0.12345 }
```
In this example, uniqueID is a symbol used as a property key. It’s less likely to conflict with other properties because symbols are unique.

Using Symbols for Metaprogramming
JavaScript has several built-in symbols (e.g., `Symbol.iterator`, `Symbol.toStringTag`) that you can use to customize how objects behave in specific scenarios.

For example, you can define a custom iterator for a class by using `Symbol.iterator`:

```js
class Fibonacci {
  constructor(limit) {
    this.limit = limit;
  }

  *[Symbol.iterator]() {
    let a = 0, b = 1;
    for (let i = 0; i < this.limit; i++) {
      yield a;
      [a, b] = [b, a + b];
    }
  }
}

const sequence = new Fibonacci(5);
console.log([...sequence]); // Outputs: [0, 1, 1, 2, 3]
```
In this example, `Symbol.iterator` allows `Fibonacci` instances to be iterated over like an array, generating a sequence of numbers.

- Summary

	- Define a class with `class ClassName`.

	- Add methods inside the class definition.

	- Static methods (`static methodName()`) belong to the class, not instances.

	- Extend classes with `extends` for inheritance.

	- Symbols provide unique keys and enable metaprogramming features such as custom iterators.

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `node 20.x.x` and `npm 9.x.x`

- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`

- All your files should end with a new line

- A `README.md` file, at the root of the folder of the project, is mandatory

- Your code should use the `js` extension

- Your code will be tested using `Jest` and the command `npm run test`

- Your code will be verified against lint using `ESLint`

- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`

## Setup
### Install NodeJS 20.x.x
(in your home directory):

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```
### Install Jest, Babel, and ESLint
in your project directory:

- Install `Jest` using: `npm install --save-dev jest`

- Install `Babel` using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`

- Install `ESLint` using: `npm install --save-dev eslint`

## Configuration files
`package.json`
Click to show/hide file contents

`babel.config.js`
Click to show/hide file contents

`.eslintrc.js`
Click to show/hide file contents
_______________________________________
`package.json`
Click to show/hide file contents
```json

{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
    "eslint": "^6.8.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

`babel.config.js`
Click to show/hide file contents
```js

module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};

```


`.eslintrc.js`
Click to show/hide file contents
```js

module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};

```

and…
Don’t forget to run `$ npm install` when you have the `package.json`

## Tasks
0. You used to attend a place like this at some point

***mandatory***

Implement a class named `ClassRoom`:

Prototype: `export default class ClassRoom`
It should accept one attribute named `maxStudentsSize` (Number) and assigned to `_maxStudentsSize`

```bash
bob@dylan:~$ cat 0-main.js
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room._maxStudentsSize)

bob@dylan:~$
bob@dylan:~$ npm run dev 0-main.js
10
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `0-classroom.js`


1. Let's make some classrooms

***mandatory***

Import the `ClassRoom` class from `0-classroom.js`.

Implement a function named `initializeRooms`. It should return an array of 3 `ClassRoom` objects with the sizes 19, 20, and 34 (in this order).

```bash
bob@dylan:~$ cat 1-main.js
import initializeRooms from './1-make_classrooms.js';

console.log(initializeRooms());

bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
[
  ClassRoom { _maxStudentsSize: 19 },
  ClassRoom { _maxStudentsSize: 20 },
  ClassRoom { _maxStudentsSize: 34 }
]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `1-make_classrooms.js`


2. A Course, Getters, and Setters

***mandatory***

Implement a class named `HolbertonCourse`:

- Constructor attributes:

	- `name` (String)

	- `length` (Number)

	- `students` (array of Strings)

- Make sure to verify the type of attributes during object creation

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Implement a getter and setter for each attribute.

```bash
bob@dylan:~$ cat 2-main.js
import HolbertonCourse from "./2-hbtn_course.js";

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1.name);
c1.name = "Python 101";
console.log(c1);

try {
    c1.name = 12;
}
catch(err) {
    console.log(err);
}

try {
    const c2 = new HolbertonCourse("ES6", "1", ["Bob", "Jane"]);
}
catch(err) {
    console.log(err);
}

bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
ES6
HolbertonCourse {
  _name: 'Python 101',
  _length: 1,
  _students: [ 'Bob', 'Jane' ]
}
TypeError: Name must be a string
    ...
TypeError: Length must be a number
    ...
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `2-hbtn_course.js`

3. Methods, static methods, computed methods names..... MONEY

***mandatory***

Implement a class named `Currency`:

- Constructor attributes:

	- `code` (String)

	- `name` (String)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Implement a getter and setter for each attribute.

- Implement a method named `displayFullCurrency` that will return the attributes in the following format `name (code)`.

```bash
bob@dylan:~$ cat 3-main.js
import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency());

bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
Dollars ($)
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `3-currency.js`


4. Pricing

***mandatory***

Import the class `Currency` from `3-currency.js`

Implement a class named `Pricing`:

- Constructor attributes:

	- `amount` (Number)

	- `currency` (Currency)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Implement a getter and setter for each attribute.

- Implement a method named `displayFullPrice` that returns the attributes in the following format `amount currency_name (currency_code)`.

- Implement a static method named `convertPrice`. It should accept two arguments: `amount` (Number), `conversionRate` (Number). The function should return the amount multiplied by the conversion rate.

```bash
bob@dylan:~$ cat 4-main.js
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency("EUR", "Euro"))
console.log(p);
console.log(p.displayFullPrice());

bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
Pricing {
  _amount: 100,
  _currency: Currency { _code: 'EUR', _name: 'Euro' }
}
100 Euro (EUR)
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `4-pricing.js`


5. A Building

***mandatory***

Implement a class named `Building`:

- Constructor attributes:

	- `sqft` (Number)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Implement a getter and setter for each attribute.

- Consider this class as an abstract class. And make sure that any class that extends from it should implement a method named `evacuationWarningMessage`.

	- If a class that extends from it does not have a `evacuationWarningMessage` method, throw an error with the message `Class extending Building must override evacuationWarningMessage`

```bash
bob@dylan:~$ cat 5-main.js
import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

try {
    new TestBuilding(200)
}
catch(err) {
    console.log(err);
}

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
Building { _sqft: 100 }
Error: Class extending Building must override evacuationWarningMessage
    ...
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `5-building.js`


6. Inheritance

***mandatory***

Import `Building` from `5-building.js`.

Implement a class named `SkyHighBuilding` that extends from `Building`:

- Constructor attributes:

	- `sqft` (Number) (must be assigned to the parent class `Building`)

	- `floors` (Number)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Implement a getter for each attribute.

- Override the method named `evacuationWarningMessage` and return the following string `Evacuate slowly the NUMBER_OF_FLOORS floors`.

```bash
bob@dylan:~$ cat 6-main.js
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);
console.log(building.floors);
console.log(building.evacuationWarningMessage());

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js
140
60
Evacuate slowly the 60 floors
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `6-sky_high.js`


7. Airport

***mandatory***

Implement a class named `Airport`:

- Constructor attributes:

	- `name` (String)
	- `code` (String)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- The default string description of the class should return the airport `code` (example below).

```bash
bob@dylan:~$ cat 7-main.js
import Airport from "./7-airport.js";

const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);
console.log(airportSF.toString());

bob@dylan:~$
bob@dylan:~$ npm run dev 7-main.js
Airport [SFO] { _name: 'San Francisco Airport', _code: 'SFO' }
[object SFO]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `7-airport.js`


8. Primitive - Holberton Class

***mandatory***

Implement a class named `HolbertonClass`:

- Constructor attributes:
	- `size` (Number)
	- `location` (String)

-Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- When the class is cast into a `Number`, it should return the size.

- When the class is cast into a `String`, it should return the location.

```bash
bob@dylan:~$ cat 8-main.js
import HolbertonClass from "./8-hbtn_class.js";

const hc = new HolbertonClass(12, "Mezzanine")
console.log(Number(hc));
console.log(String(hc));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js
12
Mezzanine
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `8-hbtn_class.js`


9. Hoisting

***mandatory***

Fix this code and make it work.

```js
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```

Result:

```bash
bob@dylan:~$ cat 9-main.js
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
    student => student.fullStudentDescription
);

console.log(listPrinted)

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js
[
  StudentHolberton {
    _firstName: 'Guillaume',
    _lastName: 'Salva',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'John',
    _lastName: 'Doe',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Albert',
    _lastName: 'Clinton',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Donald',
    _lastName: 'Bush',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Jason',
    _lastName: 'Sandler',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  }
]
[
  'Guillaume Salva - 2020 - San Francisco',
  'John Doe - 2020 - San Francisco',
  'Albert Clinton - 2019 - San Francisco',
  'Donald Bush - 2019 - San Francisco',
  'Jason Sandler - 2019 - San Francisco'
]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `9-hoisting.js`


10. Vroom

***mandatory***

Implement a class named `Car`:

- Constructor attributes:

	- `brand` (String)

	- `motor` (String)

	- `color` (String)

- Each attribute must be stored in an “underscore” attribute version (ex: `name` is stored in `_name`)

- Add a method named `cloneCar`. This method should return a new object of the class.

Hint: Symbols in ES6

```bash
bob@dylan:~$ cat 10-main.js
import Car from "./10-car.js";

class TestCar extends Car {}

const tc1 = new TestCar("Nissan", "Turbo", "Pink");
const tc2 = tc1.cloneCar();

console.log(tc1);
console.log(tc1 instanceof TestCar);

console.log(tc2);
console.log(tc2 instanceof TestCar);

console.log(tc1 == tc2);

bob@dylan:~$
bob@dylan:~$ npm run dev 10-main.js
TestCar { _brand: 'Nissan', _motor: 'Turbo', _color: 'Pink' }
true
TestCar { _brand: undefined, _motor: undefined, _color: undefined }
true
false
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_classes`

File: `10-car.js`

