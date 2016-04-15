#coding=utf-8

from selenium import webdriver
import unittest

class test_selenium(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(3)

	def tearDown(self):
		self.driver.quit()


	def test_app(self):

		self.driver.get('localhost:8000')

		self.assertIn('To-D',self.driver.title)

		# self.fail('finish the test')

if __name__=='__main__':
	unittest.main()