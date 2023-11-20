import configparser

class Script:
    def query(self, codEntidade):
        # cfg = configparser.ConfigParser()
        # cfg.read('cfg.ini')

        return {
        'Bem' : f""" select count(*) from scp55_bem where codentidade = {codEntidade} """,

        'TombamentoBem' : f""" select count(*) 
                            from SCP55_TOMBAMENTOBEM 
                            where IDBEM in (select idbem from scp55_bem where codentidade = {codEntidade})""",

        'SaldoAnteriorBem' : f""" SELECT
                                count(*)
                                FROM SCP55_SALDOANTERIORBEM sab
                                join SCP55_BEM b on b.IDBEM = sab.IDBEM
                                join SCP55_CONTACONTABIL cc on cc.IDCONTACONTABIL = sab.IDCONTACONTABIL
                                where 
                                sab.CODENTIDADE = {codEntidade} """

        }