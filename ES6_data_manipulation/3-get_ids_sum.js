export default function getStudentIdsSum(students) {
  return students.reduce((sum, student) => sum + student.id, 0);
}

// export default function getStudentIdsSum(students) {
//   if (!Array.isArray(students)) {
//     return 0;
//   }
//   // Use reduce to calculate the sum of all student IDs
//   return students.reduce((sum, student) => sum + student.id, 0);
// }
