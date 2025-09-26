# Teste de Desenvolvimento (Extração de informações)

Para garantir o eficiente gerenciamento dos créditos de energia provenientes de usinas de energia renovável, a extração precisa e automática de dados das notas fiscais de energia elétrica é fundamental. Para atender a essa necessidade, é proposto pela equipe de desenvolvimento que você crie uma rotina de extração de dados a partir de faturas de energia elétrica, que podem ser fornecidas em formatos variados, como imagens.

Nesta atividade, você deve editar o arquivo read.py e desenvolver uma rotina que deve realizar a leitura de uma fatura no formato de imagem e retornar um dataframe contendo as seguintes informações:

- O número da instalação da unidade consumidora.
- Mês/Ano ao qual a fatura é referente.
- Quantidade de energia elétrica consumida.
- Quantidade de energia elétrica compensada.
- Valor a pagar a distribuidora.
- Saldo de crédito de energia acumulado.

Ao desenvolver a atividade deve ser realizada a leitura do arquivo, extração do texto e por fim análise dos dados. Para isso, é sugerido o uso da biblioteca de processamento de imagens Opencv, e para a extração do texto são sugeridas ferramentas de OCR como Tesseract OCR, EasyOCR entre outras. Com o objetivo de organizar e visualizar as informações é sugerido o uso da biblioteca pandas.

As informações obtidas devem ser exibidas e estruturadas de acordo com a seguinte tabela. Essa atividade não possui gabarito, parte da atividade é analisar a fatura e extrair as informações.

| Campo | Valor |
| ----- | ----- |
| ...   | ...   |

Para analisar a fatura e realizar a extração das informações você deve utilizar o arquivo fatura.jpg, disponibilizado no repositório.

---

# Documentação do Teste

O código (script) desenvolvido para o teste de extração de dados em imagem de fatura de energia segue estrutura modular, separada por funções, e pode ser dividida nas seguintes etapas:

1. **Leitura e Extração de Texto:** Inicialmente, a função `extrair_texto` utiliza a biblioteca **OpenCV** para carregar a imagem e convertê-la para escala de cinza, um pré-processamento que otimiza o reconhecimento de texto. Em seguida, a biblioteca **EasyOCR** analisa a imagem e extrai seu conteúdo, convertendo os dados visuais em uma única string de texto bruto.
2. **Análise com Expressões Regulares:** Com o texto em mãos, a função `extrair_dados` aplica um conjunto de **expressões regulares**. Cada padrão foi cuidadosamente desenvolvido após uma análise manual do texto extraído para identificar e capturar de forma precisa cada um dos seis campos de dados solicitados.
3. **Apresentação Estruturada:** Por fim, a função principal do script utiliza a biblioteca **Pandas** para organizar as informações coletadas em um DataFrame, garantindo uma exibição final clara e estruturada no terminal.

### Como Executar o Projeto

Para executar esta solução e extrair os dados da fatura, siga os passos abaixo no seu terminal:

#### 1. Clone o repositório
   ```
   git clone <URL_DO_SEU_FORK>
   cd <NOME_DO_REPOSITORIO>
   ```

#### 2. Crie o ambiente virtual

```
python -m venv venv
```

#### 3. Ative o ambiente

###### (Windows)

```
.\venv\Scripts\activate
```

###### OU (macOS/Linux)

```
source venv/bin/activate
```

#### 4. Instale as dependências do projeto através do requirements

```
pip install -r requirements.txt
```

#### 5. Execute o projeto

```
python read.py
```

---

# Requisitos dos Desafios

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
