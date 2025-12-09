from qgis.core import QgsVectorLayer, QgsRasterLayer
from qgis import processing

vector_layer = QgsVectorLayer(r"D:\7TH SEMESTER\Adv_Predictive_Analytics\Project_Docs\Vellore Shapefile\Vellore_boundary.shp", "wards", "ogr")
raster_layer = r"D:\7TH SEMESTER\Adv_Predictive_Analytics\Project_Docs\Vellore_NDVI_Layer_Clipped.tif"

processing.run("qgis:zonalstatistics", {
    'INPUT': vector_layer,
    'INPUT_RASTER': raster_layer,
    'RASTER_BAND': 1,
    'COLUMN_PREFIX': 'NDVI_',
    'STATISTICS': [2]
})
