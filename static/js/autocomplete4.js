let autocomplete4;
function initAutocomplete() {
    autocomplete4 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete4"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        });
    autocomplete4.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
    var location = autocomplete4.getPlace();
  
    if (!location.geometry) {
      document.getElementById("autocomplete4").placeholder = "Enter location";
    }
  }