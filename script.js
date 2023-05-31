
const modal = document.querySelector("#modal");
var openModal = document.querySelectorAll(".booking");
// //const closeModal = document.querySelector(".close-button");

for (var i =0 ; i < openModal.length;i++){
  openModal[i].addEventListener("click", () => {
    modal.showModal();
  });
}

function selectOnly(id){
  var myCheckbox = document.getElementsByName("checkbox");
  Array.prototype.forEach.call(myCheckbox,function(el){
  	el.checked = false;
  });
  id.checked = true;
}

// closeModal.addEventListener("click", () => {
//   modal.close();
// });