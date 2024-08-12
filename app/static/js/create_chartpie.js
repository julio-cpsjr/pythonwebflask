function create_chartpie(id,value,question){
    var xValues = ["Não", "Sim"];
    var yValues = value;
    var barColors = [
      "#b91d47",
      "#00aba9",
    ];
    const myChartpie= new Chart(id, {
    type: "pie",
    data: {
    labels:xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues,
    }]
    },
    options: {
        title: {
          display: true,
          text: `${question}`,
          fontColor: "#ffbb33"
        },
        legend: {
            labels: {
              fontColor: "#fff"
            }
        }
    }
  });
}