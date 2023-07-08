function getCookie(c_name) {
  if (document.cookie.length > 0) {
    c_start = document.cookie.indexOf(c_name + '=');
    if (c_start != -1) {
      c_start = c_start + c_name.length + 1;
      c_end = document.cookie.indexOf(';', c_start);
      if (c_end == -1) {
        c_end = document.cookie.length;
      }
      return unescape(document.cookie.substring(c_start, c_end));
    }
  }
  return '';
}

async function getProfileData() {
    const profileUrl = 'http://kioriatravel.pythonanywhere.com/profile/';
    try {
      const response = await fetch(profileUrl, {
        method:"GET",
        headers: {
          "Authorization": "Bearer " + getCookie("access_token")
        }
      });
      if (response.ok) {
        const data = await response.json();
        
        const { first_name, last_name, email, ssn, phone_number } = data;
        const firstNameInput = document.querySelector('input[name="firstNamePersonal"]');
        const lastNameInput = document.querySelector('input[name="lastNamePersonal"]');        
        const emailInput = document.querySelector('input[name="emailPersonal"]');
        const phoneInput = document.querySelector('input[name="phoneNumber"]');
        const ssnInput = document.querySelector('input[name="ssn"]');
  
        if (firstNameInput) firstNameInput.value = first_name;
        if (lastNameInput) lastNameInput.value = last_name;
        if (emailInput) emailInput.value = email;
        if (phoneInput) phoneInput.value = phone_number;
        if (ssnInput) ssnInput.value = ssn;

      } else {
        console.log('Error retrieving profile data:', response);
      }
    } catch (error) {
      console.error('Error retrieving profile data:', error);
    }
  }
  
  // Call the function to populate the form with profile data
  getProfileData();
  
