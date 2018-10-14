const form = document.getElementById("form");
const username = document.getElementById("username");
const password = document.getElementById("password");

form.addEventListener("LOGIN",(event)=>{event.preventDefault();

    if(username.value =="admin" && password =="password"){
    window.location="./admin.html";
    
      }else if(username.value =="attendant" && password =="password"){
    window.location="./attendant.html";

      }else{
          alert("Invalid username or password");
          username.value ="";
          password.value ="";
      }
});      















 