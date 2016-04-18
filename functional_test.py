#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class test_selenium(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(3)
	def test_app(self):

		self.driver.get('localhost:8000')

		self.assertIn('To-D',self.driver.title)
		# 标题与头部包含To_D
		# head_text=self.driver.find_element_by_tag_name('td').text
		# self.assertIn('To_D',head_text)
		# 输入待办事件
		# inputbox=self.driver.find_elements_by_id('id_new_items')
		# self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a To_D item')
		# inputbox.send_keys('buy peacock features')
		# inputbox.send_keys(Keys.ENTER)
        #
        #
		# table=self.driver.find_element_by_id('id_list_table')
		# rows=self.driver.find_elements_by_tag_name('tr')
		# self.assertTrue(any(row.text=='1:Buy peacock feathers' for row in rows))





	def tearDown(self):
		self.driver.quit()	

if __name__=='__main__':
	unittest.main()