# arquivo: acudes_maranhao_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado do Maranhão
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)


import json

acudes_maranhao = [
    {
        "nome": "Flores",
        "municipios_limite": ["Joselândia"],
        "lat": -4.7500,
        "lon": -44.8333
    },
    {
        "nome": "Pericumã",
        "municipios_limite": ["Pinheiro"],
        "lat": -2.4555,
        "lon": -45.0107
    }
]

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_maranhao.json", "w", encoding="utf-8") as f:
        json.dump(acudes_maranhao, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_maranhao:
        if acude["lat"] is not None and acude["lon"] is not None:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [acude["lon"], acude["lat"]]
                },
                "properties": {
                    "nome": acude["nome"],
                    "municipios_limite": acude["municipios_limite"]
                }
            }
            geojson["features"].append(feature)

    with open("acudes_maranhao.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_maranhao.json e acudes_maranhao.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")