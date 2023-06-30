function toggleData() {
    var data1 = document.getElementById("data1");
    var data2 = document.getElementById("data2");
    var Employer = document.getElementById("Employer");
    var Employee = document.getElementById("Employee");
    if (data1.style.display === "none") {
      data1.style.display = "block";
      Employee.style.display = "block";
      data2.style.display = "none";
      Employer.style.display="none";

    } else {
      data1.style.display = "none";
      Employee.style.display = "none";
      data2.style.display = "block";
      Employer.style.display="block";
    }
    return x
  }
 function Register() {
  var popup = document.getElementById("Register");
  popup.classList.toggle("show");
}
  function hireNow() {
  var popupe = document.getElementById("hire");
  popupe.classList.toggle("show");
  }
  function Login() {
  var loginEl = document.getElementById("login");
   loginEl.classList.toggle("show");
}

