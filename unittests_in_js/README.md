# unittests_in_js

# Task0
```bash
mkdir unittests_in_js && cd unittests_in_js
npm init -y
npm install mocha --save-dev

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test 0-calcul.test.js

> task_0@1.0.0 test
> mocha 0-calcul.test.js

/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:138
    throw createUnsupportedError(
    ^

Error: Option 0-calcul.test.js is unsupported by the mocha cli
    at createUnsupportedError (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/errors.js:238:13)
    at createErrorForNumericPositionalArg (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:138:11)
    at parse (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:189:5)
    at loadOptions (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:291:14)
    at Object.<anonymous> (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/bin/mocha.js:29:14)
    at Module._compile (node:internal/modules/cjs/loader:1529:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:164:12) {
  code: 'ERR_MOCHA_UNSUPPORTED'
}

Node.js v20.19.0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./0-calcul.test.js

> task_0@1.0.0 test
> mocha ./0-calcul.test.js



  calculateNumber
    ✔ should return 4 when adding 1 and 3
    ✔ should round second argument
    ✔ should round both arguments down
    ✔ should round first argument up
    ✔ should round both arguments correctly when .5 case
    ✔ should handle negative numbers
    ✔ should handle mix of positive and negative


  7 passing (4ms)
```

explication erreur mocha:
Parce que Mocha refuse les arguments positionnels “numériques”.

Dans npm test 0-calcul.test.js, Mocha reçoit l’argument 0-calcul.test.js qui commence par un chiffre. Depuis les versions récentes, Mocha l’interprète comme un numeric positional arg et lève ERR_MOCHA_UNSUPPORTED (cf. createErrorForNumericPositionalArg). D’où l’erreur.

Dans npm test -- ./0-calcul.test.js, deux choses changent :

-- garantit que l’argument est bien transmis au script (bonne pratique avec npm).

Le préfixe ./ fait que l’argument ne commence plus par un chiffre : Mocha le traite alors comme un chemin de fichier valide et tout passe.

Solutions rapides

Utiliser un préfixe chemin :
npm test -- ./0-calcul.test.js

Renommer le fichier pour ne pas commencer par un chiffre (ex. test-0-calcul.test.js).

Configurer le script pour viser un motif/glob :
"test": "mocha './**/*.test.js'"
(les quotes et/ou ./ évitent le cas « numérique en tête »).

En bref : c’est le nom qui commence par “0” qui déclenche l’erreur de Mocha ; le ./ contourne, ou renomme le fichier.


package json
```json
{
  "name": "task_0",
  "version": "1.0.0",
  "description": "",
  "main": "0-calcul.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1"
  }
}
```

# Task1

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./1-calcul.test.js

> task_1@1.0.0 test
> mocha ./1-calcul.test.js



  calculateNumber(type, a, b)
    SUM
      ✔ should sum rounded numbers
    SUBTRACT
      ✔ should subtract rounded numbers
    DIVIDE
      ✔ should divide rounded numbers
      ✔ should return "Error" when rounded divisor is 0
    Invalid type (optional)
      ✔ should throw on invalid type


  5 passing (7ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#
```

package json
```json
{
  "name": "task_1",
  "version": "1.0.0",
  "description": "",
  "main": "1-calcul.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1"
  }
}
```

calculateNumber('SUM', 1.4, 4.5)
calculateNumber('SUBTRACT', 1.4, 4.5)
calculateNumber('DIVIDE', 1.4, 4.5)
calculateNumber('DIVIDE', 1.4, 0)

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# node
Welcome to Node.js v20.19.0.
Type ".help" for more information.
> calculateNumber('SUM', 1.4, 4.5)
, 4.5)
calculateNumber('DIVIDE', 1.4, 0)Uncaught ReferenceError: calculateNumber is not defined
> calculateNumber('SUBTRACT', 1.4, 4.5)
Uncaught ReferenceError: calculateNumber is not defined
> calculateNumber('DIVIDE', 1.4, 4.5)
Uncaught ReferenceError: calculateNumber is not defined
> calculateNumber('DIVIDE', 1.4, 0)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# node
Welcome to Node.js v20.19.0.
Type ".help" for more information.
> const calculateNumber = require('./1-calcul.js')
undefined
> const calculateNumber = require('./1-calcul.js');
Uncaught SyntaxError: Identifier 'calculateNumber' has already been declared
> calculateNumber('SUM', 1.4, 4.5)
6
> calculateNumber('SUBTRACT', 1.4, 4.5)
-4
> calculateNumber('DIVIDE', 1.4, 4.5)
0.2
> calculateNumber('DIVIDE', 1.4, 0)
'Error'
>
```

# Task2

```bash
npm i -D chai
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm i -D chai

added 1 package, and audited 93 packages in 1s

29 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./2-calcul_chai.test.js

> task_2@1.0.0 test
> mocha ./2-calcul_chai.test.js



  calculateNumber(type, a, b)
    SUM
      ✔ should sum rounded numbers
    SUBTRACT
      ✔ should subtract rounded numbers
    DIVIDE
      ✔ should divide rounded numbers
      ✔ should return "Error" when rounded divisor is 0
    Invalid type (optional)
      ✔ should throw on invalid type


  5 passing (7ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test 2-calcul_chai.test.js

> task_2@1.0.0 test
> mocha 2-calcul_chai.test.js

/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:138
    throw createUnsupportedError(
    ^

Error: Option 2-calcul_chai.test.js is unsupported by the mocha cli
    at createUnsupportedError (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/errors.js:238:13)
    at createErrorForNumericPositionalArg (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:138:11)
    at parse (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:189:5)
    at loadOptions (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/lib/cli/options.js:291:14)
    at Object.<anonymous> (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/node_modules/mocha/bin/mocha.js:29:14)
    at Module._compile (node:internal/modules/cjs/loader:1529:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:164:12) {
  code: 'ERR_MOCHA_UNSUPPORTED'
}

Node.js v20.19.0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#
```

package json
```json
{
  "name": "task_2",
  "version": "1.0.0",
  "description": "",
  "main": "2-calcul_chai.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1"
  }
}
```

# Task3

```bash
npm i -D sinon
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm i -D sinon

added 7 packages, removed 1 package, and audited 99 packages in 7s

30 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./3-payment.test.js

> task_3@1.0.0 test
> mocha ./3-payment.test.js



  sendPaymentRequestToApi
The total is: 120
    ✔ should use Utils.calculateNumber("SUM", 100, 20) and log the total


  1 passing (7ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#
```

package json
```json
{
  "name": "task_3",
  "version": "1.0.0",
  "description": "",
  "main": "3-payment.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1"
  }
}

{
  "name": "task_3",
  "version": "1.0.0",
  "description": "",
  "main": "3-payment.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}
```

# Task4

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./4-payment.test.js

> task_3@1.0.0 test
> mocha ./4-payment.test.js



  sendPaymentRequestToApi (with stub)
The total is: 10
    ✔ should stub Utils.calculateNumber to return 10 and log the correct total


  1 passing (14ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./4-payment.test.js

> task_4@1.0.0 test
> mocha ./4-payment.test.js



  sendPaymentRequestToApi (with stub)
The total is: 10
    ✔ should stub Utils.calculateNumber to return 10 and log the correct total


  1 passing (7ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#
```

package json
```json
{
  "name": "task_4",
  "version": "1.0.0",
  "description": "",
  "main": "4-payment.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}
```

# Task5

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js# npm test -- ./5-payment.test.js

> task_5@1.0.0 test
> mocha ./5-payment.test.js



  sendPaymentRequestToApi (hooks + single spy)
The total is: 120
    ✔ logs "The total is: 120" and is called once for (100, 20)
The total is: 20
    ✔ logs "The total is: 20" and is called once for (10, 10)


  2 passing (7ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/unittests_in_js#
```

package json
```json
{
  "name": "task_5",
  "version": "1.0.0",
  "description": "",
  "main": "5-payment.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}
```

# Task6

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# npm test -- ./6-payment_token.test.js

> task_6@1.0.0 test
> mocha ./6-payment_token.test.js



  getPaymentTokenFromAPI
    ✔ resolves with the expected object when success=true


  1 passing (5ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js#
```

package json
```json
{
  "name": "task_6",
  "version": "1.0.0",
  "description": "",
  "main": "6-payment_token.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}
```

# Task7

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# npm i -D chai

added 6 packages, and audited 105 packages in 5s

30 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js#


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# npm test -- ./7-skip.test.js

> task_7@1.0.0 test
> mocha ./7-skip.test.js



  Testing numbers
    ✔ 1 is equal to 1
    ✔ 2 is equal to 2
    - 1 is equal to 3
    ✔ 3 is equal to 3
    ✔ 4 is equal to 4
    ✔ 5 is equal to 5
    ✔ 6 is equal to 6
    ✔ 7 is equal to 7


  7 passing (5ms)
  1 pending

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js#
```

package json
```json
{
  "name": "task_7",
  "version": "1.0.0",
  "description": "",
  "main": "7-skip.test.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "chai": "^5.3.3",
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}
```

# Task8

Depuis 8-api/, installe :

```bash
npm i
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# npm i
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated har-validator@5.1.5: this library is no longer supported
npm warn deprecated mkdirp@0.5.4: Legacy versions of mkdirp are no longer supported. Please update to mkdirp 1.x. (Note that the API surface has changed to use Promises in 1.x.)
npm warn deprecated glob@7.1.3: Glob versions prior to v9 are no longer supported
npm warn deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm warn deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm warn deprecated debug@3.2.6: Debug versions >=3.2.0 <3.2.7 || >=4 <4.3.1 have a low-severity ReDos regression when used in a Node.js environment. It is recommended you upgrade to 3.2.7 or 4.3.1. (https://github.com/visionmedia/debug/issues/797)
npm warn deprecated sinon@7.5.0: 16.1.1

added 283 packages, and audited 284 packages in 22s

80 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (1 low, 1 moderate, 1 high, 5 critical)

To address all issues possible (including breaking changes), run:
  npm audit fix --force

Some issues need review, and may require choosing
a different dependency.

Run `npm audit` for details.
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api#
```

Terminal 1
```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# cd 8-api/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# ls
api.js  api.test.js  node_modules  package-lock.json  package.json
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# node api.js
API available on localhost port 7865
```
![alt text](image.png)

Terminal 2
```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# cd 8-api/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# ls
api.js  api.test.js  node_modules  package-lock.json  package.json

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api#  curl http://localhost:7865 ; echo ""
Welcome to the payment system

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# npm test api.test.js

> 8-api@1.0.0 test
> ./node_modules/mocha/bin/mocha api.test.js



  Index page
    ✓ Correct status code?
    ✓ Correct result?
    ✓ Content-Type header looks right?


  3 passing (44ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api#
```

package json
```json
{
  "name": "task_8",
  "version": "1.0.0",
  "description": "",
  "main": "0-calcul.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}

{
  "name": "8-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/mocha/bin/mocha"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```

# Task9

Terminal 1
```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/8-api# cd  ..
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# ls
0-calcul.js       2-calcul_chai.js       4-payment.test.js        7-skip.test.js  node_modules
0-calcul.test.js  2-calcul_chai.test.js  5-payment.js             8-api           old_package.json
1-calcul.js       3-payment.js           5-payment.test.js        9-api           package-lock.json
1-calcul.test.js  3-payment.test.js      6-payment_token.js       README.md       package.json
10-api            4-payment.js           6-payment_token.test.js  image.png       utils.js
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# cd 9-api/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# ls
api.js  api.test.js  package.json
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# node api.js
node:internal/modules/cjs/loader:1215
  throw err;
  ^

Error: Cannot find module 'express'
Require stack:
- /mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/api.js
    at Module._resolveFilename (node:internal/modules/cjs/loader:1212:15)
    at Module._load (node:internal/modules/cjs/loader:1043:27)
    at Module.require (node:internal/modules/cjs/loader:1298:19)
    at require (node:internal/modules/helpers:182:18)
    at Object.<anonymous> (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/api.js:1:17)
    at Module._compile (node:internal/modules/cjs/loader:1529:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:164:12) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/api.js'
  ]
}

Node.js v20.19.0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# npm i
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated har-validator@5.1.5: this library is no longer supported
npm warn deprecated mkdirp@0.5.4: Legacy versions of mkdirp are no longer supported. Please update to mkdirp 1.x. (Note that the API surface has changed to use Promises in 1.x.)
npm warn deprecated glob@7.1.3: Glob versions prior to v9 are no longer supported
npm warn deprecated debug@3.2.6: Debug versions >=3.2.0 <3.2.7 || >=4 <4.3.1 have a low-severity ReDos regression when used in a Node.js environment. It is recommended you upgrade to 3.2.7 or 4.3.1. (https://github.com/visionmedia/debug/issues/797)
npm warn deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm warn deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm warn deprecated sinon@7.5.0: 16.1.1

added 283 packages, and audited 284 packages in 15s

80 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (1 low, 1 moderate, 1 high, 5 critical)

To address all issues possible (including breaking changes), run:
  npm audit fix --force

Some issues need review, and may require choosing
a different dependency.

Run `npm audit` for details.
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# node api.js
API available on localhost port 7865

```

Terminal 2
```bash
10-api            4-payment.js           6-payment_token.test.js  image.png       utils.js
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# cd 9-api/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# ls
api.js  api.test.js  node_modules  package-lock.json  package.json
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# npm test api.t
est.js

> 9-api@1.0.0 test
> ./node_modules/mocha/bin/mocha api.test.js

/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/api.test.js:65



SyntaxError: Unexpected end of input
    at wrapSafe (node:internal/modules/cjs/loader:1472:18)
    at Module._compile (node:internal/modules/cjs/loader:1501:20)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at Module.require (node:internal/modules/cjs/loader:1298:19)
    at require (node:internal/modules/helpers:182:18)
    at /mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/mocha.js:334:36
    at Array.forEach (<anonymous>)
    at Mocha.loadFiles (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/mocha.js:331:14)
    at Mocha.run (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/mocha.js:809:10)
    at exports.singleRun (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/cli/run-helpers.js:108:16)
    at exports.runMocha (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/cli/run-helpers.js:142:13)
    at exports.handler (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/cli/run.js:292:3)
    at Object.runCommand (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/yargs/lib/command.js:242:26)
    at Object.parseArgs [as _parseArgs] (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/yargs/yargs.js:1096:28)
    at Object.parse (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/yargs/yargs.js:575:25)
    at exports.main (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/lib/cli/cli.js:68:6)
    at Object.<anonymous> (/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api/node_modules/mocha/bin/mocha:162:29)
    at Module._compile (node:internal/modules/cjs/loader:1529:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:164:12)
    at node:internal/main/run_main_module:28:49

Node.js v20.19.0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# npm test api.test.js

> 9-api@1.0.0 test
> ./node_modules/mocha/bin/mocha api.test.js



  Index page
    ✓ Correct status code?
    ✓ Correct result?
    ✓ Content-Type header looks right?

  Cart page
    ✓ Correct status code when :id is a number
    ✓ Correct result when :id is a number
    ✓ 404 when :id is NOT a number
    ✓ Works with other numeric ids


  7 passing (73ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# curl http://localhost:7865/cart/12 ; echo ""
Payment methods for cart 12
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# curl http://localhost:7865/cart/hello -v
*   Trying 127.0.0.1:7865...
* Connected to localhost (127.0.0.1) port 7865 (#0)
> GET /cart/hello HTTP/1.1
> Host: localhost:7865
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< X-Powered-By: Express
< Content-Security-Policy: default-src 'none'
< X-Content-Type-Options: nosniff
< Content-Type: text/html; charset=utf-8
< Content-Length: 149
< Date: Wed, 27 Aug 2025 09:09:30 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
<
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /cart/hello</pre>
</body>
</html>
* Connection #0 to host localhost left intact
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api#
```

package json
```json
{
  "name": "task_9",
  "version": "1.0.0",
  "description": "",
  "main": "0-calcul.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}

{
  "name": "9-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/mocha/bin/mocha"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}

```

# Task10

Terminal 1
```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# node api.js
API available on localhost port 7865
^C
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/9-api# cd ..
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js# cd 10-api/
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api# ls
api.js  api.test.js  package.json
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api# npm i
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated har-validator@5.1.5: this library is no longer supported
npm warn deprecated mkdirp@0.5.4: Legacy versions of mkdirp are no longer supported. Please update to mkdirp 1.x. (Note that the API surface has changed to use Promises in 1.x.)
npm warn deprecated glob@7.1.3: Glob versions prior to v9 are no longer supported
npm warn deprecated debug@3.2.6: Debug versions >=3.2.0 <3.2.7 || >=4 <4.3.1 have a low-severity ReDos regression when used in a Node.js environment. It is recommended you upgrade to 3.2.7 or 4.3.1. (https://github.com/visionmedia/debug/issues/797)
npm warn deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm warn deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm warn deprecated sinon@7.5.0: 16.1.1

added 283 packages, and audited 284 packages in 22s

80 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (1 low, 1 moderate, 1 high, 5 critical)

To address all issues possible (including breaking changes), run:
  npm audit fix --force

Some issues need review, and may require choosing
a different dependency.

Run `npm audit` for details.
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api# node api.js
API available on localhost port 7865
```

Terminal 2
```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api#  curl http://localhost:7865/available_payments ; echo ""
{"payment_methods":{"credit_cards":true,"paypal":false}}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api# curl -XPOST http://localhost:7865/login -d '{ "userName": "Betty" }' -H 'Content-Type: application/json' ; echo ""
Welcome Betty
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api# npm test api.test.js

> 10-api@1.0.0 test
> ./node_modules/mocha/bin/mocha api.test.js



  Index page
    ✓ Correct status code?
    ✓ Correct result?
    ✓ Content-Type header looks right?

  Cart page
    ✓ Correct status code when :id is a number
    ✓ Correct result when :id is a number
    ✓ 404 when :id is NOT a number
    ✓ Works with other numeric ids

  GET /available_payments
    ✓ returns correct status and JSON body
    ✓ Content-Type is application/json

  POST /login
    ✓ returns "Welcome Betty" for userName=Betty
    ✓ returns "Welcome " when userName is missing


  11 passing (68ms)

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/unittests_in_js/10-api#
```

package json
```json
{
  "name": "task_10",
  "version": "1.0.0",
  "description": "",
  "main": "0-calcul.js",
  "scripts": {
    "test": "mocha"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "mocha": "^11.0.1",
    "sinon": "^21.0.0"
  }
}

{
  "name": "10-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/mocha/bin/mocha"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}

```
