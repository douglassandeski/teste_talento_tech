﻿# talento_tech_final
# Jogo Pong

Um jogo simples de Pong implementado em Python usando a biblioteca Pygame.

## Objetivos do Projeto

- Desenvolver um jogo básico de Pong para dois jogadores, demonstrando conceitos fundamentais no desenvolvimento de jogos com Pygame.
- Aprimorar a compreensão de detecção de colisões, manipulação de entradas do teclado e loops de jogo em tempo real.
- Fornecer um ponto de partida para quem deseja aprender desenvolvimento de jogos em Python.

## Funcionalidades

1. Jogo para Dois Jogadores:
   - O jogador 1 usa as teclas `W` (cima) e `S` (baixo) para controlar o paddle esquerdo.
   - O jogador 2 usa as setas `CIMA` e `BAIXO` para controlar o paddle direito.

2. Sistema de Pontuação:
   - Um ponto é atribuído a um jogador quando o adversário não consegue retornar a bola.
   - As pontuações são exibidas na tela.

3. Detecção de Colisões:
   - A bola rebate nos paddles e nas bordas da tela.

4. Jogabilidade em Tempo Real:
   - Movimento suave dos paddles e da bola com manipulação de entrada em tempo real.

## Cronograma de Desenvolvimento
 
| Etapa           | Descrição da Tarefa                                                      | Prazo Estimado       
| 1. Configuração | Configurar o ambiente Pygame e criar a janela do jogo.                   | 1 dia               
| 2. Paddles      | Adicionar os paddles e habilitar o movimento com o teclado.              | 1 dia               
| 3. Bola         | Implementar a bola com movimento e detecção básica de colisão.           | 1 dia              
| 4. Pontuação    | Adicionar a mecânica de pontuação e exibir os pontos na tela.            | 1 dia               
| 5. Polimento    | Refinar a física do jogo, adicionar melhorias visuais e realizar testes. | 1 dia               

## Como Executar

1. Certifique-se de que o Python está instalado no seu sistema.
2. Instale a biblioteca Pygame executando:
   ```bash
   pip install pygame
   ```
3. Salve o código do jogo em um arquivo chamado `pong_game.py`.
4. Execute o jogo com:
   ```bash
   python pong_game.py
   ```

## Melhorias Futuras

- Adicionar uma tela de menu com opções para iniciar o jogo ou sair.
- Introduzir IA para o modo de um jogador.
- Incluir efeitos sonoros para batidas nos paddles e pontuações.

## Requisitos

- Python 3.6+
- Biblioteca Pygame

