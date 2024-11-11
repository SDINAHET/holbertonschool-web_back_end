// 0-constants.js

export function taskFirst() {
  const task = 'I prefer const when I can.'; // Using const since the variable does not change
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let'; // Using let because we modify the variable
  combination += getLast(); // Concatenating a string to combination

  return combination;
}
