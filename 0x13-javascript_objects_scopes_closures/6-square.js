#!/usr/bin/node
module.exports = class Square extends require('./5-square/Square') {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char);
      }
      process.stdout.write('\n');
    }
  }
};
