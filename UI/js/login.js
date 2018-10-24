const form = document.getElementById("form-login");
const username = document.getElementById("username");
const password = document.getElementById("password");

form.addEventListener("submit",(event)=>{event.preventDefault();

    if(username.value ==="admin" && password.value =="password"){
    window.location= "admin.html";

      
    }else if(username.value ==="attendant" && password.value =="password"){
    window.location="attendant.html";

      }else{
          alert("Invalid username or password");
          username.value ="";
          password.value ="";
      }
});      















 