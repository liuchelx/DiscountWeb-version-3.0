$(document).ready(function() {
    console.log("ready");
    console.log("countDownArea1");
    console.log("countDownArea2");
    console.log("countDownArea3");
    console.log("countDownArea4");
    countDown('countDownArea1');
    
    countDown('countDownArea2');
   
    countDown('countDownArea3');
    
    countDown('countDownArea4');
    
    //console.log(document.getElementById(forloopID).innerHTML)

    
});

function countDown(forloopID){

        var pTime = new Date(document.getElementById(forloopID).innerHTML).getTime();
  
        var x = setInterval(function() {
        
            var now = new Date().getTime();
 
            var distance = pTime - now;

            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) + 24* Math.floor(distance / (1000 * 60 * 60 * 24));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
            document.getElementById(forloopID).innerHTML =hours + "h "+ minutes + "m " + seconds + "s ";
    
        }, 1000);
    }