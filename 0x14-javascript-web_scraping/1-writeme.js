#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const data = String(process.argv[3]);

fs.writeFile(file, data, 'utf-8', function (error) {
  if (error) throw error;
});
