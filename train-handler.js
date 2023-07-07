// const hotelContainer = document.getElementById('hotelTicketsContainer');
// const sampleData = [
//     {
//         id:1,
//         name:"tehran",
//         description: "xxxxx",
//         location: "tehran",
//         locationdestenation: "mashhad",
//         imageSrc: "./images/pexels-pascal-borener-113017.jpg",
//         numOf: 20,
//         // date: 
//         // datereverse:
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/page2.html"


//     },
//     {
//         id:2,
//         name:"mashhad",
//         description: "yyyyyyy",
//         location: "mashhad",
//         imageSrc: "./images/pexels-pixabay-358220.jpg",
//         locationdestenation: "tehran",
//         numOf: 10,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/page2.html"

//     },
//     {
//         id:3,
//         name:"shiraz",
//         description: "yyyyyyy",
//         location: "shiraz",
//         imageSrc: "./images/plane222.jpg",
//         locationdestenation: "shiraz",
//         numOf: 30,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/page2.html"

//     },
//     {
//         id:4,
//         name:"tabriz",
//         description: "yyyyyyy",
//         location: "tabriz",
//         imageSrc: "./images/hotel4.jpg",
//         locationdestenation: "mashhad",
//                 numOf: 20,
//                 startDate: new Date("2023-06-28"),
//                 finishDate: new Date("2023-07-05"),
//                 togo: "./forms/page2.html"

//     },
//     {
//         id:5,
//         name:"sari",
//         description: "yyyyyyy",
//         location: "sari",
//         imageSrc: "./images/hotel3.jpg",
//         locationdestenation: "mashhad",
//                 numOf: 20,
//                 startDate: new Date("2023-06-28"),
//                 finishDate: new Date("2023-07-05"),
//                 togo: "./forms/page2.html"

//     },
//     {
//         id:5,
//         name:"esfahan",
//         description: "yyyyyyy",
//         location: "esfahan",
//         imageSrc: "./images/hotel3.jpg",
//         locationdestenation: "mashhad",
//          numOf: 20,
//          startDate: new Date("2023-06-28"),
//          finishDate: new Date("2023-07-05"),
//     }
// ];


// let dataToShow;
// const handleChange = (event) => {
//   const { name, value } = event.target;

//   if (name === 'location') {
//     dataToShow = sampleData.filter(data => data.location.toLowerCase().includes(value.toLowerCase()));
//   } else if (name === 'locationdestenation') {
//     dataToShow = sampleData.filter(data => data.locationdestenation.toLowerCase().includes(value.toLowerCase()));
//   } else if (name === 'numOf') {
//     dataToShow = sampleData.filter(data => data.numOf >= parseInt(value));
//   } else if (name === 'startDate' || name === 'finishDate') {
//     const startDate = new Date(document.getElementById('startDate').value);
//     const finishDate = new Date(document.getElementById('finishDate').value);

//     dataToShow = sampleData.filter(data => {
//       const dataDate = new Date(data.startDate);
//       return dataDate >= startDate && dataDate <= finishDate;
//     });
//   }

//   showData();
// };


  
// // function filterDataByLocation(data, location, locationDestination) {
// //   return data.filter(
// //     item =>
// //       item.location.toLowerCase() === location.toLowerCase() &&
// //       item.locationdestenation.toLowerCase() === locationDestination.toLowerCase()
// //   );
// // }
// // function filterByNumOfPeople(data, num) {
// //     return data.filter(item => item.numOf === num);
// //   }
  
// //   const filteredData = filterByNumOfPeople(sampleData, 2);
// //   console.log(filteredData);

// function filterByNumOfPeople(data, condition) {
//     if (condition === 'below') {
//       return data.filter(item => item.numOf < 20);
//     } else if (condition === 'more') {
//       return data.filter(item => item.numOf >= 20);
//     } else {
//       return data; // Return the original array if the condition is invalid
//     }
//   }
  
//   const filteredDataBelow20 = filterByNumOfPeople(sampleData, 'below');
//   console.log('Below 20:', filteredDataBelow20);
  
//   const filteredDataMoreThan20 = filterByNumOfPeople(sampleData, 'more');
//   console.log('More than 20:', filteredDataMoreThan20);


//   const showData = () => {
//     if(!dataToShow){
//         dataToShow = sampleData;
//     }
//     while (hotelContainer.firstChild) {
//         hotelContainer.removeChild(hotelContainer.firstChild);
//     }
//     dataToShow.map(data => {
//         // Create the required HTML elements
//         const colDiv = document.createElement('div');
//         colDiv.classList.add('col');
      
//         const cardDiv = document.createElement('div');
//         cardDiv.classList.add('card222');
      
//         const img = document.createElement('img');
//         img.src = data.imageSrc;
//         img.classList.add('card-img-top');
//         img.alt = '...';
      
//         const cardBodyDiv = document.createElement('div');
//         cardBodyDiv.classList.add('card222-body');
      
//         const titleH5 = document.createElement('h5');
//         titleH5.classList.add('card-title');
//         titleH5.textContent = data.name;
      
//         const descriptionP = document.createElement('p');
//         descriptionP.classList.add('card-text');
//         descriptionP.textContent = data.description;  
//         const button = document.createElement('button');
//         const buttonLink = document.createElement('a');
//         buttonLink.href = './forms/index.html';
//         buttonLink.classList.add('btn', 'btn-primary');
//         buttonLink.textContent = 'more information';
//         button.appendChild(buttonLink);
      
//         // Append the elements to build the hierarchy
//         cardBodyDiv.appendChild(titleH5);
//         cardBodyDiv.appendChild(descriptionP);
//         cardBodyDiv.appendChild(button);
      
//         cardDiv.appendChild(img);
//         cardDiv.appendChild(cardBodyDiv);
      
//         colDiv.appendChild(cardDiv);
      
//         hotelContainer.appendChild(colDiv);
//       });
//   }

//   showData();


const hotelContainer = document.getElementById('hotelTicketsContainer');
// const sampleData = [
//     {
//         id:1,
//         name:"tehran",
//         description: "xxxxx",
//         location: "tehran",
//         locationdestenation: "mashhad",
//         imageSrc: "./images/pexels-pascal-borener-113017.jpg",
//         numOf: 20,
//         // date: 
//         // datereverse:
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/index.html"
//     },
//     {
//         id:2,
//         name:"mashhad",
//         description: "yyyyyyy",
//         location: "mashhad",
//         imageSrc: "./images/pexels-pixabay-358220.jpg",
//         locationdestenation: "tehran",
//         numOf: 10,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/flight1.html"
//     },
//     {
//         id:3,
//         name:"shiraz",
//         description: "yyyyyyy",
//         location: "shiraz",
//         imageSrc: "./images/plane222.jpg",
//         locationdestenation: "shiraz",
//         numOf: 30,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/flight2.html"
//     },
//     {
//         id:4,
//         name:"tabriz",
//         description: "yyyyyyy",
//         location: "tabriz",
//         imageSrc: "./images/hotel4.jpg",
//         locationdestenation: "mashhad",
//         numOf: 20,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/flight1.html"

//     },
//     {
//         id:5,
//         name:"sari",
//         description: "yyyyyyy",
//         location: "sari",
//         imageSrc: "./images/hotel3.jpg",
//         locationdestenation: "mashhad",
//         numOf: 20,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/flight1.html"
//     },
//     {
//         id:5,
//         name:"esfahan",
//         description: "yyyyyyy",
//         location: "esfahan",
//         imageSrc: "./images/hotel3.jpg",
//         locationdestenation: "mashhad",
//         numOf: 20,
//         startDate: new Date("2023-06-28"),
//         finishDate: new Date("2023-07-05"),
//         togo: "./forms/flight1.html"
//     }
// ];

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

const showData = () => {
    if (!dataToShow) {
        dataToShow = sampleData;
    }
    while (hotelContainer.firstChild) {
        hotelContainer.removeChild(hotelContainer.firstChild);
    }
    dataToShow.map(data => {
        // Create the required HTML elements
        const colDiv = document.createElement('div');
        colDiv.classList.add('col');
      
        const cardDiv = document.createElement('div');
        cardDiv.classList.add('card222');
      
        const img = document.createElement('img');
        img.src = data.imageSrc;
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
      
        const button = document.createElement('button');
        const buttonLink = document.createElement('a');
        buttonLink.href = data.togo;
        buttonLink.classList.add('btn', 'btn-primary');
        buttonLink.textContent = 'more information';
        button.appendChild(buttonLink);
      
        // Append the elements to build the hierarchy
        cardBodyDiv.appendChild(titleH5);
        cardBodyDiv.appendChild(descriptionP);
        cardBodyDiv.appendChild(button);
      
        cardDiv.appendChild(img);
        cardDiv.appendChild(cardBodyDiv);
      
        colDiv.appendChild(cardDiv);
      
        hotelContainer.appendChild(colDiv);
    });
}

showData();
