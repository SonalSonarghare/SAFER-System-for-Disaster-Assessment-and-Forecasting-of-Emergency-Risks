function initMap() {
    // Initialize Google Earth Engine
    ee.initialize();

    // Your GEE code here
    var ROI = table.filter(ee.Filter.eq('NAME_2', 'Gorakhpur'));
    
Map.addLayer(ROI)
Map.centerObject(ROI)

var collection = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
  .filter(
    ee.Filter.or(
      ee.Filter.eq('orbitProperties_pass', 'DESCENDING'),
      ee.Filter.eq('orbitProperties_pass', 'ASCENDING')
    )
  )

var before = collection.filter(ee.Filter.date('2022-08-10', '2022-08-30')).filterBounds(ROI)
var after = collection.filter(ee.Filter.date('2022-10-01', '2022-10-26')).filterBounds(ROI)

print(after)
print(before)

var after_image = after.select('VH').mosaic().clip(ROI)
var before_image = before.select('VH').mosaic().clip(ROI)

// Apply Lee filtering to before and after images
var before_filtered = before_image.focal_median(30, 'circle', 'meters')
var after_filtered = after_image.focal_median(30, 'circle', 'meters')

Map.addLayer(before_filtered, { min: -25, max: 0 }, 'Before (Filtered)')
Map.addLayer(after_filtered, { min: -25, max: 0 }, 'After (Filtered)')

var before_s = before_filtered
var after_s = after_filtered

// Calculate the difference
var difference = after_s.subtract(before_s)

var flood_extent = difference.lt(-3)
var flood = flood_extent.updateMask(flood_extent)
Map.addLayer(difference, {}, 'Difference')

// Define a threshold for identifying permanent water bodies
var permanent_water = before_s.lt(-20) // Adjust this threshold as needed

// Update mask for permanent water bodies
var permanent_water_mask = permanent_water.updateMask(permanent_water)

// Add the "Flood" layer in red color
Map.addLayer(flood, { palette: 'FF0000' }, 'Flood')

// Add the "Permanent Water Bodies" layer in blue color
Map.addLayer(permanent_water_mask, { palette: '0000FF' }, 'Permanent Water Bodies')

// Calculate the flooded area and print it
var floodedArea = flood.reduceRegion({
  reducer: ee.Reducer.sum(),
  geometry: ROI,
  scale: 10, // Adjust the scale based on your data resolution
  maxPixels: 1e13 // Adjust as needed
});

// Get the flooded area in square meters
var floodedAreaSqMeters = ee.Number(floodedArea.get('VH'));

// Convert square meters to square kilometers
var floodedAreaSqKm = floodedAreaSqMeters.divide(1000000);

// Print the flooded area
print('Flooded Area (Square Meters):',floodedAreaSqMeters);
print('Flooded Area (Square Kilometers):', floodedAreaSqKm);


// Add labels on the map
// Add labels on the map
var labelFlood = ui.Label('Flood', { color: 'black' });
var labelWater = ui.Label('Water Bodies', { color: 'black' });
var labelLegend = ui.Label('Legend', { color: 'black',fontWeight: 'bold',fontSize: '20px' });

// Create a red rectangle to go beside the "Flood" label
var redRectangle = ui.Panel({
  style: {
    width: '20px', // Adjust the width as needed
    height: '20px', // Adjust the height as needed
    backgroundColor: 'FF0000', // Red color
    margin: '5px', // Adjust the margin as needed
  },
});

// Create a blue rectangle to go beside the "Water Bodies" label
var blueRectangle = ui.Panel({
  style: {
    width: '20px', // Adjust the width as needed
    height: '20px', // Adjust the height as needed
    backgroundColor: 'blue', // Blue color
    margin: '5px', // Adjust the margin as needed
  },
});

var Legend= ui.Panel({
  widgets: [labelLegend],
  layout: ui.Panel.Layout.Flow('horizontal'), // Horizontal layout
});
// Create a horizontal panel for "Flood" label and red rectangle
var floodPanel = ui.Panel({
  widgets: [redRectangle, labelFlood],
  layout: ui.Panel.Layout.Flow('horizontal'), // Horizontal layout
});

// Create a horizontal panel for "Water Bodies" label and blue rectangle
var waterBodiesPanel = ui.Panel({
  widgets: [blueRectangle, labelWater],
  layout: ui.Panel.Layout.Flow('horizontal'), // Horizontal layout
});

// Create a vertical panel to hold both label-rectangle combinations
var labelPanel = ui.Panel({
  widgets: [Legend,floodPanel, waterBodiesPanel],
  style: { position: 'middle-right' },
});

// Add the label panel to the map
Map.add(labelPanel);

    // Add the GEE map to the HTML element
    var map = new google.maps.Map(document.getElementById('map-container'),
     {
        center: { lat:20.5937, lng: 78.9629 },
        zoom:10
    });

    // Display the GEE map on the web page
    Map.addTo(map);
}

// Call the initMap function when the page loads
google.maps.event.addDomListener(window, 'load', initMap);
