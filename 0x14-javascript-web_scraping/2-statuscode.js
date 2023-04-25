#!/usr/bin/node

const request = require('request');
const url = process.argb[2];

request(url, (error, response, body) => {
  if (error) throw error;

  console.log(response.statusCode);
});
