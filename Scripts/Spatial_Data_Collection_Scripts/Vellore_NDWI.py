import ee
ee.Initialize(project='active-freehold-465811-h1')

# Load AOI (Vellore boundary shapefile)
aoi = ee.FeatureCollection("projects/active-freehold-465811-h1/assets/Vellore_boundary")

# Sentinel-2 SR Collection
image = (ee.ImageCollection("COPERNICUS/S2_SR")
         .filterBounds(aoi)
         .filterDate('2024-08-01', '2025-08-01')
         .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
         .median())

# NDWI = (Green - NIR) / (Green + NIR)
ndwi = image.normalizedDifference(['B3', 'B8']).rename('NDWI')

# Export NDWI
task = ee.batch.Export.image.toDrive(
    image=ndwi,
    description='NDWI_Vellore',
    folder='GEE_exports',
    fileNamePrefix='NDWI_Vellore_2024_2025',
    scale=10,
    region=aoi.geometry(),
    maxPixels=1e13
)
task.start()

print("NDWI export started. Check your Google Drive -> GEE_exports folder.")
