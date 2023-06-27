const sampleData = [
    // {
    //   id: 1,
    //   type: 'economy',
    //   numOf: 20,
    //   departier: '6:40',
    //   arrivalTime: '7:40',
    // },
    // {
    //   id: 2,
    //   type: 'systematic',
    //   numOf: 10,
    //   departier: '8:00',
    //   arrivalTime: '9:00',
    // },
    // {
    //   id: 3,
    //   type: 'bouing',
    //   numOf: 30,
    //   departier: '10:30',
    //   arrivalTime: '11:30',
    // },
    // {
    //   id: 4,
    //   type: 'premium',
    //   numOf: 15,
    //   departier: '13:15',
    //   arrivalTime: '14:15',
    // },
  ];
  
  // Get the div element with the class "form-holder"
  const formHolderDiv = document.querySelector('.form-holder');
  
  // Iterate over the sample data
  sampleData.forEach((data) => {
    // Create a new h1 element for the type
    const typeHeading = document.createElement('h1');
    typeHeading.textContent = data.type;
  
    // Create a new h1 element for the number of flights
    const numOfFlightsHeading = document.createElement('h1');
    numOfFlightsHeading.textContent = `Number of Flights: ${data.numOf}`;
  
    // Create a new h1 element for the departier time
    const departierHeading = document.createElement('h1');
    departierHeading.textContent = `Departier: ${data.departier}`;
  
    // Create a new h1 element for the arrival time
    const arrivalTimeHeading = document.createElement('h1');
    arrivalTimeHeading.textContent = `Arrival Time: ${data.arrivalTime}`;
  
    // Create a new div element to hold the data
    const dataDiv = document.createElement('div');
    dataDiv.classList.add('flight-data');
  
    // Append the headings to the data div
    dataDiv.appendChild(typeHeading);
    dataDiv.appendChild(numOfFlightsHeading);
    dataDiv.appendChild(departierHeading);
    dataDiv.appendChild(arrivalTimeHeading);
  
    // Append the data div to the form holder div
    formHolderDiv.appendChild(dataDiv);
  });
  



///////
$(function(){
	$("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        transitionEffectSpeed: 300,
        labels: {
            next: "Next",
            previous: "Back"
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            if ( newIndex === 1 ) {
                $('.steps').addClass('step-2');
            } else {
                $('.steps').removeClass('step-2');
            }
            if ( newIndex === 2 ) {
                $('.steps').addClass('step-3');
            } else {
                $('.steps').removeClass('step-3');
            }
            return true; 
        }
    });
    // Custom Jquery Steps
    $('.forward').click(function(){
    	$("#wizard").steps('next');
    })
    $('.backward').click(function(){
        $("#wizard").steps('previous');
    })
    // Select
    $('html').click(function() {
        $('.select .dropdown').hide(); 
    });
    $('.select').click(function(event){
        event.stopPropagation();
    });
    $('.select .select-control').click(function(){
        $(this).parent().next().toggle().toggleClass('active');
    })
    $('.select .dropdown li').click(function(){
        $(this).parent().toggle();
        var text = $(this).attr('rel');
        $(this).parent().prev().find('div').text(text);
    })
    // Payment
    $('.payment-block .payment-item').click(function(){
        $('.payment-block .payment-item').removeClass('active');
        $(this).addClass('active');
    })
    // Date Picker
    var dp1 = $('#dp1').datepicker().data('datepicker');
})
