import { readDatabase } from '../utils.js';

export default class StudentsController {
    static async getAllStudents(req, res) {
        const dbPath = process.argv[2];

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
            res.status(200).send(response.join('\n'));
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const dbPath = process.argv[2];
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const data = await readDatabase(dbPath);
            if (data[major]) {
                res.status(200).send(`List: ${data[major].join(', ')}`);
            } else {
                res.status(200).send('List:');
            }
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
