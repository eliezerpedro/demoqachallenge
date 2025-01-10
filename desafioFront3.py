import logging
import random
import time
from RPA.Browser.Selenium import Selenium

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class DemoQAWebTablesAutomation:
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

    def navegar_para_web_tables(self):
        try:
            self.browser.wait_until_element_is_enabled("xpath://h5[contains(text(), 'Elements')]")
            self.browser.scroll_element_into_view("xpath://h5[contains(text(), 'Elements')]")
            self.browser.click_element("xpath://h5[contains(text(), 'Elements')]")
            self.browser.wait_until_element_is_enabled("xpath://span[contains(text(), 'Web Tables')]")
            self.browser.scroll_element_into_view("xpath://span[contains(text(), 'Web Tables')]")
            self.browser.click_element("xpath://span[contains(text(), 'Web Tables')]")
            logger.info("Navegado para a página 'Web Tables' com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao navegar para 'Web Tables': {e}")
            raise

    def preencher_formulario(self):
        try:
            primeiro_nome = f"Nome{random.randint(1, 1000)}"
            sobrenome = f"Sobrenome{random.randint(1, 1000)}"
            email = f"{primeiro_nome.lower()}.{sobrenome.lower()}@email{random.randint(1, 100)}.com"
            idade = random.randint(18, 65)
            salario = random.randint(30000, 150000)
            departamentos = ['Finance', 'Engineering', 'Marketing', 'HR', 'Operations']
            departamento = random.choice(departamentos)

            self.browser.input_text("id:firstName", primeiro_nome)
            self.browser.input_text("id:lastName", sobrenome)
            self.browser.input_text("id:userEmail", email)
            self.browser.input_text("id:age", idade)
            self.browser.input_text("id:salary", salario)
            self.browser.input_text("id:department", departamento)
            self.browser.click_button("id:submit")
            logger.info(f"Formulário preenchido com sucesso: {primeiro_nome} {sobrenome}.")
            return primeiro_nome
        except Exception as e:
            logger.error(f"Erro ao preencher o formulário: {e}")
            raise

    def criar_novo_registro(self):
        try:
            self.browser.click_button("id:addNewRecordButton")
            return self.preencher_formulario()
        except Exception as e:
            logger.error(f"Erro ao criar novo registro: {e}")
            raise

    def editar_registro(self, primeiro_nome):
        try:
            self.browser.input_text("id:searchBox", primeiro_nome)
            time.sleep(1)
            self.browser.click_element(f"xpath://div[contains(text(), '{primeiro_nome}')]//..//span[@title='Edit']")
            novo_nome = self.preencher_formulario()
            logger.info(f"Registro editado com sucesso: {primeiro_nome} -> {novo_nome}.")
            return novo_nome
        except Exception as e:
            logger.error(f"Erro ao editar o registro {primeiro_nome}: {e}")
            raise

    def deletar_registro(self, primeiro_nome):
        try:
            self.browser.input_text("id:searchBox", primeiro_nome)
            time.sleep(1)
            self.browser.click_element(f"xpath://div[contains(text(), '{primeiro_nome}')]//..//span[@title='Delete']")
            logger.info(f"Registro deletado com sucesso: {primeiro_nome}.")
        except Exception as e:
            logger.error(f"Erro ao deletar o registro {primeiro_nome}: {e}")
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
        automacao = DemoQAWebTablesAutomation()
        automacao.navegar_para_web_tables()

        # Criar novo registro
        nome = automacao.criar_novo_registro()

        # Editar o registro criado
        nome_editado = automacao.editar_registro(nome)

        # Deletar o registro editado
        automacao.deletar_registro(nome_editado)

        # Finalizar a automação
        automacao.finalizar()
        logger.info("Automação de 'Web Tables' executada com sucesso!")
    except Exception as e:
        logger.error(f"Erro no processo de automação: {e}")

if __name__ == "__main__":
    main()
