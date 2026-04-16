# arquivo: acudes_ceara_dnocs_dataset.py

# # =========================
# Esse script geolocaliza açudes do estado do Ceará
# Base de dados formada a partir de arquivos coletados diretamente no Departamento Nacional de Obras contra as Secas
# Dados cruzados com a base da ANA - Agência Nacional das Águas, IBGE - Instituto Brasileiro Geográfico e Estatístico, e OpenStreetMap
# Reservatórios construídos e sob administração do DNOCS
# =========================
# formato de saída: GeoJSON e JSON (compatível com QGIS)

import json

# Primeiramente preenchemos as informações de cada açude com sua informações e latitude e longitude

acudes_ceara = [
    {
        "nome": "Araras - Paulo Sarazate",
        "municipios_limite": ["Varjota", "Pires Ferreira", "Hidrolândia", "Santa Quitéria"],
        "lat": -4.1883,
        "lon": -40.4697
    },
    {
        "nome": "Acarape - Eugênio Gudin",
        "municipios_limite": ["Redenção"],
        "lat": -4.2261,
        "lon": -38.7292
    },
    {
        "nome": "Acaraú-mirim",
        "municipios_limite": ["Massapê"],
        "lat": -3.5236,
        "lon": -40.3428
    },
    {
        "nome": "Alto Alegre",
        "municipios_limite": ["Pacoti"],
        "lat": -4.2250,
        "lon": -38.9222
    },
    {
        "nome": "Amanari",
        "municipios_limite": ["Maranguape"],
        "lat": -3.8900,
        "lon": -38.6858
    },
    {
        "nome": "Atalho",
        "municipios_limite": ["Brejo Santo"],
        "lat": -7.4933,
        "lon": -38.9800
    },
    {
        "nome": "Baú",
        "municipios_limite": ["Guaiúba"],
        "lat": -4.0397,
        "lon": -38.6372
    },
    {
        "nome": "Banabuiu - Arrojado Lisbôa",
        "municipios_limite": ["Banabuiú"],
        "lat": -5.3333,
        "lon": -39.0000
    },
    {
        "nome": "Bonito",
        "municipios_limite": ["Ipu"],
        "lat": -4.3225,
        "lon": -40.7108
    },
    {
        "nome": "Breguedofe",
        "municipios_limite": ["Coreaú"],
        "lat": -3.5419,
        "lon": -40.6572
    },
    {
        "nome": "Açude Broco (Brocas) - Caiçaras",
        "municipios_limite": ["Tauá"],
        "lat": -6.005216992333375,
        "lon": -40.324756248980925
    },
    {
        "nome": "Caio Prado",
        "municipios_limite": ["Santa Quitéria"],
        "lat": -4.0517,
        "lon": -40.1528
    },
    {
        "nome": "Carão",
        "municipios_limite": ["Tamboril"],
        "lat": -4.8328,
        "lon": -40.3200
    },
    {
        "nome": "Castanhão / Pe Cicero",
        "municipios_limite": ["Jaguaribara", "Alto Santo", "Jaguaretama", "Jaguaribe"],
        "lat": -5.5000,
        "lon": -38.4500
    },
    {
        "nome": "Caxitoré",
        "municipios_limite": ["Pentecoste"],
        "lat": -3.75587699580433,
        "lon": -39.36525436172844
    },
    {
        "nome": "Cedro",
        "municipios_limite": ["Quixadá"],
        "lat": -4.974358876292408,
        "lon": -39.06511123288999
    },
    {
        "nome": "Choró - Pompeu Sobrinho",
        "municipios_limite": ["Choró"],
        "lat": -4.838862867559654,
        "lon": -39.141762520266866
    },
    {
        "nome": "Chaval",
        "municipios_limite": ["Chaval"],
        "lat": -3.0353,
        "lon": -41.2433
    },
    {
        "nome": "Curral Velho",
        "municipios_limite": ["Morada Nova"],
        "lat": -5.1067,
        "lon": -38.3725
    },
    {
        "nome": "Ema",
        "municipios_limite": ["Iracema"],
        "lat": -5.8125,
        "lon": -38.3319
    },
    {
        "nome": "Farias de Sousa",
        "municipios_limite": ["Nova Russas"],
        "lat": -4.7067,
        "lon": -40.5628
    },
    {
        "nome": "Favelas",
        "municipios_limite": ["Tauá"],
        "lat": -5.981600,
        "lon": -40.112263
    },
    {
        "nome": "Feitiçeiro - Joaquim Távora",
        "municipios_limite": ["Jaguaribe"],
        "lat": -5.8906,
        "lon": -38.6219
    },
    {
        "nome": "Figueiredo",
        "municipios_limite": ["Alto Santo"],
        "lat": -5.5200,
        "lon": -38.2700
    },
    {
        "nome": "Fogareiro - Ato. F. Antero",
        "municipios_limite": ["Quixeramobim"],
        "lat": -5.2000,
        "lon": -39.2900
    },
    {
        "nome": "Formosa",
        "municipios_limite": ["Pacoti"],
        "lat": -4.2250,
        "lon": -38.9222
    },
    {
        "nome": "Forquilha",
        "municipios_limite": ["Acaraú"],
        "lat": -2.8878,
        "lon": -40.1200
    },
    {
        "nome": "Forquilha II",
        "municipios_limite": ["Tauá"],
        "lat": -5.531238490452609,
        "lon": -40.0812088773245
    },
    {
        "nome": "Frios",
        "municipios_limite": ["Umirim"],
        "lat": -3.6769,
        "lon": -39.3500
    },
    {
        "nome": "General Sampaio",
        "municipios_limite": ["General Sampaio"],
        "lat": -4.0511,
        "lon": -39.4542
    },
    {
        "nome": "Gomes",
        "municipios_limite": ["Mauriti"],
        "lat": -7.3886,
        "lon": -38.7708
    },
    {
        "nome": "Guaiúba",
        "municipios_limite": ["Pacatuba"],
        "lat": -4.0397,
        "lon": -38.6372
    },
    {
        "nome": "Itapebussu",
        "municipios_limite": ["Maranguape"],
        "lat": -3.8900,
        "lon": -38.6858
    },
    {
        "nome": "Janguruçu",
        "municipios_limite": ["Fortaleza"],
        "lat": -3.8398474712921966,
        "lon": -38.50824789924127  
    },
    {
        "nome": "Jaibaras - Aires de Sousa",
        "municipios_limite": ["Sobral"],
        "lat": -3.80916,
        "lon": -40.52893
    },
    {
        "nome": "Jenipapeiro",
        "municipios_limite": ["Deputado Irapuan Pinheiro"],
        "lat": -5.813128955872985,
        "lon": -39.24900978865671
    },
    {
        "nome": "Lagoa das Pombas",
        "municipios_limite": ["Aracati"],
        "lat": -4.5617,
        "lon": -37.7697
    },
    {
        "nome": "Lima Campos - Estreito I",
        "municipios_limite": ["Icó"],
        "lat": -6.4011,
        "lon": -38.8553
    },
    {
        "nome": "Mocambinho",
        "municipios_limite": ["Acaraú"],
        "lat": -2.8878,
        "lon": -40.1200
    },
    {
        "nome": "Monsenhor José Cândido",
        "municipios_limite": ["Boa Viagem"],
        "lat": -5.1275,
        "lon": -39.7325
    },
    {
        "nome": "Mulungu",
        "municipios_limite": ["Itapipoca"],
        "lat": -3.4994,
        "lon": -39.5786
    },
    {
        "nome": "Mundaú",
        "municipios_limite": ["Uruburetama"],
        "lat": -3.6231,
        "lon": -39.5106
    },
    {
        "nome": "Nova Floresta",
        "municipios_limite": ["Jaguaribe"],
        "lat": -5.8906,
        "lon": -38.6219
    },
    {
        "nome": "Orós - Pres. Juscelino Kubitschek",
        "municipios_limite": ["Orós"],
        "lat": -6.2388,
        "lon": -38.9250
    },
    {
        "nome": "Riachão",
        "municipios_limite": ["Pacatuba"],
        "lat": -4.2258,
        "lon": -38.6200
    },
    {
        "nome": "Parazinho",
        "municipios_limite": ["Granja"],
        "lat": -3.1200,
        "lon": -40.8261
    },
    {
        "nome": "Patos",
        "municipios_limite": ["Sobral"],
        "lat": -3.78301,
        "lon": -40.03282
    },
    {
        "nome": "Patu",
        "municipios_limite": ["Senador Pompeu"],
        "lat": -5.5825,
        "lon": -39.3714
    },
    {
        "nome": "Pedra Branca (Vinícius Berredo)",
        "municipios_limite": ["Pedra Branca"],
        "lat": -5.4536,
        "lon": -39.7169
    },
    {
        "nome": "Pentecoste - Pereira de Miranda",
        "municipios_limite": ["Pentecoste"],
        "lat": -3.7928,
        "lon": -39.2700
    },
    {
        "nome": "Poço da Pedra",
        "municipios_limite": ["Campos Sales"],
        "lat": -7.0742,
        "lon": -40.3756
    },
    {
        "nome": "Poço do Barro",
        "municipios_limite": ["Morada Nova"],
        "lat": -5.1067,
        "lon": -38.3725
    },
    {
        "nome": "Poço Salgado",
        "municipios_limite": ["Sobral"],
        "lat": -3.6867,
        "lon": -40.3483
    },
    {
        "nome": "Prazeres",
        "municipios_limite": ["Barro"],
        "lat": -7.1767,
        "lon": -38.7814
    },
    {
        "nome": "Premuoca",
        "municipios_limite": ["Uruoca"],
        "lat": -3.1497,
        "lon": -40.5556
    },
    {
        "nome": "Quinquê",
        "municipios_limite": ["Acopiara"],
        "lat": -6.0950,
        "lon": -39.4522
    },
    {
        "nome": "Quixabinha",
        "municipios_limite": ["Mauriti"],
        "lat": -7.3886,
        "lon": -38.7708
    },
    {
        "nome": "Quixeramobim",
        "municipios_limite": ["Quixeramobim"],
        "lat": -5.2000,
        "lon": -39.2900
    },
    {
        "nome": "Rajada",
        "municipios_limite": ["Itapipoca"],
        "lat": -3.4994,
        "lon": -39.5786
    },
    {
        "nome": "Realejo",
        "municipios_limite": ["Crateús"],
        "lat": -5.1783,
        "lon": -40.6775
    },
    {
        "nome": "Riachinho",
        "municipios_limite": ["Granja"],
        "lat": -3.1200,
        "lon": -40.8261
    },
    {
        "nome": "Riacho dos Carneiros (Manoel Balbino)",
        "municipios_limite": ["Caririaçu"],
        "lat": -7.10162485646937,
        "lon": -39.32893639867845
    },
    {
        "nome": "Riacho do Sangue",
        "municipios_limite": ["Solonópole"],
        "lat": -5.7306,
        "lon": -39.0072
    },
    {
        "nome": "Salão",
        "municipios_limite": ["Canindé"],
        "lat": -4.3586,
        "lon": -39.3111
    },
    {
        "nome": "Santa Maria do Aracatiaçu",
        "municipios_limite": ["Sobral"],
        "lat": -3.8617,
        "lon": -39.9806
    },
    {
        "nome": "Santo Antonio de Aracatiaçu",
        "municipios_limite": ["Sobral"],
        "lat": -3.9000,
        "lon": -40.0000
    },
    {
        "nome": "Santo Antonio de Russas",
        "municipios_limite": ["Russas"],
        "lat": -4.853000639256018,
        "lon": -38.17011568767755
    },
    {
        "nome": "São Francisco",
        "municipios_limite": ["Itapajé"],
        "lat": -3.6883,
        "lon": -39.5864
    },
    {
        "nome": "São Gabriel",
        "municipios_limite": ["Irauçuba"],
        "lat": -3.7464,
        "lon": -39.7831
    },
    {
        "nome": "São Mateus",
        "municipios_limite": ["Canindé"],
        "lat": -4.3586,
        "lon": -39.3111
    },
    {
        "nome": "São Miguel",
        "municipios_limite": ["Itapajé"],
        "lat": -3.6883,
        "lon": -39.5864
    },
    {
        "nome": "São Pedro da Timbaúba",
        "municipios_limite": ["Miraíma"],
        "lat": -3.5689,
        "lon": -39.9700
    },
    {
        "nome": "São Vicente",
        "municipios_limite": ["Santana do Acaraú"],
        "lat": -3.4614,
        "lon": -40.2125
    },
    {
        "nome": "Serafim Dias",
        "municipios_limite": ["Mombaça"],
        "lat": -5.7425,
        "lon": -39.6267
    },
    {
        "nome": "Serrota - Sebastião de Abreu",
        "municipios_limite": ["Pentecoste"],
        "lat": -3.7928,
        "lon": -39.2700
    },
    {
        "nome": "Serrote - Edson Queiroz",
        "municipios_limite": ["Santa Quitéria"],
        "lat": -4.0517,
        "lon": -40.1528
    },
    {
        "nome": "Açude Cachoeiro - Sobral",
        "municipios_limite": ["Sobral"],
        "lat": -3.65285,
        "lon": -40.36597
    },
    {
        "nome": "Taquara",
        "municipios_limite": ["Cariré", "Pacujá"],
        "lat": -3.4614,
        "lon": -40.2125
    },
    {
        "nome": "Tejussuoca",
        "municipios_limite": ["Tejuçuoca"],
        "lat": -3.9883,
        "lon": -39.5806
    },
    {
        "nome": "Trici",
        "municipios_limite": ["Tauá"],
        "lat": -5.914705734718784,
        "lon": -40.41467489603963
    },
    {
        "nome": "Trussu - Roberto Costa",
        "municipios_limite": ["Iguatu"],
        "lat": -6.2867,
        "lon": -39.4647
    },
    {
        "nome": "Tucunduba",
        "municipios_limite": ["Senador Sá"],
        "lat": -3.3539,
        "lon": -40.4664
    },
    {
        "nome": "Umari - Thomaz Osterne",
        "municipios_limite": ["Crato"],
        "lat": -7.098983523388175,
        "lon": -39.48705914213407
    },
    {
        "nome": "Várzea da Volta",
        "municipios_limite": ["Moraújo"],
        "lat": -3.4631,
        "lon": -40.6806
    },
    {
        "nome": "Varzea do Boi",
        "municipios_limite": ["Tauá"],
        "lat": -5.9043779741567315,
        "lon": -40.254155490428516
    }
]


# Isso transforma as informações de latitude e longitude em ponto geométricos

if __name__ == "__main__":
    # Salva como JSON simples
    with open("acudes_ceara.json", "w", encoding="utf-8") as f:
        json.dump(acudes_ceara, f, ensure_ascii=False, indent=2)

    # Gera GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for acude in acudes_ceara:
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

    with open("acudes_ceara.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"Arquivos gerados: acudes_ceara.json e acudes_ceara.geojson")
    print(f"Total de açudes com coordenadas: {len(geojson['features'])}")