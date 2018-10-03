# -*- coding: utf-8 -*-
import subprocess as processos
import os
mod = 1
class Coleta_inf_Linux:
    @staticmethod
    def infoSystem(obn):
        for item in obn:
            comandos = obn[item]["comandos"]
            if mod == 0:
                out, error = processos.Popen([comandos], stdout=processos.PIPE, stderr=processos.PIPE,shell=True).communicate()
                retornos = out.split('\n')
            else:
                echo_stdout = os.popen(comandos, 'r')
                retornos = echo_stdout.read().split('\n')
                obn[item]["retornos"] = retornos
        return obn

    @staticmethod
    def chamadas(obn):
        for item in obn:
            mensagem = obn[item]["mensagem"]
            retornos = obn[item]["retornos"]
            print("""

                          {}
        -----------------------------------------

           """.format(mensagem, retornos))
            for result in retornos:
                if result.strip() != "":
                    print(result.strip())

if os.geteuid() == 0:
    print("We're root!")


    lista_de_retornos = []
    _dicionarioSistema = {"p1": {"comandos": "cat /proc/cpuinfo", "mensagem": "CPU", "retornos": lista_de_retornos},
                      "p2": {"comandos": "cat /proc/meminfo", "mensagem": "MEMORIA", "retornos": lista_de_retornos},
                      "p3": {"comandos": "lscpi", "mensagem": "Disco #1", "retornos": lista_de_retornos},
                      "p4": {"comandos": "fdisk -l ", "mensagem": "Disco #2", "retornos": lista_de_retornos},
                      "p5": {"comandos": "df -h", "mensagem": "Montagem do sistema de Arquivos",
                             "retornos": lista_de_retornos},
                      "p6": {"comandos": "cat /etc/lsb-release", "mensagem": "Versão baseado no debian",
                             "retornos": lista_de_retornos},
                      "p7": {"comandos": "hdparm -i /dev/sda", "mensagem": "Versão do Disco,Config Disk",
                             "retornos": lista_de_retornos},
                      "p8": {"comandos": "lshw", "mensagem": "Detalhes Disco", "retornos": lista_de_retornos}
                      }

    dicionario1 = Coleta_inf_Linux.infoSystem(_dicionarioSistema)
    Coleta_inf_Linux.chamadas(dicionario1)

    _dicionarioApps_consumos = {
    "p1": {"comandos": "top -n 1", "mensagem": "Visão Geral #1 ", "retornos": lista_de_retornos},
    "p2": {"comandos": "vmstat  1 5", "mensagem": "Visão Geral #2", "retornos": lista_de_retornos},
    # gerar blocos grande para testes
    "p3": {"comandos": " tail -n5  /proc/slabinfo", "mensagem": "Memoria alocada para o Kernel",
           "retornos": lista_de_retornos}
    }
    dicionario2 = Coleta_inf_Linux.infoSystem(_dicionarioApps_consumos)
    Coleta_inf_Linux.chamadas(dicionario2)

    _dicionarioServicos = {
    "p1": {"comandos": "chkconfig --list", "mensagem": "Serviços Ativos e Desativados", "retornos": lista_de_retornos},
    "p2": {"comandos": "service --status-all", "mensagem": "Todos os Serviços", "retornos": lista_de_retornos}
    }
    dicionario3 = Coleta_inf_Linux.infoSystem(_dicionarioServicos)
    Coleta_inf_Linux.chamadas(dicionario3)

else:
    print("We're not root.")
