# ES6 Basics

![Project badge](https://img.shields.io/badge/Progress-0%25-red)
- **Your score will be updated as you progress.**

## Resources (Read or watch):
- `ECMAScript 6 - ECMAScript 2015` https://www.w3schools.com/js/js_es6.asp

- `Statements and declarations` https://intranet.hbtn.io/rltoken/OHkTGVz-DLmzmrpDuWDYBw https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements

- `Arrow functions` https://intranet.hbtn.io/rltoken/5FxmFLP2qwTEo0puWUVHsQ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

- `Default parameters` https://intranet.hbtn.io/rltoken/qZm6g37BqHVD9G96MLsnsg https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters

- `Rest parameters` https://intranet.hbtn.io/rltoken/qD9tUS00akyWTDU7MKUAuA https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters

- `Javascript ES6 — Iterables and Iterators` https://intranet.hbtn.io/rltoken/oeJc6rHh9gd0zAJKkpVhhg https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

	- What ES6 is
	- New features introduced in ES6
	- The difference between a constant and a variable
	- Block-scoped variables
	- Arrow functions and function parameters default to them
	- Rest and spread function parameters
	- String templating in ES6
	- Object creation and their properties in ES6
	- Iterators and for-of loops

### describe learning objectives
ES6, or ECMAScript 2015, introduced a significant set of new features to JavaScript, making the language more powerful, expressive, and easier to work with. Here’s an overview of ES6 and some of its most important features:

1. What ES6 Is
ES6 (ECMAScript 2015) is the sixth major version of the ECMAScript standard and is often referred to as ES2015. It introduced major improvements and new syntax to JavaScript, making the language more modern and aligned with programming practices found in other languages. ES6 aimed to improve JavaScript’s readability, maintainability, and efficiency.

2. New Features Introduced in ES6
ES6 introduced several significant features, including:

- let and const for block-scoped variable declarations

- Arrow functions for shorter and more readable function syntax

- Classes for defining object-oriented structures

- Template literals for easier string interpolation

- Default parameters in functions

- Rest and spread operators for managing arrays and objects flexibly

- Destructuring assignment for extracting values from arrays and objects

- Modules for better code organization

- Promises for improved asynchronous programming

- Enhanced object literals with shorthand syntax and computed properties

- Symbols as unique identifiers for properties

3. The Difference Between a Constant and a Variable
- Variable: Defined with `let` or `var`, it can be reassigned. let is block-scoped, while `var` is function-scoped and has hoisting behavior.

```js
let age = 25;
age = 26; // Reassignment is allowed
```
- Constant: Defined with `const`, it cannot be reassigned after its initial assignment and must be initialized at declaration. `const` is block-scoped.

```js
const birthYear = 1995;
// birthYear = 1996; // Error: Assignment to constant variable
```
4. Block-Scoped Variables
In ES6, `let` and `const` introduced block scoping, meaning they are only accessible within the block `({ })` in which they are declared. This is particularly useful in for loops and if statements.

```js
if (true) {
  let x = 10;
  const y = 20;
  console.log(x); // 10
  console.log(y); // 20
}
// console.log(x); // Error: x is not defined
// console.log(y); // Error: y is not defined
```
5. Arrow Functions and Default Parameters
Arrow functions provide a more concise syntax for writing functions and automatically bind the `this` context, which is helpful for callback functions.

```js
const add = (a, b = 0) => a + b;

console.log(add(5, 10)); // 15
console.log(add(5));     // 5 (uses default parameter `b = 0`)
```
In this example, `b` defaults to `0` if not provided.

6. Rest and Spread Function Parameters
- Rest Parameters `(...)`: Collects all remaining arguments into an array.

```js
function multiply(multiplier, ...args) {
  return args.map(arg => arg * multiplier);
}

console.log(multiply(2, 1, 2, 3)); // [2, 4, 6]
```

- Spread Syntax `(...)`: Expands elements from an array or object into individual elements.

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(combined); // [1, 2, 3, 4, 5, 6]
```
7. String Templating in ES6
Template literals allow embedded expressions in strings using backticks (`) and ${}` syntax, making string interpolation easier.

```js
const name = 'Alice';
const greeting = `Hello, ${name}!`;
console.log(greeting); // "Hello, Alice!"
```
This syntax allows multi-line strings and embedded expressions directly in the string.

8. Object Creation and Properties in ES6
ES6 introduced several enhancements to object literals, including shorthand property names, method definitions, and computed property names.

- Shorthand Properties:

```js
const name = 'Alice';
const age = 25;
const person = { name, age }; // { name: 'Alice', age: 25 }
```

- Method Definitions:

```js
const person = {
  greet() {
    return 'Hello!';
  }
};
```

- Computed Property Names:

```js
const prop = 'age';
const person = {
  name: 'Alice',
  [prop]: 25 // age: 25
};
```
9. Iterators and for-of Loops
ES6 introduced the `for-of` loop, which iterates over iterable objects like arrays, strings, and maps. The `for-of` loop provides a simpler way to access each element directly.

```js
const array = [1, 2, 3];
for (const num of array) {
  console.log(num); // 1, then 2, then 3
}
```
The `for-of` loop can be used with any object implementing the iterator protocol, such as arrays and strings.


## Requirements

### General

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `node 20.x.x` and `npm 9.x.x`

- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`

- All your files should end with a new line

- A `README.md` file, at the root of the folder of the project, is mandatory

- Your code should use the `js` extension

- Your code will be tested using the `Jest Testing Framework` https://intranet.hbtn.io/rltoken/k18kRmC2WpcC_85dA44gBA  https://jestjs.io/

- Your code will be analyzed using the linter `ESLint` along with specific rules that we’ll provide https://intranet.hbtn.io/rltoken/awTYlxNaMZw7HShPeC9D5w  https://eslint.org/

- All of your functions must be exported

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
après résolution problème installation node js
```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

installation error:
```bash
apt install npm
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# nodejs -v
v12.22.9
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# npm -v
Command 'npm' not found, but can be installed with:
apt install npm
```

### Install Jest, Babel, and ESLint
in your project directory:

- Install `Jest` using: `npm install --save-dev jest`

- Install `Babel` using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`

- Install `ESLint` using: `npm install --save-dev eslint`

### Configuration files
Please create the following 3 files (with the provided contents) in the project directory:

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

## Finally…
Don’t forget to run `npm install` from the terminal of your project folder to install all necessary project dependencies. Do not push on your repository the folder node_modules that has been created.

etape `npm install`
```bash
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm install
npm error code EISDIR
npm error syscall read
npm error errno -21
npm error Could not read package.json: Error: EISDIR: illegal operation on a directory, read
npm error A complete log of this run can be found in: /root/.npm/_logs/2024-11-11T12_09_02_468Z-debug-0.log
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm install
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
npm warn deprecated har-validator@5.1.5: this library is no longer supported
npm warn deprecated source-map-resolve@0.5.3: See https://github.com/lydell/source-map-resolve#deprecated
npm warn deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
npm warn deprecated source-map-url@0.4.1: See https://github.com/lydell/source-map-url#deprecated
npm warn deprecated request-promise-native@1.0.9: request-promise-native has been deprecated because it extends the now deprecated request package, see https://github.com/request/request/issues/3142
npm warn deprecated abab@2.0.6: Use your platform's native atob() and btoa() methods instead
npm warn deprecated left-pad@1.3.0: use String.prototype.padStart()
npm warn deprecated w3c-hr-time@1.0.2: Use your platform's native performance.now() and performance.timeOrigin.
npm warn deprecated rimraf@2.6.3: Rimraf versions prior to v4 are no longer supported
npm warn deprecated domexception@1.0.1: Use your platform's native DOMException instead
npm warn deprecated sane@4.1.0: some dependency vulnerabilities fixed, support for node < 10 dropped, and newer ECMAScript syntax/features added
npm warn deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm warn deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm warn deprecated eslint@6.8.0: This version is no longer supported. Please see https://eslint.org/version-support for other options.

added 731 packages, and audited 732 packages in 1m

87 packages are looking for funding
  run `npm fund` for details

37 vulnerabilities (31 moderate, 6 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# nodejs -v
v20.18.0
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm -v
10.8.2
```

root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# nodejs -v
v20.18.0
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm -v
10.8.2


Résultat installation mais erreur 1ère tentative:
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_cl
asses# nodejs -v
v12.22.9
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_cl
asses# npm -v
8.5.1

Résultat installation mais erreur 2ème tentative:
```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

Résultat installation mais erreur 2ème tentative:
```bash
$ nodejs -v
v20.18.0
$ npm -v
10.8.2
```

## Tasks
0. Const or let?

***mandatory***

Modify

	- function `taskFirst` to instantiate variables using `const`

	- function `taskNext` to instantiate variables using `let`

```js
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
```

Execution example:

```bash
bob@dylan:~$ cat 0-main.js
import { taskFirst, taskNext } from './0-constants.js';

console.log(`${taskFirst()} ${taskNext()}`);

bob@dylan:~$
bob@dylan:~$ npm run dev 0-main.js
I prefer const when I can. But sometimes let is okay
bob@dylan:~$
```

***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `0-constants.js`

1. Block Scope

***mandatory***

Given what you’ve read about `var` and hoisting, modify the variables inside the function `taskBlock` so that the variables aren’t overwritten inside the conditional block.

```js
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}
```
Execution:
```bash
bob@dylan:~$ cat 1-main.js
import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));
console.log(taskBlock(false));
bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
[ false, true ]
[ false, true ]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `1-block-scoped.js`


2. Arrow functions

***mandatory***

Rewrite the following standard function to use ES6’s arrow syntax of the function `add` (it will be an anonymous function after)

```js
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = function add(newNeighborhood) {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```
Execution:
```bash
bob@dylan:~$ cat 2-main.js
import getNeighborhoodsList from './2-arrow.js';

const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res);
bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
[ 'SOMA', 'Union Square', 'Noe Valley' ]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `2-arrow.js`


3. Parameter defaults

***mandatory***

Condense the internals of the following function to 1 line - without changing the name of each function/variable.

Hint: The key here to define default parameter values for the function parameters.

```js
export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
  if (expansion1989 === undefined) {
    expansion1989 = 89;
  }

  if (expansion2019 === undefined) {
    expansion2019 = 19;
  }
  return initialNumber + expansion1989 + expansion2019;
}
```
Execution:
```bash
bob@dylan:~$ cat 3-main.js
import getSumOfHoods from './3-default-parameter.js';

console.log(getSumOfHoods(34));
console.log(getSumOfHoods(34, 3));
console.log(getSumOfHoods(34, 3, 4));
bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
142
56
41
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `3-default-parameter.js`


4. Rest parameter syntax for functions

***mandatory***

Modify the following function to return the number of arguments passed to it using the rest parameter syntax
```js
export default function returnHowManyArguments() {

}
Example:

> returnHowManyArguments("Hello", "Holberton", 2020);
3
>
```
Execution:
```bash
bob@dylan:~$ cat 4-main.js
import returnHowManyArguments from './4-rest-parameter.js';

console.log(returnHowManyArguments("one"));
console.log(returnHowManyArguments("one", "two", 3, "4th"));
bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
1
4
bob@dylan:~$
```
**Repo:**

GitHub `repository: holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `4-rest-parameter.js`


5. The wonders of spread syntax

***mandatory***

Using spread syntax, concatenate 2 arrays and each character of a string by modifying the function below. Your function body should be one line long.

```js
export default function concatArrays(array1, array2, string) {
}
```
Execution:
```bash
bob@dylan:~$ cat 5-main.js
import concatArrays from './5-spread-operator.js';

console.log(concatArrays(['a', 'b'], ['c', 'd'], 'Hello'));

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
[
  'a', 'b', 'c',
  'd', 'H', 'e',
  'l', 'l', 'o'
]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `5-spread-operator.js`


6. Take advantage of template literals

***mandatory***

Rewrite the return statement to use a template literal so you can the substitute the variables you’ve defined.

```js
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return 'As of ' + year + ', it was the seventh-highest income county in the United States'
        / ', with a per capita personal income of ' + budget.income + '. As of 2015, San Francisco'
        / ' proper had a GDP of ' + budget.gdp + ', and a GDP per capita of ' + budget.capita + '.';
}
```
Execution:
```bash
bob@dylan:~$ cat 6-main.js
import getSanFranciscoDescription from './6-string-interpolation.js';

console.log(getSanFranciscoDescription());

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js
As of 2017, it was the seventh-highest income county in the United States, with a per capita personal income of $119,868. As of 2015, San Francisco proper had a GDP of $154.2 billion, and a GDP per capita of $178,479.
bob@dylan:~$
```

***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `6-string-interpolation.js`


7. Object property value shorthand syntax

***mandatory***

Notice how the keys and the variable names are the same?

Modify the following function’s `budget` object to simply use the object property value shorthand syntax instead.

```js
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}
```
Execution:

```bash
bob@dylan:~$ cat 7-main.js
import getBudgetObject from './7-getBudgetObject.js';

console.log(getBudgetObject(400, 700, 900));

bob@dylan:~$
bob@dylan:~$ npm run dev 7-main.js
{ income: 400, gdp: 700, capita: 900 }
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `7-getBudgetObject.js`


8. No need to create empty objects before adding in properties

***mandatory***

Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names on the `budget` object

```js
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear()}`] = income;
  budget[`gdp-${getCurrentYear()}`] = gdp;
  budget[`capita-${getCurrentYear()}`] = capita;

  return budget;
}
```
Execution:
```bash
bob@dylan:~$ cat 8-main.js
import getBudgetForCurrentYear from './8-getBudgetCurrentYear.js';

console.log(getBudgetForCurrentYear(2100, 5200, 1090));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js
{ 'income-2021': 2100, 'gdp-2021': 5200, 'capita-2021': 1090 }
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `8-getBudgetCurrentYear.js`


9. ES6 method properties

***mandatory***

Rewrite `getFullBudgetObject` to use ES6 method properties in the `fullBudget` object

```js
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars: function (income) {
      return `$${income}`;
    },
    getIncomeInEuros: function (income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
```
Execution:
```bash
bob@dylan:~$ cat 9-main.js
import getFullBudgetObject from './9-getFullBudget.js';

const fullBudget = getFullBudgetObject(20, 50, 10);

console.log(fullBudget.getIncomeInDollars(fullBudget.income));
console.log(fullBudget.getIncomeInEuros(fullBudget.income));

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js
$20
20 euros
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `9-getFullBudget.js`


10. For...of Loops

***mandatory***

Rewrite the function `appendToEachArrayValue` to use ES6’s `for...of` operator. And don’t forget that `var` is not ES6-friendly.

```js
export default function appendToEachArrayValue(array, appendString) {
  for (var idx in array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
```
Execution:
```bash
bob@dylan:~$ cat 10-main.js
import appendToEachArrayValue from './10-loops.js';

console.log(appendToEachArrayValue(['appended', 'fixed', 'displayed'], 'correctly-'));

bob@dylan:~$
bob@dylan:~$ npm run dev 10-main.js
[ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ]
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `10-loops.js`


11. Iterator

***mandatory***

Write a function named `createEmployeesObject` that will receive two arguments:

   - `departmentName` (String)

   - `employees` (Array of Strings)
```js
export default function createEmployeesObject(departmentName, employees) {

}
The function should return an object with the following format:

{
     $departmentName: [
          $employees,
     ],
}
```
Execution:
```bash
bob@dylan:~$ cat 11-main.js
import createEmployeesObject from './11-createEmployeesObject.js';

console.log(createEmployeesObject("Software", [ "Bob", "Sylvie" ]));

bob@dylan:~$
bob@dylan:~$ npm run dev 11-main.js
{ Software: [ 'Bob', 'Sylvie' ] }
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `11-createEmployeesObject.js`


12. Let's create a report object

***mandatory***

Write a function named `createReportObject` whose parameter, `employeesList`, is the return value of the previous function `createEmployeesObject`.

```js
export default function createReportObject(employeesList) {

}
createReportObject should return an object containing the key `allEmployees` and a method property called `getNumberOfDepartments`.

`allEmployees` is a key that maps to an object containing the department name and a list of all the employees in that department. If you’re having trouble, use the spread syntax.

The method property receives `employeesList` and returns the number of departments. I would suggest suggest thinking back to the ES6 method property syntax.

{
  allEmployees: {
     engineering: [
          'John Doe',
          'Guillaume Salva',
     ],
  },
};
```
Execution:
```bash
bob@dylan:~$ cat 12-main.js
import createEmployeesObject from './11-createEmployeesObject.js';
import createReportObject from './12-createReportObject.js';

const employees = {
    ...createEmployeesObject('engineering', ['Bob', 'Jane']),
    ...createEmployeesObject('marketing', ['Sylvie'])
};

const report = createReportObject(employees);
console.log(report.allEmployees);
console.log(report.getNumberOfDepartments(report.allEmployees));

bob@dylan:~$
bob@dylan:~$ npm run dev 12-main.js
{ engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] }
2
bob@dylan:~$
```
***Repo:***

GitHub repository: `holbertonschool-web_back_end`

Directory: `ES6_basic`

File: `12-createReportObject.js`


```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

```bash
$ nodejs -v
v12.22.9
$ npm -v
8.5.1
```

## Problème installation:
erreur installation:
```bash
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_classes#
 cd ..
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# ls
ES6_basic  ES6_classes  README.md
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# cd ES6_basic/
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic#ll
s
0-constants.js               12-createReportObject.js  5-spread-operator.js       9-getFullBudget.js
1-block-scoped.js            2-arrow.js                6-string-interpolation.js  README.md
10-loops.js                  3-default-parameter.js    7-getBudgetObject.js
11-createEmployeesObject.js  4-rest-parameter.js       8-getBudgetCurrentYear.js
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic#cc
d ..
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
2024-11-11 01:29:29 - Installing pre-requisites
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Get:5 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [1911 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [913 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security InRelease [106 kB]
Err:7 http://security.ubuntu.com/ubuntu xenial-security InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
Reading package lists... Done
W: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
E: The repository 'http://security.ubuntu.com/ubuntu xenial-security InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
2024-11-11 01:29:34 - Error: Failed to run 'apt-get update' (Exit Code: 0)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  htop
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libjs-highlight.js libnode72 nodejs-doc
Suggested packages:
  npm
The following NEW packages will be installed:
  libjs-highlight.js libnode72 nodejs nodejs-doc
0 upgraded, 4 newly installed, 0 to remove and 1 not upgraded.
Need to get 13.7 MB of archives.
After this operation, 53.8 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-highlight.js all 9.18.5+dfsg1-1 [367 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libnode72 amd64 12.22.9~dfsg-1ubuntu3.6 [10.8 MB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 nodejs-doc all 12.22.9~dfsg-1ubuntu3.6 [2411 kB]
Setting up nodejs (12.22.9~dfsg-1ubuntu3.6) ...
update-alternatives: using /usr/bin/nodejs to provide /usr/bin/js (js) in auto mode
Setting up nodejs-doc (12.22.9~dfsg-1ubuntu3.6) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# nodejs -v
v12.22.9
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# npm -v
Command 'npm' not found, but can be installed with:
apt install npm
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# npm install --save-dev jest
Command 'npm' not found, but can be installed with:
apt install npm
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end# cd ES6_basic/
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic#ll
s
0-constants.js               12-createReportObject.js  5-spread-operator.js       9-getFullBudget.js
1-block-scoped.js            2-arrow.js                6-string-interpolation.js  README.md
10-loops.js                  3-default-parameter.js    7-getBudgetObject.js
11-createEmployeesObject.js  4-rest-parameter.js       8-getBudgetCurrentYear.js
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic# npm install --save-dev jest
Command 'npm' not found, but can be installed with:
apt install npm
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic#aa
pt install npm
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  htop
Use 'apt autoremove' to remove it.
The following additional packages will be installed:
  gyp libjs-events libjs-inherits libjs-is-typedarray libjs-psl libjs-source-map libjs-sprintf-js
  libjs-typedarray-to-buffer libnode-dev libnotify-bin libnotify4 libuv1-dev node-abab node-abbrev
  node-agent-base node-ansi-regex node-ansi-styles node-ansistyles node-aproba node-archy
  node-are-we-there-yet node-argparse node-arrify node-asap node-asynckit node-balanced-match
  node-brace-expansion node-builtins node-cacache node-chalk node-chownr node-clean-yaml-object
  node-cli-table node-clone node-color-convert node-color-name node-colors node-columnify
  node-combined-stream node-commander node-console-control-strings node-copy-concurrently node-core-util-is
  node-coveralls node-cssom node-cssstyle node-debug node-decompress-response node-defaults
  node-delayed-stream node-delegates node-depd node-diff node-encoding node-end-of-stream node-err-code
  node-escape-string-regexp node-esprima node-events node-fancy-log node-fetch node-foreground-child
  node-form-data node-fs-write-stream-atomic node-fs.realpath node-function-bind node-gauge node-get-stream
  node-glob node-got node-graceful-fs node-growl node-gyp node-has-flag node-has-unicode
  node-hosted-git-info node-https-proxy-agent node-iconv-lite node-iferr node-imurmurhash node-indent-string
  node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer node-is-plain-obj
  node-is-typedarray node-isarray node-isexe node-js-yaml node-jsdom node-json-buffer
  node-json-parse-better-errors node-jsonparse node-kind-of node-lcov-parse node-lodash-packages
  node-log-driver node-lowercase-keys node-lru-cache node-mime node-mime-types node-mimic-response
  node-minimatch node-minimist node-minipass node-mkdirp node-move-concurrently node-ms node-mute-stream
  node-negotiator node-nopt node-normalize-package-data node-npm-bundled node-npm-package-arg node-npmlog
  node-object-assign node-once node-opener node-osenv node-p-cancelable node-p-map node-path-is-absolute
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-psl node-pump
  node-punycode node-quick-lru node-read node-read-package-json node-readable-stream node-resolve node-retry
  node-rimraf node-run-queue node-safe-buffer node-semver node-set-blocking node-signal-exit node-slash
  node-slice-ansi node-source-map node-source-map-support node-spdx-correct node-spdx-exceptions
  node-spdx-expression-parse node-spdx-license-ids node-sprintf-js node-ssri node-stack-utils
  node-stealthy-require node-string-decoder node-string-width node-strip-ansi node-supports-color node-tap
  node-tap-mocha-reporter node-tap-parser node-tar node-text-table node-time-stamp node-tmatch
  node-tough-cookie node-typedarray-to-buffer node-unique-filename node-universalify node-util-deprecate
  node-validate-npm-package-license node-validate-npm-package-name node-wcwidth.js node-webidl-conversions
  node-whatwg-fetch node-which node-wide-align node-wrappy node-write-file-atomic node-ws node-yallist
Suggested packages:
  libjs-angularjs gnome-shell | notification-daemon node-nyc
The following NEW packages will be installed:
  gyp libjs-events libjs-inherits libjs-is-typedarray libjs-psl libjs-source-map libjs-sprintf-js
  libjs-typedarray-to-buffer libnode-dev libnotify-bin libnotify4 libuv1-dev node-abab node-abbrev
  node-agent-base node-ansi-regex node-ansi-styles node-ansistyles node-aproba node-archy
  node-are-we-there-yet node-argparse node-arrify node-asap node-asynckit node-balanced-match
  node-brace-expansion node-builtins node-cacache node-chalk node-chownr node-clean-yaml-object
  node-cli-table node-clone node-color-convert node-color-name node-colors node-columnify
  node-combined-stream node-commander node-console-control-strings node-copy-concurrently node-core-util-is
  node-coveralls node-cssom node-cssstyle node-debug node-decompress-response node-defaults
  node-delayed-stream node-delegates node-depd node-diff node-encoding node-end-of-stream node-err-code
  node-escape-string-regexp node-esprima node-events node-fancy-log node-fetch node-foreground-child
  node-form-data node-fs-write-stream-atomic node-fs.realpath node-function-bind node-gauge node-get-stream
  node-glob node-got node-graceful-fs node-growl node-gyp node-has-flag node-has-unicode
  node-hosted-git-info node-https-proxy-agent node-iconv-lite node-iferr node-imurmurhash node-indent-string
  node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer node-is-plain-obj
  node-is-typedarray node-isarray node-isexe node-js-yaml node-jsdom node-json-buffer
  node-json-parse-better-errors node-jsonparse node-kind-of node-lcov-parse node-lodash-packages
  node-log-driver node-lowercase-keys node-lru-cache node-mime node-mime-types node-mimic-response
  node-minimatch node-minimist node-minipass node-mkdirp node-move-concurrently node-ms node-mute-stream
  node-negotiator node-nopt node-normalize-package-data node-npm-bundled node-npm-package-arg node-npmlog
  node-object-assign node-once node-opener node-osenv node-p-cancelable node-p-map node-path-is-absolute
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-psl node-pump
  node-punycode node-quick-lru node-read node-read-package-json node-readable-stream node-resolve node-retry
  node-rimraf node-run-queue node-safe-buffer node-semver node-set-blocking node-signal-exit node-slash
  node-slice-ansi node-source-map node-source-map-support node-spdx-correct node-spdx-exceptions
  node-spdx-expression-parse node-spdx-license-ids node-sprintf-js node-ssri node-stack-utils
  node-stealthy-require node-string-decoder node-string-width node-strip-ansi node-supports-color node-tap
  node-tap-mocha-reporter node-tap-parser node-tar node-text-table node-time-stamp node-tmatch
  node-tough-cookie node-typedarray-to-buffer node-unique-filename node-universalify node-util-deprecate
  node-validate-npm-package-license node-validate-npm-package-name node-wcwidth.js node-webidl-conversions
  node-whatwg-fetch node-which node-wide-align node-wrappy node-write-file-atomic node-ws node-yallist npm
0 upgraded, 184 newly installed, 0 to remove and 1 not upgraded.
Need to get 5103 kB of archives.
After this operation, 36.4 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 gyp all 0.1+20210831gitd6c5dd5-5 [238 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-events all 3.3.0+~3.0.0-2 [9734 B]
Get:3 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-is-typedarray all 1.0.0-4 [3804 B]
Get:4 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-psl all 1.8.0+ds-6 [76.3 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-sprintf-js all 1.1.2+ds1+~1.1.2-1 [12.8 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-typedarray-to-buffer all 4.0.0-2 [4658 B]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libuv1-dev amd64 1.43.0-1ubuntu0.1 [130 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libnode-dev amd64 12.22.9~dfsg-1ubuntu3.6 [609 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnotify4 amd64 0.7.9-3ubuntu5.22.04.1 [20.3 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnotify-bin amd64 0.7.9-3ubuntu5.22.04.1 [7560 B]
Get:11 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-abab all 2.0.5-2 [6578 B]
Get:12 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ms all 2.1.3+~cs0.7.31-2 [5782 B]
Get:13 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-debug all 4.3.2+~cs4.1.7-1 [17.6 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-yallist all 4.0.0+~4.0.1-1 [8322 B]
Get:15 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-lru-cache all 6.0.0+~5.1.1-1 [11.3 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-semver all 7.3.5+~7.3.8-1 [41.5 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-agent-base all 6.0.2+~cs5.4.2-1 [17.9 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansi-regex all 5.0.1-1 [4984 B]
Get:19 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansistyles all 0.1.3-5 [4546 B]
Get:20 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-aproba all 2.0.0-2 [5620 B]
Get:21 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-delegates all 1.0.0-3 [4280 B]
Get:22 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-inherits all 2.0.4-4 [3468 B]
Get:23 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-inherits all 2.0.4-4 [3010 B]
Get:24 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-core-util-is all 1.0.3-1 [4066 B]
Get:25 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-safe-buffer all 5.2.1+~cs2.1.2-2 [15.7 kB]
Get:26 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-string-decoder all 1.3.0-5 [7046 B]
Get:27 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-process-nextick-args all 2.0.1-2 [3730 B]
Get:28 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-util-deprecate all 1.0.2-3 [4202 B]
Get:29 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-isarray all 2.0.5-3 [3934 B]
Get:30 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-readable-stream all 3.6.0+~cs3.0.0-1 [32.6 kB]
Get:31 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-are-we-there-yet all 3.0.0+~1.1.0-1 [8920 B]
Get:32 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-arrify all 2.0.1-2 [3610 B]
Get:33 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-asap all 2.0.6+~2.0.0-1 [14.4 kB]
Get:34 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-asynckit all 0.4.0-4 [10.6 kB]
Get:35 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-builtins all 4.0.0-1 [3860 B]
Get:36 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-chownr all 2.0.0-1 [4404 B]
Get:37 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-fs.realpath all 1.0.0-2 [6106 B]
Get:38 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-wrappy all 1.0.2-2 [3658 B]
Get:39 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-once all 1.4.0-4 [4708 B]
Get:40 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-inflight all 1.0.6-2 [3940 B]
Get:41 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-balanced-match all 2.0.0-1 [4910 B]
Get:42 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-brace-expansion all 2.0.1-1 [7458 B]
Get:43 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-minimatch all 3.1.1+~3.0.5-1 [16.9 kB]
Get:44 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-path-is-absolute all 2.0.0-2 [4062 B]
Get:45 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-glob all 7.2.1+~cs7.6.15-1 [131 kB]
Get:46 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-graceful-fs all 4.2.4+repack-1 [12.5 kB]
Get:47 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-mkdirp all 1.0.4+~1.0.2-1 [11.4 kB]
Get:48 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-iferr all 1.0.2+~1.0.2-1 [4610 B]
Get:49 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-imurmurhash all 0.1.4+dfsg+~0.1.1-1 [8510 B]
Get:50 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-fs-write-stream-atomic all 1.0.10-5 [5256 B]
Get:51 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-rimraf all 3.0.2-1 [10.1 kB]
Get:52 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-run-queue all 2.0.0-2 [5092 B]
Get:53 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-copy-concurrently all 1.0.5-8 [7118 B]
Get:54 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-move-concurrently all 1.0.1-4 [5120 B]
Get:55 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-escape-string-regexp all 4.0.0-2 [4328 B]
Get:56 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-indent-string all 4.0.0-2 [4122 B]
Get:57 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-p-map all 4.0.0+~3.1.0+~3.0.1-1 [8058 B]
Get:58 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-promise-inflight all 1.0.1+~1.0.0-1 [4896 B]
Get:59 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ssri all 8.0.1-2 [19.6 kB]
Get:60 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-unique-filename all 1.1.1+ds-1 [3832 B]
Get:61 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-cacache all 15.0.5+~cs13.9.21-3 [34.9 kB]
Get:62 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-clean-yaml-object all 0.1.0-5 [4718 B]
Get:63 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-clone all 2.1.2-3 [8344 B]
Get:64 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-color-name all 1.1.4+~1.1.1-2 [6076 B]
Get:65 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-color-convert all 2.0.1-1 [10.2 kB]
Get:66 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-colors all 1.4.0-3 [12.3 kB]
Get:67 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-strip-ansi all 6.0.1-1 [4184 B]
Get:68 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-defaults all 1.0.3+~1.0.3-1 [4288 B]
Get:69 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-wcwidth.js all 1.0.2-1 [7278 B]
Get:70 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-columnify all 1.5.4+~1.5.1-1 [12.6 kB]
Get:71 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-console-control-strings all 1.1.0-2 [5428 B]
Get:72 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-growl all 1.10.5-4 [7064 B]
Get:73 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-sprintf-js all 1.1.2+ds1+~1.1.2-1 [3916 B]
Get:74 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-argparse all 2.0.1-2 [33.2 kB]
Get:75 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-esprima all 4.0.1+ds+~4.0.3-2 [69.3 kB]
Get:76 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-js-yaml all 4.1.0+dfsg+~4.0.5-6 [62.7 kB]
Get:77 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-lcov-parse all 1.0.0+20170612git80d039574ed9-5 [5084 B]
Get:78 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-log-driver all 1.2.7+git+20180219+bba1761737-7 [5436 B]
Get:79 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-plain-obj all 3.0.0-2 [3994 B]
Get:80 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-buffer all 2.0.5-2 [4128 B]
Get:81 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-kind-of all 6.0.3+dfsg-2 [8628 B]
Get:82 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-minimist all 1.2.5+~cs5.3.2-1 [9434 B]
Get:83 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-cssom all 0.4.4-3 [14.1 kB]
Get:84 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-cssstyle all 2.3.0-2 [30.3 kB]
Get:85 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-delayed-stream all 1.0.0-5 [5464 B]
Get:86 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-combined-stream all 1.0.8+~1.0.3-1 [7432 B]
Get:87 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-mime all 3.0.0+dfsg+~cs3.96.1-1 [38.1 kB]
Get:88 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-mime-types all 2.1.33-1 [6944 B]
Get:89 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-form-data all 3.0.1-1 [13.4 kB]
Get:90 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-events all 3.3.0+~3.0.0-2 [3090 B]
Get:91 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-https-proxy-agent all 5.0.0+~cs8.0.0-3 [16.4 kB]
Get:92 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-iconv-lite all 0.6.3-2 [167 kB]
Get:93 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-lodash-packages all 4.17.21+dfsg+~cs8.31.198.20210220-5 [166 kB]
Get:94 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-stealthy-require all 1.1.1-5 [7176 B]
Get:95 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-punycode all 2.1.1-5 [9902 B]
Get:96 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-psl all 1.8.0+ds-6 [39.6 kB]
Get:97 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-universalify all 2.0.0-3 [4266 B]
Get:98 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tough-cookie all 4.0.0-2 [31.7 kB]
Get:99 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-webidl-conversions all 7.0.0~1.1.0+~cs15.1.20180823-2 [27.5 kB]
Get:100 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-commander all 9.0.0-2 [48.0 kB]
Get:101 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-mute-stream all 0.0.8+~0.0.1-1 [6448 B]
Get:102 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-read all 1.0.7-3 [5478 B]
Get:103 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ws all 8.5.0+~cs13.3.3-2 [49.5 kB]
Get:104 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-jsdom all 19.0.0+~cs90.11.27-1 [446 kB]
Get:105 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-fetch all 2.6.7+~2.5.12-1 [27.1 kB]
Get:106 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-coveralls all 3.1.1-1 [14.2 kB]
Get:107 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-mimic-response all 3.1.0-7 [5430 B]
Get:108 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-decompress-response all 6.0.0-2 [4656 B]
Get:109 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-diff all 5.0.0~dfsg+~5.0.1-3 [77.4 kB]
Get:110 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-err-code all 2.0.3+dfsg-3 [4918 B]
Get:111 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-time-stamp all 2.2.0-1 [5984 B]
Get:112 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-fancy-log all 1.3.3+~cs1.3.1-2 [8102 B]
Get:113 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-signal-exit all 3.0.6+~3.0.1-1 [7000 B]
Get:114 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-foreground-child all 2.0.0-3 [5542 B]
Get:115 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-function-bind all 1.1.1+repacked+~1.0.3-1 [5244 B]
Get:116 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-has-unicode all 2.0.1-4 [3948 B]
Get:117 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansi-styles all 4.3.0+~4.2.0-1 [8968 B]
Get:118 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-slice-ansi all 5.0.0+~cs9.0.0-4 [8044 B]
Get:119 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-string-width all 4.2.3+~cs13.2.3-1 [11.4 kB]
Get:120 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-wide-align all 1.1.3-4 [4228 B]
Get:121 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-gauge all 4.0.2-1 [16.3 kB]
Get:122 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-end-of-stream all 1.4.4+~1.4.1-1 [5340 B]
Get:123 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-pump all 3.0.0-5 [5160 B]
Get:124 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-get-stream all 6.0.1-1 [7324 B]
Get:125 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-lowercase-keys all 2.0.0-2 [3754 B]
Get:126 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-json-buffer all 3.0.1-1 [3812 B]
Get:127 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-p-cancelable all 2.1.1-1 [7358 B]
Get:128 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-quick-lru all 5.1.1-1 [5532 B]
Get:129 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-got all 11.8.3+~cs58.7.37-1 [122 kB]
Get:130 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-has-flag all 4.0.0-2 [4228 B]
Get:131 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-hosted-git-info all 4.0.2-1 [9006 B]
Get:132 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ip all 1.1.5+~1.1.0-1 [8140 B]
Get:133 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ip-regex all 4.3.0+~4.1.1-1 [5254 B]
Get:134 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-typedarray all 1.0.0-4 [2072 B]
Get:135 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-isexe all 2.0.0+~2.0.1-4 [6102 B]
Get:136 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-json-parse-better-errors all 1.0.2+~cs3.3.1-1 [7328 B]
Get:137 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-encoding all 0.1.13-2 [4366 B]
Get:138 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-jsonparse all 1.3.1-10 [8060 B]
Get:139 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-minipass all 3.1.6+~cs8.7.18-1 [32.9 kB]
Get:140 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-npm-bundled all 1.1.2-1 [6228 B]
Get:141 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-osenv all 0.1.5+~0.1.0-1 [5896 B]
Get:142 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-validate-npm-package-name all 3.0.0-4 [5058 B]
Get:143 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-npm-package-arg all 8.1.5-1 [8132 B]
Get:144 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-object-assign all 4.1.1-6 [4754 B]
Get:145 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-opener all 1.5.2+~1.4.0-1 [6000 B]
Get:146 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-retry all 0.13.1+~0.12.1-1 [11.5 kB]
Get:147 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-promise-retry all 2.0.1-2 [5010 B]
Get:148 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-promzard all 0.3.0-2 [6888 B]
Get:149 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-set-blocking all 2.0.0-2 [3766 B]
Get:150 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-slash all 3.0.0-2 [3922 B]
Get:151 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-source-map all 0.7.0++dfsg2+really.0.6.1-9 [93.9 kB]
Get:152 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-source-map all 0.7.0++dfsg2+really.0.6.1-9 [33.6 kB]
Get:153 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-source-map-support all 0.5.21+ds+~0.5.4-1 [14.2 kB]
Get:154 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-license-ids all 3.0.11-1 [7306 B]
Get:155 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-exceptions all 2.3.0-2 [3978 B]
Get:156 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-expression-parse all 3.0.1+~3.0.1-1 [7658 B]
Get:157 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-correct all 3.1.1-2 [5476 B]
Get:158 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-stack-utils all 2.0.5+~2.0.1-1 [9368 B]
Get:159 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-supports-color all 8.1.1+~8.1.1-1 [7048 B]
Get:160 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap-parser all 7.0.0+ds1-6 [19.4 kB]
Get:161 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap-mocha-reporter all 3.0.7+ds-2 [39.2 kB]
Get:162 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-text-table all 0.2.0-4 [4762 B]
Get:163 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tmatch all 5.0.0-4 [6002 B]
Get:164 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-typedarray-to-buffer all 4.0.0-2 [2242 B]
Get:165 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-validate-npm-package-license all 3.0.4-2 [4252 B]
Get:166 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-whatwg-fetch all 3.6.2-5 [15.0 kB]
Get:167 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-write-file-atomic all 3.0.3+~3.0.2-1 [7690 B]
Get:168 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-abbrev all 1.1.1+~1.1.2-1 [5784 B]
Get:169 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-archy all 1.0.0-4 [4728 B]
Get:170 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-chalk all 4.1.2-1 [15.9 kB]
Get:171 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-cli-table all 0.3.11+~cs0.13.3-1 [23.2 kB]
Get:172 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-depd all 2.0.0-2 [10.5 kB]
Get:173 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-nopt all 5.0.0-2 [11.3 kB]
Get:174 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-npmlog all 6.0.1+~4.1.4-1 [9968 B]
Get:175 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tar all 6.1.11+ds1+~cs6.0.6-1 [38.8 kB]
Get:176 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-which all 2.0.2+~cs1.3.2-2 [7374 B]
Get:177 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-gyp all 8.4.1-1 [34.7 kB]
Get:178 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-ini all 2.0.1-1 [6528 B]
Get:179 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-negotiator all 0.6.2+~0.6.1-1 [10.3 kB]
Get:180 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-resolve all 1.20.0+~cs5.27.9-1 [20.7 kB]
Get:181 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-normalize-package-data all 3.0.3+~2.4.1-1 [12.8 kB]
Get:182 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-read-package-json all 4.1.1-1 [10.4 kB]
Get:183 http://archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap all 12.0.1+ds-4 [43.6 kB]
Setting up node-gyp (8.4.1-1) ...
Setting up npm (8.5.1~ds-1) ...
Setting up node-coveralls (3.1.1-1) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic# npm -v
8.5.1
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic# npm install --save-dev jest
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/core@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/types@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-cli@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/console@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/reporters@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/test-result@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/transform@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-changed-files@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-config@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-haste-map@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-message-util@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-regex-util@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-resolve@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-resolve-dependencies@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-runner@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-runtime@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-snapshot@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-util@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-validate@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-watcher@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'pretty-format@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-worker@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/schemas@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'create-jest@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/test-sequencer@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-jest@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-circus@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-environment-node@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-get-type@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-preset-jest@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-plugin-jest-hoist@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/environment@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/expect@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-each@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-matcher-utils@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/fake-timers@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-mock@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'expect@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/expect-utils@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-diff@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'diff-sequences@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-docblock@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-leak-detector@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/globals@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/source-map@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm ERR! code EISDIR
npm ERR! syscall open
npm ERR! path /mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json
npm ERR! errno -21
npm ERR! EISDIR: illegal operation on a directory, open '/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json'

npm ERR! A complete log of this run can be found in:
npm ERR!     /root/.npm/_logs/2024-11-11T00_37_28_278Z-debug-0.log
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic# npm install --save-dev babel-jest @babel/core @babel/preset-env
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/schemas@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/transform@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@jest/types@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-plugin-jest-hoist@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-preset-jest@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-haste-map@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-regex-util@29.6.3',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-util@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'jest-worker@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'babel-jest@29.7.0',
npm WARN EBADENGINE   required: { node: '^14.15.0 || ^16.10.0 || >=18.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm ERR! code EISDIR
npm ERR! syscall open
npm ERR! path /mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json
npm ERR! errno -21
npm ERR! EISDIR: illegal operation on a directory, open '/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json'

npm ERR! A complete log of this run can be found in:
npm ERR!     /root/.npm/_logs/2024-11-11T00_38_06_021Z-debug-0.log
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic#
npm install --save-dev eslint
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint@9.14.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/config-array@0.18.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/core@0.7.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/eslintrc@3.1.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/js@9.14.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/plugin-kit@0.2.2',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@humanfs/node@0.16.6',
npm WARN EBADENGINE   required: { node: '>=18.18.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@humanwhocodes/retry@0.4.1',
npm WARN EBADENGINE   required: { node: '>=18.18' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint-scope@8.2.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint-visitor-keys@4.2.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'espree@10.3.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'file-entry-cache@8.0.0',
npm WARN EBADENGINE   required: { node: '>=16.0.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/object-schema@2.1.4',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'globals@14.0.0',
npm WARN EBADENGINE   required: { node: '>=18' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@humanfs/core@0.19.1',
npm WARN EBADENGINE   required: { node: '>=18.18.0' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@humanwhocodes/retry@0.3.1',
npm WARN EBADENGINE   required: { node: '>=18.18' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'flat-cache@4.0.1',
npm WARN EBADENGINE   required: { node: '>=16' },
npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
npm WARN EBADENGINE }
npm ERR! code EISDIR
npm ERR! syscall open
npm ERR! path /mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json
npm ERR! errno -21
npm ERR! EISDIR: illegal operation on a directory, open '/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_basic/package.json'

npm ERR! A complete log of this run can be found in:
npm ERR!     /root/.npm/_logs/2024-11-11T00_38_33_104Z-debug-0.log
```




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
## Résolution installation:
sic# curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
2024-11-11 12:32:09 - Installing pre-requisites
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Hit:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:4 http://security.ubuntu.com/ubuntu xenial-security InRelease [106 kB]
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Get:6 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [1930 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2148 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [308 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [2569 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [444 kB]
Err:4 http://security.ubuntu.com/ubuntu xenial-security InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
Get:11 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [913 kB]
Get:12 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [181 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [367 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [455 kB]
Reading package lists... Done
W: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
E: The repository 'http://security.ubuntu.com/ubuntu xenial-security InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
W: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
E: The repository 'http://security.ubuntu.com/ubuntu xenial-security InRelease' is not signed.
W: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
W: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures coulW: GPG error: http://security.ubuntu.com/ubuntu xenial-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5 NO_PUBKEY 3B4FE6ACC0B21F32
E: The repository 'http://security.ubuntu.com/ubuntu xenial-security InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
2024-11-11 12:32:13 - Error: Failed to run 'apt-get update' (Exit Code: 0)
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
Executing: /tmp/apt-key-gpghome.QpAiLoIWb9/gpg.1.sh --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
gpg: key 40976EAF437D05B5: public key "Ubuntu Archive Automatic Signing Key <ftpmaster@ubuntu.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
Executing: /tmp/apt-key-gpghome.RRPIOWTt36/gpg.1.sh --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
gpg: key 3B4FE6ACC0B21F32: public key "Ubuntu Archive Automatic Signing Key (2012) <ftpmaster@ubuntu.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease
Get:5 http://security.ubuntu.com/ubuntu xenial-security InRelease [106 kB]
Get:6 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [913 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security/main Translation-en [211 kB]
Fetched 1230 kB in 1s (856 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
5 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# node -v
v12.22.9
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo bash nodesource_setup.sh
sudo apt install nodejs -y
2024-11-11 12:38:57 - Installing pre-requisites
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20240203~22.04.1).
ca-certificates set to manually installed.
curl is already the newest version (7.81.0-1ubuntu1.18).
gnupg is already the newest version (2.2.27-3ubuntu2.1).
gnupg set to manually installed.
The following package was automatically installed and is no longer required:
  htop
Use 'sudo apt autoremove' to remove it.
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 5 not upgraded.
Need to get 1510 B of archives.
After this operation, 170 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 apt-transport-https all 2.4.13 [1510 B]
Fetched 1510 B in 0s (6520 B/s)
Selecting previously unselected package apt-transport-https.
(Reading database ... 103553 files and directories currently installed.)
Preparing to unpack .../apt-transport-https_2.4.13_all.deb ...
Unpacking apt-transport-https (2.4.13) ...
Setting up apt-transport-https (2.4.13) ...
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Get:6 https://deb.nodesource.com/node_20.x nodistro InRelease [12.1 kB]
Get:7 https://deb.nodesource.com/node_20.x nodistro/main amd64 Packages [9577 B]
Fetched 21.7 kB in 1s (41.5 kB/s)
Reading package lists... Done
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
2024-11-11 12:39:02 - Repository configured successfully.
2024-11-11 12:39:02 - To install Node.js, run: apt-get install nodejs -y
2024-11-11 12:39:02 - You can use N|solid Runtime as a node.js alternative
2024-11-11 12:39:02 - To install N|solid Runtime, run: apt-get install nsolid -y

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gyp htop libjs-events libjs-highlight.js libjs-inherits libjs-is-typedarray libjs-psl
  libjs-source-map libjs-sprintf-js libjs-typedarray-to-buffer libnode-dev libnode72 libnotify-bin
  libnotify4 libuv1-dev node-abab node-abbrev node-agent-base node-ansi-regex node-ansi-styles
  node-ansistyles node-aproba node-archy node-are-we-there-yet node-argparse node-arrify node-asap
  node-asynckit node-balanced-match node-brace-expansion node-builtins node-chalk node-chownr
  node-clean-yaml-object node-cli-table node-clone node-color-convert node-color-name node-colors
  node-columnify node-combined-stream node-commander node-console-control-strings node-core-util-is
  node-cssom node-cssstyle node-debug node-decompress-response node-defaults node-delayed-stream
  node-delegates node-depd node-diff node-encoding node-end-of-stream node-err-code
  node-escape-string-regexp node-events node-fancy-log node-foreground-child
  node-fs-write-stream-atomic node-fs.realpath node-function-bind node-gauge node-get-stream node-glob
Removing npm (8.5.1~ds-1) ...
Removing node-cacache (15.0.5+~cs13.9.21-3) ...
Removing node-move-concurrently (1.0.1-4) ...
Removing node-copy-concurrently (1.0.5-8) ...
Removing node-coveralls (3.1.1-1) ...
Removing node-tap (12.0.1+ds-4) ...
Removing node-tap-mocha-reporter (3.0.7+ds-2) ...
Removing node-tap-parser (7.0.0+ds1-6) ...
Removing node-js-yaml (4.1.0+dfsg+~4.0.5-6) ...
Removing node-esprima (4.0.1+ds+~4.0.3-2) ...
Removing node-fetch (2.6.7+~2.5.12-1) ...
Removing node-jsdom (19.0.0+~cs90.11.27-1) ...
Removing node-form-data (3.0.1-1) ...
Removing node-gyp (8.4.1-1) ...
Removing node-mime-types (2.1.33-1) ...
Removing node-mime (3.0.0+dfsg+~cs3.96.1-1) ...
Removing node-tar (6.1.11+ds1+~cs6.0.6-1) ...
Removing node-mkdirp (1.0.4+~1.0.2-1) ...
Removing node-nopt (5.0.0-2) ...
Removing node-opener (1.5.2+~1.4.0-1) ...
Removing node-which (2.0.2+~cs1.3.2-2) ...
Removing node-ws (8.5.0+~cs13.3.3-2) ...
Removing nodejs-doc (12.22.9~dfsg-1ubuntu3.6) ...
(Reading database ... 101319 files and directories currently installed.)
Preparing to unpack .../nodejs_20.18.0-1nodesource1_amd64.deb ...
Unpacking nodejs (20.18.0-1nodesource1) over (12.22.9~dfsg-1ubuntu3.6) ...
dpkg: error processing archive /var/cache/apt/archives/nodejs_20.18.0-1nodesource1_amd64.deb (--unpack):
 trying to overwrite '/usr/include/node/common.gypi', which is also in package libnode-dev 12.22.9~dfsg-1ubuntu3.6
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/nodejs_20.18.0-1nodesource1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# node -v
v12.22.9
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo apt-get remove --purge nodejs npm -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gyp htop libjs-events libjs-highlight.js libjs-inherits libjs-is-typedarray libjs-psl
  libjs-source-map libjs-sprintf-js libjs-typedarray-to-buffer libnode-dev libnode72 libnotify-bin
  libnotify4 libuv1-dev node-abbrev node-ansi-regex node-ansi-styles node-ansistyles
  node-are-we-there-yet node-arrify node-asap node-asynckit node-balanced-match node-brace-expansion
  node-chownr node-clean-yaml-object node-color-convert node-color-name node-commander
  node-core-util-is node-decompress-response node-delayed-stream node-delegates node-depd node-diff
  node-encoding node-end-of-stream node-err-code node-escape-string-regexp node-fancy-log
  node-foreground-child node-fs.realpath node-function-bind node-get-stream node-glob node-growl
  node-has-flag node-has-unicode node-hosted-git-info node-iconv-lite node-iferr node-imurmurhash
  node-indent-string node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer
  node-is-plain-obj node-is-typedarray node-isarray node-isexe node-json-parse-better-errors
  node-jsonparse node-kind-of node-lodash-packages node-lowercase-keys node-lru-cache
  node-mimic-response node-minimatch node-minimist node-minipass node-mute-stream node-negotiator
  node-npm-bundled node-once node-osenv node-p-cancelable node-p-map node-path-is-absolute
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-pump
  node-quick-lru node-read node-readable-stream node-resolve node-retry node-safe-buffer
  node-set-blocking node-signal-exit node-slash node-slice-ansi node-source-map node-spdx-correct
  node-spdx-exceptions node-spdx-expression-parse node-spdx-license-ids node-sprintf-js
  node-stealthy-require node-string-decoder node-supports-color node-text-table node-time-stamp
  node-tmatch node-typedarray-to-buffer node-universalify node-util-deprecate
  node-validate-npm-package-license node-webidl-conversions node-whatwg-fetch node-wrappy node-yallist
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  node-abab* node-agent-base* node-aproba* node-archy* node-argparse* node-builtins* node-chalk*
  node-cli-table* node-clone* node-colors* node-columnify* node-combined-stream*
  node-console-control-strings* node-cssom* node-cssstyle* node-debug* node-defaults* node-events*
  node-fs-write-stream-atomic* node-gauge* node-got* node-graceful-fs* node-https-proxy-agent*
  node-json-buffer* node-lcov-parse* node-log-driver* node-ms* node-normalize-package-data*
  node-npm-package-arg* node-npmlog* node-object-assign* node-psl* node-punycode*
  node-read-package-json* node-rimraf* node-run-queue* node-semver* node-source-map-support*
  node-ssri* node-stack-utils* node-string-width* node-strip-ansi* node-tough-cookie*
  node-unique-filename* node-validate-npm-package-name* node-wcwidth.js* node-wide-align*
  node-write-file-atomic* nodejs* npm*
0 upgraded, 0 newly installed, 50 to remove and 5 not upgraded.
After this operation, 3996 kB disk space will be freed.
(Reading database ... 101319 files and directories currently installed.)
Removing node-abab (2.0.5-2) ...
Removing node-https-proxy-agent (5.0.0+~cs8.0.0-3) ...
Removing node-agent-base (6.0.2+~cs5.4.2-1) ...
Removing node-run-queue (2.0.0-2) ...
Removing node-npmlog (6.0.1+~4.1.4-1) ...
Removing node-gauge (4.0.2-1) ...
Removing node-aproba (2.0.0-2) ...
Removing node-archy (1.0.0-4) ...
Removing node-argparse (2.0.1-2) ...
Removing node-npm-package-arg (8.1.5-1) ...
Removing node-validate-npm-package-name (3.0.0-4) ...
Removing node-builtins (4.0.0-1) ...
Removing node-chalk (4.1.2-1) ...
Removing node-cli-table (0.3.11+~cs0.13.3-1) ...
Removing node-columnify (1.5.4+~1.5.1-1) ...
Removing node-wide-align (1.1.3-4) ...
Removing node-string-width (4.2.3+~cs13.2.3-1) ...
Removing node-wcwidth.js (1.0.2-1) ...
Removing node-defaults (1.0.3+~1.0.3-1) ...
Removing node-clone (2.1.2-3) ...
Removing node-colors (1.4.0-3) ...
Removing node-combined-stream (1.0.8+~1.0.3-1) ...
Removing node-console-control-strings (1.1.0-2) ...
Removing node-cssstyle (2.3.0-2) ...
Removing node-cssom (0.4.4-3) ...
Removing node-debug (4.3.2+~cs4.1.7-1) ...
Removing node-events (3.3.0+~3.0.0-2) ...
Removing node-fs-write-stream-atomic (1.0.10-5) ...
Removing node-got (11.8.3+~cs58.7.37-1) ...
Removing node-graceful-fs (4.2.4+repack-1) ...
Removing node-json-buffer (3.0.1-1) ...
Removing node-lcov-parse (1.0.0+20170612git80d039574ed9-5) ...
Removing node-log-driver (1.2.7+git+20180219+bba1761737-7) ...
Removing node-ms (2.1.3+~cs0.7.31-2) ...
Removing node-read-package-json (4.1.1-1) ...
Removing node-normalize-package-data (3.0.3+~2.4.1-1) ...
Removing node-object-assign (4.1.1-6) ...
Removing node-tough-cookie (4.0.0-2) ...
Removing node-psl (1.8.0+ds-6) ...
Removing node-punycode (2.1.1-5) ...
Removing node-rimraf (3.0.2-1) ...
Removing node-semver (7.3.5+~7.3.8-1) ...
Removing node-source-map-support (0.5.21+ds+~0.5.4-1) ...
Removing node-ssri (8.0.1-2) ...
Removing node-stack-utils (2.0.5+~2.0.1-1) ...
Removing node-strip-ansi (6.0.1-1) ...
Removing node-unique-filename (1.1.1+ds-1) ...
Removing node-write-file-atomic (3.0.3+~3.0.2-1) ...
Removing nodejs (12.22.9~dfsg-1ubuntu3.6) ...
Processing triggers for man-db (2.10.2-1) ...
(Reading database ... 100294 files and directories currently installed.)
Purging configuration files for npm (8.5.1~ds-1) ...
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo apt-get autoremove -y
sudo apt-get autoclean
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  gyp htop libjs-events libjs-highlight.js libjs-inherits libjs-is-typedarray libjs-psl
  libjs-source-map libjs-sprintf-js libjs-typedarray-to-buffer libnode-dev libnode72 libnotify-bin
  libnotify4 libuv1-dev node-abbrev node-ansi-regex node-ansi-styles node-ansistyles
  node-are-we-there-yet node-arrify node-asap node-asynckit node-balanced-match node-brace-expansion
  node-chownr node-clean-yaml-object node-color-convert node-color-name node-commander
  node-core-util-is node-decompress-response node-delayed-stream node-delegates node-depd node-diff
  node-encoding node-end-of-stream node-err-code node-escape-string-regexp node-fancy-log
  node-foreground-child node-fs.realpath node-function-bind node-get-stream node-glob node-growl
  node-has-flag node-has-unicode node-hosted-git-info node-iconv-lite node-iferr node-imurmurhash
  node-indent-string node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer
  node-is-plain-obj node-is-typedarray node-isarray node-isexe node-json-parse-better-errors
  node-jsonparse node-kind-of node-lodash-packages node-lowercase-keys node-lru-cache
  node-mimic-response node-minimatch node-minimist node-minipass node-mute-stream node-negotiator
  node-npm-bundled node-once node-osenv node-p-cancelable node-p-map node-path-is-absolute
  node-process-nextick-args node-promise-inflight node-promise-retry node-promzard node-pump
  node-quick-lru node-read node-readable-stream node-resolve node-retry node-safe-buffer
  node-set-blocking node-signal-exit node-slash node-slice-ansi node-source-map node-spdx-correct
  node-spdx-exceptions node-spdx-expression-parse node-spdx-license-ids node-sprintf-js
  node-stealthy-require node-string-decoder node-supports-color node-text-table node-time-stamp
  node-tmatch node-typedarray-to-buffer node-universalify node-util-deprecate
  node-validate-npm-package-license node-webidl-conversions node-whatwg-fetch node-wrappy node-yallist
0 upgraded, 0 newly installed, 117 to remove and 5 not upgraded.
After this operation, 67.1 MB disk space will be freed.
(Reading database ... 100294 files and directories currently installed.)
Removing gyp (0.1+20210831gitd6c5dd5-5) ...
Removing htop (3.0.5-7build2) ...
Removing libjs-events (3.3.0+~3.0.0-2) ...
Removing libjs-highlight.js (9.18.5+dfsg1-1) ...
Removing node-are-we-there-yet (3.0.0+~1.1.0-1) ...
Removing node-readable-stream (3.6.0+~cs3.0.0-1) ...
Removing node-glob (7.2.1+~cs7.6.15-1) ...
Removing node-inherits (2.0.4-4) ...
Removing libjs-inherits (2.0.4-4) ...
Removing node-typedarray-to-buffer (4.0.0-2) ...
Removing node-is-typedarray (1.0.0-4) ...
Removing libjs-is-typedarray (1.0.0-4) ...
Removing libjs-psl (1.8.0+ds-6) ...
Removing node-source-map (0.7.0++dfsg2+really.0.6.1-9) ...
Removing libjs-source-map (0.7.0++dfsg2+really.0.6.1-9) ...
Removing node-sprintf-js (1.1.2+ds1+~1.1.2-1) ...
Removing libjs-sprintf-js (1.1.2+ds1+~1.1.2-1) ...
Removing libjs-typedarray-to-buffer (4.0.0-2) ...
Removing libnode-dev (12.22.9~dfsg-1ubuntu3.6) ...
Removing libnode72:amd64 (12.22.9~dfsg-1ubuntu3.6) ...
Removing node-growl (1.10.5-4) ...
Removing libnotify-bin (0.7.9-3ubuntu5.22.04.1) ...
Removing libnotify4:amd64 (0.7.9-3ubuntu5.22.04.1) ...
Removing libuv1-dev:amd64 (1.43.0-1ubuntu0.1) ...
Removing node-abbrev (1.1.1+~1.1.2-1) ...
Removing node-ansi-regex (5.0.1-1) ...
Removing node-slice-ansi (5.0.0+~cs9.0.0-4) ...
Removing node-ansi-styles (4.3.0+~4.2.0-1) ...
Removing node-ansistyles (0.1.3-5) ...
Removing node-minimist (1.2.5+~cs5.3.2-1) ...
Removing node-arrify (2.0.1-2) ...
Removing node-asap (2.0.6+~2.0.0-1) ...
Removing node-asynckit (0.4.0-4) ...
Removing node-minimatch (3.1.1+~3.0.5-1) ...
Removing node-brace-expansion (2.0.1-1) ...
Removing node-balanced-match (2.0.0-1) ...
Removing node-chownr (2.0.0-1) ...
Removing node-clean-yaml-object (0.1.0-5) ...
Removing node-color-convert (2.0.1-1) ...
Removing node-color-name (1.1.4+~1.1.1-2) ...
Removing node-commander (9.0.0-2) ...
Removing node-core-util-is (1.0.3-1) ...
Removing node-decompress-response (6.0.0-2) ...
Removing node-delayed-stream (1.0.0-5) ...
Removing node-delegates (1.0.0-3) ...
Removing node-depd (2.0.0-2) ...
Removing node-diff (5.0.0~dfsg+~5.0.1-3) ...
Removing node-minipass (3.1.6+~cs8.7.18-1) ...
Removing node-encoding (0.1.13-2) ...
Removing node-get-stream (6.0.1-1) ...
Removing node-pump (3.0.0-5) ...
Removing node-end-of-stream (1.4.4+~1.4.1-1) ...
Removing node-promise-retry (2.0.1-2) ...
Removing node-err-code (2.0.3+dfsg-3) ...
Removing node-p-map (4.0.0+~3.1.0+~3.0.1-1) ...
Removing node-escape-string-regexp (4.0.0-2) ...
Removing node-fancy-log (1.3.3+~cs1.3.1-2) ...
Removing node-foreground-child (2.0.0-3) ...
Removing node-fs.realpath (1.0.0-2) ...
Removing node-resolve (1.20.0+~cs5.27.9-1) ...
Removing node-function-bind (1.1.1+repacked+~1.0.3-1) ...
Removing node-supports-color (8.1.1+~8.1.1-1) ...
Removing node-has-flag (4.0.0-2) ...
Removing node-has-unicode (2.0.1-4) ...
Removing node-hosted-git-info (4.0.2-1) ...
Removing node-iconv-lite (0.6.3-2) ...
Removing node-iferr (1.0.2+~1.0.2-1) ...
Removing node-imurmurhash (0.1.4+dfsg+~0.1.1-1) ...
Removing node-indent-string (4.0.0-2) ...
Removing node-inflight (1.0.6-2) ...
Removing node-ini (2.0.1-1) ...
Removing node-ip (1.1.5+~1.1.0-1) ...
Removing node-ip-regex (4.3.0+~4.1.1-1) ...
Removing node-kind-of (6.0.3+dfsg-2) ...
Removing node-is-buffer (2.0.5-2) ...
Removing node-is-plain-obj (3.0.0-2) ...
Removing node-isarray (2.0.5-3) ...
Removing node-isexe (2.0.0+~2.0.1-4) ...
Removing node-json-parse-better-errors (1.0.2+~cs3.3.1-1) ...
Removing node-jsonparse (1.3.1-10) ...
Removing node-lodash-packages (4.17.21+dfsg+~cs8.31.198.20210220-5) ...
Removing node-lowercase-keys (2.0.0-2) ...
Removing node-lru-cache (6.0.0+~5.1.1-1) ...
Removing node-mimic-response (3.1.0-7) ...
Removing node-promzard (0.3.0-2) ...
Removing node-read (1.0.7-3) ...
Removing node-mute-stream (0.0.8+~0.0.1-1) ...
Removing node-negotiator (0.6.2+~0.6.1-1) ...
Removing node-npm-bundled (1.1.2-1) ...
Removing node-once (1.4.0-4) ...
Removing node-osenv (0.1.5+~0.1.0-1) ...
Removing node-p-cancelable (2.1.1-1) ...
Removing node-path-is-absolute (2.0.0-2) ...
Removing node-process-nextick-args (2.0.1-2) ...
Removing node-promise-inflight (1.0.1+~1.0.0-1) ...
Removing node-quick-lru (5.1.1-1) ...
Removing node-retry (0.13.1+~0.12.1-1) ...
Removing node-string-decoder (1.3.0-5) ...
Removing node-safe-buffer (5.2.1+~cs2.1.2-2) ...
Removing node-set-blocking (2.0.0-2) ...
Removing node-signal-exit (3.0.6+~3.0.1-1) ...
Removing node-slash (3.0.0-2) ...
Removing node-validate-npm-package-license (3.0.4-2) ...
Removing node-spdx-correct (3.1.1-2) ...
Removing node-spdx-expression-parse (3.0.1+~3.0.1-1) ...
Removing node-spdx-exceptions (2.3.0-2) ...
Removing node-spdx-license-ids (3.0.11-1) ...
Removing node-stealthy-require (1.1.1-5) ...
Removing node-text-table (0.2.0-4) ...
Removing node-time-stamp (2.2.0-1) ...
Removing node-tmatch (5.0.0-4) ...
Removing node-universalify (2.0.0-3) ...
Removing node-util-deprecate (1.0.2-3) ...
Removing node-webidl-conversions (7.0.0~1.1.0+~cs15.1.20180823-2) ...
Removing node-whatwg-fetch (3.6.2-5) ...
Removing node-wrappy (1.0.2-2) ...
Removing node-yallist (4.0.0+~4.0.1-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Del libssl-dev 3.0.2-0ubuntu1.17 [2375 kB]
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# node -v
npm -v
-bash: /usr/bin/node: No such file or directory
-bash: /usr/bin/npm: No such file or directory
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
2024-11-11 12:41:05 - Installing pre-requisites
Hit:1 https://deb.nodesource.com/node_20.x nodistro InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:3 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:4 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20240203~22.04.1).
curl is already the newest version (7.81.0-1ubuntu1.18).
gnupg is already the newest version (2.2.27-3ubuntu2.1).
apt-transport-https is already the newest version (2.4.13).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:6 https://deb.nodesource.com/node_20.x nodistro InRelease
Reading package lists... Done
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
2024-11-11 12:41:11 - Repository configured successfully.
2024-11-11 12:41:11 - To install Node.js, run: apt-get install nodejs -y
2024-11-11 12:41:11 - You can use N|solid Runtime as a node.js alternative
2024-11-11 12:41:11 - To install N|solid Runtime, run: apt-get install nsolid -y

root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# sudo bash nodesource_setup.sh
sudo apt install nodejs -y
2024-11-11 12:41:26 - Installing pre-requisites
Hit:1 https://deb.nodesource.com/node_20.x nodistro InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:3 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:4 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
curl is already the newest version (7.81.0-1ubuntu1.18).
gnupg is already the newest version (2.2.27-3ubuntu2.1).
apt-transport-https is already the newest version (2.4.13).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:6 https://deb.nodesource.com/node_20.x nodistro InRelease
Reading package lists... Done
W: http://security.ubuntu.com/ubuntu/dists/xenial-security/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
2024-11-11 12:41:33 - Repository configured successfully.
2024-11-11 12:41:33 - To install Node.js, run: apt-get install nodejs -y
2024-11-11 12:41:33 - You can use N|solid Runtime as a node.js alternative
2024-11-11 12:41:33 - To install N|solid Runtime, run: apt-get install nsolid -y

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  nodejs
0 upgraded, 1 newly installed, 0 to remove and 5 not upgraded.
Need to get 0 B/31.8 MB of archives.
After this operation, 197 MB of additional disk space will be used.
Selecting previously unselected package nodejs.
(Reading database ... 96008 files and directories currently installed.)
Preparing to unpack .../nodejs_20.18.0-1nodesource1_amd64.deb ...
Unpacking nodejs (20.18.0-1nodesource1) ...
Setting up nodejs (20.18.0-1nodesource1) ...
Processing triggers for man-db (2.10.2-1) ...
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# nodejs -v
v20.18.0
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm -v
10.8.2
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic#


Solution Task
1. Task1
To modify the taskFirst and taskNext functions to use const and let where appropriate, follow these steps:

Task Description:

- taskFirst: Use const to declare variables that do not change after their initial assignment.

- taskNext: Use let to declare variables that will be modified (in this case, combination).

Code Implementation
You need to update the 0-constants.js file with the changes:

```js
// 0-constants.js

export function taskFirst() {
  const task = 'I prefer const when I can.';  // Using const since the variable does not change
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';  // Using let because we modify the variable
  combination += getLast();  // Concatenating a string to combination

  return combination;
}
```
Explanation of Changes:

- In taskFirst(), I replaced var with const because the task variable is not reassigned, making const the appropriate choice.

- In taskNext(), I replaced var with let because the combination variable is reassigned when concatenating the string returned by getLast().
Testing the Code
Make sure to test the code using 0-main.js:

```js
// 0-main.js

import { taskFirst, taskNext } from './0-constants.js';

console.log(`${taskFirst()} ${taskNext()}`);
```
Expected Output:
When you run the following command:

```bash
npm run dev 0-main.js
```
The output should be:

```plaintext
I prefer const when I can. But sometimes let is okay
```
Directory Structure:
Ensure the structure is like this:

```css
holbertonschool-web_back_end
└── ES6_basic
    ├── 0-constants.js
    └── 0-main.js
```
This will complete the task.

