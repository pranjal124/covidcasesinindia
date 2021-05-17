var use2 = document.getElementById("mobile");
function fo3(e){
    var value=document.getElementById("mobile").value;
    if(value.length ==9)
    { var small=document.getElementById("small1");
      small.style.color="green";
      small.innerHTML="Mobile number is valid";}
    else{var small=document.getElementById("small1");
    small.style.color="red";
      small.innerHTML="Mobile number should be 10 digit and right";}
    }
use2.addEventListener("keypress",fo3,false);
