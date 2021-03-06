# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# create_names.py
# Created on: 2016-05-06 15:39:29.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------
#run this third no args
# C:\Python27\ArcGIS10.3\python.exe create_names.py

# Import arcpy module
import arcpy
import os

# Local variables:
HUC_12_NC = "E:\\wbdhu12_a_us_september2015.gdb\\WBD\\HUC_12_NC"
HUC12_NAMES_VIEW = "HUC12_NAMES_VIEW"
HUC12_NAMES_VIEW__3_ = HUC12_NAMES_VIEW
HUC12_NAMES_VIEW__4_ = HUC12_NAMES_VIEW__3_
HUC_8_NC = "E:\\wbdhu8_a_us_september2015.gdb\\WBD\\HUC_8_NC"
HUC8_NAMES_VIEW = "HUC8_NAMES_VIEW"
HUC8_NAMES_VIEW__4_ = HUC8_NAMES_VIEW
HUC8_NAMES_VIEW__3_ = HUC8_NAMES_VIEW__4_
HUC_6_NC = "E:\\wbdhu6_a_us_september2015.gdb\\WBD\\HUC_6_NC"
HUC6_NAMES_VIEW = "HUC6_NAMES_VIEW"
HUC6_NAMES_VIEW__2_ = HUC6_NAMES_VIEW
HUC6_NAMES_VIEW__3_ = HUC6_NAMES_VIEW__2_
rbrp_huc_names_TMP = "E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP"
rbrp_huc_names = rbrp_huc_names_TMP


RDRBP_AGO_gdb = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb"
Delete_succeeded = "true"

# Process: Make Table View (3)
arcpy.MakeTableView_management(HUC_12_NC, HUC12_NAMES_VIEW, "", "", "OBJECTID OBJECTID HIDDEN NONE;SHAPE SHAPE HIDDEN NONE;TNMID TNMID HIDDEN NONE;METASOURCEID METASOURCEID HIDDEN NONE;SOURCEDATADESC SOURCEDATADESC HIDDEN NONE;SOURCEORIGINATOR SOURCEORIGINATOR HIDDEN NONE;SOURCEFEATUREID SOURCEFEATUREID HIDDEN NONE;LOADDATE LOADDATE HIDDEN NONE;GNIS_ID GNIS_ID HIDDEN NONE;AREAACRES AREAACRES HIDDEN NONE;AREASQKM AREASQKM HIDDEN NONE;STATES STATES VISIBLE NONE;HUC12 ID VISIBLE NONE;NAME NAME VISIBLE NONE;HUTYPE HUTYPE HIDDEN NONE;HUMOD HUMOD HIDDEN NONE;TOHUC TOHUC HIDDEN NONE;NONCONTRIBUTINGACRES NONCONTRIBUTINGACRES HIDDEN NONE;NONCONTRIBUTINGSQKM NONCONTRIBUTINGSQKM HIDDEN NONE;SHAPE_Length SHAPE_Length HIDDEN NONE;SHAPE_Area SHAPE_Area HIDDEN NONE")

# Process: Add Field
arcpy.AddField_management(HUC12_NAMES_VIEW, "TYPE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(HUC12_NAMES_VIEW__3_, "TYPE", "'HUC 12'", "PYTHON", "")


# Process: Add Field
arcpy.AddField_management(HUC12_NAMES_VIEW, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC12_NAMES_VIEW, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC12_NAMES_VIEW, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(HUC12_NAMES_VIEW, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC12_NAMES_VIEW, "MAIN", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC12_NAMES_VIEW, "SUB", "!NAME!", "PYTHON", "")



# Process: Make Table View (2)
arcpy.MakeTableView_management(HUC_8_NC, HUC8_NAMES_VIEW, "", "", "OBJECTID OBJECTID HIDDEN NONE;SHAPE SHAPE HIDDEN NONE;TNMID TNMID HIDDEN NONE;METASOURCEID METASOURCEID HIDDEN NONE;SOURCEDATADESC SOURCEDATADESC HIDDEN NONE;SOURCEORIGINATOR SOURCEORIGINATOR HIDDEN NONE;SOURCEFEATUREID SOURCEFEATUREID HIDDEN NONE;LOADDATE LOADDATE HIDDEN NONE;GNIS_ID GNIS_ID HIDDEN NONE;AREAACRES AREAACRES HIDDEN NONE;AREASQKM AREASQKM HIDDEN NONE;STATES STATES VISIBLE NONE;HUC8 ID VISIBLE NONE;NAME NAME VISIBLE NONE;SHAPE_Length SHAPE_Length HIDDEN NONE;SHAPE_Area SHAPE_Area HIDDEN NONE")

# Process: Add Field (2)
arcpy.AddField_management(HUC8_NAMES_VIEW, "TYPE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(HUC8_NAMES_VIEW__4_, "TYPE", "'HUC 8'", "PYTHON", "")



# Process: Add Field (2)
arcpy.AddField_management(HUC8_NAMES_VIEW, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC8_NAMES_VIEW, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC8_NAMES_VIEW, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(HUC8_NAMES_VIEW, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC8_NAMES_VIEW, "MAIN", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC8_NAMES_VIEW, "SUB", "!NAME!", "PYTHON", "")


# Process: Make Table View
arcpy.MakeTableView_management(HUC_6_NC, HUC6_NAMES_VIEW, "", "", "OBJECTID OBJECTID HIDDEN NONE;SHAPE SHAPE HIDDEN NONE;TNMID TNMID HIDDEN NONE;METASOURCEID METASOURCEID HIDDEN NONE;SOURCEDATADESC SOURCEDATADESC HIDDEN NONE;SOURCEORIGINATOR SOURCEORIGINATOR HIDDEN NONE;SOURCEFEATUREID SOURCEFEATUREID HIDDEN NONE;LOADDATE LOADDATE HIDDEN NONE;GNIS_ID GNIS_ID HIDDEN NONE;AREAACRES AREAACRES HIDDEN NONE;AREASQKM AREASQKM HIDDEN NONE;STATES STATES VISIBLE NONE;HUC6 ID VISIBLE NONE;NAME NAME VISIBLE NONE;SHAPE_Length SHAPE_Length HIDDEN NONE;SHAPE_Area SHAPE_Area HIDDEN NONE")

# Process: Add Field (3)
arcpy.AddField_management(HUC6_NAMES_VIEW, "TYPE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(HUC6_NAMES_VIEW__2_, "TYPE", "'HUC 6'", "PYTHON", "")

# Process: Add Field (3)
arcpy.AddField_management(HUC6_NAMES_VIEW, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC6_NAMES_VIEW, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC6_NAMES_VIEW, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(HUC6_NAMES_VIEW, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC6_NAMES_VIEW, "MAIN", "!NAME!", "PYTHON", "")
arcpy.CalculateField_management(HUC6_NAMES_VIEW, "SUB", "!ID!", "PYTHON", "")


# Process: Merge
arcpy.Merge_management("HUC12_NAMES_VIEW;HUC8_NAMES_VIEW;HUC6_NAMES_VIEW", rbrp_huc_names_TMP, "STATES \"STATES\" true true false 50 Text 0 0 ,First,#,HUC12_NAMES_VIEW,STATES,-1,-1,HUC8_NAMES_VIEW,STATES,-1,-1,HUC6_NAMES_VIEW,STATES,-1,-1;ID \"HUC12\" true true false 12 Text 0 0 ,First,#,HUC12_NAMES_VIEW,ID,-1,-1,HUC8_NAMES_VIEW,ID,-1,-1,HUC6_NAMES_VIEW,ID,-1,-1;NAME \"NAME\" true true false 120 Text 0 0 ,First,#,HUC12_NAMES_VIEW,NAME,-1,-1,HUC8_NAMES_VIEW,NAME,-1,-1,HUC6_NAMES_VIEW,NAME,-1,-1;TYPE \"TYPE\" true true false 100 Text 0 0 ,First,#,HUC12_NAMES_VIEW,TYPE,-1,-1,HUC8_NAMES_VIEW,TYPE,-1,-1,HUC6_NAMES_VIEW,type,-1,-1;VALUE \"VALUE\" true true false 100 Text 0 0 ,First,#,HUC12_NAMES_VIEW,VALUE,-1,-1,HUC8_NAMES_VIEW,VALUE,-1,-1,HUC6_NAMES_VIEW,VALUE,-1,-1;MAIN \"MAIN\" true true false 100 Text 0 0 ,First,#,HUC12_NAMES_VIEW,MAIN,-1,-1,HUC8_NAMES_VIEW,MAIN,-1,-1,HUC6_NAMES_VIEW,MAIN,-1,-1;SUB \"SUB\" true true false 100 Text 0 0 ,First,#,HUC12_NAMES_VIEW,SUB,-1,-1,HUC8_NAMES_VIEW,SUB,-1,-1,HUC6_NAMES_VIEW,SUB,-1,-1")


# Process: Table to Table
arcpy.TableToTable_conversion(rbrp_huc_names_TMP, RDRBP_AGO_gdb, "rbrp_huc_names", "", "STATES \"STATES\" true true false 50 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,STATES,-1,-1;ID \"HUC12\" true true false 12 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,ID,-1,-1;NAME \"NAME\" true true false 120 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,NAME,-1,-1;TYPE \"TYPE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,TYPE,-1,-1;VALUE \"VALUE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,VALUE,-1,-1;MAIN \"MAIN\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,MAIN,-1,-1;SUB \"SUB\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,SUB,-1,-1", "")


#copy each huc level for the State to the temp file geo-databases
arcpy.FeatureClassToFeatureClass_conversion (HUC_12_NC, RDRBP_AGO_gdb, 'HUC_12_MAP',"","STATES \"STATES\" true true false 50 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,STATES,-1,-1;ID \"ID\" true true false 12 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,ID,-1,-1;NAME \"NAME\" true true false 120 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,NAME,-1,-1;TYPE \"TYPE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,TYPE,-1,-1;VALUE \"VALUE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,VALUE,-1,-1;MAIN \"MAIN\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,MAIN,-1,-1;SUB \"SUB\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,SUB,-1,-1")
calclayer = os.path.join(RDRBP_AGO_gdb, 'HUC_12_MAP')
arcpy.CalculateField_management(calclayer, "ID", "!VALUE!", "PYTHON", "")

arcpy.FeatureClassToFeatureClass_conversion (HUC_8_NC, RDRBP_AGO_gdb, 'HUC_8_MAP',"","STATES \"STATES\" true true false 50 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,STATES,-1,-1;ID \"ID\" true true false 12 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,ID,-1,-1;NAME \"NAME\" true true false 120 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,NAME,-1,-1;TYPE \"TYPE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,TYPE,-1,-1;VALUE \"VALUE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,VALUE,-1,-1;MAIN \"MAIN\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,MAIN,-1,-1;SUB \"SUB\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,SUB,-1,-1")
calclayer = os.path.join(RDRBP_AGO_gdb, 'HUC_8_MAP')
arcpy.CalculateField_management(calclayer, "ID", "!VALUE!", "PYTHON", "")

arcpy.FeatureClassToFeatureClass_conversion (HUC_6_NC, RDRBP_AGO_gdb, 'HUC_6_MAP',"","STATES \"STATES\" true true false 50 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,STATES,-1,-1;ID \"ID\" true true false 12 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,ID,-1,-1;NAME \"NAME\" true true false 120 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,NAME,-1,-1;TYPE \"TYPE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,TYPE,-1,-1;VALUE \"VALUE\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,VALUE,-1,-1;MAIN \"MAIN\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,MAIN,-1,-1;SUB \"SUB\" true true false 100 Text 0 0 ,First,#,E:\\ncdeq\\RDRBP_AGO.gdb\\rbrp_huc_names_TMP,SUB,-1,-1")
calclayer = os.path.join(RDRBP_AGO_gdb, 'HUC_6_MAP')
arcpy.CalculateField_management(calclayer, "ID", "!VALUE!", "PYTHON", "")


# Process: Delete
arcpy.Delete_management(rbrp_huc_names_TMP, "")
