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

###  Instalação das dependências e execução do programa

Para rodar o script, abra um terminal na pasta do projeto e instale as dependências  

```
pip install -r requirements.txt
```
<br>

Uma vez feita a instalação, basta rodar o arquivo read.py

linux
```
python3 read.py
```
<br>

windows
```
py read.py
```

### Explicação do código

O código é constituído de 4 funções: 

- <b>crop_img</b>: Utiliza a biblioteca ***OpenCV*** do python para recortar a imagem. Foi desenvolvida para reduzir a fatura em regiões que contém os valores-alvo e reduzir a quantidade de caracteres desnecessários no arquivo final de texto, facilitando o filtro por regex. Para visualização das imagens recortadas, altere o parâmetro 'save'.
- <b>transcript_img</b>: Utiliza ***pytesseract*** para realizar a tarnscrição do texto de uma imagem definida como parâmetro da função.
- <b>bill_summary</b>: Realiza o pré-processamento da fatura, cortando a imagem em regiões de interesse e transcrevendo o conteúdo para um arquivo de texto.
- <b>pipeline</b>: É a função responsável por rodar o bill_sumary e montar o dataframe do ***Pandas*** com a estrutura desejada.

<br>

Em contraste à atividade anterior, dessa vez o código foi escrito de forma mais segmentada e comentada para melhorar a experiência de leitura de terceiros. 

A abordagem de cortar as imagens foi escolhida para reduzir o tamanho do texto onde será realizada a busca com regex. Entretanto, essa abordagem parte do princípio que a fatura seguirá sempre na mesma estrutura. O código foi pensado única e exclusivamente para a fatura fornecida no teste.

Apesar disso, o código ainda pode ser reutilizado para outras estruturas de fatura, bastando apenas que as zonas de interesse sejam redefinidas e o regex utilizado seja revisado e adaptado.

Também foi implementado um requirements.txt como sugerido na entrevista técnica.

Eu optei por usar apenas a função re.findall() para realizar as buscas por regex. Dessa forma, se o regex falhar não haverá quebra de código, ao invés disso a função retornará uma lista vazia.

Sobre as regiões de interesse, eu optei por extrair as informações da seção de 'Valores Faturados', 'Informações Gerais' e do rodapé da fatura. A seção de valores faturados contem dados suficientes para preencher os valores de Energia Consumida e Energia compensada, além do valor total a pagar, entretando não foi dessa seção que eu retirei esse dado. Da seção de informações gerai, foi recortada apenas a primeira linha, pois essa contem o valor de crédito acumulado. O rodapé da fatura foi escolhido pois ele é a área que contem o número da instalação, data e total a pagar com o menor número de caracteres desnecessários para a pesquisa.

Dessa forma, a busca com regex foi realizada com uma facilidade extremamente maior em relação ao primeiro teste. O processamento de imagens pode aumentar o custo computacional do programa, entretanto o carregamento e recorte da imagem são operações leves e seu custo computacional é compensado pelo tempo de desenvolvimento e adaptabilidade do código para outras estruturas de fatura.




# Requisitos dos Desafios

1. Utilize a linguagem Python para desenvolver a solução.
2. No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3. Faça um fork do repositório, para iniciar o desenvolvimento.
4. A entrega deve ser realizada por meio de um pull request para o repositório original.
5. Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste. Se o pull request for realizado antes dos 5 minutos restantes haverá eliminação do candidato.
6. A entrega deve ser realizada até às 17h30. Caso o prazo não seja cumprido, haverá perda de pontos.
