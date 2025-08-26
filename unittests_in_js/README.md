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
```

# Task4

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task5

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task6

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task7

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task8

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task9

```bash

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
    "mocha": "^11.0.1"
  }
}
```

# Task10

```bash

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
    "mocha": "^11.0.1"
  }
}
```
