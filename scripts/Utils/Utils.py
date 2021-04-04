# coding=utf-8
import math as math

class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = float(math.sqrt(math.pow(self.x, 2.0) + math.pow(self.y, 2.0) + math.pow(self.z, 2.0)))
    
    @classmethod
    def getDistanceBetweenTwoPoints(cls, pointA, pointB):
        return math.sqrt(math.pow(pointB.x - pointA.x,2) + math.pow(pointB.y - pointA.y,2) + math.pow(pointB.z - pointA.z,2))
    
    @classmethod
    def getDotProduct(cls, vecA, vecB):
        return vecA.x * vecB.x + vecA.y * vecB.y + vecA.z * vecB.z

    # @classmethod
    # def getCrossProduct(cls, vecA, vecB, angle):
    #     return vecA.magnitude * vecB.magnitude * math.sin(angle) * Vector3.getDotProduct(vecA,vecB)

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y-other.y, self.z-other.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y+other.y, self.z+other.z)

    @classmethod
    def getAngleBetweenVector(cls, vecA, vecB):
        if(vecA.magnitude *vecB.magnitude != 0):
            return math.degrees(math.acos(Vector3.getDotProduct(vecA,vecB)/(vecA.magnitude *vecB.magnitude)))
        else:
            return 0

