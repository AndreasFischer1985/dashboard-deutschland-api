# Dashboard Deutschland API

Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.


## Get

**URL:** https://www.dashboard-deutschland.de/api/dashboard/get
	
Die API ermöglicht Zugriff auf alle gültigen Einträge des id-Parameters (siehe unten, Indikatoren).


## Indikatoren

**URL:** www.dashboard-deutschland.de/api/tile/indicators
	
Die API ermöglicht Zugriff auf unterschiedliche Indikatoren im JSON-Format über einfache GET-request.


**Parameter:** *id* (Optional)

- data_adv_flugverkehr
- data_aussenhandel
- data_ba_arbeitslose_und_stellen
- data_bruttoinlandsprodukt
- data_corona_zuschuesse
- data_einnahmen_gemeinschaft_bundes_landessteuern
- data_ifo_geschaeftsklima
- data_kfw_sondermassnahme_neu
- data_preisentwicklung
- data_umsatz_ausgewaehlte_branchen
- defacto_ges_diag_covid19_hospitalizationincidence_map_de
- ginsy_ges_bev_sterbl_abs_sterbl_de
- ginsy_ges_diag_covid19_7_tage_inzidenz_map_de
- tile_1648135639982
- data_erwerbstaetige
- data_ba_kurzarbeit
- data_iab_ifo_barometer
- data_bau_auftragseingang
- data_bau_produktionsindex_baugewerbe
- data_bau_umsatz_mixmodelle
- data_bau_bauleistungspreise
- data_bau_beschaeftigung_vgr
- data_bau_kapazitaetsauslastung_bbsr
- data_bau_verbesserung_energieeffizienz
- data_woh_baugenehmigungen_wohnflaeche
- data_woh_baugenehmigungen_wohnungen
- data_woh_baugenehmigungen_bautraeger
- data_woh_genehmigte_u_fertiggestellte_wohnungen
- data_woh_energieverbrauch_anwendung
- data_woh_energieverbrauch_energietraeger
- data_woh_nettokaltmiete;data_woh_bruttokaltmiete
- data_woh_preise_immobilien_hpi_haueser
- data_woh_preise_immobilien_hpi_wohnungen
- data_woh_preise_ooh_hpi_bauland
- ginsy_ges_impfung_covid19_impfstatus_map_de
- ginsy_ges_impfung_covid19_gesamtzahl_de
- ginsy_ges_diag_covid19_neuinfektionen_de
- ginsy_ges_diag_covid19_faelle_de
- ginsy_ges_bev_sterbl_rel_sterbl_map_de
- ginsy_ges_infra_ausst_intensivbetten_de
- data_ifo_rwi_exporte_container
- data_aussenhandelsbilanz
- data_aussenhandel_laender
- data_aussenhandel_laendergruppen
- data_gfk_hde_konsum
- data_preise_gold_kupfer
- data_preise_oel
- data_preise_strom
- data_wechselkurs_usd_eur
- data_markit_bme_einkaufsmanager
- data_ifo_produktionserwartungen
- data_vda_pkw;data_vdma_blitzumfragen
- data_auftragseingang_vg
- data_auftragseingang_ausgewaehlte_branchen
- data_produktion_vg
- data_produktion_ausgewaehlte_branchen
- data_umsatz_vg
- data_destatis_lkw_maut_fahrleistungsindex
- data_umsatz_gastgewerbe_beherbergung
- data_einzelhandelsumsatz_vergleich_internet
- data_adv_flugverkehr;data_flightradar24_flugverkehr
- data_buergschaften
- data_wirtschaftsstabilisierungsfonds
- data_bnetza_realisierter_stromverbrauch
- data_zew_konjunktur
- data_bundesbank_aktivitaetsindex
- data_mobilitaet_mobilfunk
- data_mobilitaet_mobilfunk_karte
- data_mobilitaet_google_de_arbeit
- data_mobilitaet_google_de_erholung
- data_mobilitaet_google_eu_arbeit
- data_mobilitaet_google_eu_erholung
- data_mobilitaet_mobilfunk_hotspot
- data_mobilitaet_hystree
- data_gemeinschaft_bundes_landessteuern
- data_gemeindesteuern
- data_steuereinnahmen_insgesamt_gemeinden
- data_steuereinnahmen_bund_laender
- data_boersenkurse
- data_zinsspread_10_j_anleihen
- data_umlaufrenditen_bundesanleihen
- data_staats_und_unt_anleihen


Id des gewünschten Indikators. Mehrere Semikolon-getrennte Angaben sind möglich. Gesundheitsindikatoren (beginnend mit "ginsy_ges") lassen sich neben der o.g. Variante auch nach Regionen von Bundesländern unterteilt anfordern, durch einen Unterstrich, gefolgt von einer das Bundesland repräsentierenden Zahl (z.B. 9 für Bayern).


## Geojson

**URL:** www.dashboard-deutschland.de/geojson/de-all.geo.json
	
Die API ermöglicht Zugriff auf Geojson-Daten zu Deutschland und den Ländern (00-DE_admin1_400).


## Beispiel

```bash
indicators=$(curl -m 60 'https://www.dashboard-deutschland.de/api/tile/indicators?ids=data_adv_flugverkehr;data_aussenhandel;data_ba_arbeitslose_und_stellen;data_bruttoinlandsprodukt;data_corona_zuschuesse;data_einnahmen_gemeinschaft_bundes_landessteuern;data_ifo_geschaeftsklima;data_kfw_sondermassnahme_neu;data_preisentwicklung;data_umsatz_ausgewaehlte_branchen;defacto_ges_diag_covid19_hospitalizationincidence_map_de;ginsy_ges_bev_sterbl_abs_sterbl_de;ginsy_ges_diag_covid19_7_tage_inzidenz_map_de;tile_1648135639982
')
```
