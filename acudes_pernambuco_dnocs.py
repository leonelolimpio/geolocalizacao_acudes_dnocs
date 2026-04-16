# arquivo: acudes_pernambuco_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado de Pernambuco
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_pernambuco = [
    {
        "nome": "Abóboras",
        "municipios_limite": ["Parnamirim"],
        "lat": -8.0906,
        "lon": -39.5786
    },
    {
        "nome": "Araripina - Baixio",
        "municipios_limite": ["Araripina"],
        "lat": -7.2083,
        "lon": -40.4928
    },
    {
        "nome": "Arcoverde",
        "municipios_limite": ["Pedra"],
        "lat": -8.4964,
        "lon": -36.9408
    },
    {
        "nome": "Arrodeio",
        "municipios_limite": ["São José do Belmonte"],
        "lat": -7.8575,
        "lon": -38.7594
    },
    {
        "nome": "Barra",
        "municipios_limite": ["Sertânia"],
        "lat": -8.0753,
        "lon": -37.2642
    },
    {
        "nome": "Barra do Juá",
        "municipios_limite": ["Floresta"],
        "lat": -8.6008,
        "lon": -38.5686
    },
    {
        "nome": "Belo Jardim",
        "municipios_limite": ["Belo Jardim"],
        "lat": -8.3317,
        "lon": -36.4253
    },
    {
        "nome": "Boa Vista",
        "municipios_limite": ["Salgueiro"],
        "lat": -8.0742,
        "lon": -39.1197
    },
    {
        "nome": "Bonito Grande",
        "municipios_limite": ["Bonito"],
        "lat": -8.4714,
        "lon": -35.7292
    },
    {
        "nome": "Cachoeira I",
        "municipios_limite": ["São Francisco"],
        "lat": -8.7469,
        "lon": -38.9686
    },
    {
        "nome": "Cachoeira II",
        "municipios_limite": ["Serra Talhada"],
        "lat": -7.974117938706715,
        "lon": -38.32343538097117
    },
    {
        "nome": "Cruzeiro",
        "municipios_limite": ["São José do Belmonte"],
        "lat": -7.8575,
        "lon": -38.7594
    },
    {
        "nome": "Custódia",
        "municipios_limite": ["Custódia"],
        "lat": -8.0872,
        "lon": -37.6433
    },
    {
        "nome": "Engº Severino Guerra",
        "municipios_limite": ["Betânia"],
        "lat": -8.2758,
        "lon": -38.0339
    },
    {
        "nome": "Entremontes",
        "municipios_limite": ["Parnamirim"],
        "lat": -8.0906,
        "lon": -39.5786
    },
    {
        "nome": "Garanhuns",
        "municipios_limite": ["Garanhuns"],
        "lat": -8.943387,
        "lon": -36.493225
    },
    {
        "nome": "Guilherme de Azevedo",
        "municipios_limite": ["Caruaru"],
        "lat": -8.36047179184193,
        "lon": -36.03204468053237
    },
    {
        "nome": "Jucazinho",
        "municipios_limite": ["Surubim", "Cumaru", "Alagoinha"],
        "lat": -8.0217,
        "lon": -35.7533
    },
    {
        "nome": "Malhada da Pedra",
        "municipios_limite": ["Caruaru"],
        "lat": -8.248143933047158,
        "lon": -35.91609829621145
    },
    {
        "nome": "Mororó",
        "municipios_limite": ["Pedra"],
        "lat": -8.4964,
        "lon": -36.9408
    },
    {
        "nome": "Parnamirim",
        "municipios_limite": ["Parnamirim"],
        "lat": -8.0906,
        "lon": -39.5786
    },
    {
        "nome": "Patí",
        "municipios_limite": ["Ouricuri"],
        "lat": -7.8825,
        "lon": -40.0817
    },
    {
        "nome": "Pau Branco",
        "municipios_limite": ["São Francisco"],
        "lat": -8.7469,
        "lon": -38.9686
    },
    {
        "nome": "Pedra d´Água",
        "municipios_limite": ["Pesqueira"],
        "lat": -8.3583,
        "lon": -36.6956
    },
    {
        "nome": "Poço da Cruz (Eng. Fco. Saboia)",
        "municipios_limite": ["Ibimirim"],
        "lat": -8.5403,
        "lon": -37.6903
    },
    {
        "nome": "Quebra Unha",
        "municipios_limite": ["Floresta"],
        "lat": -8.6008,
        "lon": -38.5686
    },
    {
        "nome": "Rosário",
        "municipios_limite": ["Iguaraci"],
        "lat": -7.8308,
        "lon": -37.5083
    },
    {
        "nome": "Saco I",
        "municipios_limite": ["Serra Talhada"],
        "lat": -7.9919,
        "lon": -38.2950
    },
    {
        "nome": "Saco II",
        "municipios_limite": ["Santa Maria da Boa Vista"],
        "lat": -8.8017,
        "lon": -39.8250
    },
    {
        "nome": "Salgueiro",
        "municipios_limite": ["Salgueiro"],
        "lat": -8.0742,
        "lon": -39.1197
    },
    {
        "nome": "São Caetano",
        "municipios_limite": ["São Caetano"],
        "lat": -8.3258,
        "lon": -36.1392
    },
    {
        "nome": "Serigi",
        "municipios_limite": ["Ouricuri"],
        "lat": -7.8825,
        "lon": -40.0817
    },
    {
        "nome": "Serra dos Cavalos",
        "municipios_limite": ["Caruaru"],
        "lat": -8.361625625117147,
        "lon": -36.03834933655988
    },
    {
        "nome": "Serrinha",
        "municipios_limite": ["Serra Talhada"],
        "lat": -7.9919,
        "lon": -38.2950
    },
    {
        "nome": "Tamboril I",
        "municipios_limite": ["Rio Branco"],
        "lat": -7.9000,
        "lon": -38.1500
    },
    {
        "nome": "Tamboril II - Eng.º Camacho",
        "municipios_limite": ["Ouricuri"],
        "lat": -7.8825,
        "lon": -40.0817
    },
    {
        "nome": "Terra Nova",
        "municipios_limite": ["Petrolina"],
        "lat": -9.3939,
        "lon": -40.5078
    },
    {
        "nome": "Vertente do Heráclito",
        "municipios_limite": ["Surubim"],
        "lat": -7.8289,
        "lon": -35.7547
    },
    {
        "nome": "Vira Beiju",
        "municipios_limite": ["Petrolina"],
        "lat": -9.3939,
        "lon": -40.5078
    }
]

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_pernambuco.json", "w", encoding="utf-8") as f:
        json.dump(acudes_pernambuco, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_pernambuco:
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

    with open("acudes_pernambuco.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_pernambuco.json e acudes_pernambuco.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")