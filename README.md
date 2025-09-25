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

|    Campo    |    Valor    | 
|-------------|-------------|
|     ...     |     ...     |

Para analisar a fatura e realizar a extração das informações você deve utilizar o arquivo fatura.jpg, disponibilizado no repositório.

# Documentação do Teste

- Escreva a documentação do teste abaixo.

# Requisitos dos Desafios

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original. Caso não consiga, os arquivos podem ser enviados para o email falecom@dg.energy, porém com penalidade de pontos.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
