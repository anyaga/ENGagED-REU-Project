//Fix this function

function onClick() 
{
    /*document.getElementById("demo").innerHTML = --; */// should open a pop-up
}

  
  // Change style of navbar on scroll
  window.onscroll = function() {myFunction()};
  function myFunction() {
      var navbar = document.getElementById("myNavbar");
      if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
          navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
      } else {
          navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
      }
  }
  
  // Used to toggle the menu on small screens when clicking on the menu button
  function toggleFunction() {
      var x = document.getElementById("navDemo");
      if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
      } else {
          x.className = x.className.replace(" w3-show", "");
      }
  }

  function myPop() 
  {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }

  /*---Collapsible--
  var coll = document.getElementsByClassName("collapsible");
  var i;
  
  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }
  */

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
  });
  
  /*--Opening and Closing Collapsible--*/
 /* var instance = M.Collapsible.getInstance(elem);*/

 document.querySelectorAll('.collapsible_button').forEach(button => {
    button.addEventListener('click', () => {
        //const collapsibleContent = button.nextElementSibling;
        button.classList.toggle('.active, .collapsible_button:hover');
        /*
        if(button.classList.contains('.active, .collapsible_button:hover')) {
            collapsibleContent.style.maxHeight = collapsible.scrollHeight + 'px';
        } else {
            collapsibleContent.style.maxHeight = 0;
        }
        */
    });
 });
