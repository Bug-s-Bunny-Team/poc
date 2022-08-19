<script lang="ts">
    import * as L from 'leaflet';

	export const library = `<svg style="width:30px;height:30px" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor"><path d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg>`;
    import { MapPresenter } from '../presenters/MapPresenter.js';
	import type { Location } from "../models"

    let map;
    let presenter=new MapPresenter();
	let rankedList: Promise<Location[]>;
	let markerLocations = [];
	presenter.rankedList.subscribe(_rankedList => {rankedList = _rankedList});
  
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
	
	function makeIcon() {
		return new L.Icon({
			iconUrl: './src/assets/icon.png',
			iconSize: [40, 40],
			iconAnchor: [20, 30], // [half of iconSize.x, 3/4 of iconSize.y] dependent on image used
			popupAnchor: [-3, -76],
			shadowUrl: null
		});
	}

	function createMarker(loc: [number, number]) {
		let marker = L.marker(loc, {icon: makeIcon()});
		return marker;
	}
	

	let markerLayers;
  	function mapAction(container) {
		rankedList.then(locations => {
			locations.forEach(location => {
				markerLocations.push([location.position.lat, location.position.long]);
			});

			map = createMap(container); 
			
			markerLayers = L.layerGroup();
			for(let location of markerLocations) {
				let m = createMarker(location);
				markerLayers.addLayer(m);
			}

			markerLayers.addTo(map);
			
			return {
			destroy: () => {
						map.remove();
						map = null;
					}
			};
		})

	}

	function resizeMap() {
	  if(map) map.invalidateSize();
    }
</script>
<svelte:window on:resize={resizeMap} />


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
    integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
    crossorigin=""/>
 
 <div style="height:80vh;width:100%" use:mapAction/>

 <style>
 </style>
