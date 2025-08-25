const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Lire le fichier de manière asynchrone
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Diviser le contenu du fichier en lignes, filtrer les lignes vides
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Enlever la ligne d'en-tête
      lines.shift();

      // Initialisation de la structure de données pour compter les étudiants
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

      // Afficher le nombre total d'étudiants
      console.log(`Number of students: ${totalStudents}`);

      // Afficher le nombre d'étudiants et leurs noms pour chaque domaine
      for (const [field, names] of Object.entries(students)) {
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
