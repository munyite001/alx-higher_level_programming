#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + episode, function (error, response, body) {
  if (error) throw error;
  if (response.statusCode === 200) {
    const res = JSON.parse(body);
    console.log(res.title);
  } else {
    console.log('Error code: ', response.statusCode);
  }
});
