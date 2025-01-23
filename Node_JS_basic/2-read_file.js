const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const students = lines.slice(1); // Skip the header line
    const fields = {};

    students.forEach((student) => {
      const details = student.split(',').map((item) => item.trim()); // Trim whitespace from each field
      if (details.length >= 4) { // Ensure valid student entry
        const field = details[3]; // The field of study is the 4th column
        const firstName = details[0]; // First name is the 1st column

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    });

    console.log(`Number of students: ${students.length}`);

    for (const [field, firstNames] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${firstNames.length}. List: ${firstNames.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
