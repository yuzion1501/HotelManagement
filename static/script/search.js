// var home = document.getElementById("returnHome").addEventListener("click", function() {
//     window.location.href = "/home";
//   });

  
const reservation_form = document.querySelector("#modal");
var openModal = document.querySelectorAll(".booking");
const room_id_input = document.getElementById('room-id-input');

  openModal.forEach(button => {
    button.addEventListener('click', function() {
        // Get the room ID from the data attribute
        reservation_form.showModal();
        const id = button.closest('.room').dataset.roomId;
        room_id_input.value = id;
    })
  })

  function showNotification() {
    alert('Thank you for submitting the form!');
  }

  // openModal.forEach(button => {
  //   button.addEventListener('click', function() {
  //       // Get the room ID from the data attribute
  //       reservation_form.close();
  //   })
  // })

  var close_button = document.getElementById("return-home").addEventListener("click", function() {
    window.location.href = '/';
  });

  var close_button = document.getElementById("close-form").addEventListener("click", function() {
    reservation_form.close();
  });
  