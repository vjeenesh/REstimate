function getBath() {
  var sqft = document.getElementsByName("bath");
  for (var i in sqft) {
    if (sqft[i].checked) {
      return parseInt(i) + 1; // indexing starts at 0
    }
  }

  return -1; //for invalids
}

function getBHK() {
  var bhk = document.getElementsByName("bhk");
  for (var i in bhk) {
    if (bhk[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1;
}

function estimatePrice() {
  var sqft = document.getElementById("total_sqft");
  var location = document.getElementById("location");
  var bhk = getBHK();
  var bath = getBath();
  var estPrice = document.getElementById("est_price");
  // console.log(sqft, location, bhk, bath);
  url = "http://127.0.0.1:5000/predict_price";
  $.post(
    url,
    {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bath,
      location: location.value,
    },
    function (data, status) {
      // console.log(data.est_price);
      estPrice.style.fontWeight = "bolder";
      if (data.est_price >= 100) {
        estPrice.value =
          (data.est_price / 100).toPrecision(3).toString() + " CR Rs.";
      } else {
        estPrice.value = data.est_price.toString() + " Lakh Rs.";
      }
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var loc_options = document.getElementById("location_options");
      $("#location_options").empty();
      for (var i in locations) {
        var option = new Option(locations[i]);
        $("#location_options").append(option);
      }
    }
  });
}

window.onload = onPageLoad();
