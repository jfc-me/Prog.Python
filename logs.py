# -*- coding: utf-8 -*-
from os import system as chamadas


class Log:
    global COMMAND

    def __init__(self):
        self._command = ''
        self._consulta = "/var/log/auth.log"

    def _get_command(self):
        return self._command

    def _set_command(self, ent):
        self._command = ent

    cmd = property(fget=_get_command, fset=_set_command)

    def exec(self):
        print(50 * "-", "\n", "[ > ] Todas as instruçoes\n", 50 * "-")
        COMMAND = ' | grep '
        comando_usado = Log().cmd = "cat " + self._consulta + COMMAND
        chamadas(comando_usado + '"COMMAN"')

        def activates_apt_get():
            print(50 * "-", "\n", "[ > ] apt-get usado \n", 50 * "-")
            nonlocal comando_usado
            apt_get = comando_usado
            chamadas(apt_get + '/usr/bin/apt-get')

            def reboot():
                print(50 * "-", "\n", "[ > ] Reboots \n", 50 * "-")
                nonlocal COMMAND
                ver = COMMAND
                reboots = Log().cmd = '/usr/bin/last' + ver + 'reboot'
                chamadas(reboots)

            reboot()
        activates_apt_get()


Log().exec()
