import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("I am disgusted")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        result = emotion_detector("I am afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_joy(self):
        result = emotion_detector("I am glad")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
