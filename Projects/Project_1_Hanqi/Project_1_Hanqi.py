# Explore the json file
import json
import arcpy
import os

def importNoTaxJSON(workspace=r"F:\OneDrive - Louisiana State University\LSU_Course\GEOG\GEOG 4057 GIS Programming\GEOG4057_Hanqi\Projects\Project_1_Hanqi", json_file="no_tax.json", out_fc='notax_fc_tool.shp'):
    
    with open(json_file,'r') as file:
        tax_json=json.load(file)
    
    arcpy.FromWKT(tax_json['data'][8][8])
    for row in tax_json['data']:
        row[8] = arcpy.FromWKT(row[8])
    
    
    ## Create a feature class and write fileds
    fcname = out_fc
    fc_fullname = os.path.join(workspace, fcname)
    if arcpy.Exists(fc_fullname):
        arcpy.Delete_management(fc_fullname)
        
    arcpy.CreateFeatureclass_management(workspace, fcname, "POLYGON",spatial_reference=arcpy.SpatialReference(4326))
    fields = tax_json['meta']['view']['columns']
    
    field_type = ['TEXT','TEXT','LONG','LONG', 'TEXT', 'LONG','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT']
    field_names = []
    for ind, field in enumerate(fields):
        name = field['name']
        if field['name'] == 'the_geom':
            continue
        if field['name'].lower() == 'id':
            name =  f'id_{ind}'
        max_len = min(10,len(name))
        name = name[:max_len]
        field_names.append(name)
    field_names = [field.replace(' ', '_') for field in field_names]
    field_names = [field.replace('.', '_') for field in field_names]
    
    for ind, field_name in enumerate(field_names):
        arcpy.management.AddField(fc_fullname, field_name=field_name, field_type = field_type[ind])
        
    field_names.append('SHAPE@')
    
        
    with arcpy.da.InsertCursor(fc_fullname, field_names) as cursor:
        for row in tax_json['data']:
            new_row = []
            for ind, value in enumerate(row):
                if ind == 8:  # Skip the geometry field for now
                    continue
                if value is None:
                    value = ""  # Replace None with an empty string
                new_row.append(value)
            new_row.append(row[8])  # Add the geometry field at the end
            cursor.insertRow(new_row)

def main():
    importNoTaxJSON(out_fc='out_fc.shp')
    
if __name__ == "__main__":
    main()