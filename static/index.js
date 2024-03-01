const canvas = document.getElementById("image-canv");
const ctx = canvas.getContext("2d");
const imageInput = document.getElementById("image-input");
const loadingImgEl = document.getElementById("loading-img");
const detectBtnEl = document.getElementById("detect-btn");
const rmBtnEl = document.getElementById("rm-btn");
const predictionTextEl = document.getElementById("prediction-text");
const predictionTextContent = predictionTextEl.innerHTML;
let imgFile;

imageInput.addEventListener("change", function (event) {
  imgFile = event.target.files[0]; // get the first file
  const reader = new FileReader(); // create a reader

  reader.onload = function () {
    // when the reader has loaded
    const img = new Image(); // create an image
    img.onload = function () {
      // when the image has loaded
      let width = img.width;
      let height = img.height;
      const aspectRatio = width / height;

      if (canvas.width < width) {
        width = canvas.width;
        height = width / aspectRatio;
      }

      if (canvas.height < height) {
        height = canvas.height;
        width = height * aspectRatio;
      }

      const x = (canvas.width - width) / 2;
      const y = (canvas.height - height) / 2;

      ctx.drawImage(img, x, y, width, height); // draw the image on the canvas
      document.getElementById("upload-btn").style.display = "none"; // hide the upload button
      detectBtnEl.removeAttribute("disabled"); // enable the detect button
      detectBtnEl.className = "detect-btn-active";
      rmBtnEl.removeAttribute("disabled"); // enable the remove button
      rmBtnEl.className = "rm-btn-active";
    };
    img.src = reader.result; // set the image source
  };
  reader.readAsDataURL(imgFile);
});

function detectBreed() {
  loadingImgEl.style.display = "flex";
  let formdata = new FormData();
  formdata.append("file", imgFile);
  fetch("/predict/", {
    method: "POST",
    body: formdata,
  })
    .then((response) => response.json()) // parse the response as JSON
    .then((result) => {
      let res = result["status"];
      if (res === "Success") {
        const breed = result["breed"];
        loadingImgEl.style.display = "none";
        displayBreed(breed);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function displayBreed(breed) {
  predictionTextEl.className = "post-detection";
  predictionTextEl.textContent = `A ${breed}`;
}

function removeImage() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  document.getElementById("upload-btn").style.display = "";
  predictionTextEl.innerHTML = predictionTextContent;
  detectBtnEl.disabled = true;
  detectBtnEl.className = "detect-btn-disabled";
  rmBtnEl.disabled = true;
  rmBtnEl.className = "rm-btn-disabled";
  predictionTextEl.className = "pre-detection";
}
