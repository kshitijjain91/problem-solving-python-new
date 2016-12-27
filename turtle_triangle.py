# program to draw a triangle using three points, a color and a turtle object
import turtle
from turtle import Turtle, Screen

def draw_triangle(points, color, my_turtle):
	my_turtle.fillcolor(color)
	my_turtle.up()
	my_turtle.goto(points[0][0], points[0][1])
	my_turtle.down()
	my_turtle.begin_fill()
	my_turtle.goto(points[1][0], points[1][1])
	my_turtle.goto(points[2][0], points[2][1])
	my_turtle.goto(points[0][0], points[0][1])
	my_turtle.end_fill()


def main():
	my_points = [[-100, -50], [0,100], [100, -50]]
	color = "blue"
	my_turtle = Turtle()
	my_win = Screen()
	draw_triangle(my_points, color, my_turtle)
	my_win.exitonclick()


