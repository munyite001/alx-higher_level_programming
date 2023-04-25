#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const idx in movies) {
      const filmChars = movies[idx].characters;
      for (const charIdx in filmChars) {
        if (filmChars[charIdx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error: code', response.statusCode);
  }
});
