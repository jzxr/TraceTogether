var map, pointarray, heatmap;
var mainMap = {};
var dataArray = {};
var dataIndex = [];
var _mink, _maxk;
var radius, opacity;

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function handleFileSelect(evt) {
    var file = evt.target.files[0];
    mainMap = {};
    dataArray = {};
    dataIndex = [];
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function (results) {
            csv = [];
            if (results.meta.fields.indexOf("weight") == -1) {
                for (idx in results["data"]) {
                    var row = results["data"][idx];
                    csv.push(new google.maps.LatLng(row["lat"], row["lon"]))
                }
            } else {
                var max = results["data"][0]["weight"];
                _maxk = results["data"][0]["interval"];
                _mink = results["data"][0]["interval"];
                _mink = results["data"][0]["interval"];
                for (idx in results["data"]) {
                    var row = results["data"][idx];
                    max = Math.max(max, row["weight"]);
                    _maxk = Math.max(_maxk, row["interval"]);

                    _mink = Math.min(_mink, row["interval"]);
                    var _h = row["interval"]
                    if (_h in mainMap) {
                        mainMap[_h].push({
                            location: new google.maps.LatLng(row["lat"], row["lon"]),
                            weight: row["weight"]
                        });
                    } else {
                        mainMap[_h] = [];
                        dataArray[_h] = [];
                        dataArray[_h].push(_h);
                        dataIndex.push(_h);
                        mainMap[_h].push({
                            location: new google.maps.LatLng(row["lat"], row["lon"]),
                            weight: row["weight"]
                        });
                    }
                }
            }
            loadHeatmap(mainMap[_mink]);
        }
    });
}

function toggleHeatmap() {
    heatmap.setMap(heatmap.getMap() ? null : map);
  }
  
function initialize() {
    var mapOptions = {
        zoom: 12,
        center: new google.maps.LatLng(1.364917, 103.822872)
    };

    map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);
}

function setOptions() {
    heatmap.set('opacity', opacity / 100);
    heatmap.set('radius', radius);
}

function loadHeatmap(csv) {
    var pointArray = new google.maps.MVCArray(csv);

    if (heatmap) heatmap.setMap(null);

    heatmap = new google.maps.visualization.HeatmapLayer({
        data: pointArray,
        radius: $("#radius-slider").slider("value"),
        opacity: $("#opacity-slider").slider("value")
    });

    heatmap.setMap(map);
    setOptions();
}