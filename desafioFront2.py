import logging
from RPA.Browser.Selenium import Selenium
import time

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class DemoQAAlertFrameWindowAutomation:
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

    def navegar_para_browser_windows(self):
        try:
            self.browser.wait_until_element_is_enabled("xpath://h5[contains(text(), 'Alerts, Frame & Windows')]")
            self.browser.scroll_element_into_view("xpath://h5[contains(text(), 'Alerts, Frame & Windows')]")
            self.browser.click_element("xpath://h5[contains(text(), 'Alerts, Frame & Windows')]")
            self.browser.wait_until_element_is_enabled("xpath://span[contains(text(), 'Browser Windows')]")
            self.browser.scroll_element_into_view("xpath://span[contains(text(), 'Browser Windows')]")
            self.browser.click_element("xpath://span[contains(text(), 'Browser Windows')]")
            logger.info("Navegado para a página 'Browser Windows' com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao navegar para 'Browser Windows': {e}")
            raise

    def abrir_mais_janelas(self):
        try:
            self.browser.execute_javascript("window.scrollTo(0, document.body.scrollHeight);")
            self.browser.click_element("id:windowButton")
            logger.info("Nova janela aberta com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao abrir nova janela: {e}")
            raise

    def verificar_efeitos_janela(self):
        try:
            self.browser.switch_window(locator="NEW")
            if self.browser.find_element("xpath://h1[contains(text(), 'This is a sample page')]"):
                self.browser.close_window()
            logger.info("Efeito de mudança de janela verificado e janela fechada com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao verificar o efeito da janela: {e}")
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
        automacao = DemoQAAlertFrameWindowAutomation()
        automacao.navegar_para_browser_windows()
        automacao.abrir_mais_janelas()
        automacao.verificar_efeitos_janela()
        automacao.finalizar()
        logger.info("Automação de 'Alerts, Frame & Windows' executada com sucesso!")
    except Exception as e:
        logger.error(f"Erro no processo de automação: {e}")

if __name__ == "__main__":
    main()
