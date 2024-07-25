from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        response_1 = emotion_detector('I am glad this happened')
        result_1 = json.loads(response_1)
        dominant_emotion_1 = max(result_1["emotionPredictions"][0]["emotion"], key=result_1["emotionPredictions"][0]["emotion"].get)
        self.assertEqual(dominant_emotion_1, 'joy')
        
        response_2 = emotion_detector('I am really mad about this')
        result_2 = json.loads(response_2)
        dominant_emotion_2 = max(result_2["emotionPredictions"][0]["emotion"], key=result_2["emotionPredictions"][0]["emotion"].get)
        self.assertEqual(dominant_emotion_2, 'anger')
        
        response_3 = emotion_detector('I feel disgusted just hearing about this')
        result_3 = json.loads(response_3)
        dominant_emotion_3 = max(result_3["emotionPredictions"][0]["emotion"], key=result_3["emotionPredictions"][0]["emotion"].get)
        self.assertEqual(dominant_emotion_3, 'disgust')
        
        response_4 = emotion_detector('I am so sad about this')
        result_4 = json.loads(response_4)
        dominant_emotion_4 = max(result_4["emotionPredictions"][0]["emotion"], key=result_4["emotionPredictions"][0]["emotion"].get)
        self.assertEqual(dominant_emotion_4, 'sadness')
        
        response_5 = emotion_detector('I am really afraid that this will happen')
        result_5 = json.loads(response_5)
        dominant_emotion_5 = max(result_5["emotionPredictions"][0]["emotion"], key=result_5["emotionPredictions"][0]["emotion"].get)
        self.assertEqual(dominant_emotion_5, 'fear')

if __name__ == '__main__':
    unittest.main()
