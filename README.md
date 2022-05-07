# Dashboard Deutschland API

Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.


## Get

**URL:** https://www.dashboard-deutschland.de/api/dashboard/get
	
Die API ermöglicht über diese URL den Zugriff auf alle gültigen Einträge des id-Parameters getrennt nach id-Kategorien (siehe unten, Indikatoren). 


## Indikatoren

**URL:** www.dashboard-deutschland.de/api/tile/indicators
	
Die API ermöglicht über diese URL Zugriff auf unterschiedliche Indikatoren im JSON-Format über einfache GET-requests mit nur einem Parameter (namens *id*). Der Parameter id spezifiziert den gewünschten Indikator. Mögliche Ausprägungen sind im Folgenden nach Kategorien getrennt aufgelistet und in runden Klammern kurz erläutert. Mehrere Semikolon-getrennte Angaben sind möglich. Gesundheitsindikatoren (beginnend mit "ginsy_ges") lassen sich über eine Variation der u.g. id auch nach Regionen von Bundesländern unterteilt anfordern - durch Ergänzung eines Unterstrichs, gefolgt von einer das Bundesland repräsentierenden Zahl (z.B. 9 für Bayern).

**id-Kategorie "Aktuelles im Fokus":**

- data_bruttoinlandsprodukt *(Entwicklung des Bruttoinlandsprodukts)*
- data_preisentwicklung *(Preisentwicklung)*
- data_corona_zuschuesse *(Corona-Zuschüsse)*
- data_ba_arbeitslose_und_stellen *(Arbeitslosigkeit und offene Stellen)*
- tile_1649694802780 *(Nettostromerzeugung)*
- data_aussenhandel *(Außenhandel)*
- ginsy_ges_diag_covid19_7_tage_inzidenz_map_de *(7-Tage-Inzidenz)*
- data_ifo_geschaeftsklima *(ifo Geschäftsklima)*
- defacto_ges_diag_covid19_hospitalizationincidence_map_de *(Covid-19-Hospitalisierungen)*
- ginsy_ges_bev_sterbl_abs_sterbl_de *(Wöchentliche Sterbefallzahlen in Deutschland)*
- tile_1649679768351 *(Füllstand deutscher Erdgasspeicher)*
- data_kfw_sondermassnahme_neu *(KfW-Sonderprogramm)*
- data_aussenhandel_laender *(Außenhandel mit ausgewählten Ländern)*
- tile_1648135639982 *(Kraftstoffpreise an öffentlichen Tankstellen)*


**id-Kategorie "Arbeitsmarkt":**

- data_erwerbstaetige *(Erwerbstätigkeit)*
- data_ba_arbeitslose_und_stellen *(Arbeitslosigkeit und offene Stellen)*
- data_iab_ifo_barometer *(Stimmungsindikatoren Arbeitsmarkt)*
- data_ba_kurzarbeit *(Kurzarbeit)*


**id-Kategorie "Bauen":**

- data_bau_verbesserung_energieeffizienz *(Umsatz mit Maßnahmen zur Verbesserung der Energieeffizienz von Gebäuden)*
- data_bau_auftragseingang *(Auftragseingang im Bauhauptgewerbe)*
- data_bau_kapazitaetsauslastung_bbsr *(Kapazitätsauslastung im Baugewerbe)*
- data_bau_beschaeftigung_vgr *(Beschäftigung im Baugewerbe)*
- data_bau_produktionsindex_baugewerbe *(Produktion im Baugewerbe)*
- data_bau_bauleistungspreise *(Baupreisindizes)*
- data_bau_umsatz_mixmodelle *(Umsatz im Bauhaupt- und Ausbaugewerbe)*


**id-Kategorie "Wohnen":**

- data_woh_energieverbrauch_energietraeger *(Energieverbrauch für Wohnen nach Energieträgern)*
- data_woh_preise_immobilien_hpi_wohnungen *(Preisindex für Eigentumswohnungen nach Kreistypen)*
- data_woh_nettokaltmiete *(Verbraucherpreisindex für Nettokaltmiete nach Kreistypen)*
- data_woh_bruttokaltmiete *(Verbraucherpreisindex für Nettokaltmiete, Wohnungsnebenkosten und Haushaltsenergie)*
- data_woh_preise_immobilien_hpi_haueser *(Preisindex für Ein- und Zweifamilienhäuser nach Kreistypen)*
- data_woh_energieverbrauch_anwendung *(Energieverbrauch für Wohnen nach Anwendungsbereichen)*
- data_woh_baugenehmigungen_bautraeger *(Anzahl der genehmigten Wohnungen nach Bauherr)*
- data_woh_baugenehmigungen_wohnflaeche *(Wohnfläche in genehmigten Neubauwohnungen)*
- data_woh_baugenehmigungen_wohnungen *(Anzahl genehmigter Wohnungen im Neubau nach Gebäudeart)*
- data_woh_genehmigte_u_fertiggestellte_wohnungen *(Genehmigte und fertiggestellte Wohnungen)*
- data_woh_preise_ooh_hpi_bauland *(Preisindizes zu Bau oder Erwerb von Wohneigentum)*


**id-Kategorie "Gesundheit":**

- ginsy_ges_impfung_covid19_impfstatus_map_de *(Covid-19-Impfstatus)*
- ginsy_ges_bev_sterbl_rel_sterbl_map_de *(Relative Sterbefallzahlen in Deutschland im Vergleich)*
- ginsy_ges_bev_sterbl_abs_sterbl_de *(Wöchentliche Sterbefallzahlen in Deutschland)*
- ginsy_ges_impfung_covid19_gesamtzahl_de *(Gesamtzahl der Covid-19-Impfungen)*
- ginsy_ges_infra_ausst_intensivbetten_de *(Krankenhauskapazitäten)*
- ginsy_ges_diag_covid19_7_tage_inzidenz_map_de *(7-Tage-Inzidenz)*
- ginsy_ges_diag_covid19_neuinfektionen_de *(Infektionsgeschehen)*
- ginsy_ges_diag_covid19_faelle_de *(Covid-19-Fälle)*
- defacto_ges_diag_covid19_hospitalizationincidence_map_de *(Covid-19-Hospitalisierungen)*


**id-Kategorie "Außenhandel":**

- data_aussenhandel *(Außenhandel)*
- data_aussenhandel_laender *(Außenhandel mit ausgewählten Ländern)*
- data_aussenhandel_laendergruppen *(Außenhandel mit ausgewählten Ländergruppen)*
- data_ifo_rwi_exporte_container *(Exporterwartungen und Containerumschlag)*
- data_aussenhandelsbilanz *(Außenhandelsbilanz)*


**id-Kategorie "Konsum":**

- data_gfk_hde_konsum *(Stimmungsindikatoren Konsum)*


**id-Kategorie "Preise":**

- data_wechselkurs_usd_eur *(Wechselkurs US-Dollar/Euro)*
- data_preisentwicklung *(Preisentwicklung)*
- data_preise_strom *(Strompreis)*
- data_preise_gold_kupfer *(Gold- und Kupferpreis)*
- tile_1648135639982 *(Kraftstoffpreise an öffentlichen Tankstellen)*
- data_preise_oel *(Ölpreis (Sorte Brent))*


**id-Kategorie "Branchen":**

- data_markit_bme_einkaufsmanager *(S&P Global/BME Einkaufsmanagerindex)*
- data_umsatz_ausgewaehlte_branchen *(Umsatz in Branchen des Verarbeitenden Gewerbes)*
- data_adv_flugverkehr *(Flugverkehr Deutschland)*
- data_umsatz_gastgewerbe_beherbergung *(Umsatz im Gastgewerbe)*
- data_vdma_blitzumfragen *(Blitzumfragen im Maschinen- und Anlagenbau)*
- data_destatis_lkw_maut_fahrleistungsindex *(LKW-Maut-Fahrleistungsindex)*
- data_vda_pkw *(Automobilindustrie)*
- data_produktion_vg *(Produktion im Produzierenden Gewerbe)*
- data_produktion_ausgewaehlte_branchen *(Produktion in Branchen des Produzierenden Gewerbes)*
- data_flightradar24_flugverkehr *(Flugverkehr weltweit)*
- data_einzelhandelsumsatz_vergleich_internet *(Einzelhandelsumsatz)*
- data_umsatz_vg *(Umsatz im Verarbeitenden Gewerbe)*
- data_auftragseingang_vg *(Auftragseingang im Verarbeitenden Gewerbe)*
- data_ifo_produktionserwartungen *(ifo Produktionserwartungen)*
- data_auftragseingang_ausgewaehlte_branchen *(Auftragseingang in Branchen des Verarbeitenden Gewerbes)*


**id-Kategorie "Konjunkturprogramm":**

- data_kfw_sondermassnahme_neu *(KfW-Sonderprogramm)*
- data_corona_zuschuesse *(Corona-Zuschüsse)*
- data_wirtschaftsstabilisierungsfonds *(Wirtschaftsstabilisierungsfonds)*
- data_buergschaften *(Bürgschaften)*


**id-Kategorie "Volkswirtschaft":**

- tile_1649694802780 *(Nettostromerzeugung)*
- data_bundesbank_aktivitaetsindex *(Wöchentlicher Aktivitätsindex)*
- data_zew_konjunktur *(ZEW Konjunkturausblick)*
- tile_1649679768351 *(Füllstand deutscher Erdgasspeicher)*
- data_bruttoinlandsprodukt *(Entwicklung des Bruttoinlandsprodukts)*
- data_ifo_geschaeftsklima *(ifo Geschäftsklima)*
- data_bnetza_realisierter_stromverbrauch *(Stromverbrauch)*


**id-Kategorie "Mobilität":**

- tile_1650550636596 *(Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im bundesweiten Vergleich)*
- data_mobilitaet_mobilfunk *(Mobilitätsindikatoren auf Grundlage von Mobilfunkdaten)*
- tile_1650548728319 *(Mobilitätstrends: Besuche von Einzelhandel und Erholungseinrichtungen im europäischen Vergleich)*
- data_mobilitaet_mobilfunk_hotspot *(Tägliche Mobilitätsveränderung und 7-Tage-Inzidenz auf Kreisebene auf Grundlage von Mobilfunkdaten)*
- tile_1650548254089 *(Mobilitätstrends: Besuche des Arbeitsplatzes im europäischen Vergleich)*
- tile_1650547629071 *(Mobilitätstrends: Besuche des Arbeitsplatzes im bundesweiten Vergleich)*
- data_mobilitaet_mobilfunk_karte *(Tägliche Veränderung der Mobilität auf Kreisebene auf Grundlage von Mobilfunkdaten)*
- data_mobilitaet_hystreet *(Passantenfrequenzen: Veränderung in ausgewählten Großstädten)*


**id-Kategorie "Öffentliche Finanzen":**

- tile_1650978797816 *(Verschuldung des Bundeshaushalts und seiner Sondervermögen)*
- tile_1650978274644 *(Verschuldung des erweiterten Bundeshaushalts nach Restlaufzeiten)*
- data_einnahmen_gemeinschaft_bundes_landessteuern *(Bereinigte kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern)*
- tile_1650979109395 *(Anteil der Grünen Bundeswertpapiere an der Verschuldung des erweiterten Bundeshaushalts)*
- tile_1650977632272 *(Verschuldung der größten Sondervermögen des Bundes)*
- data_steuereinnahmen_bund_laender *(Kassenmäßige Steuereinnahmen von Bund und Ländern)*
- data_gemeinschaft_bundes_landessteuern *(Kassenmäßige Steuereinnahmen aus Gemeinschaft-, Bundes- und Landessteuern)*
- data_steuereinnahmen_insgesamt_gemeinden *(Kassenmäßige Steuereinnahmen insgesamt und der Gemeinden/Gemeindeverbände)*
- data_gemeindesteuern *(Kassenmäßige Steuereinnahmen aus Gemeindesteuern)*


**id-Kategorie "Finanzmärkte":**

- data_zinsspread_10_j_anleihen *(Renditespreads 10-jähriger Staatsanleihen gegenüber Deutschland)*
- data_boersenkurse *(Aktienindizes)*
- data_staats_und_unt_anleihen *(Umlaufrenditen Staats- und Unternehmensanleihen)*
- data_umlaufrenditen_bundesanleihen *(Renditen Bundeswertpapiere)*


**id-Kategorie "Kreditwirtschaft":**

- data_kreditwirtschaft *(Kreditvergaben und Online-Transaktionen)*


**id-Kategorie "Ukraine":**

- data_gfk_hde_konsum *(Stimmungsindikatoren Konsum)*
- data_markit_bme_einkaufsmanager *(S&P Global/BME Einkaufsmanagerindex)*
- tile_1649679768351 *(Füllstand deutscher Erdgasspeicher)*
- data_ifo_rwi_exporte_container *(Exporterwartungen und Containerumschlag)*
- data_vdma_blitzumfragen *(Blitzumfragen im Maschinen- und Anlagenbau)*
- tile_1649694802780 *(Nettostromerzeugung)*
- data_ifo_geschaeftsklima *(ifo Geschäftsklima)*
- tile_1648135639982 *(Kraftstoffpreise an öffentlichen Tankstellen)*
- data_aussenhandel_laender *(Außenhandel mit ausgewählten Ländern)*
- data_preisentwicklung *(Preisentwicklung)*


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
