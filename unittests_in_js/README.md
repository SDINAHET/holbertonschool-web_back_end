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

