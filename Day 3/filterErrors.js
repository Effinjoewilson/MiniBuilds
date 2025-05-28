const fs = require('fs');
const readline = require('readline');

// Input and output file streams
const readStream = fs.createReadStream('server.log');
const writeStream = fs.createWriteStream('error.log');

// Read line-by-line
const rl = readline.createInterface({
  input: readStream,
  crlfDelay: Infinity,
});

// Filter and write
rl.on('line', (line) => {
  if (line.toLowerCase().includes('error')) {
    writeStream.write(line + '\n');
  }
});

rl.on('close', () => {
  console.log('Finished filtering error logs.');
});
