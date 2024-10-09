# Pyhon PowerUp - Automação de Tarefas :snake
Projeto desenvolvido durante o intensivão "Jornada Python" do canal [Hashtag Programação]

## Objetivo:
O objetivo deste projeto era criar uma automação de cadastro de itens em um sistema ficticio, usando um banco de dados em *.csv*

## Passo a passo (Script):
    1. **[Passo 01]**: Entrar no sistema
    1. **[Passo 02]**: Fazer o login
    1. **[Passo 03]**: Importar a base de dados
    1. **[Passo 04]**: Cadastrar um produto
    1. **[Passo 05]**: Repetir o processo de cadastro para os outros produtos da base

## Como rodar o programa:
    **Requisitos:** Possuir o python e algum editor de código instalado em sua máquina

    1. Clone o repositório para sua máquina;
    2. Instale as bibliotecas pyautogui e pandas no seu ambiente
        *pip install _libname_
    3. Execute o arquivo _main.py_, porém [**ATENÇÃO**] => O programa utiliza o posicionamento do mouse para clicar em alguns campos utilizado o *pyautogui*, então talvez seja necessário executá-lo em modo debugger e nos lugar em que há a função *pyautogui.click(x=,y=)* execute o arquivo getPosition e coloque o mouse na posição para conseguir as coordenadas dos respectivos campos.

*Se chegou até aqui, sinta-se a vontade para analisar e sugerir melhorias e alterações para este projeto*
*Projeto sem intenção de monetização apenas utilizado para aprendizado*