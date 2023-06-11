import pytest
from selene import browser
from selene.support.conditions import be, have

@pytest.fixture(scope="module")
def window_sise():
    browser.config.window_width = 1720
    browser.config.window_height = 1280


def test_positive(window_sise):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print('Все проходит успешно')


def test_negative(window_sise):
    browser.open('https://google.com')
    random_string = 'ОТАЛИДЛУРДАДШСТШУРИДСЫДЩЩЫЩ'
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'По запросу {random_string} ничего не найдено.'))
    print('Этого не существует поэтому и не нашли:)')