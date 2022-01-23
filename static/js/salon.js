let map;

function initMap() {
    const coords = { lat: 44.95587, lng: 24.93418 };
    map = new google.maps.Map(document.getElementById("map"), {
      center: coords,
      zoom: 20,
      type: "ROADMAP"
    });
    // new google.maps.Marker({
    //     position: coords,
    //     map,
    //     title: "WAZZA INK TATTOO",
        
    // });
}
initMap()
