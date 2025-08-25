const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf-8');

    // Split the file into lines and filter out empty ones
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove the header row
    lines.shift();

    // Initialize data structure to count students
    const students = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const [firstname, field] = line.split(',');

      if (firstname && field) {
        totalStudents += 1;

        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname);
      }
    });

    // Log total number of students
    console.log(`Number of students: ${totalStudents}`);

    // Log the number of students and their names per field
    for (const [field, names] of Object.entries(students)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
      );
    }
  } catch (err) {
    // Handle file not found or read error
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
