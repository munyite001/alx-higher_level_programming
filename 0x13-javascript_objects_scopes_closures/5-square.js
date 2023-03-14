#!/usr/bin/node
import Rectangle from './4-rectangle.js/Rectangle';

module.export = class Square extends Rectangle {
  constructor (size, w, h) {
    super(w, h);
    this.size = size;
  }
};
