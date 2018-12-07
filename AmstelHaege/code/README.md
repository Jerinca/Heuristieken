# Algoritmes Amstelhaege

## Random
Met random.py kunnen huizen volledig random worden geplaatst. De plaatsing houdt rekening met de constraints. 

## Greedy
Er zijn drie verschillende greedies gecreeerd:
- greedy_obj_func: selecteert de positie met de hoogste waarde voor elk huis om te plaatsen. 
- greedy_distance_extended: selecteert de positie met de grootste vrijstand voor elk huis om te plaatsen. 
- greedy_heuristics: afstand tot maison > 2 * afstand tot overige type huizen.

## Hill Climber
De hill climbers worden gerund met random oplossingen en oplossingen die uit de greedy komen. Er zijn drie verschillende hill climbers:
- hill_climber_random: random huizen worden verplaatst naar random gekozen x- en y-coordinaten. 
- hill_climber_systematic: elk huis in de lijst van huizen wordt verplaatst naar alle mogelijke posities in de wijk. De algoritme blijft door de lijst van huizen heen gaan en de huizen systematisch verplaatsen tot er geen waardevermeerdering meer optreedt voor alle huizen. -
- hill_climber_rdm_sys: dit is een combinatie van de bovenstaande twee typen. Het selecteert namelijk random huizen, maar verplaatst de huizen systematisch door de hele wijk. 

*Let op: op dit moment worden de algoritmes nog niet vanuit main.py gerund, maar vanuit de algoritme files zelf. 

      

