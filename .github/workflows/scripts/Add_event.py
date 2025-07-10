import sys
import json
import re

def parse_issue_body(body):
    # Exemplo simples: extraia campos do corpo da issue
    # Adapte conforme o formato real do corpo gerado pelo template
    data = {}
    patterns = {
        "Nome do Evento": r"Nome do Evento\s*\n([^\n]+)",
        "Formato do Evento": r"Formato do Evento\s*\n([^\n]+)",
        "Ano do Evento": r"Ano do Evento\s*\n([^\n]+)",
        "Local do Evento": r"Local do Evento\s*\n([^\n]+)",
        "Data de Início": r"Data de Início\s*\n([^\n]+)",
        "Data de Término": r"Data de Término\s*\n([^\n]+)",
        "Site do Evento": r"Site do Evento\s*\n([^\n]+)",
        "Descrição": r"Descrição\s*\n([^\n]+)",
        "Contato": r"Contato\s*\n([^\n]+)",
        "Observações": r"Observações\s*\n([^\n]+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, body)
        if match:
            data[key] = match.group(1).strip()
    return data

if __name__ == "__main__":
    body = sys.argv[1]
    evento = parse_issue_body(body)
    with open('eventos.json', 'a', encoding='utf-8') as f:
        json.dump(evento, f, ensure_ascii=False)
        f.write('\n')