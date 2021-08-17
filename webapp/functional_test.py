from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)  # 암묵적 대기

    def tearDown(self) -> None:  # 테스트에 에러가 발생해도 tearDown 이 실행된다.
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다.
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test')

        # 그녀는 바로 작업을 추가하기로 한다


if __name__ == '__main__':
    unittest.main(warnings='ignore')
