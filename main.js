

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('login-container');
const popup = getElementById("btncv2")



signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

popup.addEventListener('click', () => {
                          const box = document.getElementsByClassName('pop-up');

                          box.style.display = 'none';
                          });                          
                          

                          
    
                        