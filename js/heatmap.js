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
            if (results.meta.fields.indexOf("Weight") == -1) {
                for (idx in results["data"]) {
                    var row = results["data"][idx];
                    csv.push(new google.maps.LatLng(row["Latitute"], row["Longtitute"]))
                }
            } else {
                var max = results["data"][0]["Weight"];
                _maxk = results["data"][0]["Interval"];
                _mink = results["data"][0]["Interval"];
                _mink = results["data"][0]["Interval"];
                for (idx in results["data"]) {
                    var row = results["data"][idx];
                    max = Math.max(max, row["Weight"]);
                    _maxk = Math.max(_maxk, row["Interval"]);

                    _mink = Math.min(_mink, row["Interval"]);
                    var _h = row["Interval"]
                    if (_h in mainMap) {
                        mainMap[_h].push({
                            location: new google.maps.LatLng(row["Latitute"], row["Longtitute"]),
                            weight: row["Weight"]
                        });
                    } else {
                        mainMap[_h] = [];
                        dataArray[_h] = [];
                        dataArray[_h].push(_h);
                        dataIndex.push(_h);
                        mainMap[_h].push({
                            location: new google.maps.LatLng(row["Latitute"], row["Longtitute"]),
                            weight: row["Weight"]
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