#!/usr/bin/node
module.export = class Square extends require('./4-rectangle.js/Rectangle') {
  constructor (size) {
    super(size, size);
  }
};
