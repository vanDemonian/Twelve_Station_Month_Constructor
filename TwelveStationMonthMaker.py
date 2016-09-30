#!/usr/bin/python

def TwelveStationMonthMaker(name):

	"""	
	Delivers the x and y coordinates required
	to place the image within a grid:

		12 stations
		4 times of day
		31 days 	                

	    Format 0: h (4 x 12) x w 31
	    		31 columns across by 48 rows high
				1 - 31 days across
	    		station by time of day on vertical axis
	    		12 horizontal bands  - Stations 1 - 2


	    Format 1: h (12 x 4) x w 31
	    		31 columns across by 48 rows high
	    		1 - 31 days across
	    		time of day by station on vertical axis
	    		4 horizontal bands  - 6am, 12noon, 6pm, midnight


	    Format 2: h 31 x w (4 x 12)
	    		48 columns across by 31 rows high
				1 - 31 days on vertical axis
	    		station by time of day on horizontal axis
	    		12 vertical bands  - Stations 1 - 2




		each image dimension  = 680 x 452
					
		print size
		total x pixels = 21080  = 680 x 31
		total y pixels = 21696  = 12 x 4 x 452

		1488  cells   = ((4 times of day) x (12 stations)) x 31 days

	"""	

	#____________________________________________________________________________
	format 		= 3
	xstep 		= 680
	ystep 		= 452

	location 	= str(name[0:7])
	date 		= str(name[8:18])

	year 		= int(name[8:12])
	month 		= int(name[13:15])
	day 		= int(name[16:18])

	hour 		= int(name[19:21])
	minute 		= int(name[22:24])
	second 		= int(name[25:27])

	seconds_since_midnight = (int(second) + int(minute*60) + int(hour*3600))
	Secs = seconds_since_midnight

	#____________________________________________________________________________
	if location == 'NAVARRE':
		loc = 1
	if location == 'STCLAIR':
		loc = 2
	if location == 'KINGWIL':
		loc = 3
	if location == 'BRADYSL':
		loc = 4
	if location == 'MEADUPS':
		loc = 5
	if location == 'MEADPOW':
		loc = 6
	if location == 'MEADDWN':
		loc = 7
	if location == 'MONA___':
		loc = 8
	if location == 'MONTAGU':
		loc = 9
	if location == 'HUNTNOR':
		loc = 10
	if location == 'HUNTSOU':
		loc = 11
	if location == 'TAROONA':
		loc = 12


	if Secs >= 21300 and Secs <= 21600:
		time = 6
	elif Secs >= 42900 and Secs <= 43200:
		time = 12
	elif Secs >= 64500 and Secs <= 64800:
		time = 18
	elif Secs >= 86100 and Secs <= 86400:
		time = 24


#_____________________________________________________________________________________________________________________________________________


	#__________________________________
	#	format 0 
	#__________________________________

	if format == 0:

		if   day == 1:
			colNum = 0
		elif day == 2:
			colNum = 1
		elif day == 3:
			colNum = 2
		elif day == 4:
			colNum = 3
		elif day == 5:
			colNum = 4
		elif day == 6:
			colNum = 5
		elif day == 7:
			colNum = 6
		elif day == 8:
			colNum = 7
		elif day == 9:
			colNum = 8
		elif day == 10:
			colNum = 9

		elif day == 11:
			colNum = 10
		elif day == 12:
			colNum = 11
		elif day == 13:
			colNum = 12
		elif day == 14:
			colNum = 13
		elif day == 15:
			colNum = 14
		elif day == 16:
			colNum = 15
		elif day == 17:
			colNum = 16
		elif day == 18:
			colNum = 17
		elif day == 19:
			colNum = 18
		elif day == 20:
			colNum = 19

		elif day == 21:
			colNum = 20
		elif day == 22:
			colNum = 21
		elif day == 23:
			colNum = 22
		elif day == 24:
			colNum = 23
		elif day == 25:
			colNum = 24
		elif day == 26:
			colNum = 25
		elif day == 27:
			colNum = 26
		elif day == 28:
			colNum = 27
		elif day == 29:
			colNum = 28
		elif day == 30:
			colNum = 29
		elif day == 31:
			colNum = 30


		# 31 columns = one column for each day of the month


		if colNum == 0:
			x_Coordinate = 0*xstep
		if colNum == 1:
			x_Coordinate = 1*xstep
		if colNum == 2:
			x_Coordinate = 2*xstep
		if colNum == 3:
			x_Coordinate = 3*xstep
		if colNum == 4:
			x_Coordinate = 4*xstep
		if colNum == 5:
			x_Coordinate = 5*xstep
		if colNum == 6:
			x_Coordinate = 6*xstep

		if colNum == 7:
			x_Coordinate = 7*xstep
		if colNum == 8:
			x_Coordinate = 8*xstep
		if colNum == 9:
			x_Coordinate = 9*xstep
		if colNum == 10:
			x_Coordinate = 10*xstep
		if colNum == 11:
			x_Coordinate = 11*xstep
		if colNum == 12:
			x_Coordinate = 12*xstep
		if colNum == 13:
			x_Coordinate = 13*xstep

		if colNum == 14:
			x_Coordinate = 14*xstep
		if colNum == 15:
			x_Coordinate = 15*xstep
		if colNum == 16:
			x_Coordinate = 16*xstep
		if colNum == 17:
			x_Coordinate = 17*xstep
		if colNum == 18:
			x_Coordinate = 18*xstep
		if colNum == 19:
			x_Coordinate = 19*xstep
		if colNum == 20:
			x_Coordinate = 20*xstep

		if colNum == 21:
			x_Coordinate = 21*xstep
		if colNum == 22:
			x_Coordinate = 22*xstep
		if colNum == 23:
			x_Coordinate = 23*xstep
		if colNum == 24:
			x_Coordinate = 24*xstep
		if colNum == 25:
			x_Coordinate = 25*xstep
		if colNum == 26:
			x_Coordinate = 26*xstep
		if colNum == 27:
			x_Coordinate = 27*xstep

		if colNum == 28:
			x_Coordinate = 28*xstep
		if colNum == 29:
			x_Coordinate = 29*xstep
		if colNum == 30:
			x_Coordinate = 30*xstep
	
	#____________________________________________________________________________


		#__________location 1 NAVARRE______________


		if time == 6 and loc == 1:
			y_Coordinate = 0*ystep
		if time == 12 and loc == 1:
			y_Coordinate = 1*ystep
		if time == 18 and loc == 1:
			y_Coordinate = 2*ystep
		if time == 24 and loc == 1:
			y_Coordinate = 3*ystep

		#__________location 2 STCLAIR______________

		if time == 6 and loc == 2:
			y_Coordinate = 4*ystep
		if time == 12 and loc == 2:
			y_Coordinate = 5*ystep
		if time == 18 and loc == 2:
			y_Coordinate = 6*ystep
		if time == 24 and loc == 2:
			y_Coordinate = 7*ystep

		#__________location 3 KINGWIL______________

		if time == 6 and loc == 3:
			y_Coordinate = 8*ystep
		if time == 12 and loc == 3:
			y_Coordinate = 9*ystep
		if time == 18 and loc == 3:
			y_Coordinate = 10*ystep
		if time == 24 and loc == 3:
			y_Coordinate = 11*ystep

		#__________location 4 BRADYSL______________

		if time == 6 and loc == 4:
			y_Coordinate = 12*ystep
		if time == 12 and loc == 4:
			y_Coordinate = 13*ystep
		if time == 18 and loc == 4:
			y_Coordinate = 14*ystep
		if time == 24 and loc == 4:
			y_Coordinate = 15*ystep

		#__________location 5 MEADUPS______________

		if time == 6 and loc == 5:
			y_Coordinate = 16*ystep
		if time == 12 and loc == 5:
			y_Coordinate = 17*ystep
		if time == 18 and loc == 5:
			y_Coordinate = 18*ystep
		if time == 24 and loc == 5:
			y_Coordinate = 19*ystep

		#__________location 6 MEADPOW______________

		if time == 6 and loc == 6:
			y_Coordinate = 20*ystep
		if time == 12 and loc == 6:
			y_Coordinate = 21*ystep
		if time == 18 and loc == 6:
			y_Coordinate = 22*ystep
		if time == 24 and loc == 6:
			y_Coordinate = 23*ystep

		#__________location 7 MEADDWN______________

		if time == 6 and loc == 7:
			y_Coordinate = 24*ystep
		if time == 12 and loc == 7:
			y_Coordinate = 25*ystep
		if time == 18 and loc == 7:
			y_Coordinate = 26*ystep
		if time == 24 and loc == 7:
			y_Coordinate = 27*ystep

		#__________location 8 MONA_________________

		if time == 6 and loc == 8:
			y_Coordinate = 28*ystep
		if time == 12 and loc == 8:
			y_Coordinate = 29*ystep
		if time == 18 and loc == 8:
			y_Coordinate = 30*ystep
		if time == 24 and loc == 8:
			y_Coordinate = 31*ystep

		#__________location 9 MONTAGU______________

		if time == 6 and loc == 9:
			y_Coordinate = 32*ystep
		if time == 12 and loc == 9:
			y_Coordinate = 33*ystep
		if time == 18 and loc == 9:
			y_Coordinate = 34*ystep
		if time == 24 and loc == 9:
			y_Coordinate = 35*ystep

		#__________location 10 HUNTNOR_____________

		if time == 6 and loc == 10:
			y_Coordinate = 36*ystep
		if time == 12 and loc == 10:
			y_Coordinate = 37*ystep
		if time == 18 and loc == 10:
			y_Coordinate = 38*ystep
		if time == 24 and loc == 10:
			y_Coordinate = 39*ystep

		#__________location 11 HUNTSOU_____________

		if time == 6 and loc == 11:
			y_Coordinate = 40*ystep
		if time == 12 and loc == 11:
			y_Coordinate = 41*ystep
		if time == 18 and loc == 11:
			y_Coordinate = 42*ystep
		if time == 24 and loc == 11:
			y_Coordinate = 43*ystep

		#__________location 12 TAROONA_____________

		if time == 6 and loc == 12:
			y_Coordinate = 44*ystep
		if time == 12 and loc == 12:
			y_Coordinate = 45*ystep
		if time == 18 and loc == 12:
			y_Coordinate = 46*ystep
		if time == 24 and loc == 12:
			y_Coordinate = 47*ystep

#_____________________________________________________________________________________________________________________________________________


	#__________________________________
	#	format 1 
	#__________________________________

	if format == 1:

		if   day == 1:
			colNum = 0
		elif day == 2:
			colNum = 1
		elif day == 3:
			colNum = 2
		elif day == 4:
			colNum = 3
		elif day == 5:
			colNum = 4
		elif day == 6:
			colNum = 5
		elif day == 7:
			colNum = 6
		elif day == 8:
			colNum = 7
		elif day == 9:
			colNum = 8
		elif day == 10:
			colNum = 9

		elif day == 11:
			colNum = 10
		elif day == 12:
			colNum = 11
		elif day == 13:
			colNum = 12
		elif day == 14:
			colNum = 13
		elif day == 15:
			colNum = 14
		elif day == 16:
			colNum = 15
		elif day == 17:
			colNum = 16
		elif day == 18:
			colNum = 17
		elif day == 19:
			colNum = 18
		elif day == 20:
			colNum = 19

		elif day == 21:
			colNum = 20
		elif day == 22:
			colNum = 21
		elif day == 23:
			colNum = 22
		elif day == 24:
			colNum = 23
		elif day == 25:
			colNum = 24
		elif day == 26:
			colNum = 25
		elif day == 27:
			colNum = 26
		elif day == 28:
			colNum = 27
		elif day == 29:
			colNum = 28
		elif day == 30:
			colNum = 29
		elif day == 31:
			colNum = 30


		# 31 columns = one column for each day of the month

		if colNum == 0:
			x_Coordinate = 0*xstep
		if colNum == 1:
			x_Coordinate = 1*xstep
		if colNum == 2:
			x_Coordinate = 2*xstep
		if colNum == 3:
			x_Coordinate = 3*xstep
		if colNum == 4:
			x_Coordinate = 4*xstep
		if colNum == 5:
			x_Coordinate = 5*xstep
		if colNum == 6:
			x_Coordinate = 6*xstep

		if colNum == 7:
			x_Coordinate = 7*xstep
		if colNum == 8:
			x_Coordinate = 8*xstep
		if colNum == 9:
			x_Coordinate = 9*xstep
		if colNum == 10:
			x_Coordinate = 10*xstep
		if colNum == 11:
			x_Coordinate = 11*xstep
		if colNum == 12:
			x_Coordinate = 12*xstep
		if colNum == 13:
			x_Coordinate = 13*xstep

		if colNum == 14:
			x_Coordinate = 14*xstep
		if colNum == 15:
			x_Coordinate = 15*xstep
		if colNum == 16:
			x_Coordinate = 16*xstep
		if colNum == 17:
			x_Coordinate = 17*xstep
		if colNum == 18:
			x_Coordinate = 18*xstep
		if colNum == 19:
			x_Coordinate = 19*xstep
		if colNum == 20:
			x_Coordinate = 20*xstep

		if colNum == 21:
			x_Coordinate = 21*xstep
		if colNum == 22:
			x_Coordinate = 22*xstep
		if colNum == 23:
			x_Coordinate = 23*xstep
		if colNum == 24:
			x_Coordinate = 24*xstep
		if colNum == 25:
			x_Coordinate = 25*xstep
		if colNum == 26:
			x_Coordinate = 26*xstep
		if colNum == 27:
			x_Coordinate = 27*xstep

		if colNum == 28:
			x_Coordinate = 28*xstep
		if colNum == 29:
			x_Coordinate = 29*xstep
		if colNum == 30:
			x_Coordinate = 30*xstep
	
	#____________________________________________________________________________



		if time == 6 and loc == 1:
			y_Coordinate = 0*ystep
		if time == 6 and loc == 2:
			y_Coordinate = 1*ystep
		if time == 6 and loc == 3:
			y_Coordinate = 2*ystep
		if time == 6 and loc == 4:
			y_Coordinate = 3*ystep
		if time == 6 and loc == 5:
			y_Coordinate = 4*ystep
		if time == 6 and loc == 6:
			y_Coordinate = 5*ystep
		if time == 6 and loc == 7:
			y_Coordinate = 6*ystep
		if time == 6 and loc == 8:
			y_Coordinate = 7*ystep
		if time == 6 and loc == 9:
			y_Coordinate = 8*ystep
		if time == 6 and loc == 10:
			y_Coordinate = 9*ystep
		if time == 6 and loc == 11:
			y_Coordinate = 10*ystep
		if time == 6 and loc == 12:
			y_Coordinate = 11*ystep

		#__________12noon______________
		if time == 12 and loc == 1:
			y_Coordinate = 12*ystep
		if time == 12 and loc == 2:
			y_Coordinate = 13*ystep
		if time == 12 and loc == 3:
			y_Coordinate = 14*ystep
		if time == 12 and loc == 4:
			y_Coordinate = 15*ystep
		if time == 12 and loc == 5:
			y_Coordinate = 16*ystep
		if time == 12 and loc == 6:
			y_Coordinate = 17*ystep
		if time == 12 and loc == 7:
			y_Coordinate = 18*ystep
		if time == 12 and loc == 8:
			y_Coordinate = 19*ystep
		if time == 12 and loc == 9:
			y_Coordinate = 20*ystep
		if time == 12 and loc == 10:
			y_Coordinate = 21*ystep
		if time == 12 and loc == 11:
			y_Coordinate = 22*ystep
		if time == 12 and loc == 12:
			y_Coordinate = 23*ystep
			
		#__________18pm______________
		if time == 18 and loc == 1:
			y_Coordinate = 24*ystep
		if time == 18 and loc == 2:
			y_Coordinate = 25*ystep
		if time == 18 and loc == 3:
			y_Coordinate = 26*ystep
		if time == 18 and loc == 4:
			y_Coordinate = 27*ystep
		if time == 18 and loc == 5:
			y_Coordinate = 28*ystep
		if time == 18 and loc == 6:
			y_Coordinate = 29*ystep
		if time == 18 and loc == 7:
			y_Coordinate = 30*ystep
		if time == 18 and loc == 8:
			y_Coordinate = 31*ystep
		if time == 18 and loc == 9:
			y_Coordinate = 32*ystep
		if time == 18 and loc == 10:
			y_Coordinate = 33*ystep
		if time == 18 and loc == 11:
			y_Coordinate = 34*ystep
		if time == 18 and loc == 12:
			y_Coordinate = 35*ystep
			
		#__________24midnight______________
		if time == 24 and loc == 1:
			y_Coordinate = 36*ystep
		if time == 24 and loc == 2:
			y_Coordinate = 37*ystep
		if time == 24 and loc == 3:
			y_Coordinate = 38*ystep
		if time == 24 and loc == 4:
			y_Coordinate = 39*ystep
		if time == 24 and loc == 5:
			y_Coordinate = 40*ystep
		if time == 24 and loc == 6:
			y_Coordinate = 41*ystep
		if time == 24 and loc == 7:
			y_Coordinate = 42*ystep
		if time == 24 and loc == 8:
			y_Coordinate = 43*ystep
		if time == 24 and loc == 9:
			y_Coordinate = 44*ystep
		if time == 24 and loc == 10:
			y_Coordinate = 45*ystep
		if time == 24 and loc == 11:
			y_Coordinate = 46*ystep
		if time == 24 and loc == 12:
			y_Coordinate = 47*ystep


#_____________________________________________________________________________________________________________________________________________


	#__________________________________
	#	format 2 
	#__________________________________

	if format == 2:

		if   day == 1:
			rowNum = 0
		elif day == 2:
			rowNum = 1
		elif day == 3:
			rowNum = 2
		elif day == 4:
			rowNum = 3
		elif day == 5:
			rowNum = 4
		elif day == 6:
			rowNum = 5
		elif day == 7:
			rowNum = 6
		elif day == 8:
			rowNum = 7
		elif day == 9:
			rowNum = 8
		elif day == 10:
			rowNum = 9

		elif day == 11:
			rowNum = 10
		elif day == 12:
			rowNum = 11
		elif day == 13:
			rowNum = 12
		elif day == 14:
			rowNum = 13
		elif day == 15:
			rowNum = 14
		elif day == 16:
			rowNum = 15
		elif day == 17:
			rowNum = 16
		elif day == 18:
			rowNum = 17
		elif day == 19:
			rowNum = 18
		elif day == 20:
			rowNum = 19

		elif day == 21:
			rowNum = 20
		elif day == 22:
			rowNum = 21
		elif day == 23:
			rowNum = 22
		elif day == 24:
			rowNum = 23
		elif day == 25:
			rowNum = 24
		elif day == 26:
			rowNum = 25
		elif day == 27:
			rowNum = 26
		elif day == 28:
			rowNum = 27
		elif day == 29:
			rowNum = 28
		elif day == 30:
			rowNum = 29
		elif day == 31:
			rowNum = 30

		# 31 rows = one row for each day of the month

		if rowNum == 0:
			y_Coordinate = 0*ystep
		if rowNum == 1:
			y_Coordinate = 1*ystep
		if rowNum == 2:
			y_Coordinate = 2*ystep
		if rowNum == 3:
			y_Coordinate = 3*ystep
		if rowNum == 4:
			y_Coordinate = 4*ystep
		if rowNum == 5:
			y_Coordinate = 5*ystep
		if rowNum == 6:
			y_Coordinate = 6*ystep

		if rowNum == 7:
			y_Coordinate = 7*ystep
		if rowNum == 8:
			y_Coordinate = 8*ystep
		if rowNum == 9:
			y_Coordinate = 9*ystep
		if rowNum == 10:
			y_Coordinate = 10*ystep
		if rowNum == 11:
			y_Coordinate = 11*ystep
		if rowNum == 12:
			y_Coordinate = 12*ystep
		if rowNum == 13:
			y_Coordinate = 13*ystep

		if rowNum == 14:
			y_Coordinate = 14*ystep
		if rowNum == 15:
			y_Coordinate = 15*ystep
		if rowNum == 16:
			y_Coordinate = 16*ystep
		if rowNum == 17:
			y_Coordinate = 17*ystep
		if rowNum == 18:
			y_Coordinate = 18*ystep
		if rowNum == 19:
			y_Coordinate = 19*ystep
		if rowNum == 20:
			y_Coordinate = 20*ystep

		if rowNum == 21:
			y_Coordinate = 21*ystep
		if rowNum == 22:
			y_Coordinate = 22*ystep
		if rowNum == 23:
			y_Coordinate = 23*ystep
		if rowNum == 24:
			y_Coordinate = 24*ystep
		if rowNum == 25:
			y_Coordinate = 25*ystep
		if rowNum == 26:
			y_Coordinate = 26*ystep
		if rowNum == 27:
			y_Coordinate = 27*ystep

		if rowNum == 28:
			y_Coordinate = 28*ystep
		if rowNum == 29:
			y_Coordinate = 29*ystep
		if rowNum == 30:
			y_Coordinate = 30*ystep
		
	#____________________________________________________________________________


		if time == 6 and loc == 1:
			x_Coordinate = 0*xstep
		if time == 12 and loc == 1:
			x_Coordinate = 1*xstep
		if time == 18 and loc == 1:
			x_Coordinate = 2*xstep
		if time == 24 and loc == 1:
			x_Coordinate = 3*xstep

		#__________location 2 STCLAIR______________

		if time == 6 and loc == 2:
			x_Coordinate = 4*xstep
		if time == 12 and loc == 2:
			x_Coordinate = 5*xstep
		if time == 18 and loc == 2:
			x_Coordinate = 6*xstep
		if time == 24 and loc == 2:
			x_Coordinate = 7*xstep

		#__________location 3 KINGWIL______________

		if time == 6 and loc == 3:
			x_Coordinate = 8*xstep
		if time == 12 and loc == 3:
			x_Coordinate = 9*xstep
		if time == 18 and loc == 3:
			x_Coordinate = 10*xstep
		if time == 24 and loc == 3:
			x_Coordinate = 11*xstep

		#__________location 4 BRADYSL______________

		if time == 6 and loc == 4:
			x_Coordinate = 12*xstep
		if time == 12 and loc == 4:
			x_Coordinate = 13*xstep
		if time == 18 and loc == 4:
			x_Coordinate = 14*xstep
		if time == 24 and loc == 4:
			x_Coordinate = 15*xstep

		#__________location 5 MEADUPS______________

		if time == 6 and loc == 5:
			x_Coordinate = 16*xstep
		if time == 12 and loc == 5:
			x_Coordinate = 17*xstep
		if time == 18 and loc == 5:
			x_Coordinate = 18*xstep
		if time == 24 and loc == 5:
			x_Coordinate = 19*xstep

		#__________location 6 MEADPOW______________

		if time == 6 and loc == 6:
			x_Coordinate = 20*xstep
		if time == 12 and loc == 6:
			x_Coordinate = 21*xstep
		if time == 18 and loc == 6:
			x_Coordinate = 22*xstep
		if time == 24 and loc == 6:
			x_Coordinate = 23*xstep

		#__________location 7 MEADDWN______________

		if time == 6 and loc == 7:
			x_Coordinate = 24*xstep
		if time == 12 and loc == 7:
			x_Coordinate = 25*xstep
		if time == 18 and loc == 7:
			x_Coordinate = 26*xstep
		if time == 24 and loc == 7:
			x_Coordinate = 27*xstep

		#__________location 8 MONA_________________

		if time == 6 and loc == 8:
			x_Coordinate = 28*xstep
		if time == 12 and loc == 8:
			x_Coordinate = 29*xstep
		if time == 18 and loc == 8:
			x_Coordinate = 30*xstep
		if time == 24 and loc == 8:
			x_Coordinate = 31*xstep

		#__________location 9 MONTAGU______________

		if time == 6 and loc == 9:
			x_Coordinate = 32*xstep
		if time == 12 and loc == 9:
			x_Coordinate = 33*xstep
		if time == 18 and loc == 9:
			x_Coordinate = 34*xstep
		if time == 24 and loc == 9:
			x_Coordinate = 35*xstep

		#__________location 10 HUNTNOR_____________

		if time == 6 and loc == 10:
			x_Coordinate = 36*xstep
		if time == 12 and loc == 10:
			x_Coordinate = 37*xstep
		if time == 18 and loc == 10:
			x_Coordinate = 38*xstep
		if time == 24 and loc == 10:
			x_Coordinate = 39*xstep

		#__________location 11 HUNTSOU_____________

		if time == 6 and loc == 11:
			x_Coordinate = 40*xstep
		if time == 12 and loc == 11:
			x_Coordinate = 41*xstep
		if time == 18 and loc == 11:
			x_Coordinate = 42*xstep
		if time == 24 and loc == 11:
			x_Coordinate = 43*xstep

		#__________location 12 TAROONA_____________

		if time == 6 and loc == 12:
			x_Coordinate = 44*xstep
		if time == 12 and loc == 12:
			x_Coordinate = 45*xstep
		if time == 18 and loc == 12:
			x_Coordinate = 46*xstep
		if time == 24 and loc == 12:
			x_Coordinate = 47*xstep

		colNum = rowNum


#_____________________________________________________________________________________________________________________________________________

	#__________________________________
	#	format 3 
	#__________________________________

	if format == 3:

		if   day == 1:
			rowNum = 0
		elif day == 2:
			rowNum = 1
		elif day == 3:
			rowNum = 2
		elif day == 4:
			rowNum = 3
		elif day == 5:
			rowNum = 4
		elif day == 6:
			rowNum = 5
		elif day == 7:
			rowNum = 6
		elif day == 8:
			rowNum = 7
		elif day == 9:
			rowNum = 8
		elif day == 10:
			rowNum = 9

		elif day == 11:
			rowNum = 10
		elif day == 12:
			rowNum = 11
		elif day == 13:
			rowNum = 12
		elif day == 14:
			rowNum = 13
		elif day == 15:
			rowNum = 14
		elif day == 16:
			rowNum = 15
		elif day == 17:
			rowNum = 16
		elif day == 18:
			rowNum = 17
		elif day == 19:
			rowNum = 18
		elif day == 20:
			rowNum = 19

		elif day == 21:
			rowNum = 20
		elif day == 22:
			rowNum = 21
		elif day == 23:
			rowNum = 22
		elif day == 24:
			rowNum = 23
		elif day == 25:
			rowNum = 24
		elif day == 26:
			rowNum = 25
		elif day == 27:
			rowNum = 26
		elif day == 28:
			rowNum = 27
		elif day == 29:
			rowNum = 28
		elif day == 30:
			rowNum = 29
		elif day == 31:
			rowNum = 30

		# 31 rows = one row for each day of the month

		if rowNum == 0:
			y_Coordinate = 0*ystep
		if rowNum == 1:
			y_Coordinate = 1*ystep
		if rowNum == 2:
			y_Coordinate = 2*ystep
		if rowNum == 3:
			y_Coordinate = 3*ystep
		if rowNum == 4:
			y_Coordinate = 4*ystep
		if rowNum == 5:
			y_Coordinate = 5*ystep
		if rowNum == 6:
			y_Coordinate = 6*ystep

		if rowNum == 7:
			y_Coordinate = 7*ystep
		if rowNum == 8:
			y_Coordinate = 8*ystep
		if rowNum == 9:
			y_Coordinate = 9*ystep
		if rowNum == 10:
			y_Coordinate = 10*ystep
		if rowNum == 11:
			y_Coordinate = 11*ystep
		if rowNum == 12:
			y_Coordinate = 12*ystep
		if rowNum == 13:
			y_Coordinate = 13*ystep

		if rowNum == 14:
			y_Coordinate = 14*ystep
		if rowNum == 15:
			y_Coordinate = 15*ystep
		if rowNum == 16:
			y_Coordinate = 16*ystep
		if rowNum == 17:
			y_Coordinate = 17*ystep
		if rowNum == 18:
			y_Coordinate = 18*ystep
		if rowNum == 19:
			y_Coordinate = 19*ystep
		if rowNum == 20:
			y_Coordinate = 20*ystep

		if rowNum == 21:
			y_Coordinate = 21*ystep
		if rowNum == 22:
			y_Coordinate = 22*ystep
		if rowNum == 23:
			y_Coordinate = 23*ystep
		if rowNum == 24:
			y_Coordinate = 24*ystep
		if rowNum == 25:
			y_Coordinate = 25*ystep
		if rowNum == 26:
			y_Coordinate = 26*ystep
		if rowNum == 27:
			y_Coordinate = 27*ystep

		if rowNum == 28:
			y_Coordinate = 28*ystep
		if rowNum == 29:
			y_Coordinate = 29*ystep
		if rowNum == 30:
			y_Coordinate = 30*ystep
		
	#____________________________________________________________________________



		if time == 6 and loc == 1:
			x_Coordinate = 0*xstep
		if time == 6 and loc == 2:
			x_Coordinate = 1*xstep
		if time == 6 and loc == 3:
			x_Coordinate = 2*xstep
		if time == 6 and loc == 4:
			x_Coordinate = 3*xstep
		if time == 6 and loc == 5:
			x_Coordinate = 4*xstep
		if time == 6 and loc == 6:
			x_Coordinate = 5*xstep
		if time == 6 and loc == 7:
			x_Coordinate = 6*xstep
		if time == 6 and loc == 8:
			x_Coordinate = 7*xstep
		if time == 6 and loc == 9:
			x_Coordinate = 8*xstep
		if time == 6 and loc == 10:
			x_Coordinate = 9*xstep
		if time == 6 and loc == 11:
			x_Coordinate = 10*xstep
		if time == 6 and loc == 12:
			x_Coordinate = 11*xstep

		#__________12noon______________
		if time == 12 and loc == 1:
			x_Coordinate = 12*xstep
		if time == 12 and loc == 2:
			x_Coordinate = 13*xstep
		if time == 12 and loc == 3:
			x_Coordinate = 14*xstep
		if time == 12 and loc == 4:
			x_Coordinate = 15*xstep
		if time == 12 and loc == 5:
			x_Coordinate = 16*xstep
		if time == 12 and loc == 6:
			x_Coordinate = 17*xstep
		if time == 12 and loc == 7:
			x_Coordinate = 18*xstep
		if time == 12 and loc == 8:
			x_Coordinate = 19*xstep
		if time == 12 and loc == 9:
			x_Coordinate = 20*xstep
		if time == 12 and loc == 10:
			x_Coordinate = 21*xstep
		if time == 12 and loc == 11:
			x_Coordinate = 22*xstep
		if time == 12 and loc == 12:
			x_Coordinate = 23*xstep
			
		#__________18pm______________
		if time == 18 and loc == 1:
			x_Coordinate = 24*xstep
		if time == 18 and loc == 2:
			x_Coordinate = 25*xstep
		if time == 18 and loc == 3:
			x_Coordinate = 26*xstep
		if time == 18 and loc == 4:
			x_Coordinate = 27*xstep
		if time == 18 and loc == 5:
			x_Coordinate = 28*xstep
		if time == 18 and loc == 6:
			x_Coordinate = 29*xstep
		if time == 18 and loc == 7:
			x_Coordinate = 30*xstep
		if time == 18 and loc == 8:
			x_Coordinate = 31*xstep
		if time == 18 and loc == 9:
			x_Coordinate = 32*xstep
		if time == 18 and loc == 10:
			x_Coordinate = 33*xstep
		if time == 18 and loc == 11:
			x_Coordinate = 34*xstep
		if time == 18 and loc == 12:
			x_Coordinate = 35*xstep
			
		#__________24midnight______________
		if time == 24 and loc == 1:
			x_Coordinate = 36*xstep
		if time == 24 and loc == 2:
			x_Coordinate = 37*xstep
		if time == 24 and loc == 3:
			x_Coordinate = 38*xstep
		if time == 24 and loc == 4:
			x_Coordinate = 39*xstep
		if time == 24 and loc == 5:
			x_Coordinate = 40*xstep
		if time == 24 and loc == 6:
			x_Coordinate = 41*xstep
		if time == 24 and loc == 7:
			x_Coordinate = 42*xstep
		if time == 24 and loc == 8:
			x_Coordinate = 43*xstep
		if time == 24 and loc == 9:
			x_Coordinate = 44*xstep
		if time == 24 and loc == 10:
			x_Coordinate = 45*xstep
		if time == 24 and loc == 11:
			x_Coordinate = 46*xstep
		if time == 24 and loc == 12:
			x_Coordinate = 47*xstep


		colNum = rowNum



	return  colNum, location, year, month, day, date, xstep, ystep, x_Coordinate, y_Coordinate



