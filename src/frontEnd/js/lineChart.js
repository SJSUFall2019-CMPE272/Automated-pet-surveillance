var feedCount;
var totalMeals;
function incrementFeedCount()
{
var feedCounter = Number(localStorage.getItem("feedCount"));
var mealsCounter = Number(localStorage.getItem("totalMeals" ));
if(feedCounter==null)
{
  feedCounter = 0;
}
if(mealsCounter == null)
{
  mealsCounter = 4;
}
feedCounter++;
mealsCounter++;
  localStorage.setItem("feedCount", feedCounter);
  localStorage.setItem("totalMeals", mealsCounter);

}



// x-axis

var day = ["Sun", "Mon", "Tue", "Wed", "Thurs","Fri", "Sat"];
// data for drawing
var notificationCount = [1,0,2,2,3,2,1];
var manualFeedFrequency = [1,2,0,localStorage.getItem("feedCount"),0,1,2]
//creating a graph
var ctx = document.getElementById("lineChart");
var lineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: day,
    datasets: [
      {
        data: notificationCount,
        label: "Number of Notifications",
        borderColor: "#3e95cd",
        fill: false,
      },
      {
        data: manualFeedFrequency,
        label: "Number of Manual treats",
        borderColor: "#8e5ea2",
        fill: false,
      }
    ],

  },
  options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 1

                }
            }]
        }
    }
});
