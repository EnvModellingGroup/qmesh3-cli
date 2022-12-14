#!/usr/bin/env python

#    Copyright (C) 2013 Alexandros Avdis and others. See the AUTHORS file for a full list of copyright holders.
#
#    This file is part of QMesh.
#
#    QMesh is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    QMesh is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QMesh.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import qmesh

class Test_cli_mesh(unittest.TestCase):
    '''Todo: add test documentation as class docstring '''

    def setUp(self):
            import inspect, os
            qmesh.LOG.setLevel('WARNING')
            thisFileName = inspect.getfile(inspect.currentframe())
            self.thisPath = os.path.dirname(os.path.abspath(thisFileName))

    def create_equator_shapefiles(self):
        '''Create equator as shape-file, for testing purposes'''
        qmesh.initialise()
        equatorLine = qmesh.vector.primitiveShapes.loxodromicLine( \
                                startPoint = (-179,0), \
                                trueNorthBearing = 90, \
                                numbPoints=10, \
                                loopArounds = 0, \
                                endPoint = (179,0), \
                                coordRefSystem_string = "EPSG:4326")
        equatorLine.asShapes().writeFile(self.thisPath+'/equator.shp')

    def create_circular_lake(self):
        '''Create a circle as shape-file, for testing purposes'''
        qmesh.initialise()
        islandShoreline = qmesh.vector.primitiveShapes.Circle(
                                centerPointXi = 0.0,
                                centerPointEta = 45.0,
                                radius = 25,
                                numbPoints = 100,
                                coordRefSystem_string = "EPSG:4326")
        islandShoreline.asShapes().writeFile(self.thisPath+'/circularLake.shp')

    def test_halfGlobe(self):
        '''Todo: Add docstring'''
        import subprocess
        #Create shapefiles.
        self.create_equator_shapefiles()
        #Try the conversion
        returnCode = subprocess.call(["qmesh","-v=error",
                                      "generate_mesh",
                                      "--tcs=PCC",
                                      "--isGlobal",
                                      self.thisPath+"/equator.shp",
                                      self.thisPath+"/halfGlobe"])
        self.assertEqual(returnCode,0)

    def test_circularLake_PCC(self):
        '''Todo: Add docstring'''
        import subprocess
        #Create shapefiles.
        self.create_circular_lake()
        #Try the conversion
        returnCode = subprocess.call(["qmesh","-v=error",
                                      "generate_mesh",
                                      self.thisPath+"/circularLake.shp",
                                      self.thisPath+"/circularLake_PCC",
                                      "--tcs=PCC"])
        self.assertEqual(returnCode,0)

    def test_circularLake_UTM30N(self):
        '''Todo: Add docstring'''
        import subprocess
        #Create shapefiles.
        self.create_circular_lake()
        #Try the conversion
        returnCode = subprocess.call(["qmesh","-v=error",
                                      "generate_mesh",
                                      self.thisPath+"/circularLake.shp",
                                      self.thisPath+"/circularLake_UTM30N",
                                      "--tcs=EPSG:32630"])
        self.assertEqual(returnCode,0)

if __name__ == '__main__':
    unittest.main()
