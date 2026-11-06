E-handelsanalys – Snabbrapport och GitHub-samarbete

Projektbeskrivning

Detta projekt är ett grupparbete i kursen "Pythonprogrammering och statistisk dataanalys". Vi har analyserat försäljningsdata från en fiktiv e-handelsplattform med syftet att ta fram ett beslutsunderlag inför kommande kampanjperioder.
Analysen omfattar bland annat försäljningsintäkter, produktkategorier, geografiska skillnader, försäljningsutveckling över tid, genomsnittligt ordervärde (AOV) och avvikande beställningar.

Viktiga filer
För att underlätta granskningen har vi sammanställt de filer som är relevanta för projektets slutresultat:

notebooks/report.ipynb – Gruppens gemensamma huvudrapport.

notebooks/report1.ipynb – Mattias separata rapportdel med kompletterande analys.

src/metrics.py – Funktioner för beräkning av nyckeltal och statistiska mått.

src/viz.py – Funktioner för visualisering av analysresultaten.

src/io_utils.py – Funktioner för datainläsning.

data/ecommerce_sales.csv – Datasetet som ligger till grund för analysen.

requirements.txt – De Pythonpaket och versionsnummer som behövs för att köra projektet.

Projektet är utvecklat i Python med Jupyter Notebook. Rapporten använder funktioner från projektets egna Pythonmoduler för datainläsning, beräkningar och visualiseringar.

Arbetsprocess och samarbete
Grupparbetet har genomförts med hjälp av GitHub, där vi har använt separata branches och Pull Requests för att möjliggöra parallellt arbete och gemensam granskning.
Varje gruppmedlem har ansvarat för sin tilldelade frågeställning och arbetat självständigt med tillhörande analyser, beräkningar och visualiseringar. Arbetet har utförts i separata notebooks och Pythonfiler för att undvika konflikter och underlätta samarbetet.

För att säkerställa en enhetlig struktur, konsekvent kod och ett sammanhängande språk i slutrapporten valde vi att låta en gruppmedlem ansvara för den tekniska sammanställningen. Detta innebar att de individuellt utvecklade funktionerna och analyserna integrerades i de gemensamma filerna.

Samtliga gruppmedlemmar har varit delaktiga i den gemensamma arbetsprocessen genom regelbundna möten, diskussioner, granskning och återkoppling på rapportens innehåll.

Vi har valt att behålla de individuella arbetsfilerna i GitHub-repot för att dokumentera arbetsprocessen och visa hur projektet har utvecklats. Dessa filer utgör arbetsmaterial och behöver inte granskas för att ta del av projektets slutresultat.

Ansvarsfördelning
Ylva, Vafa och Fredrik: Har ansvarat för sina respektive frågeställningar och genomfört tillhörande analyser. Var och en har utvecklat egna funktioner för beräkningar och visualiseringar samt dokumenterat sina resultat i separata notebooks. Arbetet har därefter sammanställts i den gemensamma huvudrapporten report.ipynb, med tillhörande funktioner i metrics.py och viz.py.

Mattias: Ansvarar för sin tilldelade frågeställning och kompletterande analys, som presenteras i report1.ipynb.

Slutrapport
Projektets huvudsakliga resultat, visualiseringar, slutsatser och rekommendationer presenteras i notebooks/report.ipynb.
Mattias kompletterande analys presenteras senare, separat i notebooks/report1.ipynb.
Övriga notebooks och Pythonfiler har behållits som dokumentation av gruppens arbetsprocess.
