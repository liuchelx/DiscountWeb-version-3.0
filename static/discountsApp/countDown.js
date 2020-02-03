$(document).ready(function() {
  //since we have four items to display on the index, then do the fucntion four times
  countDown("countDownArea1");

  countDown("countDownArea2");

  countDown("countDownArea3");

  countDown("countDownArea4");
});

function countDown(forloopID) {
  let date = $("#" + forloopID).html();
  if (date) {
    var pTime = new Date(date);
    
  }
  var x = setInterval(function() {
    var now = new Date().getTime();
    var EndTime = pTime.getTime();
    var distance = EndTime - now;

    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) + 24 * Math.floor(distance / (1000 * 60 * 60 * 24));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    $("#" + forloopID).html(`${hours}h ${minutes} m ${seconds}s`);
  }, 1000);
}
