const hotelContainer = document.getElementById('hotelTicketsContainer');
const sampleData = [
    {
        id:1,
        name:"tehran",
        description: "xxxxx",
        location: "tehran",
        imageSrc: "./images/hotel1.jpg",
        numOf: 20,

    },
    {
        id:2,
        name:"mashhad",
        description: "yyyyyyy",
        location: "mashhad",
        imageSrc: "./images/hotel2.jpg",
        numOf: 10,
    },
    {
        id:3,
        name:"shiraz",
        description: "yyyyyyy",
        location: "shiraz",
        imageSrc: "./images/hotel2.jpg",
        numOf: 30,
    },
    {
        id:4,
        name:"tabriz",
        description: "yyyyyyy",
        location: "tariz",
        imageSrc: "./images/hotel4.jpg",
                numOf: 20,
    },
    {
        id:5,
        name:"sari",
        description: "yyyyyyy",
        location: "sari",
        imageSrc: "./images/hotel3.jpg",
                numOf: 20,
    },
    {
        id:5,
        name:"esfahan",
        description: "yyyyyyy",
        location: "esfahan",
        imageSrc: "./images/hotel3.jpg",
                numOf: 20,
    }
];

let dataToShow;


const handleChange = (event) => {
    const { name, value } = event.target;
  
    if (!value) {
      dataToShow = sampleData;
      showData();
      return;
    }
    let newData;
    if (name === 'numOf') {
        newData = sampleData.filter(data => data.numOf >= value);
    } else {
      newData = sampleData.filter(data => data[name].includes(value));
    }
    dataToShow = newData;
  
    showData();
  };
  

// function filterByNumOfPeople(data, num) {
//     return data.filter(item => item.numOf === num);
//   }
  
//   const filteredData = filterByNumOfPeople(sampleData, 2);
//   console.log(filteredData);

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
    if(!dataToShow){
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
        buttonLink.href = 'page2.html';
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