import ee
ee.Initialize(project='active-freehold-465811-h1')

# Load AOI (replace with your Vellore shapefile asset path)
aoi = ee.FeatureCollection("projects/active-freehold-465811-h1/assets/Vellore_boundary")

# Load Sentinel-2 Surface Reflectance
image = (ee.ImageCollection("COPERNICUS/S2_SR")
         .filterBounds(aoi)
         .filterDate('2024-08-01', '2025-08-01')   # 1 year range
         .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
         .median())

# Compute NDVI = (NIR - RED) / (NIR + RED)
ndvi = image.normalizedDifference(['B8','B4']).rename('NDVI')

# Export NDVI raster to Google Drive
task = ee.batch.Export.image.toDrive(
    image=ndvi,
    description='NDVI_Vellore',
    folder='GEE_exports',
    fileNamePrefix='NDVI_Vellore_2024_2025',
    scale=10,                      # Sentinel-2 resolution
    region=aoi.geometry(),
    maxPixels=1e13
)
task.start()

print("NDVI export started. Check your Google Drive -> GEE_exports folder.")
