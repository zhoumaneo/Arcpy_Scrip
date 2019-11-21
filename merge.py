import arcpy
from arcpy import env
import os
inputpath = "D:\\pycharm_project\\input\\"
citys = os.listdir(inputpath)
for city in citys:
    citypath = inputpath + str(city)
    city_poipath = citypath + "\\"+str(city)+"_poi"
    css = os.listdir(city_poipath)
    for cs in css:
        cs_poipath = city_poipath + "\\"+str(cs)+"\\shp\\fishnet"
        env.workspace = cs_poipath
        output = cs_poipath + "\\merge.shp"
        shps = arcpy.ListFiles("*.shp")
        shppaths = [cs_poipath + "\\" + i for i in shps]
        in_file = shppaths[:2]
        fieldMappings = arcpy.FieldMappings()
        fm = arcpy.FieldMap()
        for field in arcpy.ListFields(in_file,"Join_Count"):
            fm.addInputField(in_file,field.name)
        fm.mergeRule = 'Sum'
        f_name = fm.outputField
        f_name.name = 'Sum_Join_Count'
        fm.outputField = f_name
        fieldMappings.addFieldMap(fm)
        arcpy.Merge_management(in_file,output,fieldMappings)
