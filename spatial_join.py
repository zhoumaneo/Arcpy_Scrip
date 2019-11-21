# -*- coding: utf-8 -*-
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
        cs_poipath = city_poipath + "\\"+str(cs)+"\\shp"
        target_features = citypath + "\\" + str(city) + "_FishNet\\"+str(cs)+".shp"
        env.workspace = cs_poipath
        shps = arcpy.ListFiles("*.shp")
        cs_fish_net = cs_poipath + "\\fishnet"
        os.makedirs(cs_fish_net)
        for shp in shps:
            try:
                join_features = cs_poipath + "\\"+shp
                out_feature_class = cs_fish_net+"\\"+shp
                fieldmappings = arcpy.FieldMappings()
                fieldmappings.addTable(target_features)
                fieldmappings.addTable(join_features)
                x = fieldmappings.findFieldMapIndex("type")
                fieldmappings.removeFieldMap(x)
                y = fieldmappings.findFieldMapIndex("city")
                fieldmappings.removeFieldMap(y)
                z = fieldmappings.findFieldMapIndex("district")
                fieldmappings.removeFieldMap(z)
                p = fieldmappings.findFieldMapIndex("gpsx")
                fieldmappings.removeFieldMap(p)
                q = fieldmappings.findFieldMapIndex("gpsy")
                fieldmappings.removeFieldMap(q)
                arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,"#","#",fieldmappings)
            except:
                print city,cs,shp
