import argparse
from google.cloud import videointelligence
import io

def analyse_video(path):
	video_client=videointelligence.VideoIntelligenceServiceClient()
	features = [videointelligence.enums.Feature.LABEL_DETECTION]
	with io.open(path, 'rb') as video:
		input_data=video.read()

	try:
		operation=video_client.annotate_video(features=features, input_content=input_data)
		result=operation.result(timeout=90)
	except Exception as e:
		print("Error with video processing: "+e)
		exit()

	print("Analysis is Complete..")

	# Process video/segment level label annotations
	segment_labels = result.annotation_results[0].segment_label_annotations
	for i, segment_label in enumerate(segment_labels):
		print('Video label description: {}'.format(segment_label.entity.description))
		for category_entity in segment_label.category_entities:
			print ("Label category description: "+category_entity.description)	
		for i, segment in enumerate(segment_label.segments):
			confidence = segment.confidence
			print ("The accuracy of the identification in this case is " +str(confidence) + "\n")
