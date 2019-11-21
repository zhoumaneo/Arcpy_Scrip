import os
import arcpy
from arcpy import env
import arcgisscripting
gp = arcgisscripting.create()
spatial_ref = r'D:\pycharm_project\WGS1984.prj'
x_corrods = 'gpsx'
y_corrods = 'gpsy'
path = "D:\\pycharm_project\\input\\"
files = os.listdir(path)
for file in files:
    citypath = path + str(file) + '\\'
    css = os.listdir(citypath)
    for cs in css:
        cspath = citypath + str(cs)
        env.workspace = cspath
        pathout = cspath + '\\shp'
        os.makedirs(pathout)
        files = arcpy.ListFiles("*.csv")
        try:
            for file1 in files:
                print file1
                info = os.path.basename(file1).split('.')[0].replace('-', '_')
                intable = file1
                outlayer = info
                print'outlayer', outlayer
                gp.MakeXYEventLayer_management(intable, x_corrods, y_corrods, outlayer, spatial_ref)
                print'MakeXYEventLayer over'
                gp.FeatureClassToShapefile_conversion(outlayer, pathout)
                print'ToShapefile over'

        except:
            print gp.GetMessages()