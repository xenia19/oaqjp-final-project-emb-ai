from EmotionDetection.emotion_detection import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')
        
        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I am really mad about this')
        self.assertEqual(result_2['label'], 'anger')
        
        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'disgust')

        result_4 = sentiment_analyzer('I am so sad about this')
        self.assertEqual(result_4['label'], 'sadness')

        result_5 = sentiment_analyzer('I am really afraid that this will happen')
        self.assertEqual(result_5['label'], 'fear')

if __name__ == '__main__':
    unittest.main()