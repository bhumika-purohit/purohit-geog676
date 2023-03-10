#create a gdb and garage feature
import arcpy

arcpy.env.workspace = r'I:\GEOG 676\Lab 4\codes_env'
folder_path = r'I:\GEOG 676\Lab 4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'I:\GEOG 676\Lab 4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
Garage_Points = gdb_path + '\\' + garage_layer_name

#open campus gdb, copy building feature to our gdb
campus = r'I:\GEOG 676\Lab 4\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management('Garage_Points', gdb_path + '\Garage_Points_reprojected', spatial_ref)

#Buffer the Garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

#Intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings],gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', 'I:\GEOG 676\Lab 4', 'nearbyBuildings.csv')