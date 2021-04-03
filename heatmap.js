let map, heatmap;

function initMap() {
    
    var singapore = new google.maps.LatLng(1.364917, 103.822872);
    
    map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: singapore,
    mapTypeId: "satellite",
  });
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
  });
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  const gradient = [
    "rgba(0, 255, 255, 0)",
    "rgba(0, 255, 255, 1)",
    "rgba(0, 191, 255, 1)",
    "rgba(0, 127, 255, 1)",
    "rgba(0, 63, 255, 1)",
    "rgba(0, 0, 255, 1)",
    "rgba(0, 0, 223, 1)",
    "rgba(0, 0, 191, 1)",
    "rgba(0, 0, 159, 1)",
    "rgba(0, 0, 127, 1)",
    "rgba(63, 0, 91, 1)",
    "rgba(127, 0, 63, 1)",
    "rgba(191, 0, 31, 1)",
    "rgba(255, 0, 0, 1)",
  ];
  heatmap.set("gradient", heatmap.get("gradient") ? null : gradient);
}

function changeRadius() {
  heatmap.set("radius", heatmap.get("radius") ? null : 50);
}

function changeOpacity() {
  heatmap.set("opacity", heatmap.get("opacity") ? null : 0.2);
}

// Heatmap data: 500 Points
function getPoints() {
  return [
    {location: new google.maps.LatLng(1.314917, 103.822872), weight: 5},
    {location: new google.maps.LatLng(1.324917, 103.857872), weight: 4},
    {location: new google.maps.LatLng(1.354917, 103.522872), weight: 6},
    {location: new google.maps.LatLng(1.374917, 103.772872), weight: 7},
    {location: new google.maps.LatLng(1.374917, 103.122872), weight: 5},
    {location: new google.maps.LatLng(1.374917, 103.222872), weight: 3},
    {location: new google.maps.LatLng(1.374917, 103.322872), weight: 2},
    {location: new google.maps.LatLng(1.314917, 103.422872), weight: 9},
    {location: new google.maps.LatLng(1.355917, 103.622872), weight: 2},
    {location: new google.maps.LatLng(1.332917, 103.644873), weight: 3},
    new google.maps.LatLng(1.364917, 103.822872),
    new google.maps.LatLng(1.334917, 103.822872),
    new google.maps.LatLng(1.324917, 103.812872),
    new google.maps.LatLng(1.384917, 103.812872),
    new google.maps.LatLng(1.374917, 103.822872),
    new google.maps.LatLng(1.364917, 103.836872),
    new google.maps.LatLng(1.356917, 103.76872),
    new google.maps.LatLng(1.354917, 103.845872),
  ];
}