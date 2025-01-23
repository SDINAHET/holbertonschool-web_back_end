const fs = require('fs');

/**
 * Reads the database file and organizes students by field.
 * @param {string} filePath - Path to the database file.
 * @returns {Promise<object>} - Promise resolving to an object with students grouped by field.
 */
const readDatabase = (filePath) => new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            reject(new Error('Cannot load the database'));
            return;
        }

        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = {};

        lines.slice(1).forEach((line) => {
            const [firstname, , , field] = line.split(',');

            if (!students[field]) {
                students[field] = [];
            }
            students[field].push(firstname);
        });

        resolve(students);
    });
});

module.exports = { readDatabase };
