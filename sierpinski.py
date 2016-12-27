# program to draw sierpinski triangles recursively

from turtle import Turtle, Screen
from turtle_triangle import draw_triangle

def sierpinski(points, my_turtle, degree):
	colors = ["blue", "green", "red", "yellow"]
	if degree > 0:
		color = colors[degree % 4]
		draw_triangle(points, color, my_turtle)
		point_1 = [points[0][0], points[0][1]]
		point_2 = [points[1][0], points[1][1]]
		point_3 = [points[2][0], points[2][1]]
		new_points = [mid_point([point_1, point_2]), mid_point([point_2, point_3]), mid_point([point_3, point_1])]
		degree = degree - 1
		sierpinski([point_1, new_points[0], new_points[2]], my_turtle, degree)
		sierpinski([point_2, new_points[0], new_points[1]], my_turtle, degree)
		sierpinski([point_3, new_points[1], new_points[2]], my_turtle, degree)



def mid_point(points):
	return [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]


def main():
	my_points = [[-100, -50], [0,100], [100, -50]]
	degree = 5
	my_turtle = Turtle()
	my_win = Screen()
	sierpinski(my_points, my_turtle, degree)
	my_win.exitonclick()
 
main()