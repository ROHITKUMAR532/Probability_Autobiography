function calculate() {
  const name = document.getElementById("name").value;
  const age = document.getElementById("age").value;
  const profession = document.getElementById("profession").value;

  if (!name || !age || !profession) {
    alert("Please fill all fields");
    return;
  }

  fetch("http://127.0.0.1:8000/api/profile/create/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: name,
      age: age,
      profession: profession
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);

    document.getElementById("result").innerText =
      "Success Probability: " + data.probability + "%";

    showChart(data.probability);
  })
  .catch(error => {
    console.error("Error:", error);
    alert("Server error");
  });
}

function showChart(value) {
  const ctx = document.getElementById("chart").getContext("2d");

  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Success", "Remaining"],
      datasets: [{
        data: [value, 100 - value]
      }]
    }
  });
}