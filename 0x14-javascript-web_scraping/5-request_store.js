#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, (error, body) => {
  if (error) throw error;
  fs.writeFile(path, body, 'utf-8');
});
