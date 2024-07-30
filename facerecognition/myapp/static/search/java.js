const dropArea = document.getElementById("drop-area");
const imputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");


imputFile.addEventListener("change", uploadImage);

function uploadImage(){
   
   let imgLink = URL.createObjectURL(imputFile.files[0]);
   imageView.style.backgroundImage = `url(${imgLink})`;
   imageView.textContent = "";
   imageView.style.border= 0;

}
dropArea.addEventListener("dragover", function(e){
    e.preventDefault();
});
dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    imputFile.files = e.dataTransfer.files;
    uploadImage();
});
