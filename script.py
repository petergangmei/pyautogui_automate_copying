
import pyautogui as py
import time
from utils import locate_image, locate_image_strong

word_location 			= py.locateCenterOnScreen("img/word.PNG", confidence=0.7)
english_word_location 	= py.locateCenterOnScreen("img/english_word.PNG", confidence=0.9)
check_word_location 	= py.locateCenterOnScreen("img/check_word.PNG", confidence=0.9)



print('starting the program...')
	
# time.sleep(1)
duration =0.3
short = 0.2
count = 0
while True:
	
	py.moveTo(word_location, duration=duration)
	py.moveRel(0,760, duration=duration)

	py.click(duration=short)
	py.click(duration=0.5)

	py.hotkey('ctrl', 'c')
	py.press('down')
	py.moveTo(english_word_location, duration=duration)
	py.click()
	py.hotkey('ctrl', 'v')
	py.sleep(0.2)

	if locate_image_strong("check_word.PNG"):
		py.moveTo(check_word_location, duration=duration)
		py.click()
	else:
		print('exited loop due to word not copied')
		break;

	time.sleep(1.6);
	if locate_image("open_code.PNG"):
		py.moveTo(locate_image("open_code.PNG"), duration=duration)
		py.click()
		time.sleep(1)
		py.click(clicks=3, interval=0.1)
		py.hotkey('ctrl', 'c')

		py.moveTo(locate_image("close_tap.PNG"), duration=duration)
		py.moveRel(-15,-5, duration=short)
		py.click()
		py.moveTo(locate_image("meanings.PNG"), duration=duration)
		py.click()
		py.hotkey('ctrl', 'v')
		py.moveTo(locate_image("submit_word.PNG"), duration=duration)
		py.click()
		count+=1
		print("count: ", count)

	else:
		py.moveTo(locate_image("find_word.PNG"), duration=duration)
		py.click()