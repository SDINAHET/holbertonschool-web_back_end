import fs from 'fs/promises';

export async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.split('\n').filter((line) => line);
        const fields = {};

        lines.slice(1).forEach((line) => {
            const [firstname, , , field] = line.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });

        return fields;
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}
