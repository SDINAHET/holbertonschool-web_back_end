const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
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

          if (!students[field]) {
            students[field] = [];
          }

          students[field].push(firstname);
        }
      });

      let output = `Number of students: ${totalStudents}\n`;
      for (const [field, names] of Object.entries(students)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    const databasePath = process.argv[2];
    if (!databasePath) {
      res.end('Cannot load the database');
      return;
    }

    try {
      const studentData = await countStudents(databasePath);
      res.end(studentData);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);
module.exports = app;
