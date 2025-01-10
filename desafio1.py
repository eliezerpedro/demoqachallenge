import logging
from RPA.Browser.Selenium import Selenium
import random
import datetime
import time
import os

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class DemoQAFormAutomation:
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

    def gerar_dados_pessoais(self):
        try:
            primeiro_nome = f"Nome{random.randint(1, 1000)}"
            sobrenome = f"Sobrenome{random.randint(1, 1000)}"
            email = f"{primeiro_nome.lower()}.{sobrenome.lower()}@email{random.randint(1, 100)}.com"
            genero = random.choice(["Male", "Female", "Other"])
            celular = f"9{random.randint(100000000, 999999999)}"
            data_nascimento = datetime.date(
                random.randint(1990, 2010),
                random.randint(1, 12),
                random.randint(1, 28)
            ).strftime("%d %b %Y")
            hobbies = random.choice(["Sports", "Reading", "Music"])
            endereco = f"Rua Aleatória {random.randint(1, 1000)}, Bairro {random.randint(1, 100)}"
            estado = f"Estado{random.randint(1, 5)}"
            cidade = f"Cidade{random.randint(1, 20)}"

            logger.info("Dados pessoais gerados com sucesso.")
            return {
                "primeiro_nome": primeiro_nome,
                "sobrenome": sobrenome,
                "email": email,
                "genero": genero,
                "celular": celular,
                "data_nascimento": data_nascimento,
                "hobbies": hobbies,
                "endereco": endereco,
                "estado": estado,
                "cidade": cidade
            }
        except Exception as e:
            logger.error(f"Erro ao gerar dados pessoais: {e}")
            raise

    def preencher_formulario(self, dados):
        try:
            self.navegar_para_formulario()
            self.browser.input_text("xpath://input[@id='firstName']", dados["primeiro_nome"])
            self.browser.input_text("xpath://input[@id='lastName']", dados["sobrenome"])
            self.browser.input_text("xpath://input[@id='userEmail']", dados["email"])
            self.browser.click_element(f"xpath://label[contains(text(), '{dados['genero']}')]")
            self.browser.input_text("xpath://input[@id='userNumber']", dados["celular"])
            self.browser.input_text("xpath://input[@id='dateOfBirthInput']", dados["data_nascimento"])
            self.selecionar_areas_interesse(dados["hobbies"])
            self.carregar_arquivo()
            self.preencher_endereco(dados)
            logger.info("Formulário preenchido com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao preencher o formulário: {e}")
            self.browser.close_all_browsers()
            raise

    def navegar_para_formulario(self):
        try:
            self.browser.wait_until_element_is_enabled("xpath://h5[contains(text(), 'Forms')]")
            self.browser.scroll_element_into_view("xpath://h5[contains(text(), 'Forms')]")
            self.browser.click_element("xpath://h5[contains(text(), 'Forms')]")
            self.browser.wait_until_element_is_enabled("xpath://span[contains(text(), 'Practice Form')]")
            self.browser.scroll_element_into_view("xpath://span[contains(text(), 'Practice Form')]")
            self.browser.click_element("xpath://span[contains(text(), 'Practice Form')]")
            logger.info("Navegado para o formulário com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao navegar até o formulário: {e}")
            raise

    def selecionar_areas_interesse(self, hobbies):
        try:
            self.browser.click_element("id:subjectsContainer")
            campo_input = self.browser.find_element("css:div.subjects-auto-complete__control input")
            self.browser.input_text_when_element_is_visible(campo_input, "Math")
            time.sleep(1)
            self.browser.press_keys(campo_input, "ENTER")
            self.browser.click_element(f"xpath://label[contains(text(), '{hobbies}')]")
            logger.info("Áreas de interesse selecionadas com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao selecionar áreas de interesse: {e}")
            raise

    def carregar_arquivo(self):
        try:
            caminho_arquivo = os.path.join(os.getcwd(), "teste.txt")
            self.browser.input_text("id:uploadPicture", caminho_arquivo)
            self.browser.wait_until_element_is_visible("id:uploadPicture", timeout=5)
            logger.info("Arquivo carregado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao carregar o arquivo: {e}")
            raise

    def preencher_endereco(self, dados):
        try:
            self.browser.click_element("id:currentAddress")
            self.browser.input_text("xpath://textarea[@id='currentAddress']", dados["endereco"])
            self.selecionar_localizacao(dados)
            logger.info("Endereço preenchido com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao preencher o endereço: {e}")
            raise

    def selecionar_localizacao(self, dados):
        try:
            self.browser.scroll_element_into_view("id:state")
            self.browser.click_element("id:state")
            self.browser.click_element("xpath://div[contains(text(), 'NCR')]")
            self.browser.click_element("id:city")
            self.browser.click_element("xpath://div[contains(text(), 'Delhi')]")
            logger.info("Localização selecionada com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao selecionar localização: {e}")
            raise

    def enviar_formulario(self):
        try:
            self.browser.click_button("xpath://button[@id='submit']")
            self.browser.wait_until_element_is_visible("xpath://button[@id='closeLargeModal']")
            self.browser.click_button("xpath://button[@id='closeLargeModal']")
            self.browser.close_all_browsers()
            logger.info("Formulário enviado e processo finalizado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao enviar o formulário: {e}")
            self.browser.close_all_browsers()
            raise

def main():
    try:
        automacao = DemoQAFormAutomation()
        dados = automacao.gerar_dados_pessoais()
        automacao.preencher_formulario(dados)
        automacao.enviar_formulario()
        logger.info("Dados preenchidos com sucesso!")
    except Exception as e:
        logger.error(f"Erro no processo de automação: {e}")

if __name__ == "__main__":
    main()
