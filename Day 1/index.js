const fs = require('fs').promises;
const path = require('path');

const files = ['file1.txt', 'file2.txt', 'file3.txt'];

async function readFileAsync(fileName) {
  const filePath = path.join(__dirname, 'files', fileName);

  console.log(`\n Starting to read: ${fileName}`);

  try {
    const data = await fs.readFile(filePath);
    console.log(` Finished reading ${fileName}: ${data.toString().trim()}`);
  } catch (err) {
    console.error(` Error reading ${fileName}:`, err.message);
  }
}

async function processFiles() {
  console.log('\n Microtask: process.nextTick');
  process.nextTick(() => {
    console.log(' process.nextTick executed');
  });

  console.log('\n Timer: setTimeout');
  setTimeout(() => {
    console.log(' setTimeout executed after 0ms');
  }, 0);

  console.log('\n Immediate: setImmediate');
  setImmediate(() => {
    console.log(' setImmediate executed');
  });

  for (const file of files) {
    await readFileAsync(file);
  }

  console.log('\n All files processed.');
}

processFiles();
