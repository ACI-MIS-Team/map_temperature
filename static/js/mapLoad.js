var baseurl = "http://maps.codemaven.net";
//mapbox load
BANGLA_STYLE = baseurl + "/geocode/banglastyle/";
ENGLISH_STYLE = baseurl + "/geocode/englsihstyle/";
mapboxgl.accessToken = "pk.eyJ1IjoidmxhZGltaXJtYWthcm92MTcxIiwiYSI6ImNreTJsdGw0djBhZmwyb24xZ21ianN4Z2wifQ.wNcF-6rCTVkX3oRvBLL4YA";
var map = new mapboxgl.Map({
  container: "map", // container ID
  style: ENGLISH_STYLE, // style URL
  center: [90.3510153, 23.7645784], // starting position [lng, lat]
  zoom: 4, // starting zoom
  attributionControl: false,
});
// Define some sample point coordinates with popup content
var points = [
  {
    type: "Feature",
    properties: {
      title: "Ambagan (Ctg)",
      description: "Weather Station in Ambagan (Ctg)",
    },
    geometry: {
      type: "Point",
      coordinates: [91.8009, 22.3375], // Ambagan (Ctg)
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Badalgachhi",
      description: "Weather Station in Badalgachhi",
    },
    geometry: {
      type: "Point",
      coordinates: [88.8736, 24.8925], // Badalgachhi
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Barisal",
      description: "Weather Station in Barisal",
    },
    geometry: {
      type: "Point",
      coordinates: [90.37, 22.7], // Barisal
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Bhola",
      description: "Weather Station in Bhola",
    },
    geometry: {
      type: "Point",
      coordinates: [90.7513, 22.6859], // Bhola
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Bogra",
      description: "Weather Station in Bogra",
    },
    geometry: {
      type: "Point",
      coordinates: [89.3711, 24.8487], // Bogra
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Chandpur",
      description: "Weather Station in Chandpur",
    },
    geometry: {
      type: "Point",
      coordinates: [90.8509, 23.2333], // Chandpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Chittagong",
      description: "Weather Station in Chittagong",
    },
    geometry: {
      type: "Point",
      coordinates: [91.8333, 22.3667], // Chittagong
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Chuadanga",
      description: "Weather Station in Chuadanga",
    },
    geometry: {
      type: "Point",
      coordinates: [88.9333, 23.6167], // Chuadanga
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Comilla",
      description: "Weather Station in Comilla",
    },
    geometry: {
      type: "Point",
      coordinates: [91.2, 23.45], // Comilla
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Cox's Bazar",
      description: "Weather Station in Cox's Bazar",
    },
    geometry: {
      type: "Point",
      coordinates: [92.0092, 21.4272], // Cox's Bazar
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Dhaka",
      description: "Weather Station in Dhaka",
    },
    geometry: {
      type: "Point",
      coordinates: [90.4125, 23.8103], // Dhaka
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Dimla",
      description: "Weather Station in Dimla",
    },
    geometry: {
      type: "Point",
      coordinates: [88.9381, 25.63], // Dimla
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Dinajpur",
      description: "Weather Station in Dinajpur",
    },
    geometry: {
      type: "Point",
      coordinates: [88.6346, 25.629], // Dinajpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Faridpur",
      description: "Weather Station in Faridpur",
    },
    geometry: {
      type: "Point",
      coordinates: [89.8353, 23.6071], // Faridpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Feni",
      description: "Weather Station in Feni",
    },
    geometry: {
      type: "Point",
      coordinates: [91.4037, 23.0235], // Feni
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Gopalgonj",
      description: "Weather Station in Gopalgonj",
    },
    geometry: {
      type: "Point",
      coordinates: [89.7945, 23.0258], // Gopalgonj
    },
  },

  {
    type: "Feature",
    properties: {
      title: "Ishurdi",
      description: "Weather Station in Ishurdi",
    },
    geometry: {
      type: "Point",
      coordinates: [89.1509, 24.1306], // Ishurdi
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Jessore",
      description: "Weather Station in Jessore",
    },
    geometry: {
      type: "Point",
      coordinates: [89.2172, 23.1676], // Jessore
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Khepupara",
      description: "Weather Station in Khepupara",
    },
    geometry: {
      type: "Point",
      coordinates: [90.8222, 22.1759], // Khepupara
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Khulna",
      description: "Weather Station in Khulna",
    },
    geometry: {
      type: "Point",
      coordinates: [89.5403, 22.8028], // Khulna
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Kumarkhali",
      description: "Weather Station in Kumarkhali",
    },
    geometry: {
      type: "Point",
      coordinates: [89.703, 23.7973], // Kumarkhali
    },
  },

  {
    type: "Feature",
    properties: {
      title: "M.court",
      description: "Weather Station in M.court",
    },
    geometry: {
      type: "Point",
      coordinates: [91.9694, 22.8007], // M.court
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Madaripur",
      description: "Weather Station in Madaripur",
    },
    geometry: {
      type: "Point",
      coordinates: [90.1968, 23.1703], // Madaripur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Mongla",
      description: "Weather Station in Mongla",
    },
    geometry: {
      type: "Point",
      coordinates: [89.5773, 22.5166], // Mongla
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Mymensingh",
      description: "Weather Station in Mymensingh",
    },
    geometry: {
      type: "Point",
      coordinates: [90.4057, 24.748], // Mymensingh
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Natrakona",
      description: "Weather Station in Natrakona",
    },
    geometry: {
      type: "Point",
      coordinates: [91.1, 24.7667], // Natrakona
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Patuakhali",
      description: "Weather Station in Patuakhali",
    },
    geometry: {
      type: "Point",
      coordinates: [90.3258, 22.3591], // Patuakhali
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rajarhat",
      description: "Weather Station in Rajarhat",
    },
    geometry: {
      type: "Point",
      coordinates: [88.584, 26.1345], // Rajarhat
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rajshahi",
      description: "Weather Station in Rajshahi",
    },
    geometry: {
      type: "Point",
      coordinates: [88.6005, 24.3636], // Rajshahi
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rangamati",
      description: "Weather Station in Rangamati",
    },
    geometry: {
      type: "Point",
      coordinates: [92.2232, 22.6592], // Rangamati
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rangpur",
      description: "Weather Station in Rangpur",
    },
    geometry: {
      type: "Point",
      coordinates: [89.25, 25.75], // Rangpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Sandwip",
      description: "Weather Station in Sandwip",
    },
    geometry: {
      type: "Point",
      coordinates: [91.5086, 22.3296], // Sandwip
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Satkhira",
      description: "Weather Station in Satkhira",
    },
    geometry: {
      type: "Point",
      coordinates: [89.0933, 22.7186], // Satkhira
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Sitakunda",
      description: "Weather Station in Sitakunda",
    },
    geometry: {
      type: "Point",
      coordinates: [91.7905, 22.5386], // Sitakunda
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Srimangal",
      description: "Weather Station in Srimangal",
    },
    geometry: {
      type: "Point",
      coordinates: [91.7516, 24.3065], // Srimangal
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Sydpur",
      description: "Weather Station in Sydpur",
    },
    geometry: {
      type: "Point",
      coordinates: [90.2171, 23.7045], // Sydpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Sylhet",
      description: "Weather Station in Sylhet",
    },
    geometry: {
      type: "Point",
      coordinates: [91.8833, 24.8995], // Sylhet
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Tangail",
      description: "Weather Station in Tangail",
    },
    geometry: {
      type: "Point",
      coordinates: [89.9139, 24.2446], // Tangail
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Tarash",
      description: "Weather Station in Tarash",
    },
    geometry: {
      type: "Point",
      coordinates: [88.7425, 25.7636], // Tarash
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Teknaf",
      description: "Weather Station in Teknaf",
    },
    geometry: {
      type: "Point",
      coordinates: [92.3105, 20.8622], // Teknaf
    },
  },
];

// Add a source for your points
map.on("load", function () {
  map.addSource("points", {
    type: "geojson",
    data: {
      type: "FeatureCollection",
      features: points,
    },
  });

  map.addLayer({
    id: "points",
    type: "circle",
    source: "points",
    paint: {
      "circle-radius": 10, // Increase the circle size
      "circle-color": "#FF5733", // Customize the color (e.g., orange)
      "circle-opacity": 0.7, // Adjust the opacity
      "circle-stroke-width": 2, // Add a border
      "circle-stroke-color": "#FF5733", // Border color matching the circle color
    },
  });
  // Add a hover popup
  var popup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false,
  });

  map.on("mouseenter", "points", function (e) {
    map.getCanvas().style.cursor = "pointer";
    var coordinates = e.features[0].geometry.coordinates.slice();
    var title = e.features[0].properties.title;
    var description = e.features[0].properties.description;

    popup
      .setLngLat(coordinates)
      .setHTML("<h3>" + title + "</h3><p>" + description + "</p>")
      .addTo(map);
  });

  map.on("mouseleave", "points", function () {
    map.getCanvas().style.cursor = "";
    popup.remove();
  });
});
