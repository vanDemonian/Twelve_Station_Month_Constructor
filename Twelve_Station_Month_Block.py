#!/usr/bin/python
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL import ImageFont
from PIL import ImageDraw
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from TwelveStationMonthMaker import *


outputDir = 'Outputs'


def Twelve_Station_Month_Block(MONTH):

	'Creates a 12 station month print from a list of JPGs'

	backGround = (255,255,255)

	"""
	each image resized to 680 x 452

	(4 times of day) x (12 camera stations) x (31 days)		

	total x = 21 080 
	total y = 21 696

        
	"""

	imageWidth  = imW = 21080
	imageHeight = imH = 21696
	printSize   = (imW, imH)

	thumbSize   = (680, 452)


	quality = 100


	if os.path.isdir(outputDir) != 1:
            os.mkdir(outputDir)

	cellInfo = []
	monthName = os.path.basename(MONTH[0])
	
	location = monthName[0:7]
	thisMonth = monthName[8:15]
	
	print '\n the month is  ', thisMonth
	print ' '


	#create new Proof.tiff file
	Proofimg = Image.new('RGB', printSize, backGround)

	#fnt = ImageFont.truetype('TrueTypeFonts/arial.ttf', 30)

	#process all thumbs from day
	for name in MONTH:

	
		#resize
		print "final paste loop name ", name
		img = Image.open(name).resize(thumbSize)
		name = os.path.basename(name)
		#parse cellInfo
		nameInfo = TwelveStationMonthMaker(name) # call to cellNUmbers function that delivers info for each image in proof set 
		cellInfo.append(nameInfo) #list of cellInfo for each cell

   		Proofimg.paste(img,(nameInfo[8],nameInfo[9]))
   		#print "cellInfo = ", nameInfo[8][0],nameInfo[8][1]


   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.tif','tiff', quality=quality)#tiff
   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.jpg','jpeg', quality =100)#jpeg

   	#Proofimg.save(outputDir +'/'+ location + '_' + thisMonth +'_'+'.tif','tiff', quality = quality )#tiff
   	Proofimg.save(outputDir +'/'+ 'TwelveStations' + '_' + thisMonth +'_'+'.tif','tiff', quality = quality )#jpeg

	print 'cellInfo ', cellInfo




