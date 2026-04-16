# arquivo: acudes_riograndedonorte_dnocs_dataset.py

# =========================
# Esse script geolocaliza açudes do estado do Rio Grande do Norte
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas e IBGE - Instituto Brasileiro Geográfico e Estatístico
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_rn = [
    {
        "nome": "Acari",
        "municipios_limite": ["Acari"],
        "lat": -6.4328,
        "lon": -36.6347
    },
    {
        "nome": "Alecrim",
        "municipios_limite": ["Santana do Matos"],
        "lat": -5.9047,
        "lon": -36.6349
    },
    {
        "nome": "Angicos - Arapuã",
        "municipios_limite": ["José da Penha"],
        "lat": -6.355079695213014,
        "lon": -38.276857008610065
    },
    {
        "nome": "Armando R. Gonçalves - Açu",
        "municipios_limite": ["Açu", "Itajá", "Ipanguaçu"],
        "lat": -5.667686702560129,
        "lon": -36.89049306743237
    },
    {
        "nome": "Ausentes",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Barrocas",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Bêbado",
        "municipios_limite": ["Macaíba"],
        "lat": -5.8583,
        "lon": -35.3536
    },
    {
        "nome": "Bonito II",
        "municipios_limite": ["São Miguel"],
        "lat": -6.211961587647248,
        "lon": -38.432040997987926
    },
    {
        "nome": "Caldeirão de Parelhas",
        "municipios_limite": ["Parelhas"],
        "lat": -6.7106,
        "lon": -36.6869
    },
    {
        "nome": "Cerro Corá",
        "municipios_limite": ["Cerro Corá"],
        "lat": -6.0456,
        "lon": -36.3458
    },
    {
        "nome": "Corredor",
        "municipios_limite": ["Martins", "Antônio Martins"],
        "lat": -6.1883,
        "lon": -37.9456
    },
    {
        "nome": "Cruzeta",
        "municipios_limite": ["Cruzeta"],
        "lat": -6.3830,
        "lon": -36.8000
    },
    {
        "nome": "Currais",
        "municipios_limite": ["Currais Novos"],
        "lat": -6.2641,
        "lon": -36.5174
    },
    {
        "nome": "Currais Novos",
        "municipios_limite": ["Currais Novos"],
        "lat": -6.2606,
        "lon": -36.5175
    },
    {
        "nome": "Dourado",
        "municipios_limite": ["Currais Novos"],
        "lat": -6.2606,
        "lon": -36.5175
    },
    {
        "nome": "Flechas",
        "municipios_limite": ["José da Penha"],
        "lat": -6.3060944043411835,
        "lon": -38.252336986960216
    },
    {
        "nome": "Ingá I",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Inharé",
        "municipios_limite": ["Santa Cruz"],
        "lat": -6.2250,
        "lon": -36.0228
    },
    {
        "nome": "Itans",
        "municipios_limite": ["Caicó"],
        "lat": -6.5073,
        "lon": -37.0389
    },
    {
        "nome": "Japi II",
        "municipios_limite": ["São José do Campestre"],
        "lat": -6.3158,
        "lon": -35.7136
    },
    {
        "nome": "Lucrécia",
        "municipios_limite": ["Lucrécia"],
        "lat": -6.1200,
        "lon": -37.8150
    },
    {
        "nome": "Malhada Vermelha",
        "municipios_limite": ["Severiano Melo"],
        "lat": -5.784979464411098,
        "lon": -37.91716486046026
    },
    {
        "nome": "Marcelino Vieira",
        "municipios_limite": ["Marcelino Vieira"],
        "lat": -6.332830879107141,
        "lon": -38.179220647949265
    },
    {
        "nome": "Marechal Dutra",
        "municipios_limite": ["Acari"],
        "lat": -6.4328,
        "lon": -36.6347
    },
    {
        "nome": "Mendobim",
        "municipios_limite": ["Açu"],
        "lat": -5.642970355951721,
        "lon": -36.93181587493812
    },
    {
        "nome": "Morcêgo",
        "municipios_limite": ["Campo Grande"],
        "lat": -5.8710621994640775,
        "lon": -37.34823272476516
    },
    {
        "nome": "Mossoró",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Mundo Novo",
        "municipios_limite": ["Caicó"],
        "lat": -6.4586,
        "lon": -37.0964
    },
    {
        "nome": "Nova Cruz",
        "municipios_limite": ["Nova Cruz"],
        "lat": -6.4781,
        "lon": -35.4339
    },
    {
        "nome": "Passagem das Traíras",
        "municipios_limite": ["São José do Seridó", "Jardim do Seridó", "Caicó"],
        "lat": -6.5114,
        "lon": -36.9142
    },
    {
        "nome": "Pataxó",
        "municipios_limite": ["Ipanguaçu"],
        "lat": -5.4983,
        "lon": -36.8553
    },
    {
        "nome": "Pau",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Pau dos Ferros",
        "municipios_limite": ["Pau dos Ferros"],
        "lat": -6.16472506773881,
        "lon": -38.17787666811692
    },
    {
        "nome": "Pauzinhos",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Pessoa",
        "municipios_limite": ["São Miguel"],
        "lat": -6.215937358056781,
        "lon": -38.498186649096354
    },
    {
        "nome": "Pilões",
        "municipios_limite": ["Pilões"],
        "lat": -6.271781630515335,
        "lon": -38.039927933316704
    },
    {
        "nome": "Poço Branco (Engº Jose Batista)",
        "municipios_limite": ["Poço Branco"],
        "lat": -5.6211,
        "lon": -35.6628
    },
    {
        "nome": "Mirim - Portalegre",
        "municipios_limite": ["Portalegre"],
        "lat": -6.0178383515546425,
        "lon": -38.01550165621779
    },
    {
        "nome": "Riacho da Cruz II",
        "municipios_limite": ["Riacho da Cruz"],
        "lat": -5.9358,
        "lon": -37.9467
    },
    {
        "nome": "Sabugi",
        "municipios_limite": ["São João do Sabugi"],
        "lat": -6.7442,
        "lon": -37.2694
    },
    {
        "nome": "Saco",
        "municipios_limite": ["Mossoró"],
        "lat": -5.1875,
        "lon": -37.3442
    },
    {
        "nome": "Santa Cruz do Trairi",
        "municipios_limite": ["Santa Cruz", "Tangará"],
        "lat": -6.225049032376593,
        "lon": -36.03146609687101
    },
    {
        "nome": "Santa Cruz I",
        "municipios_limite": ["Santa Cruz"],
        "lat": -5.762648366212078,
        "lon": -37.801186358812785
    },
    {
        "nome": "Santana (Gangorra)",
        "municipios_limite": ["Rafael Fernandes"],
        "lat": -6.2183730166579,
        "lon": -38.264349327197586
    },
    {
        "nome": "Santo Antônio de Caraúbas",
        "municipios_limite": ["Caraúbas"],
        "lat": -5.7928,
        "lon": -37.5564
    },
    {
        "nome": "Serra Negra",
        "municipios_limite": ["Serra Negra do Norte"],
        "lat": -6.6592,
        "lon": -37.3989
    },
    {
        "nome": "Sossego",
        "municipios_limite": ["Rodolfo Fernandes"],
        "lat": -5.793332486993979,
        "lon": -38.06913298883977
    },
    {
        "nome": "Tesoura",
        "municipios_limite": ["Francisco Dantas"],
        "lat": -6.0778,
        "lon": -38.1214
    },
    {
        "nome": "Totoró",
        "municipios_limite": ["Currais Novos"],
        "lat": -6.2606,
        "lon": -36.5175
    },
    {
        "nome": "Trairi",
        "municipios_limite": ["Tangará", "Santa Cruz"],
        "lat": -6.1992,
        "lon": -35.8017
    },
    {
        "nome": "Umarizal",
        "municipios_limite": ["Umarizal"],
        "lat": -6.053610148923561,
        "lon": -37.77932056317078
    }
]

if __name__ == "__main__":
    with open("acudes_rn.json", "w", encoding="utf-8") as f:
        json.dump(acudes_rn, f, ensure_ascii=False, indent=2)

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_rn:
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

    with open("acudes_rn.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_rn.json e acudes_rn.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")