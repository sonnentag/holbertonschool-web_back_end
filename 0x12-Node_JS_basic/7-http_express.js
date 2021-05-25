const express = require('express');
const countStudents = require('./3-read_file_async');

const DB = process.argv[2];
const port = 1245;
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const studentCount = await countStudents(DB);
    res.send('This is the list of our students\n');
    res.send(`${studentCount.join('\n')}`);
  } catch (error) {
    res.send('This is the list of our students\n');
    res.send(`${error.message}`);
  }
});

app.listen(port);

module.exports = app;
