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


/*--Opening and Closing Collapsible--*/
 document.querySelectorAll('.collapsible_button').forEach(button =>{
    button.addEventListener('click', () => {
        button.classList.toggle('.active, .collapsible_button:hover');
    });
});

/*------------MODAL=-----------*/

var modal = document.getElementById('simModal');

//Open and close modal
var modBtn = document.getElementById('modalBtn');
var closeBtn = document.getElementsByClassName('closeBtn')[0];

//Open and close listener
modBtn.addEventListener('click', openModal); 
//closeBtn.addEventListener('click', closeModal);

//Outside Click
window.addEventListener('click', outsideClick);

function openModal()
{
  modal.style.display = 'block';
}

/*
function closeModal()
{
  modal.style.display = 'none';
}
*/
function outsideClick(e)
{
  if(e.target == modal)
  {
    modal.style.display = 'none';
  }
}