import argparse
from google.cloud import videointelligence
import io
import sys
from Database import MyDatabase

def analyse_video(path, ID, handle):
	db = MyDatabase()

	video_client = videointelligence.VideoIntelligenceServiceClient()
	features = [videointelligence.enums.Feature.LABEL_DETECTION]
	
	#input the video to API
	with io.open(path, 'rb') as video:
		input_data = video.read()
	#Generation of API result
	try:
		operation = video_client.annotate_video(features=features, input_content=input_data)
		result = operation.result(timeout=90)	
	except Exception as error:
		print("Error with video processing: " + error)
		exit()
	print("Analysis is Complete..")
	
	#label annotations display
	segment_labels = result.annotation_results[0].segment_label_annotations
	for i, segment_label in enumerate(segment_labels):
		print('Video label description: {}'.format(segment_label.entity.description))
		db.add_label(ID, handle, segment_label.entity,description)
		for category_entity in segment_label.category_entities:
			print ("Label category description: " + category_entity.description)	
	db.close_connection()

if __name__ == '__main__':
	print("Not running from Main program..")
	analyse_video(input("Enter file path: "))
