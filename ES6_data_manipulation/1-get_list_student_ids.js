export default function getListStudentIds(list) {
  if (!Array.isArray(list)) {
    return [];
  }
  // return list.map((student) => student.id);
  // Use map to extract ids
  return students.map((student) => student.id);
}
