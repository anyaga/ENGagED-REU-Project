
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