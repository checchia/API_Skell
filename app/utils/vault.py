#!/usr/bin/env python3
#   ____ _                   _     _         _   _ _____ _____
#  / ___| |__   ___  ___ ___| |__ (_) __ _  | \ | | ____|_   _|
# | |   | '_ \ / _ \/ __/ __| '_ \| |/ _` | |  \| |  _|   | |
# | |___| | | |  __/ (_| (__| | | | | (_| |_| |\  | |___  | |
#  \____|_| |_|\___|\___\___|_| |_|_|\__,_(_)_| \_|_____| |_|
# By Checchia - 09/2023
#
import os, httpx, requests

vault_token = os.getenv('VAULT_TOKEN')
vault_url = os.getenv('VAULT_URL')
api_name = 'api'

headers = {'X-Vault-Token': vault_token}


def get_vault(kv):
    url = f'{vault_url}/v1/{api_name}/data/{kv}'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        z = r.json()
        return z['data']['data']
    return "error"