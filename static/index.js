const canvas = document.getElementById("image-canv");
const ctx = canvas.getContext("2d");
const imageInput = document.getElementById("image-input");

imageInput.addEventListener("change", function (event) {
  const file = event.target.files[0]; // get the first file
  const reader = new FileReader(); // create a reader

  reader.onload = function () {
    // when the reader has loaded
    const img = new Image(); // create an image
    img.onload = function () {
      // when the image has loaded
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height); // draw the image on the canvas
      document.getElementById("upload-btn").style.display = "none"; // hide the upload button
      document.getElementById("detect-btn").removeAttribute("disabled"); // enable the detect button
    };
    img.src = reader.result; // set the image source
  };
  reader.readAsDataURL(file);
});
