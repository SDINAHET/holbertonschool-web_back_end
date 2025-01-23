Here’s how to implement the function displayMessage in the file 0-console.js:

Steps:
Create a file named 0-console.js.
Implement the displayMessage function that uses console.log to print the string passed as an argument.
Export the function using module.exports.
Implementation:
0-console.js:

javascript
Copier
Modifier
function displayMessage(message) {
    console.log(message);
}

module.exports = displayMessage;
Explanation:
The displayMessage function takes a single argument message and prints it to the console using console.log.
The module.exports statement makes the function available for importing into other files, such as 0-main.js.
Testing the Function:
To test the function:

Create a 0-main.js file in the same directory.
Add the following code to 0-main.js:
0-main.js:

javascript
Copier
Modifier
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");
Run the script using Node.js:
bash
Copier
Modifier
node 0-main.js
Expected Output:
When you run node 0-main.js, it should output:

Copier
Modifier
Hello NodeJS!
This implementation meets the requirements specified for the task.


____________________________________________________________________

Here’s the implementation for the program 1-stdin.js:

Implementation:
1-stdin.js:
javascript
Copier
Modifier
// Display the initial prompt
console.log("Welcome to Holberton School, what is your name?");

process.stdin.on('data', (data) => {
  // Read user input and remove the newline character
  const name = data.toString().trim();

  // Display the user's name
  console.log(`Your name is: ${name}`);

  // Exit the process
  console.log("This important software is now closing");
  process.exit();
});
How It Works:
The program starts by displaying the message:

vbnet
Copier
Modifier
Welcome to Holberton School, what is your name?
It listens for user input through process.stdin.on('data', ...).

This event is triggered when the user inputs text and presses Enter.
Once input is received, it:

Trims any extra whitespace or newline characters from the input.
Displays the message:
arduino
Copier
Modifier
Your name is: INPUT
The program then displays the closing message:

csharp
Copier
Modifier
This important software is now closing
Finally, the program exits with process.exit().

Directory Structure:
c
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 1-stdin.js
How to Run the Program:
Navigate to the Node_JS_basic directory.

Run the script:

bash
Copier
Modifier
node 1-stdin.js
Alternatively, test it with a piped input:

bash
Copier
Modifier
echo "John" | node 1-stdin.js
Example Output:
Case 1: Manual Input
bash
Copier
Modifier
$ node 1-stdin.js
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
This important software is now closing
Case 2: Piped Input
bash
Copier
Modifier
$ echo "John" | node 1-stdin.js
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
This implementation meets all requirements, works with manual and piped input, and correctly handles the child process testing scenario.

_________________________________________________________________

Here's the implementation for the countStudents function in 2-read_file.js:

Implementation
2-read_file.js:
javascript
Copier
Modifier
const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf-8');

    // Split the file into lines and filter out empty ones
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove the header row
    const header = lines.shift();

    // Initialize data structure to count students
    const students = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const [firstname, lastname, age, field] = line.split(',');

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
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
      );
    }
  } catch (err) {
    // Handle file not found or read error
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
How It Works:
File Reading:

The fs.readFileSync method reads the file synchronously.
Throws an error if the file doesn't exist or cannot be accessed.
Processing Lines:

Splits the file contents into lines and removes any empty lines.
The header row is removed as it's not relevant to the student data.
Parsing CSV:

Each line is split into fields: firstname, lastname, age, and field.
Students are grouped by their field of study, and their names are stored in an array.
Logging Results:

Logs the total number of students.
Logs the count and names of students in each field.
Error Handling:

If the file cannot be read, an error is thrown with the message Cannot load the database.
Example Database (database.csv):
csv
Copier
Modifier
firstname,lastname,age,field
Johann,Smith,25,CS
Arielle,Brown,22,CS
Jonathan,Doe,24,CS
Emmanuel,Doe,23,CS
Guillaume,Smith,23,CS
Katie,Holmes,23,CS
Guillaume,Holmes,25,SWE
Joseph,Allen,22,SWE
Paul,Dupont,24,SWE
Tommy,Doe,23,SWE
Testing:
2-main_0.js (Error Case):
javascript
Copier
Modifier
const countStudents = require('./2-read_file');

countStudents('nope.csv');
Output:

plaintext
Copier
Modifier
Error: Cannot load the database
2-main_1.js (Successful Case):
javascript
Copier
Modifier
const countStudents = require('./2-read_file');

countStudents('database.csv');
Output:

plaintext
Copier
Modifier
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 2-read_file.js
    ├── 2-main_0.js
    ├── 2-main_1.js
    └── database.csv
How to Run:
Place the files in the directory as shown.
Test the error case:
bash
Copier
Modifier
node 2-main_0.js
Test the successful case:
bash
Copier
Modifier
node 2-main_1.js
This implementation adheres to the requirements and provides the expected output.


___________________________________________________________________

Here’s how to implement the countStudents function in the 3-read_file_async.js file, using asynchronous file reading with promises.

Implementation
3-read_file_async.js:
javascript
Copier
Modifier
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read the file asynchronously
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split the file into lines and filter out empty ones
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove the header row
      const header = lines.shift();

      // Initialize data structure to count students
      const students = {};
      let totalStudents = 0;

      lines.forEach((line) => {
        const [firstname, lastname, age, field] = line.split(',');

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
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
How It Works:
Asynchronous File Reading:

The fs.readFile function is used to read the file asynchronously.
If there's an error (e.g., file not found), it rejects the promise with the error message Cannot load the database.
Processing the Data:

The file content is split into lines, with empty lines filtered out.
The header row is removed as it's not part of the student data.
Student data is parsed, grouped by field, and their names are stored.
Logging Results:

Logs the total number of students.
Logs the count and names of students for each field.
Promise Resolution:

Resolves the promise after logging the results.
Example Database (database.csv):
csv
Copier
Modifier
firstname,lastname,age,field
Johann,Smith,25,CS
Arielle,Brown,22,CS
Jonathan,Doe,24,CS
Emmanuel,Doe,23,CS
Guillaume,Smith,23,CS
Katie,Holmes,23,CS
Guillaume,Holmes,25,SWE
Joseph,Allen,22,SWE
Paul,Dupont,24,SWE
Tommy,Doe,23,SWE
Testing:
3-main_0.js (Error Case):
javascript
Copier
Modifier
const countStudents = require('./3-read_file_async');

countStudents('nope.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });
Output:

plaintext
Copier
Modifier
Error: Cannot load the database
3-main_1.js (Successful Case):
javascript
Copier
Modifier
const countStudents = require('./3-read_file_async');

countStudents('database.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });

console.log('After!');
Output:

plaintext
Copier
Modifier
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 3-read_file_async.js
    ├── 3-main_0.js
    ├── 3-main_1.js
    └── database.csv
How to Run:
Place the files in the Node_JS_basic directory.
Test the error case:
bash
Copier
Modifier
node 3-main_0.js
Test the successful case:
bash
Copier
Modifier
node 3-main_1.js
This implementation follows the requirements, uses asynchronous file reading, and logs the expected output while maintaining non-blocking execution.



_____________________________________________

Here’s how to create a small HTTP server using Node.js's http module as specified:

Implementation
4-http.js:
javascript
Copier
Modifier
const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  // Set the response header to plain text
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send the response body
  res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245);

// Export the server for reuse or testing
module.exports = app;
Explanation:
HTTP Server Creation:

The http.createServer() function is used to create the server.
It accepts a callback function (req, res) that handles incoming requests and sends responses.
Response Handling:

Sets the Content-Type header to text/plain to ensure the response is plain text.
Sends the response body with the text "Hello Holberton School!" using res.end().
Listening on Port 1245:

The server listens on port 1245 using app.listen(1245).
Exporting the Server:

The server instance app is exported to allow testing or reusing in other modules.
Testing:
Start the Server:
Run the following command in terminal 1:

bash
Copier
Modifier
node 4-http.js
Test with curl:
In terminal 2, test the server by sending requests to different endpoints:

Default endpoint:

bash
Copier
Modifier
curl localhost:1245 && echo ""
Output:

plaintext
Copier
Modifier
Hello Holberton School!
Any other endpoint:

bash
Copier
Modifier
curl localhost:1245/any_endpoint && echo ""
Output:

plaintext
Copier
Modifier
Hello Holberton School!
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    └── 4-http.js
Expected Behavior:
The server listens on port 1245.
Responds with "Hello Holberton School!" to any HTTP request made to any endpoint.
This implementation fulfills the requirements, ensuring the server responds correctly to all requests.

_________________________________________________________________


Here’s how to create a more complex HTTP server as described:

Implementation
5-http.js:
javascript
Copier
Modifier
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
How It Works:
countStudents Function:

Reads the file asynchronously using fs.readFile.
Processes the CSV file, removing empty lines and grouping students by their field of study.
Resolves with a formatted string containing the number of students and their details.
HTTP Server:

Listens on port 1245.
Handles two paths:
/: Responds with "Hello Holberton School!".
/students: Responds with "This is the list of our students" followed by the processed student data from the CSV file.
Uses the process.argv[2] to get the path to the database file from the command line.
Error Handling:

If the file path is not provided or cannot be read, it responds with "Cannot load the database".
Not Found Handler:

Responds with 404 Not Found for any other endpoints.
Example Database (database.csv):
csv
Copier
Modifier
firstname,lastname,age,field
Johann,Smith,25,CS
Arielle,Brown,22,CS
Jonathan,Doe,24,CS
Emmanuel,Doe,23,CS
Guillaume,Smith,23,CS
Katie,Holmes,23,CS
Guillaume,Holmes,25,SWE
Joseph,Allen,22,SWE
Paul,Dupont,24,SWE
Tommy,Doe,23,SWE
Testing:
Start the Server:
Run the following command in terminal 1:

bash
Copier
Modifier
node 5-http.js database.csv
Test with curl:
Default endpoint:

bash
Copier
Modifier
curl localhost:1245 && echo ""
Output:

plaintext
Copier
Modifier
Hello Holberton School!
/students endpoint:

bash
Copier
Modifier
curl localhost:1245/students && echo ""
Output:

plaintext
Copier
Modifier
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 5-http.js
    ├── database.csv
Notes:
Ensure the database.csv file is correctly formatted.
Test the /students endpoint without providing a database file:
bash
Copier
Modifier
node 5-http.js
Output:
plaintext
Copier
Modifier
Cannot load the database
This implementation fulfills all requirements and handles edge cases effectively.

___________________________________

Here's how to implement the HTTP server using Express as described:

Implementation
6-http_express.js:
javascript
Copier
Modifier
const express = require('express');

// Create an Express app
const app = express();

// Define the root endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for reuse or testing
module.exports = app;
Explanation:
Express Setup:

express() is used to create an Express application.
Defining Routes:

The / endpoint is defined using app.get. When accessed, it responds with the text "Hello Holberton School!".
Listening on Port 1245:

The server listens on port 1245 using app.listen.
Exporting the App:

The app is exported to allow reuse in tests or other modules.
Testing:
Start the Server:
Run the following command in terminal 1:

bash
Copier
Modifier
node 6-http_express.js
Test with curl:
Root endpoint:

bash
Copier
Modifier
curl localhost:1245 && echo ""
Output:

plaintext
Copier
Modifier
Hello Holberton School!
Invalid endpoint:

bash
Copier
Modifier
curl localhost:1245/any_endpoint && echo ""
Output:

html
Copier
Modifier
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /any_endpoint</pre>
</body>
</html>
Installing Express:
If you haven’t installed Express, run the following command:

bash
Copier
Modifier
npm install express
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 6-http_express.js
Notes:
Express automatically handles routes not defined in your application, responding with an HTML error page for invalid endpoints.
The root endpoint (/) responds with the desired plain text.
This implementation meets the requirements and handles both valid and invalid routes effectively.


____________________________________________________________

Here’s the implementation for the more complex HTTP server using Express:

Implementation
7-http_express.js:
javascript
Copier
Modifier
const express = require('express');
const fs = require('fs');

// Function to count students
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      lines.shift(); // Remove the header row

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

// Create an Express app
const app = express();

// Root route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Students route
app.get('/students', async (req, res) => {
  const databasePath = process.argv[2];

  if (!databasePath) {
    res.status(500).send('Cannot load the database');
    return;
  }

  try {
    const studentData = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for reuse or testing
module.exports = app;
How It Works:
countStudents Function:

Reads the database file asynchronously using fs.readFile.
Processes the CSV file, grouping students by their field and counting total students.
Resolves a formatted string with the student data or rejects with an error message if the file cannot be read.
Express Routes:

/:
Responds with "Hello Holberton School!".
/students:
Reads the database file specified as a command-line argument.
Responds with "This is the list of our students" followed by the student data.
If the database file cannot be loaded, it responds with 500 and an error message.
Port 1245:

The server listens on port 1245 using app.listen.
Error Handling:

Properly handles missing database files or invalid file paths with meaningful error messages.
Example Database (database.csv):
csv
Copier
Modifier
firstname,lastname,age,field
Johann,Smith,25,CS
Arielle,Brown,22,CS
Jonathan,Doe,24,CS
Emmanuel,Doe,23,CS
Guillaume,Smith,23,CS
Katie,Holmes,23,CS
Guillaume,Holmes,25,SWE
Joseph,Allen,22,SWE
Paul,Dupont,24,SWE
Tommy,Doe,23,SWE
Testing:
Start the Server:
Run the following command in terminal 1:

bash
Copier
Modifier
node 7-http_express.js database.csv
Test with curl:
Root endpoint:

bash
Copier
Modifier
curl localhost:1245 && echo ""
Output:

plaintext
Copier
Modifier
Hello Holberton School!
/students endpoint:

bash
Copier
Modifier
curl localhost:1245/students && echo ""
Output:

plaintext
Copier
Modifier
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Without a database file:

bash
Copier
Modifier
node 7-http_express.js
curl localhost:1245/students && echo ""
Output:

plaintext
Copier
Modifier
Cannot load the database
Directory Structure:
markdown
Copier
Modifier
holbertonschool-web_back_end/
└── Node_JS_basic/
    ├── 7-http_express.js
    ├── database.csv
Notes:
Ensure the database file is formatted correctly.
Handle edge cases like missing or empty files gracefully.
This implementation meets all the requirements and provides clear error handling for invalid inputs.



________________________________________

Here's a detailed breakdown of how to implement the requested complex HTTP server using Express:

1. Directory Structure
The project will have the following structure:

Copier
Modifier
full_server/
├── controllers/
│   ├── AppController.js
│   ├── StudentsController.js
├── routes/
│   ├── index.js
├── utils.js
├── server.js
2. Implementing the Components
2.1 utils.js
This file contains the readDatabase function to read and process the database asynchronously.

javascript
Copier
Modifier
const fs = require('fs');

const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      lines.shift(); // Remove header row

      const fields = {};

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
};

module.exports = readDatabase;
2.2 controllers/AppController.js
This controller handles the root endpoint (/).

javascript
Copier
Modifier
class AppController {
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
2.3 controllers/StudentsController.js
This controller handles student-related endpoints.

javascript
Copier
Modifier
const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const databasePath = process.argv[2];

    try {
      const fields = await readDatabase(databasePath);

      let output = 'This is the list of our students\n';
      const sortedFields = Object.keys(fields).sort();

      for (const field of sortedFields) {
        const students = fields[field];
        output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      }

      res.status(200).send(output.trim());
    } catch (error) {
      res.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const databasePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const fields = await readDatabase(databasePath);
      const students = fields[major] || [];
      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (error) {
      res.status(500).send(error.message);
    }
  }
}

module.exports = StudentsController;
2.4 routes/index.js
This file defines the routes and links them to the appropriate controllers.

javascript
Copier
Modifier
const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

// Define routes
router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
2.5 server.js
This file initializes the Express server and links the routes.

javascript
Copier
Modifier
const express = require('express');
const router = require('./routes/index');

const app = express();

// Use the defined routes
app.use('/', router);

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;
3. .babelrc File
To enable ES6 support using babel-node, create a .babelrc file in the root directory:

json
Copier
Modifier
{
  "presets": ["@babel/preset-env"]
}
4. package.json Script
Update your package.json to include the dev script:

json
Copier
Modifier
"scripts": {
  "dev": "nodemon --exec babel-node --presets @babel/preset-env ./full_server/server.js ./database.csv"
}
5. Testing the Server
Start the Server:
In terminal 1:

bash
Copier
Modifier
npm run dev
Test Endpoints:
Root endpoint:

bash
Copier
Modifier
curl localhost:1245
Output:

plaintext
Copier
Modifier
Hello Holberton School!
Students endpoint:

bash
Copier
Modifier
curl localhost:1245/students
Output:

plaintext
Copier
Modifier
This is the list of our students
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Students by major (CS):

bash
Copier
Modifier
curl localhost:1245/students/CS
Output:

plaintext
Copier
Modifier
List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Invalid major:

bash
Copier
Modifier
curl localhost:1245/students/French
Output:

plaintext
Copier
Modifier
Major parameter must be CS or SWE
This implementation adheres to all requirements and organizes the server for scalability and maintainability.



--------------------
npx eslint 2-read_file.js --fix
npx eslint 2-read_file.js
--------------------------
Jest
npm test
-------

















