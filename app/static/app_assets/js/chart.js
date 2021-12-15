
//var endpoint = '/teste/'
var endpoint = '/chartdata/'

var labels =  [];
var labels2 =  [];
var defaultData = [];
var defaultData2 = [];
var defaultData3 = [];
var defaultData4 = [];
var defaultData5 = [];
var pielist = [];
var pielist2 = [];
var weeklist = []
var divlist = []

$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        labels = data.labels
        labels2 = data.labels2
        defaultData = data.default
        defaultData2 = data.default2
        defaultData3 = data.default3
        defaultData4 = data.default4
        defaultData5 = data.default5
        pielist2 = data.pielist2
        weeklist = data.weeklist
        pielist = data.pielist
        divlist = data.divlist

        setChart()
        console.log(data)
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})

function setChart(){
    var ctx = document.getElementById("myChart");

    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Pizza',
                data: defaultData2,
                borderColor: 'rgba(50, 115, 220, 0.6)',
                backgroundColor: 'rgba(50, 115, 220, 0.1)',
                lineTension: 0.1,
               
            },
            {
                label: 'Burgers',
                data: defaultData,
                
                borderColor: 'rgba(255, 206, 86, 0.6)',
                backgroundColor: 'rgba(255, 206, 86, 0.1)',
                lineTension: 0.1,
            },
           
            {
                label: 'Sushi',
                data: defaultData5,
                borderColor:  'rgba(75, 192, 192, 1)',
                backgroundColor:  'rgba(75, 192, 192, 0.1)',
                lineTension: 0.1,
                
            },
            {
                label: 'Outros',
                data: defaultData3,
                borderColor: 'rgba(255, 159, 64, 1)',
                backgroundColor: 'rgba(255, 159, 64, 0.1)',
                lineTension: 0.1,
                
            },
           
        ]
    },
    options: {
        scales: {
          x: {
            grid: {
              display: true
            }
          },
          y: {
            ticks: {
                min: 0, // it is for ignoring negative step.
                beginAtZero: true,
                stepSize: 10,  
                callback: function(value, index, values) {
                    return '$' + value;
                }
            },
            grid: {
              display: true
              
            }
          }
        },
      }
});
var ctx2 = document.getElementById("myChart2");

var myChart2 = new Chart(ctx2, {
type: 'bar',
data: {
    labels: labels,
    datasets: [{
            label: 'Total de Gastos Mensal',
            data: defaultData4,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor:  'rgba(54, 162, 235, 0.2)',
            lineTension: 0.1,
            borderWidth: 1,
        },
    ]
},
options: {
    scales: {
      x: {
        grid: {
          display: true
        }
      },
      y: {
        ticks: {
            min: 0, // it is for ignoring negative step.
            beginAtZero: true,
            stepSize: 10 ,
            callback: function(value, index, values) {
                return '$' + value;
            }
        },
        grid: {
          display: true
          
        }
      }
    },
  }
});
    
    var ctx3 = document.getElementById("myChart3");

    var myChart3 = new Chart(ctx3, {
    //type: 'bar',
    type: 'doughnut',
    data: {
        labels: ['Outros','Pizza','Burgers',"Sushi"],
        //labels: divlist,
        
        datasets: [{
            data: pielist,
            backgroundColor: [
                'rgba(255, 159, 64, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 159, 64, 1)', 
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false,
            },
            
        },
    }
   
    });

    var ctx4 = document.getElementById("myChart4");

    var myChart4 = new Chart(ctx4, {
    //type: 'bar',
    type: 'doughnut',
    data: {
        
        //labels: divlist,
        labels: ['Outros','Pizza','Burgers',"Sushi"],
        datasets: [{
            data: pielist2,
            backgroundColor: [
                'rgba(255, 159, 64, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                
            ],
            borderColor: [
                'rgba(255, 159, 64, 1)', 
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false,
            },
            
        },
    }
   
    });

    var ctx5 = document.getElementById("myChart5");

    var myChart5 = new Chart(ctx5, {
    type: 'bar',
    data: {
        labels: labels2,
        datasets: [{
                label: 'Dia da Semana',
                data: weeklist,
                borderColor: [
                    'rgba(252,99,132,3)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                lineTension: 0.1,
                borderWidth: 1,
            },
        ]
    },
    options: {
        scales: {
        x: {
            grid: {
            display: true
            }
        },
        y: {
            ticks: {
                min: 0, // it is for ignoring negative step.
                beginAtZero: true,
                stepSize: 1 ,
            },
            grid: {
            display: true
            }
        }
        },
        plugins: {
            legend: {
                display: false,
            },
            
        },
    }
    });

}



