#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
# By Checchia - Setembro.2023
#
import json, csv, os
from tinydb import TinyDB, Query

json_data = {
    "100": "Continuar",
    "101": "Mudando protocolos",
    "102": "Processando",
    "103": "dicas iniciais",
    "200": "OK",
    "201": "Criado",
    "202": "Aceito",
    "203": "Não autorizado",
    "204": "Sem conteúdo",
    "205": "Redefinir conteúdo",
    "206": "Conteúdo parcial",
    "207": "Multi-status",
    "208": "Já relatado",
    "300": "Múltiplas escolhas",
    "301": "Movido permanentemente",
    "302": "Encontrado",
    "303": "Consulte Outro",
    "304": "Não modificado",
    "305": "Use Proxy",
    "307": "Redirecionamento temporário",
    "400": "Pedido ruim",
    "401": "Não autorizado",
    "402": "Pagamento necessário",
    "403": "Proibido",
    "404": "Não encontrado",
    "405": "Método não permitido",
    "406": "Não aceitável",
    "407": "Autenticação de proxy necessária",
    "408": "Tempo esgotado",
    "409": "Conflito",
    "410": "Desaparecido",
    "411": "Comprimento necessário",
    "418": "eu sou um bule de chá",
    "412": "Pré-condição falhou",
    "413": "Entidade de solicitação muito grande",
    "414": "URI muito longa",
    "415": "Tipo de mídia não suportado",
    "416": "Solicitação de faixa não satisfeita",
    "417": "Expectativa falhou",
    "426": "Upgrade necessário",
    "500": "Erro interno do servidor",
    "501": "Não implementado",
    "502": "Gateway ruim",
    "503": "Serviço indisponível",
    "504": "Tempo limite de gateway",
    "505": "Versão HTTP não suportada"
}

def create_database_if_not_exists():
    db = TinyDB('/tmp/banco.json')
    if len(db.all()) == 0:
        for http_code, message in json_data.items():
            db.insert({'http_code': int(http_code), 'message': message})
        print("Banco de dados criado e populado com sucesso!")
    else:
        print("O banco de dados já existe e possui dados.")

def http_error(error_code):
    db = TinyDB('/tmp/banco.json')
    tabela = db.table('_default')
    consulta = Query()
    print("error_code", error_code)
    resultado = tabela.get(consulta.http_code == int(error_code))
    print("resultado", json.dumps(resultado))
    if resultado:
        return {"code": resultado['http_code'], "message": resultado['message']}
    else:
        return {"code": 000, "message": "Code not found"}
