# arquivo: acudes_bahia_dnocs_dataset.py

# =========================
# Esse script geolocaliza açudes do estado da Bahia
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas e IBGE - Instituto Brasileiro Geográfico e Estatístico
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

acudes_bahia = [
    {
        "nome": "Adustina",
        "municipios_limite": ["Adustina"],
        "lat": -10.54369,
        "lon": -38.111265
    },
    {
        "nome": "Anagé",
        "municipios_limite": ["Anagé"],
        "lat": -14.6153,
        "lon": -41.1358
    },
    {
        "nome": "Andorinha II",
        "municipios_limite": ["Senhor do Bonfim"],
        "lat": -10.345,
        "lon": -39.83278
    },
    {
        "nome": "Araci",
        "municipios_limite": ["Araci"],
        "lat": -11.2875,
        "lon": -39.09889
    },
    {
        "nome": "Barra do Mendes",
        "municipios_limite": ["Barra do Mendes"],
        "lat": -11.8104,
        "lon": -42.0592
    },
    {
        "nome": "Brumado - Engº Luís Vieira",
        "municipios_limite": ["Rio de Contas"],
        "lat": -13.53458,
        "lon": -41.82782
    },
    {
        "nome": "Cariacá",
        "municipios_limite": ["Monte Santo"],
        "lat": -10.48,
        "lon": -39.35611
    },
    {
        "nome": "Champrão",
        "municipios_limite": ["Condeúba"],
        "lat": -14.895,
        "lon": -41.96917
    },
    {
        "nome": "Cocorobó",
        "municipios_limite": ["Euclides da Cunha"],
        "lat": -9.882265,
        "lon": -39.039003
    },
    {
        "nome": "Delfino",
        "municipios_limite": ["Campo Formoso"],
        "lat": -10.5083,
        "lon": -40.3211
    },
    {
        "nome": "Genipapo",
        "municipios_limite": ["Itiúba"],
        "lat": -10.6947,
        "lon": -39.8536
    },
    {
        "nome": "Jacaré",
        "municipios_limite": ["Ibiassucê"],
        "lat": -14.305241,
        "lon": -42.28799
    },
    {
        "nome": "Jacurici - Rômulo Campos",
        "municipios_limite": ["Itiúba"],
        "lat": -10.69167,
        "lon": -39.85361
    },
    {
        "nome": "Juraci Magalhães",
        "municipios_limite": ["Itaberaba"],
        "lat": -12.53436,
        "lon": -40.31742
    },
    {
        "nome": "Laginha",
        "municipios_limite": ["Monte Santo"],
        "lat": -10.43833,
        "lon": -39.32694
    },
    {
        "nome": "Miguel Calmon",
        "municipios_limite": ["Serrinha"],
        "lat": -11.4269,
        "lon": -40.5943
    },
    {
        "nome": "Monteiro",
        "municipios_limite": ["Queimadas"],
        "lat": -10.9756,
        "lon": -39.6233
    },
    {
        "nome": "Morrinhos",
        "municipios_limite": ["Poções"],
        "lat": -14.56953,
        "lon": -40.292124
    },
    {
        "nome": "Pinhões",
        "municipios_limite": ["Curaçá", "Juazeiro"],
        "lat": -9.581,
        "lon": -39.88686
    },
    {
        "nome": "Quicé",
        "municipios_limite": ["Senhor do Bonfim"],
        "lat": -10.5427,
        "lon": -40.0258
    },
    {
        "nome": "Rancharia",
        "municipios_limite": ["Juazeiro"],
        "lat": -9.519858,
        "lon": -40.087424
    },
    {
        "nome": "Riacho do Onça",
        "municipios_limite": ["Queimadas"],
        "lat": -11.237709,
        "lon": -39.743937
    },
    {
        "nome": "Riacho do Paulo",
        "municipios_limite": ["Livramento de Nossa Senhora"],
        "lat": -13.6369,
        "lon": -41.8431
    },
    {
        "nome": "Riacho do Peixe",
        "municipios_limite": ["Capim Grosso"],
        "lat": -11.24167,
        "lon": -39.97556
    },
    {
        "nome": "Riacho do Sítio",
        "municipios_limite": ["Andorinha"],
        "lat": -10.17528,
        "lon": -39.95701
    },
    {
        "nome": "São Domingos",
        "municipios_limite": ["São Domingos"],
        "lat": -11.46556,
        "lon": -39.52611
    },
    {
        "nome": "Serrote",
        "municipios_limite": ["Serrolândia"],
        "lat": -11.4083,
        "lon": -40.2983
    },
    {
        "nome": "Sohen",
        "municipios_limite": ["Senhor do Bonfim"],
        "lat": -10.45978,
        "lon": -40.1869
    },
    {
        "nome": "Tabua II",
        "municipios_limite": ["Ibiassucê"],
        "lat": -14.2556,
        "lon": -42.2572
    },
    {
        "nome": "Tancão do Caititu",
        "municipios_limite": ["Condeúba"],
        "lat": -14.895,
        "lon": -41.96917
    },
    {
        "nome": "Tapera",
        "municipios_limite": ["Santa Luz"],
        "lat": -11.2525,
        "lon": -39.4578
    },
    {
        "nome": "Tremedal",
        "municipios_limite": ["Tremedal"],
        "lat": -14.97583,
        "lon": -41.41083
    },
    {
        "nome": "Truvisco",
        "municipios_limite": ["Caculé"],
        "lat": -14.57656,
        "lon": -42.3554
    },
    {
        "nome": "Valente",
        "municipios_limite": ["Valente"],
        "lat": -11.4114,
        "lon": -39.4633
    }
]

if __name__ == "__main__":
    with open("acudes_bahia.json", "w", encoding="utf-8") as f:
        json.dump(acudes_bahia, f, ensure_ascii=False, indent=2)

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_bahia:
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

    with open("acudes_bahia.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_bahia.json e acudes_bahia.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")