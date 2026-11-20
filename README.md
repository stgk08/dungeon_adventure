
# Dungeon Adventure

## Om prosjektet

Dungeon Adventure er et tekstbasert spill laget i Python som en del av IT2-prosjektet. Spillet handler om en spiller som utforsker en dungeon med forskjellige rom og fiender. Målet er å komme seg gjennom alle rommene, beseire dragen og vinne spillet.

Spilleren må ta valg underveis, for eksempel om man skal angripe, forsvare seg eller bruke en helsedrikk. Etter hvert blir fiendene sterkere, så det er viktig å bruke ressursene riktig.

## Hvordan fungerer spillet?

Dungeon Adventure er et tekstbasert eventyrspill der spilleren skal kjempe seg gjennom tre forskjellige rom. Hvert rom har sin egen fiende, og målet er å beseire alle fiendene for å komme til den siste kampen mot dragen.

Spilleren starter med 100 HP (helse) og et enkelt sverd som gjør 15 skade per angrep. Underveis møter spilleren sterkere fiender, og det blir derfor viktig å velge riktig handling i kampene.

Etter at spilleren har beseiret fienden i det andre rommet, får spilleren et nytt sverd som gjør 25 skade. Spilleren har også én helsedrikk som gir tilbake opptil 40 HP. Helsedrikken kan bare brukes én gang.

Dragen i det siste rommet er den sterkeste fienden. Den kan både utføre vanlige angrep og et kraftigere spesialangrep.

## Hvordan spiller man?

Når spillet starter, skriver spilleren inn navnet sitt. Deretter begynner eventyret.

I hvert rom møter spilleren en fiende. Man kan velge mellom tre handlinger:

1. **Attack** – Angriper fienden med våpenet sitt.
2. **Defend** – Reduserer skaden fra fiendens neste angrep.
3. **Use potion** – Bruker en helsedrikk for å få tilbake helse.

Spilleren starter med 100 HP. Hvis helsen går ned til 0, taper man spillet.

Det finnes tre rom i spillet:
- **Room 1 – The Slime Cave:** Her møter spilleren en Slime.
- **Room 2 – The Skeleton Hall:** Her møter spilleren en Skeleton. Etter kampen får spilleren et sterkere sverd.
- **Room 3 – The Dragon's Lair:** Her venter den siste og sterkeste fienden, dragen.

For å vinne må spilleren beseire alle fiendene.

## Hvordan starte spillet

Du trenger Python installert på datamaskinen.

1. Last ned eller klon prosjektet fra GitHub.
2. Åpne prosjektmappen i Visual Studio Code.
3. Åpne terminalen.
4. Kjør følgende kommando:

```bash
python main.py
```

På noen Windows-maskiner må du bruke:

```bash
py main.py
```

## Filstruktur

Prosjektet er delt inn i flere Python-filer. Hver fil har sitt eget ansvar.

| Fil | Beskrivelse |
|---|---|
| `main.py` | Starter spillet og ber spilleren skrive inn et navn. |
| `game.py` | Styrer spillets gang, rommene og spillmekanikken. |
| `character.py` | Inneholder grunnklassen Character med felles egenskaper og metoder. |
| `player.py` | Inneholder Player-klassen med spillerens handlinger. |
| `enemy.py` | Inneholder Enemy og Boss, som styrer fiendene og angrepene deres. |
| `weapon.py` | Inneholder Weapon-klassen for våpen og skade. |
| `potion.py` | Inneholder Potion-klassen for helsedrikken. |
| `room.py` | Inneholder Room-klassen som beskriver rommene og fiendene. |

## Objektorientert programmering

I prosjektet bruker vi objektorientert programmering (OOP) for å organisere koden. Vi har delt spillet inn i forskjellige klasser, slik at hver klasse har sitt eget ansvar.

Vi bruker blant annet:

- **Klasser:** For eksempel Character, Player, Enemy og Weapon.
- **Objekter:** Vi oppretter objekter fra klassene, for eksempel en spiller eller en fiende.
- **Attributter:** Egenskaper som navn, helse og skade.
- **Metoder:** Funksjoner som tilhører en klasse, for eksempel `attack()`, `defend()` og `take_damage()`.

### Arv 

Vi bruker arv for å unngå å skrive samme kode flere ganger.

- `Character` er en foreldreklasse.
- `Player` arver fra `Character`.
- `Enemy` arver fra `Character`.
- `Boss` arver fra `Enemy`.

Boss-klassen har dermed funksjonaliteten fra Enemy, men har også sitt eget spesialangrep.

Vi bruker også `super()` for å hente funksjonalitet fra foreldreklassen.

### Komposisjon 

Vi bruker komposisjon for å sette sammen forskjellige objekter.

For eksempel har Player et Weapon-objekt og et Potion-objekt. Game har også et Player-objekt og flere Room-objekter.

Dette gjør at klassene kan samarbeide uten at all koden må ligge i én stor fil.

## Teknologier og verktøy

- Python – programmeringsspråket vi bruker.
- Visual Studio Code – brukes til å skrive og teste koden.
- Git og GitHub – brukes til versjonskontroll og samarbeid.
- GitHub Live Share – brukes til å programmere sammen i sanntid.

## Testing

Vi tester spillet under utviklingen for å kontrollere at funksjonene fungerer som forventet.

### Hvordan vinner eller taper man?

- Du vinner hvis du beseirer alle tre fiendene, inkludert dragen.
- Du taper hvis karakterens helse går ned til 0 HP.

Strategien er å bruke angrep, forsvar og helsedrikken på riktig tidspunkt for å overleve alle tre kampene.

