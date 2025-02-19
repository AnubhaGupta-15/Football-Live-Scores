function FirstName(fname) {
    var message = document.getElementsByClassName("error-message");
    var letters = /^[A-Za-z]+$/;
    if ( fname =="" || fname.match(letters)) {
      text="";
      message[0].innerHTML = text;
      return true;
    }
    else {
      text="First name should contain only letters";
      message[0].innerHTML = text;
      return false;
    }
  }