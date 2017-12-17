function animate() {
  $(".card").hide();

  $(".card").each(function(index) {
    var that = this;
    setTimeout(function() {
      $(that).slideDown("slow")
    }, 120 + 80*index);
  });
}

animate();
