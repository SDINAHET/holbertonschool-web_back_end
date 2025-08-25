import { readDatabase } from '../utils.js';

export default class StudentsController {
    /**
     * Handles the /students route.
     * @param {Object} req - The HTTP request object.
     * @param {Object} res - The HTTP response object.
     */
    static async getAllStudents(req, res) {
        const dbPath = process.argv[2];

        if (!dbPath) {
            res.status(500).send('Cannot load the database');
            return;
        }

        try {
            const data = await readDatabase(dbPath);
            const response = ['This is the list of our students'];
            Object.keys(data)
                .sort()
                .forEach((field) => {
                    response.push(
                        `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}`
                    );
                });
            res.status(200).send(`${response.join('\n')}\n`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    /**
     * Handles the /students/:major route.
     * @param {Object} req - The HTTP request object.
     * @param {Object} res - The HTTP response object.
     */
    static async getAllStudentsByMajor(req, res) {
        const dbPath = process.argv[2];
        const { major } = req.params;

        if (!dbPath) {
            res.status(500).send('Cannot load the database');
            return;
        }

        if (major !== 'CS' && major !== 'SWE') {
            res.status(500).send('Major parameter must be CS or SWE');
            return;
        }

        try {
            const data = await readDatabase(dbPath);
            const students = data[major] || [];
            res.status(200).send(`List: ${students.join(', ')}\n`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
