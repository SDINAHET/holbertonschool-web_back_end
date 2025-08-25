export default function getStudentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}

// export default function getStudentsByLocation(students, city) {
//   if (!Array.isArray(students)) {
//     return [];
//   }
//   // Use filter to select students based on their location
//   return students.filter((student) => student.location === city);
// }
