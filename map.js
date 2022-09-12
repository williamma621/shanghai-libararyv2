var map = new BMapGL.Map('container'); //创造地图
map.centerAndZoom(new BMapGL.Point(121.46223, 31.233143), 15); //设置地图中心点
map.enableScrollWheelZoom(true); //启用鼠标滚轴缩放
console.log(137)

function addClickHandler(content, marker, options) {
            marker.addEventListener("click", function (e) { //监听单击事件
                openInfo(content, e, options)
        }
    );
}

function openInfo(content, e, options) {
    var p = e.target;
    var point = new BMapGL.Point(p.getPosition().lng, p.getPosition().lat);
    var infoWindow = new BMapGL.InfoWindow(content, options);  // 创建信息窗口对象
    map.openInfoWindow(infoWindow, point); //开启信息窗口
}

var dist = new BMapGL.DistrictLayer({
    name: '(上海市)',
    fillColor: '#96adf1',
    fillOpacity: 0.25
});
map.addDistrictLayer(dist);
for (var i = 0; i < info.length; i++) {
    var points = new BMapGL.Point(info[i].y, info[i].x)
    var markers = new BMapGL.Marker(points);
    map.addOverlay(markers); //在地图上标记
    var opts = {
        position: points,
        width: 400,
        height: 300,
        title: info[i].name//配置info box
    }
    addClickHandler(info[i].des,markers,opts); //设置在点击时打开
}
