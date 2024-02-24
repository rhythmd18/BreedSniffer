const canvas = document.getElementById("image-canv");
const ctx = canvas.getContext("2d");
const imageInput = document.getElementById("image-input");

imageInput.addEventListener("change", function (event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    const img = new Image();
    img.onload = function () {
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      document.getElementById("upload-btn").style.display = "none";
      document.getElementById("detect-btn").removeAttribute("disabled");
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
});
