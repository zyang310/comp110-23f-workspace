"""Making use of the Point class"""
from lessons.CQ07.point import Point

mypoint: Point = Point(1.0, 2.0)
print(mypoint.scale_by(2))
print(mypoint.y)

my_new_point: Point = mypoint.scale(2)
print(my_new_point.x)


print(mypoint.x)