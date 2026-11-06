# E-handelsanalys
*Snabbrapport och GitHub-samarbete*

## Projektbeskrivning

Detta projekt är ett grupparbete inom kursen **Pythonprogrammering och statistisk dataanalys**. Vi har analyserat försäljningsdata från en fiktiv e-handelsplattform i syfte att ta fram ett beslutsunderlag inför kommande kampanjperioder.

Analysen omfattar försäljningsintäkter, produktkategorier, geografiska skillnader, försäljningsutveckling över tid, genomsnittligt ordervärde (AOV) och avvikande beställningar.

## Viktiga filer

För att underlätta granskningen har vi sammanställt de filer som är relevanta för projektets slutresultat.

| Fil | Beskrivning |
|---|---|
| `notebooks/report.ipynb` | Gruppens gemensamma huvudrapport |
| `notebooks/report1.ipynb` | Mattias kompletterande analys |
| `src/metrics.py` | Funktioner för beräkning av nyckeltal och statistiska mått |
| `src/viz.py` | Funktioner för visualisering av analysresultaten |
| `src/io_utils.py` | Funktion för datainläsning |
| `data/ecommerce_sales.csv` | Datasetet som ligger till grund för analysen |
| `requirements.txt` | Nödvändiga Pythonpaket och deras versionsnummer |

## Pythonmiljö och reproducerbarhet

Projektet är utvecklat i **Python och Jupyter Notebook**. Rapporten använder projektets egna Pythonmoduler för datainläsning, beräkningar och visualiseringar.

De externa paket och versionsnummer som används finns angivna i `requirements.txt`.


## Arbetsprocess och GitHub-samarbete

Grupparbetet har genomförts med hjälp av GitHub, där vi har använt separata branches och Pull Requests för att möjliggöra parallellt arbete och gemensam granskning.

Varje gruppmedlem har ansvarat för sin tilldelade frågeställning och självständigt utvecklat tillhörande analyser, beräkningar och visualiseringar i separata notebooks och Pythonfiler.

För att säkerställa en enhetlig struktur, konsekvent kod och ett sammanhängande språk valde vi att låta en gruppmedlem ansvara för den tekniska sammanställningen av huvudrapporten. De individuellt utvecklade funktionerna och analyserna integrerades därefter i de gemensamma filerna.

Samtliga gruppmedlemmar har varit delaktiga genom gemensamma möten, diskussioner, granskning och återkoppling.

**Vi har valt att behålla våra individuella arbetsfiler i repot** för att dokumentera arbetsprocessen och visa hur projektet har utvecklats. Dessa filer är arbetsmaterial och behöver inte granskas.

## Ansvarsfördelning

**Ylva, Vafa och Fredrik**

Har arbetat med sina respektive frågeställningar och utvecklat tillhörande analyser, beräkningsfunktioner och visualiseringar i separata filer. Arbetet har därefter sammanställts i den gemensamma huvudrapporten `report.ipynb`, med funktioner i `metrics.py` och `viz.py`.

**Mattias**

Ansvarar för sin tilldelade frågeställning och kompletterande analys, som presenteras i `report1.ipynb`.

## Slutrapport

Projektets huvudsakliga resultat, visualiseringar, slutsatser och rekommendationer presenteras i **`notebooks/report.ipynb`**.

Mattias kompletterande analys presenteras i **`notebooks/report1.ipynb`**.

Övriga notebooks och Pythonfiler har behållits som dokumentation av gruppens arbetsprocess.
