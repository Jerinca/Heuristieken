# Heuristieken - Amstelhaege

Er komt een nieuwe woonwijk in de Duivendrechtse polder, op een stuk grond van 160 x 180 meter. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld. Het doel is om voor elk huizenvariant een plattegrond te creeeren waarbij een zo hoog mogelijke waarde van de wijk bereikt kan worden.
Daarnaast zijn er eisen waar de wijk aan moet voldoen, zoals een vaste verdeling (60% eengezinswoningen, 25% bungalows, 15% maisons), 20% oppervlaktewater.

### State Space 
Voor het berekenen van de upper bound van de state space wordt enkel met eengezinswoningen gewerkt, aangezien deze het kleinst zijn en dus meer oplossingen kunnen opleveren. De oppervlak van een eengezinswoning met verplichte bijstand is 10 x 10 meter, op het gehele oppervlak van de wijk passen er dus 16 x 18 = 288 huizen (max_inlengte * max_inbreedte). Aangezien de volgorde van het plaatsen van de huizen niet uitmaakt voor het aantal oplossingen, vermening vuldigen we met de faculteit van n (aantal huizen). Gezien er met een type huis wordt gewerkt, is 50% van de oplossingen een spiegeling van een andere oplossing. De upperbound halveert dus.

```
upperbound = ((max_inlengte * max_inbreedte)!/(((max_inlengte * max_inbreedte) - n)! * n!)) * 0.5
Voor eengezinswoningen is dit dus: (288!/((288-n)! * n!)) * 0.5
```
De lower bound is 1, omdat er minimaal een oplossing is. 

### Objective Function
De upperbound van de objective function is de waarde waarbij de huizen maximale vrijstand hebben. Voor het gemak is de formule enkel gebaseerd op maisons. Een maison heeft 6 meter verplichte vrijstand rondom het huis. De extra vrijstand die een maison maximaal kan hebben is 68.5, namelijk (160 - 10.5 (= breedte van het huis) - 12 (6m vrijstand links en rechts)) / 2 = 68.75. 
```
max_vrijstand = (breedte_wijk - breedte_huis - (2 * verplichte_vrijstand))/ 2
upperbound = (n * waarde_maison) * (1 + perc_vermeerdering_maison * max_vrijstand)
Voor enkel maisons is dit dus: (n * 610000) * (1 + 0.06 * 68.5)
```

De lowerbound is de waarde waarbij de huizen geen vrijstand hebben (verplichte vrijstand niet meegerekend). 
```
lowerbound = ((perc_eengezins * waarde_eengezins) + (perc_bungalow * waarde_bungalow) + (perc_maison * waarde_maison)) * n
In dit geval is dit dus: ((0.6 * 285000) + (0.25 *399000) + (0.15 * 610000)) * n
```

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in Python3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip d.m.v.:

```
pip install -r requirements.txt
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)
Om de code te draaien met de standaardconfiguratie, gebruik:

```
python main.py
```
### Resultaten (Results)

Het random plaatsen van alle huizen wordt 10000 keer uitgevoerd en met een histogram geplot om de distributie zichtbaar te maken. De resultaten (het stap voor stap plaatsen van de huizen) die uit de greedy komen worden opgeslagen in het resultaten mapje als losse afbeeldingen, waar vervolgens een gif bestand van wordt gemaakt. Bij de verschillende hill climbers worden zowel de uiteindelijke plattegrond en het verloop van de waardevermeerdering geplot. 

Om de algoritmes met elkaar te vergelijken, wordt de gemiddelde waarde van de wijk per algoritme berekend. Daarnaast zal de runtime van de algoritmes met elkaar vergeleken worden. 

## Knelpunten

Het knelpunt van onze Amstelhaege case is dat de beste oplossing onbekend is voor de plattegronden van alle huizenvariant: we kunnen niet met zekerheid zeggen dat we de hoogste waarde van een wijk gevonden hebben. 

Verder brengen verschillende algoritmes verschillende problemen met zich mee. Bij de Hill Climber is de vrije vrijstand bijvoorbeeld niet verplicht overlappend. Door dat wel te doen zouden we de waarde van de wijk kunnen verhogen. De verplichte vrijstand is 'inbegrepen' in de afmetingen van een huis. Aangezien de huizen niet met elkaar kunnen overlappen, zorgt dit ervoor dat de verplichte vrijstand (nog) niet kunnen overlappen. 
Ook accepteren we bij de Hill Climber geen verslechtering waar vervolgens weer op door gewerkt kan worden. Een cooling scheme zou eventueel toegepast kunnen worden in een latere stadium. Daarnaast worden oplossingen die dezelfde waarde opleveren (geen verbetering, maar ook geen verslechtering) ook niet geaccepteerd. 
De runtime van de systematische hill climber is vrij lang. De (extra) waardevermeerdering die door middel van dit algoritme behaald kan worden is, vergeleken met bijvoorbeeld een greedy, waarschijnlijk vrij klein (moet nog getest worden).  

Bij de verschillende soorten Greedy's hebben we tot nog toe dezelfde volgorde van huizen plaatsen aangehouden. Eerst alle maisons, vervolgens bungalows en als laatste eensgezinswoningen. Het zou zo kunnen zijn dat als we deze volgorde aanpassen, we een nog betere waarde van de wijk kunnen krijgen.

## Auteurs (Authors)

* Jerinca Vreugdenhil
* Julien Fer
* Yang Yang To

## Dankwoord (Acknowledgments)

* StackOverflow
* Minor Programmeren UvA
