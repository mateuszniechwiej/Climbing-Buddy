// Places Autocomplete for  locations input field to edit event
//location autocomplate for Uk and Ireland searches
let autocomplete5;
function initAutocomplete() {
    autocomplete5 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete5"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        });
    autocomplete5.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
    var location = autocomplete5.getPlace();
  
    if (!location.geometry) {
      document.getElementById("autocomplete5").placeholder = "Enter location";
    }
  }