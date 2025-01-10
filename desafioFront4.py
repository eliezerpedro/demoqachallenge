import logging
import time
from RPA.Browser.Selenium import Selenium

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

class DemoQAProgressBarAutomation:
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

    def navegar_para_progress_bar(self):
        try:
            self.browser.wait_until_element_is_enabled("xpath://h5[contains(text(), 'Widgets')]")
            self.browser.scroll_element_into_view("xpath://h5[contains(text(), 'Widgets')]")
            self.browser.click_element("xpath://h5[contains(text(), 'Widgets')]")
            self.browser.wait_until_element_is_enabled("xpath://span[contains(text(), 'Progress Bar')]")
            self.browser.scroll_element_into_view("xpath://span[contains(text(), 'Progress Bar')]")
            self.browser.click_element("xpath://span[contains(text(), 'Progress Bar')]")
            logger.info("Navegado para a página 'Progress Bar' com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao navegar para 'Progress Bar': {e}")
            raise

    def iniciar_e_pausar_barra(self):
        try:
            self.browser.click_button("id:startStopButton")
            progress_text = self.browser.find_element("id=progressBar").text
            if progress_text < "25%":
                self.browser.click_button("id:startStopButton")
                logger.info("Barra de progresso pausada antes de atingir 25%.")
                time.sleep(5)
        except Exception as e:
            logger.error(f"Erro ao iniciar ou pausar a barra de progresso: {e}")
            raise

    def aguardar_barra_concluir(self, poll_interval=1):
        try:
            self.browser.click_button("id:startStopButton")
            logger.info("Aguardando barra de progresso atingir 100%.")
            while True:
                progress_text = self.browser.find_element("id=progressBar").text
                if progress_text == "100%":
                    logger.info("A barra de progresso atingiu 100%. Resetando...")
                    self.browser.click_button("id:resetButton")
                    break
                time.sleep(poll_interval)
        except Exception as e:
            logger.error(f"Erro ao monitorar a barra de progresso: {e}")
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
        automacao = DemoQAProgressBarAutomation()
        automacao.navegar_para_progress_bar()

        # Iniciar e pausar a barra de progresso
        automacao.iniciar_e_pausar_barra()

        # Aguardar a barra atingir 100% e resetar
        automacao.aguardar_barra_concluir(poll_interval=2)

        # Finalizar automação
        automacao.finalizar()
        logger.info("Automação de 'Progress Bar' executada com sucesso!")
    except Exception as e:
        logger.error(f"Erro no processo de automação: {e}")

if __name__ == "__main__":
    main()
