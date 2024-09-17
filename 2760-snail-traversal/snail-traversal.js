/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
  // Check for invalid input: if the array size doesn't match the grid size, return an empty array
  if (rowsCount * colsCount !== this.length) {
    return [];
  }

  // Initialize an empty 2D array with given dimensions
  const result = Array.from({ length: rowsCount }, () => Array(colsCount).fill(null));
  let index = 0;

  // Fill the result matrix in snail traversal order
  for (let col = 0; col < colsCount; col++) {
    if (col % 2 === 0) {
      // Fill from top to bottom
      for (let row = 0; row < rowsCount; row++) {
        result[row][col] = this[index++];
      }
    } else {
      // Fill from bottom to top
      for (let row = rowsCount - 1; row >= 0; row--) {
        result[row][col] = this[index++];
      }
    }
  }

  return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */