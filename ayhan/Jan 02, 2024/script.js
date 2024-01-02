"use strict";

const btn = document.querySelector("#btn");
const images = document.querySelectorAll(".img");

images[0].style.display = "block";
images[1].style.display = "none";
images[2].style.display = "none";

btn.addEventListener("click", () => {
  if (images[0].style.display === "block") {
    images[1].style.display = "block";
    images[0].style.display = "none";
  } else if (images[1].style.display === "block") {
    images[2].style.display = "block";
    images[1].style.display = "none";
  } else {
    images[0].style.display = "block";
    images[2].style.display = "none";
  }
});