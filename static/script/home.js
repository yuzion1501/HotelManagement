
const reservation_form = document.querySelector("#modal");
var openModal = document.querySelectorAll(".booking");
const room_id_input = document.getElementById('room-id-input');

// for (var i =0 ; i < openModal.length;i++){
//   openModal[i].addEventListener("click", () => {
//     reservation_form.showModal();
//   });
// }

openModal.forEach(button => {
  button.addEventListener('click', function() {
      // Get the room ID from the data attribute
      reservation_form.showModal();
      const id = button.closest('.room').dataset.roomId;
      room_id_input.value = id;
  })
})

var login_dialog = document.querySelector(".login_dialog");
var login = document.querySelector(".login");
// login.innerHTML = "terafsda"

login.addEventListener("click", () => {
  login_dialog.showModal();
});

var admin_login_dialog = document.querySelector(".admin-dialog");
var login_as_admin = document.querySelector("#admin_button");
login_as_admin.addEventListener("click", () => {
  login_dialog.close();
  admin_login_dialog.showModal();
});

var close_button = document.getElementById("close_button").addEventListener("click", function() {
  window.location.href = "/home";
});



function showNotification() {
  alert('Thank you for submitting the form!');
}

// function selectOnly(id){
//   var myCheckbox = document.getElementsByName("checkbox");
//   Array.prototype.forEach.call(myCheckbox,function(el){
//   	el.checked = false;
//   });
//   id.checked = true;
// }

// closeModal.addEventListener("click", () => {
//   modal.close();
// });