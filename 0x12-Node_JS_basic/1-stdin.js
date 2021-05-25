console.log("Welcome to Holberton School, what is your name?");
process.stdin.on('data', (chunk) => {
  let name = chunk.toString();
  if (name) process.stdout.write("Your name is: " + name);
});
process.stdin.on('end', () => {
  console.log("This important software is now closing");
});
