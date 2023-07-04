# For non-unique stop names store also ref of stop before it
from typing import Tuple, Dict

lastStopRefAfter: Dict[Tuple[str, str], str] = {
    ("11 Listopada", "198001"): "1848",
    ("Brzeziny", "117502"): "1176",
    ("Brzeziny", "238402"): "2431",
    ("Długa", "344901"): "3449",
    ("Fabryczna", "154601"): "1352",
    ("Fabryczna", "197701"): "1352",
    ("Głowackiego", "145502"): "1999",
    ("Jasna", "344902"): "3176",
    ("Leszno", "616501"): "6166",
    ("Leszno", "682402"): "6166",
    ("Maczka", "147501"): "1474",
    ("Maczka", "147302"): "1474",
    ("Mickiewicza", "119202"): "1193",
    ("Nowa", "170201"): "1998",
    ("Orla", "235802"): "2358",
    ("Orla", "223902"): "2358",
    ("Orla", "246852"): "2358",
    ("Parkowa", "513301"): "5134",
    ("Pańska", "310101"): "3177",
    ("Rynek", "336901"): "3368",
    ("Rynek", "345501"): "3368",
    ("Rynek", "377202"): "3368",
    ("Rynek", "347401"): "3368",
    ("Rynek", "611402"): "6115",
    ("Rynek", "336801"): "3368",
    ("Rynek", "611501"): "6115",
    ("Stare Miasto", "236001"): "2870",
    ("Szpital", "398301"): "3951",
    ("Szpital Powiatowy", "174802"): "1700",
    ("Urząd Gminy", "236701"): "2325",
    ("Urząd Gminy", "389301"): "3894",
    ("Urząd Miasta", "188102"): "1882",
    ("Urząd Miasta", "195202"): "1882",
    ("Wiejska", "182602"): "1827",
}

lastStopRefs: Dict[str, str] = {
    "11 Listopada": "1076",
    "AGRICOOP": "5138",
    "Aleksandrów": "2222",
    "Annopol": "1087",
    "Augustów": "1558",
    "Banacha": "4108",
    "Baniocha-Centrum": "3769",
    "Bielańska": "7101",
    "Bielawa-Pętla": "3843",
    "Bitwy Warszawskiej 1920 r.": "4005",
    "Błota": "2057",
    "Bobrowiec": "3840",
    "Boernerowo": "5056",
    "Bokserska": "3267",
    "Branickiego": "3385",
    "Bródno-Podgrodzie": "1152",
    "Browarna": "7100",
    "Centrum": "7013",
    "Centrum Onkologii": "3134",
    "CH Blue City": "4027",
    "Chełmska": "3059",
    "CH Łomianki": "6222",
    "Chlubna": "1483",
    "CH Marki": "1234",
    "Chomiczówka": "6048",
    "Choszczówka": "1116",
    "Chotomów": "1306",
    "CH Reduta": "4126",
    "Chrzanów": "5201",
    "CH Stara Papiernia": "3185",
    "CH Targówek": "1179",
    "CH Ursynów": "3292",
    "Cmentarz Marki": "1544",
    "Cm.Północny-Brama Gł.": "6069",
    "Cm.Północny-Brama Zach.": "6100",
    "Cm.Południowy-Brama Płd.": "3327",
    "Cm.Wolski": "5011",
    "Coopera": "5208",
    "Cybulice Duże": "6680",
    "Czarna Struga": "1244",
    "Czarnów": "3860",
    "Czarny Las": "3784",
    "Czynszowa": "1069",
    "Dąbrowa Zachodnia": "6219",
    "Dąbrówka Wiślana": "1317",
    "Dawidy": "3407",
    "Dębina": "6657",
    "Domaniewska Office Park": "3411",
    "Dw.Centralny": "7002",
    "Dw.Gdański (Rydygiera)": "6212",
    "Dworkowa": "3003",
    "Dw.Wschodni (Kijowska)": "1028",
    "Dw.Wschodni (Lubelska)": "2120",
    "Dw.Zachodni": "4044",
    "Dw.Zachodni (Tunelowa)": "5121",
    "Dziekanówek": "6660",
    "Dziekanów Leśny": "6168",
    "EC Siekierki": "3079",
    "Elsnerów": "1051",
    "Emilii Plater": "7001",
    "Esperanto": "5157",
    "Falenica": "2052",
    "Fieldorfa": "2255",
    "Fort Radiowo": "5162",
    "Fort Wawrzyszew": "6191",
    "Gassy-Pętla": "3854",
    "Gerbera": "3340",
    "Gilarska": "1215",
    "Głosków-Szkoła": "3218",
    "Gocław": "2148",
    "Gocławek": "2014",
    "Gocławek Wschodni": "2259",
    "Grochowa": "3950",
    "Grodzisk": "1182",
    "Groty": "5083",
    "Gwiaździsta": "6082",
    "Hoserów": "3158",
    "Instalatorów": "4106",
    "Jastrzębiec": "4816",
    "Julianowska-Cmentarz": "3795",
    "Juranda ze Spychowa-szkoła": "1353",
    "Kabaty-STP": "3336",
    "Kamionek": "2477",
    "Kampinos": "6817",
    "Karolin": "5092",
    "Kawęczyńska-Bazylika": "1031",
    "Kazimierzowska": "3865",
    "Kąck": "2875",
    "Kępa Okrzewska-Cmentarz": "3313",
    "Kępa Tarchomińska": "1944",
    "Kępa Zawadowska": "3159",
    "Kielecka": "3118",
    "Klarysew": "3188",
    "Klaudyn": "6112",
    "Koczargi Stare": "6152",
    "Kolejowa": "5120",
    "Koło": "5073",
    "Komornica-Szkoła": "1819",
    "Konwiktorska": "7052",
    "Kosów": "4266",
    "Krasnowola": "3419",
    "Królikarnia": "3007",
    "Książęca": "7069",
    "Lazurowa": "5192",
    "Lewinów": "1064",
    "Łomżyńska": "2841",
    "Majdan": "1744",
    "Małe Siekierki": "3323",
    "Marcelin": "1097",
    "Mariensztat": "7059",
    "Mariew": "6175",
    "Marymont-Potok": "6077",
    "Marysin": "2064",
    "Metro Bemowo": "5034",
    "Metro Bródno": "1085",
    "Metro Kondratowicza": "1146",
    "Metro Księcia Janusza": "5030",
    "Metro Marymont": "6005",
    "Metro Młociny": "6059",
    "Metro Politechnika": "7006",
    "Metro Ratusz-Arsenał": "7099",
    "Metro Słodowiec": "6006",
    "Metro Służew": "3279",
    "Metro Stadion Narodowy": "1231",
    "Metro Stokłosy": "3132",
    "Metro Trocka": "1140",
    "Metro Wierzbno": "3114",
    "Metro Wilanowska": "3009",
    "Michałówek": "2860",
    "Międzylesie": "2032",
    "Młochów": "4293",
    "Młociny-UKSW": "6145",
    "Młynów": "5067",
    "Mysiadło": "3160",
    "Natolin Płn.": "3142",
    "Nowe Bemowo": "5161",
    "Nowe Włochy": "4224",
    "Nowe Załubice": "1444",
    "Nowodwory": "1253",
    "Nowowiejska": "7090",
    "Ogińskiego": "4235",
    "Ogród Botaniczny": "3305",
    "Olecka": "2158",
    "Olesin": "1295",
    "Olszewnica Stara": "1841",
    "Opolska": "1694",
    "os.Derby": "1359",
    "os.Górczewska": "5050",
    "os.Kabaty": "3400",
    "os.Młodych": "1208",
    "os.Nowy Mokotów": "3409",
    "Osmańska-DHL": "3342",
    "Ostroroga": "5124",
    "os.Niepodległości": "1393",
    "Os.Radiówek": "2872",
    "Os.Staszica/Pętla": "4195",
    "os.Victoria": "1458",
    "Ośrodek Szkoleniowy": "2195",
    "Otwock": "2918",
    "Palmiry": "6401",
    "Palmiry-Muzeum": "6400",
    "Paluch": "4026",
    "Park Postępu": "3412",
    "Pastuszków": "2420",
    "Piaseczno": "3905",
    "Piaski": "6045",
    "Pieczyska": "3954",
    "Pilaszków": "5180",
    "Pilcha": "6629",
    "Pileckiego": "3333",
    "PKP Dąbkowizna": "1868",
    "PKP Gołąbki": "4149",
    "PKP Halinów": "2312",
    "PKP Jeziorki": "3025",
    "PKP Józefów": "2353",
    "PKP Koło": "5069",
    "PKP Legionowo": "1800",
    "PKP Legionowo Przystanek": "1197",
    "PKP Międzylesie": "2039",
    "PKP Mokry Ług": "2220",
    "PKP Olszynka Grochowska": "2108",
    "PKP Piaseczno": "3169",
    "PKP Służewiec": "3254",
    "PKP Sulejówek Miłosna": "2435",
    "PKP Ursus": "4217",
    "PKP Ursus-Niedźwiadek": "4342",
    "PKP Wesoła": "2344",
    "PKP Wołomin": "1743",
    "PKP Zacisze-Wilno": "1482",
    "PKP Zagościniec": "1772",
    "PKP Zalesie Górne": "3842",
    "pl.Bankowy": "7016",
    "pl.Hallera": "1005",
    "pl.Jana Pawła II": "1345",
    "pl.Konstytucji": "7011",
    "pl.Narutowicza": "4003",
    "pl.Niemena": "6221",
    "pl.Piłsudskiego": "7027",
    "pl.Szwedzki": "4064",
    "pl.Wilsona": "6003",
    "pl.Wolności": "1513",
    "Podolszyn": "4176",
    "POD Szczaki": "4078",
    "Podwójna": "1557",
    "Poetów": "1025",
    "Pomnik Lotnika": "4029",
    "Popularna": "4048",
    "Powsin-Park Kultury": "3056",
    "P+R Al.Krakowska": "4015",
    "P+R Nadarzyn": "4349",
    "Pruszków": "4905",
    "Przekorna": "3050",
    "Pustelnik": "1240",
    "Radzymin": "1915",
    "Rakowiecka-Sanktuarium": "3286",
    "Rechniewskiego": "2502",
    "Reduta Wolska": "5009",
    "Regulska": "4130",
    "Rembertów-Akademia": "2088",
    "Rembertów-Kolonia": "2086",
    "Rembertów-Strzelnica": "2451",
    "rondo Daszyńskiego": "5040",
    "rondo ONZ": "7088",
    'rondo "Radosława"': "7091",
    "rondo Starzyńskiego": "1006",
    "rondo Żaba": "1077",
    "Rubinowa": "3476",
    "Rynia": "1365",
    "Rzakta": "2394",
    "Sadyba": "3065",
    "Sarmacka": "3391",
    "Sasanki": "4037",
    "Siekierki-Sanktuarium": "3308",
    "Słomczyn-Szkoła": "3358",
    "Sieraków": "6139",
    "Skibińskiego": "6116",
    "Skolimów": "3179",
    "Skorosze": "4284",
    "Smugowa": "1098",
    "Sokola": "1962",
    "Spartańska": "3256",
    "Stara Miłosna (Graniczna)": "2440",
    "Stara Miłosna (Ułańska)": "2275",
    "Stare Bemowo": "5055",
    "Stare Grabie": "1775",
    "Starostwo": "5129",
    "Starostwo Powiatowe": "1379",
    "Starorzecze": "1693",
    "Stegny": "3094",
    "Strusia": "2261",
    "Strzykuły": "5801",
    "Sulejówek Miłosna": "2914",
    "Sulejówek Miłosna-Pomnik": "2436",
    "Szczęśliwice": "4119",
    "Śniegockiej": "7070",
    "Świderska": "1469",
    "Tarchomin": "1277",
    "Targowisko": "3464",
    "Terminal Autokarowy": "4202",
    "Torwar": "7076",
    "Turów": "1400",
    "Ursus-Niedźwiadek": "4221",
    "Ursus-Ratusz": "4216",
    "Ursynów Płd.": "3136",
    "Ursynów Płn.": "3120",
    "Utrata": "1043",
    "Waflowa": "3051",
    "Warszawa Al.Jerozolimskie": "4913",
    "Warszawa Gdańska": "7903",
    "Warszawa Główna": "5909",
    "Warszawa Lotnisko Chopina": "4919",
    "Warszawa Stadion": "2901",
    "Warszawa Zachodnia (Peron 9)": "5902",
    "Warsztatowa": "2868",
    "Wiatraczna": "2008",
    "Wieliszew": "1910",
    "Wieliszew-Plaża": "1815",
    "Wiertnicza": "3066",
    "Wilanów": "3044",
    "Winnica": "1947",
    "Wiśniowa Góra": "2034",
    "Witolin": "2105",
    "WKD Raków": "4089",
    "Władysławów": "4135",
    "Wola Grzybowska": "2285",
    "Wolica k.Płochocina": "5169",
    "Wyczółki": "3104",
    "Wynalazek": "3251",
    "Wyścigi": "3012",
    "Zaborów-Szkoła": "6160",
    "Zajezdnia Woronicza": "3258",
    "Zajezdnia Żoliborz": "6061",
    "Zaułek-Szkoła": "1470",
    "Zbójna Góra": "2184",
    "Zdziarska-Kanał": "1225",
    "Zegrze Płd.": "1323",
    "Zegrze Południowe": "1930",
    "Żerań FSO": "1013",
    "Żerań Wschodni": "1091",
    "Zgoda": "3701",
    "Zielona": "2379",
    "Złotokłos": "4080",
    "Znana": "5104",
}
