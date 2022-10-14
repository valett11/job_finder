import browser_cookie3
import requests
import json
from bs4 import BeautifulSoup


def main():
    """
    Будем дергать кукисы из нашего браузера, но первым делом нужно
    авторизваться на нашем сайте в браузере GoogleChrome
    Подробнее https://github.com/borisbabic/browser_cookie3
    """
    # Инициализируем наши кукисы
    cf = browser_cookie3.chrome()

    # Подготавливаем наши заголовки
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    headers = {'user-agent': useragent, 'x-requested-with': 'XMLHttpRequest'}
    url = "https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&" \
          "text=Devops&salary=&currency_code=RUR&experience=doesNotMatter&" \
          "schedule=remote&label=not_from_agency&order_by=publication_time&" \
          "search_period=7&items_on_page=100"

    # Выполняем наш запрос
    r = requests.get(url=url,
                     cookies=cf,
                     allow_redirects=True,
                     headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # Парсим с html странички интересный фрагмент  под тегом <template...
    script_text = soup.find('template').get_text().encode('utf-8')
    # Загоняю в json
    data = json.loads(script_text)  # a dictionary!
    # Дергаю нужный мне объект с вкансиями
    data = data['vacancySearchResult']['vacancies']
    # Вывожу результат
    print(json.dumps(data, ensure_ascii=False, indent=4))
    # Todo п1 п2 выполнены, нужно переходить к пунку 3 (Нужно отобрать интересные вакансии и прожать их как отлик)

if __name__ == '__main__':
    main()

