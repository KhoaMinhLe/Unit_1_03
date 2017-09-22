# Created by: Khoa Le
# Created on September 20 2017
# Created for ICS3U
# This program is to calculate the area and perimeter.

import ui

def calculate_touch_up_inside(sender):
	# Input
	length = int(view['length_textfield'].text)
	width = int(view['width_textfield'].text)
	#Process
	area = length * width
	perimeter = 2 * (length + width)
	#Output
	view['area_answer_label'].text = str(area) + 'cm^2'
	view['perimeter_answer_label'].text = str(perimeter) + 'cm'

view = ui.load_view()
view.present('sheet')
