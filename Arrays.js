// introduction to arrays
var array1 = [1, 2, 3, 4];
// pushing into the array
array1.push(5);
array1.push(7);
array1.push(50);
console.log(array1);

// deleting items from the array
// pop removes the last element in the array
console.log("Popping out elements: ");
array1.pop();
array1.pop();
console.log(array1[0]);

// array iterations
console.log("array iterations");
console.log("original array");
console.log(array1);

var len = array1.length;
console.log(len);

for (var i = 0, len; i < len; i++) {
  console.log(array1[i]);
}
