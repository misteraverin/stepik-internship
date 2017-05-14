import requests
import datetime

class stepik_api():
	"Simple wrapper for Stepik API"
	def __init__(self):
		self.BASE_URL = "https://stepik.org:443"

	def fetch_object(self, obj_class, obj_id):
		"""
		Get json description of obj_class
        :param obj_id: obj id
        :param obj_class: obj class
        :return: json txt
		"""
		api_url = '{}/api/{}s/{}'.format(self.BASE_URL, obj_class, obj_id)
		response = requests.get(api_url).json()
		return response

	def get_lesson_date(self, obj_id):
		"""
		Get lesson's update date
		:param obj_id: lesson id
        :return: string date 
		"""
		data = self.fetch_object("lesson", obj_id)
		return data['lessons'][0]['update_date']

	def convert_str_date(self, date):
		"""
		Convert string date to datetime.datetime
		"""
		return datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')

	def get_steps_id(self, obj_id):
		"""
		Get lesson's theoretical steps id
		:param obj_id: lesson id
        :return: dict with ids 
		"""
		try:
			lesson = self.fetch_object("lesson", obj_id)
			steps = []
			all_steps = lesson['lessons'][0]['steps']
			for cur_id in all_steps: 
				step = self.fetch_object("step", cur_id)
				#print(step['steps'][0]['block']['name'])
				if step['steps'][0]['block']['name'] == "text":
				 	steps.append(step['steps'][0]['id'])
		except Exception as ex:
			return ex
		return steps