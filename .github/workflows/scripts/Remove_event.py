import json
import os

def remove_event_from_json(file_path, event_name, year, month):
    with open(file_path, "r") as f:
        data = json.load(f)

    found = False
    for y in data.get("eventos", []):
        if y["ano"] == year:
            for m in y["meses"]:
                if m["mes"] == month:
                    original_count = len(m["eventos"])
                    m["eventos"] = [ev for ev in m["eventos"] if ev["nome"] != event_name]
                    if len(m["eventos"]) < original_count:
                        found = True
    if not found:
        print("Evento não encontrado para remoção.")
        return
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Evento removido e arquivo {file_path} salvo com sucesso!")

def get_removal_info_from_env():
    return {
        "ano": int(os.getenv("event_year", 0)),
        "mes": os.getenv("event_month", "").strip().lower(),
        "nome": os.getenv("event_name", "").strip(),
    }

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'db', 'database.json')
    info = get_removal_info_from_env()
    remove_event_from_json(db_path, info["nome"], info["ano"], info["mes"])
