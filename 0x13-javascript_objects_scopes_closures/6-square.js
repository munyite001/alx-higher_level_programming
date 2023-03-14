#!/usr/bin/node
module.exports = class Square extends require('./5-square/Square') {
  charPrint (c) {
    const char = c === undefined ? 'X' : 'C';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(char);
      }
      process.stdout.write('\n');
    }
  }
};
