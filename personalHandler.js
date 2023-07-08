async function getProfileData() {
    const profileUrl = 'http://kioriatravel.pythonanywhere.com/profile';
    try {
      const response = await fetch(profileUrl);
      if (response.ok) {
        const data = await response.json();
        const { full_name, email, address, phone_number } = data;
        const usernameInputs = document.querySelectorAll('input[name="username"]');
        const emailInputs = document.querySelectorAll('input[name="email"]');
        const passwordInput = document.querySelector('input[name="password"]');
        const phoneInput = document.querySelector('input[name="phone"]');
        
        usernameInputs.forEach(input => {
          input.value = full_name;
        });
  
        emailInputs.forEach(input => {
          input.value = email;
        });
  
        if (passwordInput) {
          passwordInput.value = address;
        }
  
        if (phoneInput) {
          phoneInput.value = phone_number;
        }
      } else {
        console.log('Error retrieving profile data:', response.status);
      }
    } catch (error) {
      console.error('Error retrieving profile data:', error);
    }
  }
  
  // Call the function to populate the form with profile data
  getProfileData();
  
