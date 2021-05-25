const fs = require('fs');

function countStudents(path) {

  try {
    let data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  data = data.slice(1, data.length - 1);
  console.log(`Number of students: ${data.length}`);
  const fields = {};

  for (const row of data) {
    const student = row.split(',');
    if (!fields[student[3]]) {
      fields[student[3]] = [];
    }

    fields[student[3]].push(student[0]);
  }

  for (const field in fields) {
    if (field) {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    }
  }
};

module.exports = countStudents;
