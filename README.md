# SlutProjecktProgramering1LOLLMAOMasterMind

## Description
Programet är skrivet i python. Programet är till för att man ska kunna köra Master Mind utan brädspelet.

## Technology/Languages/Built with (Teknologier/Språk/Byggt med - välj en)

-Python
-TKinter

## Requirements/Prerequisites (Krav)
-Python 3.9.6
-TKinter library

## Installation

Detta projekt är testat på Python Python 3.9.6. För att installera Python kan du besöka (https://www.python.org/downloads/)[följande länk för senaste versionen.]

Klona repot
```cmd
    git clone https://github.com/Dripmaster69/SlutProjecktProgramering1LOLLMAOMasterMind
```
## Code conventions

pep-8

## Hur det fungerar

***Använd detta utrymme för att visa användbara exempel av hur projektet kan användas. Skärmdumpar, kodexempel och demos passar in här. Du kan också länka till fler resurser, exempelvis en dokumentation.***

Master Mind går ut på att datorn genererar en lista av färjer som är ej uppvisad för användaren och sedan ska användaren gissa vilka färger som är i listan och även gissa vilken plats färgen ligger på. Man gissar i omgångar så först gissar man alla färger och resultaten man kan få tillbaka är röd vilekt inebär att färgen inte finns med i listan, gul om färgen finns med i lsitan men på fel plats och grön om färgen finns med i listan och är på rätt plats. När alla resultat visar grönt betyder det att alla färger har plaserats i rätt ordning och spelaren som gissade sin lista först eller inom 9 runder vinner spelet.

Komplicerad kod i programet:

for x in range(lenght):
    if attempt == sequence[x].value:
        if x < counter:
            if attempts[x] != sequence[x].color:
                return "🟡"
        if x > counter:
            return "🟡"

Koden ser till så att rättningen av gissningarna skickar ut rätt hint för den platsen i sekvänsen koden kollar.

window = tk.Tk()

for y in range(5):
    window.columnconfigure(y, weight=1, minsize=75)
    window.rowconfigure(y, weight=1, minsize=50)
    for x in range(3):
        frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame1.grid(row=y, column=x, padx=5, pady=5)

Koden skapar ett fönster med ett rutnät av små fönster med 5 columner och 3 rader. I varje litet fönster kan man sedan välja att lägga till vad somhelst.

Screenshoots:
Koden utan TKinter:
![Skärmklipp2](https://user-images.githubusercontent.com/95741620/168275405-9742bf24-7cd8-43e2-872c-419c7de3c714.PNG)

Koden med TKinter:
![Skärmklipp](https://user-images.githubusercontent.com/95741620/168275354-eaa0ea9b-a18e-41ea-bf2f-1b573a3f8208.PNG)

## Example (exempelkörning)

***Visa gärna, genom ett kodblock från din konsol, eller en bild, hur en exempelkörning kan gå till.***

## To do/Roadmap (Att göra/Plan)

***Det kan vara nyttigt att få andra som läser om projektet att få veta vad du saknar just nu i programmet. Gör detta gärna genom en lista där färdiga saker strukits över.***
Exempel:

- [x] Påbörja exempelreadme
- [ ] Hitta fler exempelrubriker
- [ ] Kom på bättre exempel
- [ ] Ge exempel på projekt med fullständig readme
- [ ] Ytterligare språk
    - [x] Svenska
    - [ ] Engelska

## Changelog

***Det kan vara rimligt att inkludera vad som har förändrats genom de olika iterationerna som ditt projekt gått igenom. Detta kan antingen göras i din README eller så kan du inkludera en CHANGELOG.md.***

***I changelogen ska varje rubrik vara en version. Under varje version bör du inkludera vad du lagt till eller ändrat på (added or changed) under en rubrik samt vad du tagit bort (removed) under en annan. Exempel: ***

### Version 1.0.1

#### Tillagt eller ändrat

- La till avsnitt om changelog
- La till avsnitt om kodkonventioner

#### Borttaget

- Tog bort tidigare rubriker som inte såg bra ut.
- Tog bort felaktig rubrik om innehållsförteckning

## Att bidra (Contribution)

***Inom programmeringsvärlden är det ofta populärt att man vill utveckla andras projekt och bidra till förbättring. För att underlätta detta är det bra om det i READMEn förklaras om det är tillåtet, och om det är det hur en går till väga för att kunna göra det. Detta avsnitt skulle se ut som följande:*** 

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  

Vid större förändringar önskar jag att en issue öppnas för diskussion om vad som ska förändras.

## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)

## Contact (Kontakt)

***Skriv här hur du blir kontaktad ifall det finns frågor om projektet***

Ditt Namn - @din_twitter (eller discord? annan plattform?) - email@example.com

Projektlänk: https://github.com/ditt_anv/reponamn

## Erkännanden (Acknowledgments)

***Här kan du lista resurser eller personer som har hjälpt dig med projektet. Det kan vara länkar till tutorials eller dokumentation, eller bara någon annans profil som du vill uppmärksamma. Har du inget som behöver tas här så kan du strunta i rubriken. ***

- Mamma och Pappa
- [En jättebra låt](https://www.youtube.com/watch?v=cvh0nX08nRw)
- Dan Hermansson
