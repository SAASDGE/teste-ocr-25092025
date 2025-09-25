# Teste de Desenvolvimento (Extração de informações)

Para garantir o eficiente gerenciamento dos créditos de energia provenientes de usinas de energia renovável, a extração precisa e automática de dados das notas fiscais de energia elétrica é fundamental. Para atender a essa necessidade, é proposto pela equipe de desenvolvimento que você crie uma rotina de extração de dados a partir de faturas de energia elétrica, que podem ser fornecidas em formatos variados, como PDFs e imagens.

Nesta atividade, você deve editar o arquivo read.py e desenvolver uma rotina que deve realizar a leitura de uma fatura no formato PDF e retornar um dataframe contendo as seguintes informações:

- O número da instalação
- Mês ao qual a fatura é referente
- Quantidade, preço e valor de Energia SCEE s/ ICMS.

Ao desenvolver a atividade deve ser realizada a leitura do arquivo, extração do texto e por fim análise dos dados. Para a extração de textos dos PDFs, é sugerido o uso da biblioteca pdfplumber. Além disso, para a extração de informações do texto é sugerido o uso de expressões regulares a partir da biblioteca Re, e com o objetivo de organizar e visualizar as informações é sugerido o uso da biblioteca pandas. 

As informações obtidas devem ser exibidas estruturadas de acordo com a seguinte tabela, além disso é possível observar o gabarito da atividade.

|    Campo    |    Valor    | 
|-------------|-------------|
| Instalação  |  4547896527 |
|     Mês     |   JUL/2023  |
| Quantidade  |     149     |
|    Preço    |  0,51190126 |
|    Valor    |    76,26    |

Para realizar os testes e conferir os valores você deve utilizar o arquivo fatura.pdf, disponibilizado no repositório.

# Bônus

As informações podem ser obtidas através de imagens de notas fiscais, logo é proposto como atividade bônus a extração de informações a partir de imagens. Para isso, é sugerido o uso da biblioteca de processamento de imagens Opencv, e para a extração do texto são sugeridas ferramentas de OCR como Tesseract OCR, EasyOCR entre outras. Assim como na atividade anterior, o código deve retornar as informações em um dataframe.

# Conclusão

Por fim, você terá 2 horas para desenvolver a atividade e a rotina será avaliada posteriormente.
