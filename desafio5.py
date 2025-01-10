import time
import logging
from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

class DemoQAInteractionsAutomation:
    def __init__(self):
        self.browser = Selenium()
        self.base_url = "https://demoqa.com/"
        try:
            self.browser.open_available_browser(self.base_url)
            self.browser.maximize_browser_window()
            logger.info("Navegador aberto e maximizado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao abrir o navegador: {e}")
            raise

    def navegar_para_sortable(self):
        try:
            self.browser.wait_until_element_is_enabled("xpath://h5[contains(text(), 'Interactions')]")
            self.browser.scroll_element_into_view("xpath://h5[contains(text(), 'Interactions')]")
            self.browser.click_element("xpath://h5[contains(text(), 'Interactions')]")
            self.browser.wait_until_element_is_enabled("xpath://span[contains(text(), 'Sortable')]")
            self.browser.scroll_element_into_view("xpath://span[contains(text(), 'Sortable')]")
            self.browser.click_element("xpath://span[contains(text(), 'Sortable')]")
            logger.info("Navegado para a página 'Sortable' com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao navegar para 'Sortable': {e}")
            raise

    @staticmethod
    def sort_strings_numerically(strings):
        number_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
        }
        return sorted(strings, key=lambda x: number_map[x])

    @staticmethod
    def is_sorted(elements):
        texts = [el.text for el in elements]
        sorted_texts = DemoQAInteractionsAutomation.sort_strings_numerically(texts)
        return texts == sorted_texts

    def reorganizar_elementos(self):
        try:
            action_chains = ActionChains(self.browser.driver)
            while True:
                elements = self.browser.find_elements("xpath://div[@id='demo-tabpane-list']//div//div")
                if self.is_sorted(elements):
                    logger.info("Os elementos já estão ordenados.")
                    break
                
                logger.info("Os elementos não estão ordenados. Reorganizando...")
                texts = [element.text for element in elements]
                sorted_texts = self.sort_strings_numerically(texts)
                sorted_elements = [next(el for el in elements if el.text == text) for text in sorted_texts]

                for i in range(len(sorted_elements)):
                    source = elements[i]
                    target = sorted_elements[i]
                    if source != target:
                        action_chains.drag_and_drop(source, target).perform()
                        time.sleep(0.5)
                        elements = self.browser.find_elements("xpath://div[@id='demo-tabpane-list']//div//div")
                        logger.info(f"Após mover {source.text} para {target.text}, os elementos são: {[el.text for el in elements]}")
                        if self.is_sorted(elements):
                            logger.info("Os elementos foram ordenados com sucesso.")
                            return
                time.sleep(1)
        except Exception as e:
            logger.error(f"Erro ao reorganizar os elementos: {e}")
            raise

    def finalizar(self):
        try:
            self.browser.close_all_browsers()
            logger.info("Todos os navegadores fechados com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao fechar os navegadores: {e}")
            raise

def main():
    try:
        automacao = DemoQAInteractionsAutomation()
        automacao.navegar_para_sortable()
        automacao.reorganizar_elementos()
        automacao.finalizar()
        logger.info("Automação de 'Sortable' executada com sucesso!")
    except Exception as e:
        logger.error(f"Erro no processo de automação: {e}")

if __name__ == "__main__":
    main()
