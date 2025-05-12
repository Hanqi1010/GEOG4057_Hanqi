import arcpy
import os
import ee
import pandas as pd
import sys

"""
example usage
python Project2_Hanqi.py "F:\OneDrive - Louisiana State University\LSU_Course\GEOG\GEOG 4057 GIS Programming\GEOG4057_Hanqi\Projects\Project_2_Hanqi" boundary.csv pnt_elev2 32119
"""
def getGeeElevation(workspace,csv_file,outfc_name,epsg=4326):
    """
    workspace: directory that contains input and output
    csv_file: input csv file 
    epsg: wkid code for the spatial reference, e.g. 4326 for WGS84
    outfc_name: output feature class name
    """
    
    csv_fullname = os.path.join(workspace, csv_file)
    data = pd.read_csv(csv_fullname)
    dem = ee.Image("USGS/3DEP/10m")
    geometry = [ee.Geometry.Point([x,y],f'EPSG:{epsg}') for x,y in zip(data["X"], data["Y"])]
    fc = ee.FeatureCollection(geometry)
    original_info = fc.getInfo()
    sample_fc = dem.sampleRegions(
        collection=fc,
        scale=10,
        geometries=True
    )
    sample_info = sample_fc.getInfo()
    for ind,itm in enumerate(original_info['features']):
        itm['properties'] = sample_info['features'][ind]['properties']
        
    fcname= os.path.join(workspace, outfc_name)
    if arcpy.Exists(fcname):
        arcpy.management.Delete(fcname)
    arcpy.management.CreateFeatureclass(workspace, outfc_name, geometry_type="POINT", spatial_reference=epsg)
    arcpy.management.AddField(fcname, "elevation", "FLOAT")
    
    with arcpy.da.InsertCursor(fcname, ["SHAPE@", "elevation"]) as cursor:
        for feature in original_info['features']:
            geom = feature['geometry']
            coords = geom['coordinates']
            x, y = coords[0], coords[1]
            point = arcpy.PointGeometry(arcpy.Point(x, y))
            prop = feature['properties']
            elev = prop['elevation']
            cursor.insertRow([point, elev])
    
    
def main():
    try:
        ee.Initialize(project='ee-hanqi')
    except Exception as e:
        ee.Authenticate()
        ee.Initialize(project='ee-hanqi')
    workspace = sys.argv[1]
    csv_file = sys.argv[2]
    outfc_name = sys.argv[3]
    epsg = int(sys.argv[4])
    
    
    getGeeElevation(workspace=workspace, csv_file=csv_file, outfc_name=outfc_name, epsg=epsg)
    
    # r"F:\OneDrive - Louisiana State University\LSU_Course\GEOG\GEOG 4057 GIS Programming\GEOG4057_Hanqi\Projects\Project_2_Hanqi"
    # "boundary.csv"
    # 'pnt_elev1'
    

if __name__ == "__main__":
    main()