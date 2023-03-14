#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js/Rectangle') {
  constructor (size) {
    super(size, size);
  }
};
