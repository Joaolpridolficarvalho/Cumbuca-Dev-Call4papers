import re

def parse_issue_body(body):
    patterns = {
        "ano_evento": r"Ano do Evento\s*\n([^\n]+)",
        "mes_evento": r"Mês do Evento\s*\n([^\n]+)",
        "nome_evento": r"Nome do Evento\s*\n([^\n]+)",
        "dias_evento": r"Dias do Evento\s*\n([^\n]+)",
        "url_evento": r"Site do Evento\s*\n([^\n]+)",
        "cidade_evento": r"Cidade do Evento\s*\n([^\n]+)",
        "estado_evento": r"Estado do Evento\s*\n([^\n]+)",
        "tipo_evento": r"Tipo do Evento\s*\n([^\n]+)",
    }
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, body)
        if match:
            data[key] = match.group(1).strip()
    return data