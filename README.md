# ANALISI DI MOBILITÀ CON SUMO SIMULATOR  
  
  
## DIRECTORY SCRIPT  
Contenuti gli script per esaminare gli output generati da Sumo simulator <br>
per studiare la mobilità e come si muovono pedoni/veicoli.`(Scritti per leggere fcd_dump.xml al momento)`<br>
In questa dir troviamo tre codici:  
- `xmlAnalyzer.py`:legge un file xml fornito da terminale,calcola le variazioni di celle effettuate dai pedoni;  
- `xmlPerson.py`:ha una griglia definita,legge un file xml fornito da terminale,restitusce le statistiche di ogni cella;  
- `xmlAnalyzer_graphic.py`:legge un file xml fornito da terminale ,restituisce la mappa con variazione di colori in base a quali zone sono più frequentate. <br>

Esempio:  
- python3 xmlPerson.py ~/fcd_dump.xml 


  
## DIRECTORY SCENARIO  
Contenuti i file xml di output,mappe e route. Qui è presente <br>
anche il file.sumocfg che contiene la configurazione della simulazione <br>
