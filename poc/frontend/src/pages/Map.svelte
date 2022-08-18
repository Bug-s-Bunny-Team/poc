<script>
    import * as L from 'leaflet';
    // If you're playing with this in the Svelte REPL, import the CSS using the
    // syntax in svelte:head instead. For normal development, this is better.
    //import 'leaflet/dist/leaflet.css';
    import * as markerIcons from './MapComponents/markers.js';
    import MapToolBar from './MapComponents/MapToolBar.svelte';

    let map;

    const markerLocations = [
		[45.420, 11.895],
		[45.412, 11.890],
		[45.402, 11.880],
		[45.410, 11.885],
	];
  
    function createMap(container) {
      let m = L.map(container).setView([45.420, 11.895], 13);
      L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        {
          attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
            &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
          subdomains: 'abcd',
          maxZoom: 18,
        }
      ).addTo(m);
  
      return m;
    }

	let eye = true;
	
	let toolbar = L.control({ position: 'topright' });
	let toolbarComponent;
	toolbar.onAdd = (map) => {
		let div = L.DomUtil.create('div');
		toolbarComponent = new MapToolBar({
			target: div,
			props: {}
		});
		  toolbarComponent.$on('click-reset', () => {
			map.setView([45.420, 11.895],13, { animate: true })
		})

		return div;
	}
	
	
	
	let markers = new Map();
	
	function markerIcon(count) {
		let html = `<div class="map-marker"><div>${markerIcons.library}</div><div class="marker-text">${count}</div></div>`;
		return L.divIcon({
			html,
			className: 'map-marker'
		});
	}
	

	function createMarker(loc) {
		let count = Math.ceil(Math.random() * 25);
		let marker = L.marker(loc);
		return marker;
	}
	

	let markerLayers;
  function mapAction(container) {
    map = createMap(container); 
		toolbar.addTo(map);
		
		markerLayers = L.layerGroup()
 		for(let location of markerLocations) {
 			let m = createMarker(location);
			markerLayers.addLayer(m);
 		}
		
		
		markerLayers.addTo(map);
		
    return {
       destroy: () => {
				 toolbar.remove();
				 map.remove();
				 map = null;
			 }
    };
	}
	
	// We could do these in the toolbar's click handler but this is an example
	// of modifying the map with reactive syntax.
	$: if(markerLayers && map) {
		if(eye) {
			markerLayers.addTo(map);
		} else {
			markerLayers.remove();
		}
	}

	function resizeMap() {
	  if(map) { map.invalidateSize(); }
  }



function initialView(initialView,arg1,arg2) {
throw new Error('Function not implemented.');
}
</script>
<svelte:window on:resize={resizeMap} />


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
    integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
    crossorigin=""/>
 
 <div style="height:400px;width:100%" use:mapAction />
