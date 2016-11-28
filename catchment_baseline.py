# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# dissolve.py
# Created on: 2016-04-26 12:03:19.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: dissolve <input_data>
# Description:
# ---------------------------------------------------------------------------
#run this baseline no args
#C:\Python27\ArcGIS10.3\python.exe catchment_baseline.py
# Import arcpy module
import arcpy
import json
import os


# Script arguments
input_data = arcpy.GetParameterAsText(0)

# Local variables:

#input data
path = "E:\\ncdeq\\DMS_RBRP.gdb"
temp_dissolve = "E:\\DMS_RBRP.gdb\\temp_dissolve"


#output data
outPathGDB = "E:\\ncdeq\\code\\ncdeq-data"
outGDB = "RDRBP_AGO.gdb"

#baseLine data
with open('json/catchment_baseline_mapping.json') as data_file:
    NLCDData = json.load(data_file)

#transposed_template data
with open('json/transposed_template.json') as data_file:
    transposedTemplate = json.load(data_file)

outGDBFull =  os.path.join(outPathGDB, outGDB)

#result data
transposed =  os.path.join(outGDBFull, 'ncdeq_normailized')

for field in transposedTemplate:
	fieldName = field['fieldname']
	fieldType = field['fieldType']
	fieldLength = field['Length']
	arcpy.AddField_management(transposed, fieldName, fieldType, "", "", fieldLength, "", "NULLABLE", "NON_REQUIRED", "")

#add name fields for dissovled huc data where do I get that
#update the ago db. later

#check if field exists
def FieldExist(featureclass, fieldname):
	fieldList = arcpy.ListFields(featureclass, fieldname)

	fieldCount = len(fieldList)

	if (fieldCount == 1):
		return True
	else:
		return False

#transposed_template data
with open('json/geography_levels_catchments_baseline.json') as data_file:
    geographyLevels = json.load(data_file)


aggreatate_type = "MEAN"

#this needs to live in code because the json data is inserted
chartTypes = [{'name':'NHDCat_comb_baseline',
			   'table':'NHDCat_comb_baseline',
			   'fields_conversion':NLCDData,
			   'fields_dissovled': [['GRIDCODE','FIRST'],
                                    ['HUC_12','FIRST'],
                                    ['AreaSqKM', aggreatate_type],
                                    ['Shape_Area', aggreatate_type],
			   						['ALL_base', aggreatate_type],
			   						['Hab_base_norm',aggreatate_type],
			   						['Hydro_base_norm', aggreatate_type],
			   						['WQ_base_norm', aggreatate_type],
									['MeanLikelihood_norm',aggreatate_type],
									['q2yr_base_norm',aggreatate_type],
									['q10yr_base_norm',aggreatate_type],
									['q50yr_base_norm',aggreatate_type],
									['q100yr_base_norm',aggreatate_type],
									['N_total_base_norm',aggreatate_type],
									['P_total_base_norm',aggreatate_type],
									['N_AG_base_norm',aggreatate_type],
									['N_URBAN_base_norm',aggreatate_type],
									['N_CMAQ2002KG_base_norm',aggreatate_type],
									['P_AG_base_norm',aggreatate_type],
									['P_URBAN_base_norm',aggreatate_type]
                                ]}]

#walk the chart types object and dissolve and transpose (normalize) the data
for chartType in chartTypes:
    print 'Chart Type: ' + chartType['name']
    chartTypeName = chartType['name']

    #get input table
    inputFC =  os.path.join(path, chartType['table'])

    #get fields in input data
    fields = arcpy.ListFields(  os.path.join(path, inputFC)  )

    #get json data for how to deal with each field
    input_dict = chartType['fields_conversion']

    #check of huc 6 exists if not add and calculae field
    # or is it better to not mutate the data and create a copy... and delete copy after processings
    if not FieldExist(inputFC,'HUC_6'):

        #add field
        arcpy.AddField_management(inputFC, "HUC_6", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

		#calc HUC_6
        arcpy.CalculateField_management(inputFC, "HUC_6", "!HUC_12![0:6]", "PYTHON", "")

    #walk the geograpy levels and dissolve each level
    for geog in geographyLevels:
        currentGeographyLevel = geog['fieldName']
        print 'Dissolve: ' + currentGeographyLevel
        print '  ' + geog['level']

        temp_dissolve = os.path.join(outGDBFull, geog['level'])
        dissolve = os.path.join(outGDBFull, 'dissolve')

        #if feature class exists delete
        if arcpy.Exists(temp_dissolve):
            arcpy.Delete_management(temp_dissolve)

        #dissolve on geographyLevels
        StatisticsFields = chartType['fields_dissovled']
        arcpy.Dissolve_management(inputFC, temp_dissolve, currentGeographyLevel, StatisticsFields, "MULTI_PART", "DISSOLVE_LINES" )

        #iterate fields and to send dissolve
        for field in fields:

            #find matching instance of field on data.
            #then use this to construct the dissilove varriables.
            output_dict = [x for x in input_dict if x['fieldName'] == field.name]

            #if field exists in template we will use the field in output ddata.
            #  need to know who we want the table data formated - derieved from tempatle json
            if (output_dict):
                transposeField = output_dict[0]['fieldName']
                temp_transposed = os.path.join(outGDB, 'temp_transposed_' + currentGeographyLevel + '_'  + transposeField)
                # temp_transposed = os.path.join(outGDB,'test')

                #if feature class exists delete
                if arcpy.Exists(temp_transposed):
                    arcpy.Delete_management(temp_transposed)

                arcpy.TransposeFields_management(temp_dissolve, aggreatate_type + "_" + transposeField + " " + aggreatate_type + "_" + transposeField, temp_transposed, "chart_label", "chart_value", currentGeographyLevel + ";FIRST_HUC_12")


                print '  ' + transposeField
                for f in output_dict[0]:
                    print '    ' + f

                #go through template and add missing fields
                for field in transposedTemplate:
                    fieldName = field['fieldname']
                    fieldType = field['fieldType']
                    fieldLength = field['Length']
                    if not FieldExist(temp_transposed,fieldName):
                        arcpy.AddField_management(temp_transposed, fieldName, fieldType, "", "", fieldLength, "", "NULLABLE", "NON_REQUIRED", "")

                # Process: calculate_geography_level
                arcpy.CalculateField_management(temp_transposed, "geography_level",   geog['geographyLevel'], "PYTHON", "")

                # Process: calculate_geography_match_id
                if  geog['level'] == 'Catchment' or geog['level'] == 'NLCD_Catchments'  or geog['level'] == 'catchments_baseline':
                    arcpy.CalculateField_management(temp_transposed, "geography_match_id",  "!"+ geog['match']+"!", "PYTHON", "")
                else:
                    arcpy.CalculateField_management(temp_transposed, "geography_match_id", "!"+currentGeographyLevel+"![0:"+ geog['match']+"]", "PYTHON", "")

                #process: chart Description
                arcpy.CalculateField_management(temp_transposed, "chart_description", "'" + output_dict[0]['chartDescription'] + "'", "PYTHON", "")

                # Process: Calculate_chart_type
                arcpy.CalculateField_management(temp_transposed, "chart_id","'" + output_dict[0]['chartId'] + "'" , "PYTHON", "")

                # Process: Calculate_chart_type
                arcpy.CalculateField_management(temp_transposed, "chart_matchid","'" + output_dict[0]['chartMatchId'] + "'" , "PYTHON", "")

                # Process: Calculate_chart_type
                arcpy.CalculateField_management(temp_transposed, "chart_type","'" + output_dict[0]['chartType'] + "'" , "PYTHON", "")

                # Process: Calculate_chart_level_labe
                arcpy.CalculateField_management(temp_transposed, "chart_level_label", "'" + output_dict[0]['chartLabel'] + "'", "PYTHON", "")

                # Process: Calculate_chart_level
                arcpy.CalculateField_management(temp_transposed, "chart_level", "'" + output_dict[0]['chartLevel'] + "'", "PYTHON", "")

                arcpy.CalculateField_management(temp_transposed, "ID", "!" + geog['fieldName'] + "!" , "PYTHON", "")

                # Process: Calculate_id
                arcpy.CalculateField_management(temp_transposed, "geography_label", "'"+ geog['level']+"'", "PYTHON", "")

                #round to two decimeals
                arcpy.CalculateField_management(temp_transposed, "chart_value", "round(float(!chart_value!),8)", "PYTHON", "")

                #delete field for curent geog name i.e huc12 should be id now
                if FieldExist(inputFC,currentGeographyLevel):
                    deleteFields = []
                    deleteFields.append(currentGeographyLevel)
                    t = arcpy.DeleteField_management(temp_transposed, deleteFields)

                #remove huc12
                if FieldExist(temp_transposed,'FIRST_HUC_12'):
                    deleteFields = []
                    deleteFields.append('FIRST_HUC_12')
                    t = arcpy.DeleteField_management(temp_transposed, deleteFields)

                #remove current agregated fields
                if FieldExist(temp_dissolve, aggreatate_type + "_" + transposeField):
                    deleteFields =[]
                    deleteFields.append( aggreatate_type + "_" + transposeField)
                    arcpy.DeleteField_management(temp_dissolve, deleteFields)

                #append to transpose
                arcpy.Append_management(temp_transposed,transposed)

                #delete temp transpose
                if arcpy.Exists(temp_transposed):
                    arcpy.Delete_management(temp_transposed)

for geog in geographyLevels:
    temp_dissolve = os.path.join(outGDBFull, geog['level'])

    if FieldExist(temp_dissolve, geog['fieldName']):
        arcpy.AlterField_management(temp_dissolve,  geog['fieldName'], "ID", "ID", "", "", "NON_NULLABLE", "false")

    if FieldExist(temp_dissolve, 'FIRST_HUC_12'):
        deleteFields =[]
        deleteFields.append('FIRST_HUC_12')
        arcpy.DeleteField_management(temp_dissolve, deleteFields)

#if huc_6 exists delete it
if FieldExist(inputFC,'HUC_6'):
	deleteFields = []
	deleteFields.append('HUC_6')
	t = arcpy.DeleteField_management(inputFC, deleteFields)
