import unittest

from stepik_api import stepik_api


class TestStepikApi(unittest.TestCase):
    def setUp(self):
        self.stepik = stepik_api()

    def test_get_lesson_date(self):
        lesson_dates = {"1": "2017-01-16T17:58:55Z", "300": "2016-09-13T03:47:58Z"}
        for lesson in lesson_dates.keys():
            requested_date = self.stepik.get_lesson_date(lesson)
            self.assertEqual(requested_date, lesson_dates[lesson])

    def test_fetch_object(self):
        lesson = self.stepik.fetch_object("lesson", 300)
        self.assertEqual(lesson['lessons'][0]['id'], 300)

    def test_get_steps_id(self):
        right_text_steps = [580, 578, 576, 448]
        requested_steps = self.stepik.get_steps_id(15)
        self.assertEqual(right_text_steps, requested_steps)


if __name__ == '__main__':
    unittest.main()
