# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5,6,7 should be scalene')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(7, 5, 6), 'Scalene', '7,5,6 should be scalene')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6, 7, 5), 'Scalene', '6,7,5 should be scalene')
    # Testing for invalid input:
    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(5, 6, 'a'), 'InvalidInput', '5,6,a should return InvalidInput')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(7, 'b', 6), 'InvalidInput', '7,b,6 should return InvalidInput')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle('c', 7, 5), 'InvalidInput', 'c,7,5 should return InvalidInput')
     # Testing for not a triangle:
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 10), 'NotATriangle', '5,5,10 should return NotATriangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles', '5,5,3 should be isosceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles', '5,3,5 should be isosceles')

    def testIsocelesTrianglesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles', '3,5,5 should be isosceles')
     # Testing for the lower limit of inputs:
    def testTriangleWithMinValuesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testTriangleWithMinValuesB(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'NotATriangle', '0,0,0 should return NotATriangle')

    def testTriangleWithMinValuesC(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'NotATriangle', '0,1,1 should return NotATriangle')

     # Testing for the upper limit of inputs:
    def testTriangleWithMaxValuesA(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')

    def testTriangleWithMaxValuesB(self):
        self.assertEqual(classifyTriangle(200, 200, 201), 'InvalidInput', '200,200,201 should return InvalidInput')

    def testTriangleWithMaxValuesC(self):
        self.assertEqual(classifyTriangle(201, 200, 200), 'InvalidInput', '201,200,200 should return InvalidInput')

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

