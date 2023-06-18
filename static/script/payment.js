var close_button = document.getElementById("return-home").addEventListener("click", function() {
    window.location.href = '/';
  });

var back_button = document.getElementById("return-guest").addEventListener("click", function() {
    window.history.back();
  });