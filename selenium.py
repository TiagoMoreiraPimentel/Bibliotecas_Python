from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Edge()  # abre o navegador edge.

navegador.maximize_window()  # Maximiza o navegador.

navegador.get("https://www.youtube.com/")  # acessa o link pelo navegador.

sleep(1)  # aguarda determinado tempo antes de seguir o proximo comando.

pesquisa = navegador.find_element(By.XPATH, '//*[@id="search-input"]')  # seleciona o xpath do elemento barra de pesquisa.

pesquisa.find_element(By.ID, 'search').send_keys('tiago moreira pimentel')  # seleciona o id da barra de pesquisa.

clique = navegador.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')  # seleciona o xpath da lupa de pesquisa.

clique.click()  # clica no botão de pesquisa.