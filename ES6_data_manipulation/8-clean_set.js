export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  return [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}
