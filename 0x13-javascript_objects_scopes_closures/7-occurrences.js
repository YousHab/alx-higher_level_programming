#!/usr/bin/node
function nbOccurences (list, searchElement) {
  return list.reduce((count, elt) => elt === searchElement ? count++ : count, 0);
}
module.exports = nbOccurences;
