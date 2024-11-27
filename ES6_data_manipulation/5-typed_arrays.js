export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt8(position, value);
  return view;
}

// export default function createInt8TypedArray(length, position, value) {
//   // Create a new ArrayBuffer of the given length
//   const buffer = new ArrayBuffer(length);

//   // Create a DataView to manipulate the ArrayBuffer
//   const dataView = new DataView(buffer);

//   // Check if the position is outside the range
//   if (position < 0 || position >= length) {
//     throw new Error('Position outside range');
//   }

//   // Set the Int8 value at the specified position
//   dataView.setInt8(position, value);

//   return dataView;
// }
