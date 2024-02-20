"use strict";

let arr = ["Rahman", "Ayhan", "Ahmed", "Ali"];

for (let i = 0; i < arr.length; i++) {
  const element = arr[i];
  console.log(`Элемент ${i}: ${element}`);
}

for (const name of arr) {
  if (name.length < 4) {
    console.log("nobody");
  } else {
    console.log(name);
  }
}