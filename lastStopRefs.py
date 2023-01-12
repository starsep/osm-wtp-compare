# For non-unique stop names store also ref of stop before it
from typing import Tuple, Dict

lastStopRefAfter: Dict[Tuple[str, str], str] = {
    ("11 Listopada 01", "198001"): "184801",
    ("Brzeziny 01", "117502"): "117601",
    ("Brzeziny 01", "238402"): "243101",
    ("Długa 02", "344901"): "344902",
    ("Głowackiego 01", "145502"): "199901",
    ("Jasna 02", "344902"): "317602",
    ("Leszno 02", "616501"): "616602",
    ("Leszno 02", "682402"): "616602",
    ("Maczka 03", "147501"): "147403",
    ("Maczka 04", "147302"): "147404",
    ("Mickiewicza 01", "119202"): "119301",
    ("Nowa 01", "170201"): "199801",
    ("Orla 01", "235802"): "235801",
    ("Orla 02", "223902"): "235802",
    ("Parkowa 02", "513301"): "513402",
    ("Pańska 01", "310101"): "317701",
    ("Rynek 01", "336901"): "336801",
    ("Rynek 01", "345501"): "336801",
    ("Rynek 01", "377202"): "336801",
    ("Rynek 01", "347401"): "336801",
    ("Rynek 01", "611402"): "611501",
    ("Rynek 02", "336801"): "336802",
    ("Rynek 02", "611501"): "611502",
    ("Stare Miasto 01", "236001"): "287001",
    ("Szpital 02", "398301"): "395102",
    ("Szpital Powiatowy 02", "174802"): "170002",
    ("Urząd Gminy 01", "236701"): "232501",
    ("Urząd Gminy 02", "389301"): "389402",
    ("Urząd Miasta 01", "188102"): "188201",
    ("Urząd Miasta 01", "195202"): "188201",
    ("Wiejska 01", "182602"): "182701",
}

lastStopRefs: Dict[str, str] = {
    "11 Listopada 01": "107601",
    "AGRICOOP 01": "513801",
    "Aleksandrów 01": "222201",
    "Annopol 01": "108701",
    "Annopol 02": "108702",
    "Annopol 03": "108703",
    "Augustów 02": "155802",
    "Banacha 04": "410804",
    "Banacha 05": "410805",
    "Banacha 06": "410806",
    "Baniocha-Centrum 02": "376902",
    "Bielańska 01": "710101",
    "Bielawa-Pętla 01": "384301",
    "Bitwy Warszawskiej 1920 r. 10": "400510",
    "Błota 03": "205703",
    "Boernerowo 01": "505601",
    "Bokserska 04": "326704",
    "Branickiego 03": "338503",
    "Bródno-Podgrodzie 04": "115204",
    "Bródno-Podgrodzie 05": "115205",
    "Bródno-Podgrodzie 06": "115206",
    "Bródno-Podgrodzie 07": "115207",
    "Bródno-Podgrodzie 08": "115208",
    "Browarna 02": "710002",
    "Centrum 03": "701303",
    "Centrum Onkologii 03": "313403",
    "CH Blue City 01": "402701",
    "CH Blue City 02": "402702",
    "Chełmska 04": "305904",
    "CH Łomianki 03": "622203",
    "Chlubna 02": "148302",
    "CH Marki 01": "123401",
    "CH Marki 02": "123402",
    "CH Marki 04": "123404",
    "Chomiczówka 03": "604803",
    "Chomiczówka 05": "604805",
    "Chomiczówka 06": "604806",
    "Choszczówka 01": "111601",
    "Chotomów 01": "130601",
    "CH Reduta 02": "412602",
    "Chrzanów 04": "520104",
    "CH Stara Papiernia 01": "318501",
    "CH Targówek 05": "117905",
    "CH Ursynów 04": "329204",
    "Cmentarz Marki 01": "154401",
    "Cm.Północny-Brama Gł. 03": "606903",
    "Cm.Północny-Brama Zach. 01": "610001",
    "Cm.Północny-Brama Zach. 02": "610002",
    "Cm.Południowy-Brama Płd. 01": "332701",
    "Cm.Wolski 03": "501103",
    "Cm.Wolski 04": "501104",
    "Cm.Wolski 06": "501106",
    "Cm.Wolski 07": "501107",
    "Cm.Wolski 08": "501108",
    "Cybulice Duże 02": "668002",
    "Czarna Struga 01": "124401",
    "Czarnów 01": "386001",
    "Czarny Las 01": "378401",
    "Czynszowa 01": "106901",
    "Dąbrowa Zachodnia 01": "621901",
    "Dąbrówka Wiślana 01": "131701",
    "Dąbrówka Wiślana 02": "131702",
    "Dawidy 03": "340703",
    "Dębina 01": "665701",
    "Domaniewska Office Park 01": "341101",
    "Dw.Centralny 11": "700211",
    "Dw.Centralny 14": "700214",
    "Dw.Centralny 16": "700216",
    "Dw.Centralny 21": "700221",
    "Dw.Centralny 23": "700223",
    "Dw.Centralny 25": "700225",
    "Dw.Centralny 27": "700227",
    "Dw.Centralny 29": "700229",
    "Dw.Centralny 30": "700230",
    "Dw.Gdański (Rydygiera) 01": "621201",
    "Dworkowa 06": "300306",
    "Dw.Wschodni (Kijowska) 02": "102802",
    "Dw.Wschodni (Kijowska) 05": "102805",
    "Dw.Wschodni (Kijowska) 06": "102806",
    "Dw.Wschodni (Kijowska) 07": "102807",
    "Dw.Wschodni (Kijowska) 13": "102813",
    "Dw.Wschodni (Lubelska) 01": "212001",
    "Dw.Wschodni (Lubelska) 04": "212004",
    "Dw.Wschodni (Lubelska) 06": "212006",
    "Dw.Zachodni 02": "404402",
    "Dw.Zachodni 03": "404403",
    "Dw.Zachodni 06": "404406",
    "Dziekanów Leśny 01": "616801",
    "EC Siekierki 03": "307903",
    "EC Siekierki 04": "307904",
    "EC Siekierki 05": "307905",
    "Elsnerów 01": "105101",
    "Emilii Plater 01": "700101",
    "Emilii Plater 05": "700105",
    "Esperanto 03": "515703",
    "Esperanto 05": "515705",
    "Fabryczna 02": "229402",
    "Falenica 03": "205203",
    "Falenica 04": "205204",
    "Fort Radiowo 01": "516201",
    "Fort Wawrzyszew 01": "619101",
    "Gassy-Pętla 01": "385401",
    "Gerbera 02": "334002",
    "Gilarska 04": "121504",
    "Głosków-Szkoła 01": "321801",
    "Gocław 01": "214801",
    "Gocław 02": "214802",
    "Gocław 03": "214803",
    "Gocław 04": "214804",
    "Gocław 05": "214805",
    "Gocławek 06": "201406",
    "Gocławek Wschodni 02": "225902",
    "Grochowa 01": "395001",
    "Grodzisk 04": "118204",
    "Grodzisk 06": "118206",
    "Groty 01": "508301",
    "Gwiaździsta 02": "608202",
    "Gwiaździsta 05": "608205",
    "Gwiaździsta 06": "608206",
    "Jastrzębiec 01": "481601",
    "Julianowska-Cmentarz 01": "379501",
    "Juranda ze Spychowa-szkoła 04": "135304",
    "Kabaty-STP 01": "333601",
    "Kamionek 02": "247702",
    "Kampinos 01": "681701",
    "Karolin 03": "509203",
    "Kawęczyńska-Bazylika 02": "103102",
    "Kawęczyńska-Bazylika 03": "103103",
    "Kazimierzowska 02": "386502",
    "Kąck 01": "287501",
    "Kępa Okrzewska-Cmentarz 01": "331301",
    "Kępa Tarchomińska 01": "194401",
    "Kępa Zawadowska 01": "315901",
    "Kielecka 01": "311801",
    "Klarysew 03": "318803",
    "Koczargi Stare 02": "615202",
    "Kolejowa 51": "512051",
    "Koło 03": "507303",
    "Koło 05": "507305",
    "Komornica-Szkoła 01": "181901",
    "Konwiktorska 03": "705203",
    "Konwiktorska 04": "705204",
    "Kosów 01": "426601",
    "Krasnowola 51": "341951",
    "Królikarnia 02": "300702",
    "Książęca 02": "706902",
    "Lazurowa 04": "519204",
    "Lewinów 03": "106403",
    "Łomżyńska 01": "284101",
    "Majdan 02": "174402",
    "Małe Siekierki 01": "332301",
    "Marcelin 05": "109705",
    "Mariensztat 01": "705901",
    "Mariensztat 02": "705902",
    "Mariew 01": "617501",
    "Marymont-Potok 04": "607704",
    "Marysin 03": "206403",
    "Marysin 04": "206404",
    "Metro Bemowo 01": "503401",
    "Metro Bemowo 03": "503403",
    "Metro Bródno 11": "108511",
    "Metro Bródno 13": "108513",
    "Metro Bródno 14": "108514",
    "Metro Kondratowicza 03": "114603",
    "Metro Księcia Janusza 06": "503006",
    "Metro Marymont 04": "600504",
    "Metro Marymont 11": "600511",
    "Metro Marymont 12": "600512",
    "Metro Marymont 13": "600513",
    "Metro Marymont 14": "600514",
    "Metro Marymont 16": "600516",
    "Metro Marymont 17": "600517",
    "Metro Młociny 03": "605903",
    "Metro Młociny 09": "605909",
    "Metro Młociny 14": "605914",
    "Metro Młociny 15": "605915",
    "Metro Młociny 17": "605917",
    "Metro Młociny 18": "605918",
    "Metro Młociny 19": "605919",
    "Metro Młociny 21": "605921",
    "Metro Młociny 22": "605922",
    "Metro Młociny 23": "605923",
    "Metro Młociny 24": "605924",
    "Metro Młociny 28": "605928",
    "Metro Politechnika 12": "700612",
    "Metro Politechnika 14": "700614",
    "Metro Ratusz-Arsenał 02": "709902",
    "Metro Słodowiec 01": "600601",
    "Metro Służew 03": "327903",
    "Metro Służew 04": "327904",
    "Metro Stadion Narodowy 02": "123102",
    "Metro Stadion Narodowy 03": "123103",
    "Metro Stadion Narodowy 07": "123107",
    "Metro Stokłosy 04": "313204",
    "Metro Trocka 07": "114007",
    "Metro Trocka 08": "114008",
    "Metro Trocka 09": "114009",
    "Metro Trocka 12": "114012",
    "Metro Trocka 13": "114013",
    "Metro Wierzbno 05": "311405",
    "Metro Wilanowska 09": "300909",
    "Metro Wilanowska 10": "300910",
    "Metro Wilanowska 11": "300911",
    "Metro Wilanowska 12": "300912",
    "Metro Wilanowska 14": "300914",
    "Michałówek 01": "286001",
    "Międzylesie 01": "203201",
    "Międzylesie 02": "203202",
    "Międzylesie 04": "203204",
    "Młochów 01": "429301",
    "Młociny-UKSW 01": "614501",
    "Młynów 07": "506707",
    "Mysiadło 04": "316004",
    "Natolin Płn. 04": "314204",
    "Natolin Płn. 08": "314208",
    "Natolin Płn. 22": "314222",
    "Nowe Bemowo 03": "516103",
    "Nowe Bemowo 06": "516106",
    "Nowe Bemowo 10": "516110",
    "Nowe Bemowo 12": "516112",
    "Nowe Bemowo 15": "516115",
    "Nowe Włochy 01": "422401",
    "Nowe Załubice 01": "144401",
    "Nowodwory 01": "125301",
    "Nowodwory 07": "125307",
    "Nowodwory 08": "125308",
    "Nowodwory 09": "125309",
    "Nowowiejska 02": "709002",
    "Ogińskiego 02": "423502",
    "Ogród Botaniczny 03": "330503",
    "Olecka 01": "215801",
    "Olesin 01": "129501",
    "Olszewnica Stara 01": "184101",
    "os.Derby 02": "135902",
    "os.Górczewska 05": "505005",
    "os.Górczewska 06": "505006",
    "os.Górczewska 07": "505007",
    "os.Górczewska 08": "505008",
    "os.Górczewska 09": "505009",
    "os.Górczewska 12": "505012",
    "os.Górczewska 14": "505014",
    "os.Kabaty 01": "340001",
    "os.Kabaty 02": "340002",
    "os.Kabaty 03": "340003",
    "os.Kabaty 04": "340004",
    "os.Kabaty 05": "340005",
    "os.Kabaty 06": "340006",
    "Osmańska-DHL 01": "334201",
    "os.Niepodległości 01": "139301",
    "Os.Radiówek 01": "287201",
    "Os.Staszica/Pętla 01": "419501",
    "os.Victoria 02": "145802",
    "Otwock 03": "291803",
    "Palmiry 02": "640102",
    "Paluch 01": "402601",
    "Park Postępu 02": "341202",
    "Pastuszków 01": "242001",
    "Piaski 04": "604504",
    "Pieczyska 01": "395401",
    "Pilaszków 51": "518051",
    "PKP Dąbkowizna 01": "186801",
    "PKP Gołąbki 01": "414901",
    "PKP Halinów 01": "231201",
    "PKP Jeziorki 04": "302504",
    "PKP Józefów 03": "235303",
    "PKP Legionowo 01": "180001",
    "PKP Legionowo Przystanek 01": "119701",
    "PKP Międzylesie 04": "203904",
    "PKP Mokry Ług 02": "222002",
    "PKP Mokry Ług 03": "222003",
    "PKP Olszynka Grochowska 05": "210805",
    "PKP Piaseczno 04": "316904",
    "PKP Piaseczno 05": "316905",
    "PKP Piaseczno 07": "316907",
    "PKP Służewiec 12": "325412",
    "PKP Służewiec 13": "325413",
    "PKP Służewiec 14": "325414",
    "PKP Sulejówek Miłosna 03": "243503",
    "PKP Ursus 21": "421721",
    "PKP Ursus-Niedźwiadek 04": "434204",
    "PKP Wesoła 01": "234401",
    "PKP Wołomin 01": "174301",
    "PKP Zacisze-Wilno 02": "148202",
    "PKP Zacisze-Wilno 04": "148204",
    "PKP Zagościniec 01": "177201",
    "PKP Zalesie Górne 01": "384201",
    "pl.Bankowy 02": "701602",
    "pl.Hallera 09": "100509",
    "pl.Hallera 11": "100511",
    "pl.Hallera 18": "100518",
    "pl.Jana Pawła II 01": "134501",
    "pl.Narutowicza 13": "400313",
    "pl.Narutowicza 16": "400316",
    "pl.Niemena 02": "622102",
    "pl.Piłsudskiego 02": "702702",
    "pl.Szwedzki 01": "406401",
    "pl.Wilsona 18": "600318",
    "pl.Wolności 01": "151301",
    "Podolszyn 01": "417601",
    "POD Szczaki 04": "407804",
    "Podwójna 02": "155702",
    "Poetów 02": "102502",
    "Pomnik Lotnika 03": "402903",
    "Popularna 01": "404801",
    "Powsin-Park Kultury 01": "305601",
    "P+R Al.Krakowska 01": "401501",
    "P+R Al.Krakowska 02": "401502",
    "P+R Al.Krakowska 03": "401503",
    "P+R Al.Krakowska 07": "401507",
    "P+R Al.Krakowska 09": "401509",
    "P+R Al.Krakowska 10": "401510",
    "P+R Al.Krakowska 11": "401511",
    "P+R Al.Krakowska 12": "401512",
    "P+R Al.Krakowska 13": "401513",
    "P+R Al.Krakowska 14": "401514",
    "P+R Al.Krakowska 15": "401515",
    "P+R Al.Krakowska 16": "401516",
    "P+R Nadarzyn 01": "434901",
    "Pruszków 02": "490502",
    "Przekorna 02": "305002",
    "Pustelnik 03": "124003",
    "Radzymin 01": "191501",
    "Rakowiecka-Sanktuarium 06": "328606",
    "Rechniewskiego 02": "250202",
    "Regulska 02": "413002",
    "Rembertów-Akademia 01": "208801",
    "Rembertów-Kolonia 01": "208601",
    "Rembertów-Kolonia 02": "208602",
    "Rembertów-Kolonia 03": "208603",
    "Rembertów-Strzelnica 01": "245101",
    "rondo Daszyńskiego 02": "504002",
    "rondo Daszyńskiego 89": "504089",
    "rondo ONZ 10": "708810",
    'rondo "Radosława" 04': "709104",
    "rondo Starzyńskiego 09": "100609",
    "Rubinowa 02": "347602",
    "Rynia 01": "136501",
    "Rzakta 01": "239401",
    "Sadyba 03": "306503",
    "Sadyba 05": "306505",
    "Sadyba 06": "306506",
    "Sarmacka 02": "339102",
    "Sasanki 02": "403702",
    "Siekierki-Sanktuarium 03": "330803",
    "Sieraków 01": "613901",
    "Skibińskiego 01": "611601",
    "Skolimów 01": "317901",
    "Skorosze 04": "428404",
    "Sokola 52": "196252",
    "Spartańska 02": "325602",
    "Stara Miłosna (Graniczna) 03": "244003",
    "Stara Miłosna (Graniczna) 05": "244005",
    "Stara Miłosna (Ułańska) 03": "227503",
    "Stara Miłosna (Ułańska) 04": "227504",
    "Stare Bemowo 05": "505505",
    "Stare Bemowo 06": "505506",
    "Stare Bemowo 07": "505507",
    "Stare Grabie 01": "177501",
    "Starostwo 03": "512903",
    "Starostwo Powiatowe 01": "137901",
    "Stegny 03": "309403",
    "Stegny 05": "309405",
    "Stegny 06": "309406",
    "Strusia 01": "226101",
    "Sulejówek Miłosna 01": "291401",
    "Sulejówek Miłosna-Pomnik 01": "243601",
    "Sulejówek Miłosna-Pomnik 02": "243602",
    "Szczęśliwice 01": "411901",
    "Szczęśliwice 02": "411902",
    "Szczęśliwice 03": "411903",
    "Szczęśliwice 04": "411904",
    "Szczęśliwice 05": "411905",
    "Śniegockiej 02": "707002",
    "Tarchomin 07": "127707",
    "Tarchomin 09": "127709",
    "Targowisko 01": "346401",
    "Terminal Autokarowy 01": "420201",
    "Torwar 06": "707606",
    "Torwar 07": "707607",
    "Turów 04": "140004",
    "Ursus-Niedźwiadek 01": "422101",
    "Ursus-Niedźwiadek 02": "422102",
    "Ursus-Ratusz 03": "421603",
    "Ursynów Płd. 05": "313605",
    "Ursynów Płd. 06": "313606",
    "Ursynów Płn. 05": "312005",
    "Ursynów Płn. 06": "312006",
    "Utrata 01": "104301",
    "Waflowa 03": "305103",
    "Warszawa Lotnisko Chopina 02": "491902",
    "Warszawa Stadion 01": "290101",
    "Warszawa Zachodnia (Peron 9) 08": "590208",
    "Warsztatowa 02": "286802",
    "Wiatraczna 12": "200812",
    "Wiatraczna 13": "200813",
    "Wiatraczna 22": "200822",
    "Wiatraczna 23": "200823",
    "Wieliszew-Plaża 01": "181501",
    "Wilanów 02": "304402",
    "Wilanów 03": "304403",
    "Wilanów 04": "304404",
    "Wilanów 05": "304405",
    "Wilanów 06": "304406",
    "Wilanów 07": "304407",
    "Wilanów 08": "304408",
    "Wilanów 12": "304412",
    "Winnica 04": "194704",
    "Winnica 05": "194705",
    "Winnica 06": "194706",
    "Wiśniowa Góra 01": "203401",
    "Witolin 02": "210502",
    "Witolin 03": "210503",
    "WKD Raków 03": "408903",
    "Władysławów 03": "413503",
    "Wola Grzybowska 03": "228503",
    "Wolica k.Płochocina 01": "516901",
    "Wyczółki 01": "310401",
    "Wynalazek 04": "325104",
    "Wyścigi 05": "301205",
    "Wyścigi 06": "301206",
    "Zaborów-Szkoła 02": "616002",
    "Zajezdnia Woronicza 01": "325801",
    "Zajezdnia Żoliborz 02": "606102",
    "Zaułek-Szkoła 02": "147002",
    "Zbójna Góra 01": "218401",
    "Zdziarska-Kanał 03": "122503",
    "Zegrze Płd. 03": "132303",
    "Żerań FSO 05": "101305",
    "Żerań FSO 06": "101306",
    "Żerań FSO 09": "101309",
    "Żerań FSO 10": "101310",
    "Żerań FSO 11": "101311",
    "Żerań FSO 12": "101312",
    "Żerań FSO 14": "101314",
    "Żerań Wschodni 01": "109101",
    "Żerań Wschodni 03": "109103",
    "Żerań Wschodni 04": "109104",
    "Zgoda 01": "370101",
    "Zielona 01": "237901",
    "Złotokłos 02": "408002",
    "Znana 06": "510406",
}
