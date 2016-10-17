# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# create_names_hucs.py
# Created on: 2016-05-06 16:46:04.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------
#run this fourth no args
# C:\Python27\ArcGIS10.3\python.exe create_names_hucs.py

# Import arcpy module
import arcpy


# Local variables:
Cataloging_Unit = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\huc_8"
Cataloging_Unit__3_ = Cataloging_Unit
Cataloging_Unit__7_ = Cataloging_Unit
rbrp_huc_names = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\rbrp_huc_names"
Cataloging_Unit__2_ = Cataloging_Unit__7_
HUC_12 = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\huc_12"
Cataloging_Unit__5_ = HUC_12
HUC_12__2_ = HUC_12
rbrp_huc_names__2_ = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\rbrp_huc_names"
HUC_12__4_ = HUC_12__2_
River_Basin = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\huc_6"
Cataloging_Unit__6_ = River_Basin
River_Basin__2_ = River_Basin
rbrp_huc_names__3_ = "E:\\ncdeq\\code\\ncdeq-data\\RDRBP_AGO.gdb\\rbrp_huc_names"
River_Basin__3_ = River_Basin__2_

# Process: Join Field
arcpy.JoinField_management(Cataloging_Unit, "id", rbrp_huc_names, "ID", "NAME")

# Process: Add Field
arcpy.AddField_management(Cataloging_Unit, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Cataloging_Unit, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Cataloging_Unit, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Cataloging_Unit__7_, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(Cataloging_Unit__7_, "MAIN", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(Cataloging_Unit__7_, "SUB", "!NAME!", "PYTHON", "")

# Process: Join Field (2)
arcpy.JoinField_management(HUC_12, "id", rbrp_huc_names__2_, "ID", "NAME")

# Process: Add Field (2)
arcpy.AddField_management(HUC_12, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC_12, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(HUC_12, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(HUC_12__2_, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC_12__2_, "MAIN", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(HUC_12__2_, "SUB", "!NAME!", "PYTHON", "")

# Process: Join Field (3)
arcpy.JoinField_management(River_Basin, "id", rbrp_huc_names__3_, "ID", "NAME")

# Process: Add Field (3)
arcpy.AddField_management(River_Basin, "VALUE", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(River_Basin, "MAIN", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(River_Basin, "SUB", "TEXT", "", "", "100", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(River_Basin__2_, "VALUE", "!ID!", "PYTHON", "")
arcpy.CalculateField_management(River_Basin__2_, "MAIN", "!NAME!", "PYTHON", "")
arcpy.CalculateField_management(River_Basin__2_, "SUB", "!ID!", "PYTHON", "")
