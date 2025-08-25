const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines
    const students = [];

    lines.forEach((line) => {
      const [firstname, field] = line.split(',');
      if (firstname && field) {
        students.push({ firstname, field });
      }
    });

    console.log(`Number of students: ${students.length}`);

    const fields = [...new Set(students.map((student) => student.field))];

    fields.forEach((field) => {
      const studentsInField = students.filter((student) => student.field === field).map((student) => student.firstname);
      console.log(`Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
