import json
import os

CALENDAR_ORDER = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]

def update_event_in_json(file_path, updated_event):
    with open(file_path, "r") as f:
        data = json.load(f)

    year = updated_event["ano"]
    month = updated_event["mes"]
    nome = updated_event["evento"]["nome"]

    year_exist = next((y for y in data.get("eventos", []) if y["ano"] == year), None)
    if not year_exist:
        print("Ano não encontrado.")
        return
    month_exist = next((m for m in year_exist["meses"] if m["mes"] == month), None)
    if not month_exist:
        print("Mês não encontrado.")
        return
    for idx, ev in enumerate(month_exist["eventos"]):
        if ev["nome"] == nome:
            month_exist["eventos"][idx] = updated_event["evento"]
            break
    else:
        print("Evento não encontrado.")
        return
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Evento atualizado e arquivo {file_path} salvo com sucesso!")

def get_event_from_env():
    return {
        "ano": int(os.getenv("event_year", 0)),
        "mes": os.getenv("event_month", "").strip().lower(),
        "evento": {
            "nome": os.getenv("event_name", "").strip(),
            "data": sorted(os.getenv("event_day", "").strip().replace(" ", "").split(",")),
            "url": os.getenv("event_url", "").strip(),
            "cidade": os.getenv("event_city", "").strip().title(),
            "uf": os.getenv("event_state", "").strip(),
            "tipo": os.getenv("event_type", "").strip(),
        },
    }

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'db', 'database.json')
    updated_event = get_event_from_env()
    update_event_in_json(db_path, updated_event)
