#!/usr/bin/bash
exports.converter = function (base) {
  return num => num.toString(base);
};
