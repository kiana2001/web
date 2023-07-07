


const hotelContainer = document.getElementById('hotelTicketsContainer');


const selectElementStart = document.getElementById('flightStartCitySelect');
const selectElementEnd = document.getElementById('flightEndCitySelect');
const startDate = document.getElementById("startDate");
const num_passangers = document.getElementById("flightPassangers");
const is_two_way_travel = document.getElementById("twoWayCheckbox");
const returnDate = document.getElementById("returnDate");

function showSities(cities) {

    for (const city of cities) {
        const newOption = document.createElement('option');
        newOption.textContent = city.name;
        newOption.value = city.name;
        selectElementStart.appendChild(newOption);
    }

    for (const city of cities) {
      const newOption = document.createElement('option');
      newOption.textContent = city.name;
      newOption.value = city.name;
      selectElementEnd.appendChild(newOption);
  }

}

async function getCities() {
    const cityUrl = "http://kioriatravel.pythonanywhere.com/locations";
    try {
        const response = await fetch(cityUrl, {
            method: "GET",
        })
        
        const cities = await response.json();
        showSities(cities);
        
    } catch (error) {
        console.log(error);
    }
}

getCities();
const showFlightsButton = document.getElementById("show-flight-button");

let sampleData = [];

async function getFlights() {
    const hotelUrl = "http://kioriatravel.pythonanywhere.com/flights/search?";
    
    let URLParams = {};
    if (is_two_way_travel.checked) {
      URLParams = new URLSearchParams({
        departure_city: selectElementStart.value,
        arrival_city: selectElementEnd.value,
        departure_date: startDate.value,
        num_passengers: num_passangers.value,
        is_round_trip: true,
        return_date: returnDate.value
      })
    } else {
      URLParams = new URLSearchParams({
        departure_city: selectElementStart.value,
        arrival_city: selectElementEnd.value,
        departure_date: startDate.value,
        num_passengers: num_passangers.value,
      })
    }
    try {
        const response = await fetch(hotelUrl + URLParams, {
            method: "GET",
        })
   
        const data = await response.json();
        sampleData = data
        console.log(data);
        showData(sampleData);
       
    } catch (error) {
        console.log(error);
    }
}

showFlightsButton.addEventListener("click", getFlights)

let dataToShow;

const handleChange = (event) => {
  const { name, value } = event.target;

  if (name === 'location') {
    dataToShow = sampleData.filter(data => data.location.toLowerCase().includes(value.toLowerCase()));
  } else if (name === 'locationdestenation') {
    dataToShow = sampleData.filter(data => data.locationdestenation.toLowerCase().includes(value.toLowerCase()));
  } else if (name === 'numOf') {
    dataToShow = sampleData.filter(data => data.numOf >= parseInt(value));
  } else if (name === 'startDate' || name === 'finishDate') {
    const startDate = new Date(document.getElementById('startDate').value);
    const finishDate = new Date(document.getElementById('finishDate').value);

    dataToShow = sampleData.filter(data => {
      const dataDate = new Date(data.startDate);
      return dataDate >= startDate && dataDate <= finishDate;
    });
  }

  showData();
};

function filterByNumOfPeople(data, condition) {
    if (condition === 'below') {
      return data.filter(item => item.numOf < 20);
    } else if (condition === 'more') {
      return data.filter(item => item.numOf >= 20);
    } else {
      return data; // Return the original array if the condition is invalid
    }
}

const filteredDataBelow20 = filterByNumOfPeople(sampleData, 'below');
console.log('Below 20:', filteredDataBelow20);

const filteredDataMoreThan20 = filterByNumOfPeople(sampleData, 'more');
console.log('More than 20:', filteredDataMoreThan20);

const showData = (sampleData) => {
  if (!dataToShow) {
      dataToShow = sampleData;
  }
  while (hotelContainer.firstChild) {
      hotelContainer.removeChild(hotelContainer.firstChild);
  }
  dataToShow.map(data => {
      const colDiv = document.createElement('div');
      colDiv.classList.add('col');

      const cardDiv = document.createElement('div');
      cardDiv.classList.add('card222');

      const img = document.createElement('img');
      img.src = data.image_url;
      img.classList.add('card-img-top');
      img.alt = '...';

      const cardBodyDiv = document.createElement('div');
      cardBodyDiv.classList.add('card222-body');

      const titleH5 = document.createElement('h5');
      titleH5.classList.add('card-title');
      titleH5.textContent = data.name;

      const descriptionP = document.createElement('p');
      descriptionP.classList.add('card-text');
      descriptionP.textContent = data.description;

      // const button = document.createElement('button');
      const button = document.createElement('button');
      button.classList.add('btn', 'btn-primary');
      button.textContent = 'more information';

      // Add an event listener to the button element
      button.addEventListener('click', () => {
          // Handle the redirection to page2.html
          window.location.href = './forms/flight' + data.id +'.html';
      });
      // const buttonLink = document.createElement('a');
      // buttonLink.href = data.togo;
      // buttonLink.classList.add('btn', 'btn-primary');
    
      // button.appendChild(buttonLink);

      cardBodyDiv.appendChild(titleH5);
      cardBodyDiv.appendChild(descriptionP);
      cardBodyDiv.appendChild(button);

      cardDiv.appendChild(img);
      cardDiv.appendChild(cardBodyDiv);

      colDiv.appendChild(cardDiv);

      hotelContainer.appendChild(colDiv);
  });
}

