### IMAGEM BASE
FROM python:3.7
## ALTERAÇÔES NA IMAGEM

## DIRETÒRIO DE TRABALHO
WORKDIR /code
### INSTALL PARA LIBRARY
RUN pip3 install psycopg2
#COPIA O CODIGO PYTHON PARA O CONTAINER
COPY list-data-table.py /code/
#EXECUTA O CODIGO PYTHON
CMD [ "python", "list-data-table.py" ]