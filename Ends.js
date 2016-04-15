function clickedOnMap(event)
{
    getlatlng(event.latLng);
}
function getlatlng(latlng){
    
    var xmlhttp = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            console.log(xmlhttp.responseText);
        }
    }
    xmlhttp.open("POST", "info.php", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    var params = "lat=" + latlng.lat();
    params += "&lng=" + latlng.lng();
    console.log(params);
    xmlhttp.send(params);
    
}
function overideMarkerOnClick(marker) {
    google.maps.event.addListener(marker, 'click', function() {
        getlatlng(this.getPosition());
    });
    
}