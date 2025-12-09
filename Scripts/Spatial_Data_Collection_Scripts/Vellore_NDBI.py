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

# NDBI = (SWIR - NIR) / (SWIR + NIR)
ndbi = image.normalizedDifference(['B11', 'B8']).rename('NDBI')

task = ee.batch.Export.image.toDrive(
    image=ndbi,
    description='NDBI_Vellore',
    folder='GEE_exports',
    fileNamePrefix='NDBI_Vellore_2024_2025',
    scale=30,   # SWIR has 20m resolution, resample to 30m
    region=aoi.geometry(),
    maxPixels=1e13
)
task.start()

print("NDBI export started. Check your Google Drive -> GEE_exports folder.")
