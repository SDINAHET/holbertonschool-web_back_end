const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;

/**
 * Function to count students in a CSV file.
 * @param {String} filePath Path to the CSV file.
 * @returns {Promise<String>} A formatted string with student counts.
 */
const countStudents = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    lines.shift(); // Remove header row

    const students = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const [firstname, , , field] = line.split(',');

      if (firstname && field) {
        totalStudents += 1;
        if (!students[field]) students[field] = [];
        students[field].push(firstname);
      }
    });

    let output = `Number of students: ${totalStudents}\n`;
    Object.keys(students).sort().forEach((field) => {
      output += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
    });

    resolve(output.trim());
  });
});

// Root route
app.get('/', (_, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

// Students route
app.get('/students', async (_, res) => {
  const databasePath = process.argv[2];

  if (!databasePath) {
    res.status(500).send('Cannot load the database');
    return;
  }

  try {
    const studentData = await countStudents(databasePath);
    res.setHeader('Content-Type', 'text/plain');
    res.send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
