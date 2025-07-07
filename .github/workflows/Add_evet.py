def update_readme(file_path, readme_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    lines = ["# 📅 Eventos Confirmados\n"]

    for ano_entry in sorted(data["eventos"], key=lambda y: int(y["ano"])):
        if ano_entry["arquivado"]:
            continue

        lines.append(f"\n## {ano_entry['ano']}\n")
        for mes_entry in ano_entry["meses"]:
            if mes_entry["arquivado"]:
                continue

            lines.append(f"### {mes_entry['mes'].capitalize()}\n")
            for evento in mes_entry["eventos"]:
                dias = ", ".join(evento["data"])
                lines.append(f"- **{evento['nome']}** – {dias} – {evento['cidade']}/{evento['uf']} – [{evento['tipo']}]({evento['url']})")

            lines.append("")  # linha em branco

    # TBA
    if data["tba"]:
        lines.append("\n## 📌 Eventos a Definir (TBA)\n")
        for evento in data["tba"]:
            lines.append(f"- **{evento['nome']}** – {evento['cidade']}/{evento['uf']} – [{evento['tipo']}]({evento['url']})")
        lines.append("")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"README.md atualizado com sucesso.")
