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

```bash
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic# npm run dev 0-main.js

> dev
> npx babel-node 0-main.js

I prefer const when I can. But sometimes let is okay
root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/holbertonschool-web_back_end/ES6_ba
sic#
```
