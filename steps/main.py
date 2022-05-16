from behave import given, when, then, step
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


@step(u'I acces to wallapop site')
def step_impl(context):
    driver = context.driver = webdriver.Chrome(ChromeDriverManager().install())
    URL ='https://es.wallapop.com/app/search?latitude=39.46895&longitude=-0.37686&keywords=game%20boy&filters_source=quick_filters&order_by=newest'
    driver.get(URL)


@step(u'I close the window')
def step_impl(context):
    driver = context.driver
    try:
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button')))
        accept_terms_button = driver.find_element_by_id('didomi-notice-agree-button')
        accept_terms_button.send_keys(Keys.RETURN)
        time.sleep(1)
        accept_terms_button = driver.find_elements_by_id('didomi-notice-agree-button')
        for count in range(5):
            if len(accept_terms_button) == 0:
                break
            else:
                time.sleep(3)
                count += count
    except TimeoutException:
        pass


@step(u'I read all information about screen items')
def step_impl(context):
    driver = context.driver
    context.cards = cards = driver.find_elements_by_xpath('//*[@class="ItemCardList__item"]')
    new_cards = []
    a,b = 'ºª!|"@·#$€%&/()=?´¿‚`^[+*±´¨«}{_<>].-', '                                     '
    g,h = "',", "  "
    c,d = ' ', '-'
    trans = str.maketrans(a,b)
    trans_space = str.maketrans(c,d)
    trans_symbols = str.maketrans(g,h)

    for e in range(len(cards)):
        try:
            precio = float(str(cards[e].find_element_by_xpath('./descendant::span[@class="ItemCard__price ItemCard__price--bold"]').text).split('€')[0])
            titulo_str = str(cards[e].find_element_by_xpath('./descendant::p[@class="ItemCard__title my-2 ItemCard__title--with-description"]').text).lower()
            titulo = unicodedata.normalize("NFKD", titulo_str).encode("ascii","ignore").decode("ascii")
            card_id = str(cards[e].find_element_by_xpath('./descendant::img').get_attribute('src')).split('.jpg')[0].split('/')[-2].split('p')[1]
            link_str = str(cards[e].find_element_by_xpath('./descendant::img').get_attribute('alt')).lower()
            link_str2 = unicodedata.normalize("NFKD", link_str).encode("ascii","ignore").decode("ascii")
            link_str3 = link_str2.translate(trans)
            link_str4 = link_str3.translate(trans_symbols)
            link_str5 = re.sub(r"(\S) {2,}", r"\1 ", link_str4)
            link_str6 = link_str5.translate(trans_space)
            imagen = str(cards[e].find_element_by_xpath('./descendant::img').get_attribute('src'))
            if str(link_str6)[-1:] == '-':
                link_str6 = link_str6[:-1]
            link = 'https://es.wallapop.com/item/' + link_str6 + '-' + card_id
            try:
                ele_reservado = cards[e].find_elements_by_xpath('./descendant::tsl-svg-icon[@src="/assets/icons/item-card/reserved.svg"]')
                if len(ele_reservado) == 0:
                    print('{:8.2f} \t {} \t {}     {} {}'.format(precio, card_id, titulo, link, imagen))
                    new_cards.append({'item_id':card_id,'titulo': titulo, 'precio': precio, 'enlace': link, 'imagen': imagen })
            except NoSuchElementException:
                pass
        except Exception:
            pass
    context.new_cards = new_cards


@step(u'I save the information in file')
def step_impl(context):
    driver = context.driver
    #file = open('files/items.txt', 'w')
   # for _ in range(len(context.cards)):


@step(u'I close the browser')
def step_impl(context):
    driver = context.driver
    driver.quit()