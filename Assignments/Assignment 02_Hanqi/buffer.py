import arcpy
arcpy.analysis.Buffer(
    in_features="F:/OneDrive - Louisiana State University/LSU_Course/GEOG/GEOG 4057 GIS Programming/GEOG4057_Hanqi/Assignments/Assignment02_Hanqi/DataFolder/no_retail.shp",
    out_feature_class="F:/OneDrive - Louisiana State University/LSU_Course/GEOG/GEOG 4057 GIS Programming/GEOG4057_Hanqi/Assignments/Assignment02_Hanqi/DataFolder/retail_buffer_1.shp",
    buffer_distance_or_field="500 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)