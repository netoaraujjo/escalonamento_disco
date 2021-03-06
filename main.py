#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fcfs import *
from sstf import *
from elevador import *
import copy

# funcao principal
def main():
    # Le o numero do ultimo cilindro do disco
    ultimo_cilindro = int(sys.stdin.readline())

    # Le a posicao inicial do braco do disco
    cilindro_inicial = int(sys.stdin.readline())

    # Le as requisicoes de acesso
    requisicoes = map(int, sys.stdin.readlines())

    # Instancia um objeto da class FCFS
    fcfs = FCFS()
    # Executa o algoritmo de escalonamento FCFS
    deslocamento_fcfs = fcfs.execute(cilindro_inicial, requisicoes)

    # Instancia um objeto da class SSTF
    sstf = SSTF()
    # Executa o algoritmo de escalonamento SSTF
    deslocamento_sstf = sstf.execute(cilindro_inicial, copy.deepcopy(requisicoes))

    # Instancia um objeto da class Elevador
    elevador = Elevador()
    # Executa o algoritmo de escalonamento Elevador
    deslocamento_elevador = elevador.execute(ultimo_cilindro, cilindro_inicial, requisicoes)

    # Formata a saida
    saida = 'FCFS {0}\nSSTF {1}\nELEVADOR {2}'

    # Exibe a saida
    print(saida.format(deslocamento_fcfs, deslocamento_sstf, deslocamento_elevador))

# Verifica se e o modulo principal e executa o codigo
if __name__ == "__main__":
    main()
