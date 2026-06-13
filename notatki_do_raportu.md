# Notatki do raportu

Ten plik jest pomocniczy. Można z niego brać krótkie opisy do notebooka, prezentacji albo odpowiedzi na pytania prowadzącej.

## 1. O co chodzi w projekcie

Projekt składa się z dwóch części:

- część statystyczna: opis danych, testowanie hipotez, regresja wieloraka i analiza reszt,
- część TOM: model kolejki, symulacja EDS i analiza wybranej charakterystyki z symulacji.

W części statystycznej używany jest zbiór `Student Performance` z UCI. Dane opisują uczniów portugalskich szkół średnich.

Jeden wiersz danych oznacza jednego ucznia. Kolumny opisują szkołę, rodzinę, naukę, styl życia oraz oceny.

Najważniejsza zmienna wynikowa to `G3`, czyli ocena końcowa ucznia w skali od 0 do 20.

## 2. Opis danych

### Najważniejsze zmienne

- `G3` - ocena końcowa, główna zmienna wynikowa
- `G1` - ocena z pierwszego okresu
- `G2` - ocena z drugiego okresu
- `studytime` - tygodniowy czas nauki
- `failures` - wcześniejsze niezaliczenia
- `Medu`, `Fedu` - wykształcenie matki i ojca
- `Mjob`, `Fjob` - praca matki i ojca
- `Pstatus` - czy rodzice mieszkają razem
- `famrel` - jakość relacji rodzinnych
- `higher` - czy uczeń chce iść na studia

### Skale 1-5

W części zmiennych skala 1-5 oznacza poziom cechy:

- `famrel`: 1 = bardzo złe relacje rodzinne, 5 = bardzo dobre relacje rodzinne
- `freetime`: 1 = bardzo mało wolnego czasu, 5 = bardzo dużo wolnego czasu
- `goout`: 1 = bardzo rzadkie wychodzenie ze znajomymi, 5 = bardzo częste wychodzenie
- `Dalc`: 1 = bardzo małe spożycie alkoholu w dni robocze, 5 = bardzo duże
- `Walc`: 1 = bardzo małe spożycie alkoholu w weekend, 5 = bardzo duże
- `health`: 1 = bardzo zły stan zdrowia, 5 = bardzo dobry stan zdrowia

Ogólnie 1 oznacza niski/słaby poziom cechy, a 5 wysoki/mocny poziom. Trzeba jednak zawsze patrzeć na nazwę zmiennej.

### Inne skale porządkowe

`Medu`, `Fedu` - wykształcenie matki/ojca:

- 0 = brak
- 1 = podstawowe
- 2 = 5-9 klasa
- 3 = średnie
- 4 = wyższe

`traveltime` - czas dojazdu do szkoły:

- 1 = mniej niż 15 minut
- 2 = 15-30 minut
- 3 = 30 minut - 1 godzina
- 4 = więcej niż 1 godzina

`studytime` - tygodniowy czas nauki:

- 1 = mniej niż 2 godziny
- 2 = 2-5 godzin
- 3 = 5-10 godzin
- 4 = więcej niż 10 godzin

`failures` - wcześniejsze niezaliczenia:

- 0, 1, 2, 3 oznaczają liczbę wcześniejszych niezaliczeń
- 4 oznacza 4 lub więcej

### Opis kolumn

Zmienne demograficzne i rodzinne:

- `school`: szkoła ucznia, `GP` albo `MS`
- `sex`: płeć, `F` albo `M`
- `age`: wiek ucznia
- `address`: miejsce zamieszkania, `U` = miasto, `R` = wieś
- `famsize`: liczba osób w rodzinie, `LE3` = do 3 osób, `GT3` = więcej niż 3
- `Pstatus`: status rodziców, `T` = mieszkają razem, `A` = mieszkają osobno
- `Medu`: wykształcenie matki, skala 0-4
- `Fedu`: wykształcenie ojca, skala 0-4
- `Mjob`: praca matki: `teacher`, `health`, `services`, `at_home`, `other`
- `Fjob`: praca ojca: `teacher`, `health`, `services`, `at_home`, `other`
- `guardian`: opiekun ucznia: `mother`, `father`, `other`

Zmienne szkolne i związane z nauką:

- `reason`: powód wyboru szkoły: `home`, `reputation`, `course`, `other`
- `traveltime`: czas dojazdu, skala 1-4
- `studytime`: czas nauki, skala 1-4
- `failures`: wcześniejsze niezaliczenia
- `schoolsup`: dodatkowe wsparcie szkolne, `yes` albo `no`
- `famsup`: wsparcie edukacyjne rodziny, `yes` albo `no`
- `paid`: płatne zajęcia dodatkowe, `yes` albo `no`
- `activities`: zajęcia pozalekcyjne, `yes` albo `no`
- `nursery`: czy uczeń chodził do przedszkola, `yes` albo `no`
- `higher`: czy uczeń chce iść na studia, `yes` albo `no`
- `internet`: internet w domu, `yes` albo `no`

Zmienne społeczne i styl życia:

- `romantic`: związek romantyczny, `yes` albo `no`
- `famrel`: relacje rodzinne, skala 1-5
- `freetime`: czas wolny, skala 1-5
- `goout`: wychodzenie ze znajomymi, skala 1-5
- `Dalc`: alkohol w dni robocze, skala 1-5
- `Walc`: alkohol w weekendy, skala 1-5
- `health`: zdrowie, skala 1-5
- `absences`: liczba nieobecności

Oceny:

- `G1`: ocena z pierwszego okresu, 0-20
- `G2`: ocena z drugiego okresu, 0-20
- `G3`: ocena końcowa, 0-20

## 3. Hipotezy statystyczne

### Jak czytać wyniki

- `count`: liczba osób w danej grupie
- `mean`: średnia wartość w grupie
- `median`: mediana, czyli środkowa wartość po uporządkowaniu danych
- `std`: odchylenie standardowe, czyli rozrzut wyników wokół średniej
- `p-value`: prawdopodobieństwo uzyskania takiego lub bardziej skrajnego wyniku przy założeniu, że H0 jest prawdziwa
- `alpha`: poziom istotności, tutaj 0.05

Zasada decyzji:

- jeżeli `p-value < 0.05`, odrzucamy H0
- jeżeli `p-value >= 0.05`, nie mamy podstaw do odrzucenia H0

### Hipoteza 1

Pytanie: czy uczniowie z rodzicem nauczycielem mają wyższą ocenę końcową `G3`?

- porównywane grupy: rodzic nauczyciel vs brak rodzica nauczyciela
- zmienna porównywana: `G3`, ocena końcowa w skali 0-20
- test: test t Welcha
- dlaczego ten test: porównujemy średnią zmiennej liczbowej w dwóch niezależnych grupach
- patrzymy na: średnie `G3`, statystykę t i `p-value`

### Hipoteza 2

Pytanie: czy uczniowie, których rodzice mieszkają osobno, gorzej oceniają relacje rodzinne?

- porównywane grupy: `Pstatus = A` oraz `Pstatus = T`
- zmienna porównywana: `famrel`, relacje rodzinne w skali 1-5, gdzie 1 = bardzo złe, 5 = bardzo dobre
- test: U Manna-Whitneya
- dlaczego ten test: `famrel` jest skalą porządkową 1-5, więc nie zakładamy klasycznej normalności
- patrzymy na: medianę, średnią i `p-value`

### Hipoteza 3

Pytanie: czy wyższe wykształcenie rodzica wiąże się z planem pójścia na studia?

- porównywane zmienne: wysoko wykształcony rodzic tak/nie oraz `higher` tak/nie
- skala: `Medu` i `Fedu` są w skali 0-4, gdzie 4 = wykształcenie wyższe; `higher` ma wartości `yes/no`
- test: chi-kwadrat niezależności
- dlaczego ten test: sprawdzamy zależność między dwiema zmiennymi kategorycznymi
- patrzymy na: tabelę liczebności, odsetki `yes/no` i `p-value`

### Hipoteza 4

Pytanie: czy wśród dobrych uczniów osoby z wysoko wykształconym rodzicem uczą się krócej?

- filtr: tylko uczniowie z `G3 >= 14`, czyli z dobrą oceną końcową w skali 0-20
- porównywane grupy: wysoko wykształcony rodzic tak/nie
- zmienna porównywana: `studytime`, czas nauki w skali 1-4, gdzie 1 = mniej niż 2h, 4 = więcej niż 10h
- test: U Manna-Whitneya
- dlaczego ten test: `studytime` jest skalą porządkową 1-4
- patrzymy na: medianę, średnią i `p-value`


### Krótkie wnioski z hipotez

- Hipoteza 1: wynik jest istotny statystycznie (`p-value = 0.0001`). Uczniowie z co najmniej jednym rodzicem nauczycielem osiągają wyższe oceny końcowe `G3` niż pozostali uczniowie.
- Hipoteza 2: wynik nie jest istotny statystycznie (`p-value = 0.2262`). Nie ma podstaw do stwierdzenia, że uczniowie, których rodzice mieszkają osobno, gorzej oceniają relacje rodzinne.
- Hipoteza 3: wynik jest istotny statystycznie (`p-value = 0.0000`). Istnieje zależność między wyższym wykształceniem rodzica a planem pójścia na studia.
- Hipoteza 4: wynik nie jest istotny statystycznie (`p-value = 0.2129`). Nie ma podstaw do stwierdzenia, że wśród dobrych uczniów osoby z wysoko wykształconym rodzicem uczą się krócej.

Najkrócej: potwierdziły się hipotezy 1 i 3, a hipotezy 2 i 4 nie zostały potwierdzone statystycznie.


## 4. Regresja wieloraka

Ta sekcja pomaga odpowiedzieć na pytanie: **co dokładnie widać na outputcie regresji w notebooku?**

W notebooku są dwa modele:

- **4.1 model bazowy** - krótszy, prostszy, łatwiejszy do interpretacji,
- **4.2 model rozszerzony** - dodaje więcej zmiennych społecznych, edukacyjnych i stylu życia.

Oba modele przewidują `G3`, czyli ocenę końcową ucznia w skali 0-20.

Zmienne `G1` i `G2` są pominięte celowo. To wcześniejsze oceny, które bardzo mocno przewidują `G3`. Gdyby je dodać, model byłby lepiej dopasowany, ale mniej ciekawy, bo mówiłby głównie, że wcześniejsze oceny przewidują ocenę końcową.

### 4.1 Model bazowy

Formuła:

```text
G3 ~ studytime + failures + absences + Medu + Fedu + traveltime + C(internet) + C(schoolsup) + C(higher)
```

Model bazowy zawiera najważniejsze zmienne edukacyjne i rodzinne:

- `studytime` - czas nauki,
- `failures` - wcześniejsze niezaliczenia,
- `absences` - nieobecności,
- `Medu`, `Fedu` - wykształcenie rodziców,
- `traveltime` - czas dojazdu,
- `internet`, `schoolsup`, `higher` - zmienne `yes/no` zakodowane przez `C(...)`.

Wyniki modelu bazowego:

- liczba obserwacji: 649
- `R2 = 0.2649`
- `adjusted R2 = 0.2545`
- `AIC = 3183.2231`
- `BIC = 3227.9774`
- `p-value testu F = 0.0000`

Interpretacja: model jako całość jest istotny statystycznie i wyjaśnia około 26% zmienności `G3`.

Najważniejsze zmienne istotne w modelu bazowym:

- `studytime`: dodatni wpływ, większy czas nauki wiąże się z wyższą oceną,
- `failures`: ujemny wpływ, wcześniejsze niezaliczenia wiążą się z niższą oceną,
- `C(schoolsup)[T.yes]`: ujemny współczynnik, prawdopodobnie dlatego, że wsparcie dostają uczniowie z trudnościami,
- `C(higher)[T.yes]`: dodatni wpływ, plan studiów wiąże się z wyższą oceną.

### 4.2 Model rozszerzony

Model rozszerzony jest drugim wariantem regresji. Zawiera zmienne z modelu bazowego, ale dodaje więcej informacji o wsparciu edukacyjnym, aktywnościach, czasie wolnym, alkoholu i relacjach rodzinnych.

Formuła:

```text
G3 ~ Medu + Fedu + traveltime + studytime + failures + C(schoolsup) + C(famsup) + C(paid) + C(activities) + C(higher) + absences + freetime + Walc + Dalc + famrel
```

Zmienne dodane względem modelu bazowego:

- `C(famsup)` - wsparcie edukacyjne rodziny,
- `C(paid)` - płatne zajęcia dodatkowe,
- `C(activities)` - aktywności pozalekcyjne,
- `freetime` - czas wolny po szkole,
- `Walc` - spożycie alkoholu w weekend,
- `Dalc` - spożycie alkoholu w dni robocze,
- `famrel` - jakość relacji rodzinnych.

#### Ocena dopasowania modelu rozszerzonego

W outputcie widać:

- liczba obserwacji: 649
- `R2 = 0.2858`
- `adjusted R2 = 0.2689`
- `AIC = 3176.4446`
- `BIC = 3248.0515`
- `p-value testu F = 0.0000`

Jak to powiedzieć:

Model rozszerzony jako całość jest istotny statystycznie, bo `p-value testu F = 0.0000`. Wyjaśnia około 28.6% zmienności oceny końcowej `G3`. Skorygowane `R2` wynosi około 26.9%, więc po uwzględnieniu większej liczby zmiennych model nadal wypada trochę lepiej niż model bazowy.

#### Współczynniki istotne w modelu rozszerzonym

Istotne przy poziomie 0.05 są:

- `C(schoolsup)[T.yes]`: `coef = -1.0680`, `p_value = 0.0032`
- `C(higher)[T.yes]`: `coef = 1.8129`, `p_value = 0.0000`
- `studytime`: `coef = 0.5505`, `p_value = 0.0001`
- `failures`: `coef = -1.4281`, `p_value = 0.0000`
- `Dalc`: `coef = -0.3134`, `p_value = 0.0393`

Interpretacja:

- `studytime` ma dodatni współczynnik, czyli większy czas nauki wiąże się z wyższą przewidywaną oceną końcową.
- `failures` ma ujemny współczynnik, czyli wcześniejsze niezaliczenia wiążą się z niższą oceną końcową.
- `C(higher)[T.yes]` ma dodatni współczynnik, czyli uczniowie planujący studia mają wyższą przewidywaną ocenę końcową niż uczniowie bez takiego planu.
- `C(schoolsup)[T.yes]` ma ujemny współczynnik. Nie oznacza to automatycznie, że wsparcie szkolne szkodzi. Bardziej prawdopodobne jest to, że wsparcie dostają uczniowie, którzy już wcześniej mieli trudności.
- `Dalc` ma ujemny współczynnik, czyli większe spożycie alkoholu w dni robocze wiąże się z niższą oceną końcową.

#### Zmienne nieistotne w modelu rozszerzonym

Nieistotne przy poziomie 0.05 są:

- `C(famsup)[T.yes]`
- `C(paid)[T.yes]`
- `C(activities)[T.yes]`
- `Medu`
- `Fedu`
- `traveltime`
- `absences`
- `freetime`
- `Walc`
- `famrel`

To nie znaczy, że te zmienne na pewno nie mają żadnego znaczenia. Oznacza tylko, że w tym modelu, przy kontroli pozostałych zmiennych, nie wyszły istotne statystycznie.

#### VIF w modelu rozszerzonym

VIF-y predyktorów są niskie:

- większość wartości jest blisko 1,
- najwyższe VIF-y dla zwykłych zmiennych mają `Medu`, `Fedu`, `Walc` i `Dalc`, ale nadal są poniżej 2,
- nie ma problemu silnej współliniowości.

`const` ma wysoki VIF (`58.6483`), ale stałej nie interpretujemy tak jak zwykłych predyktorów. Najważniejsze są VIF-y zmiennych objaśniających.

#### Diagnostyka reszt modelu rozszerzonego

W outputcie widać:

- `Shapiro-Wilk p-value = 0.0000`
- `Breusch-Pagan p-value = 0.0043`
- `Durbin-Watson = 1.8269`
- `Rainbow p-value = 0.0000`

Jak to powiedzieć:

- Shapiro-Wilk: `p-value < 0.05`, więc reszty odbiegają od normalności. Przy dużej próbie test jest bardzo czuły, więc nie jest to zaskakujące.
- Breusch-Pagan: `p-value = 0.0043 < 0.05`, więc pojawia się problem heteroskedastyczności, czyli nierównej wariancji reszt.
- Durbin-Watson: wynik `1.8269` jest blisko 2, więc nie widać dużego problemu autokorelacji reszt.
- Rainbow: `p-value < 0.05`, więc model może nie być idealnie liniowy.

Najkrótszy wniosek:

**Model rozszerzony ma trochę lepsze dopasowanie niż model bazowy, ale nadal nie spełnia idealnie założeń regresji, głównie przez heteroskedastyczność i możliwy problem z liniowością.**

### Porównanie modeli

Najprostsze porównanie:

- model rozszerzony ma lepsze `R2` i `adjusted R2`,
- model rozszerzony ma niższe `AIC`,
- model bazowy ma niższe `BIC`, bo jest prostszy,
- w obu modelach istotne pozostają `studytime`, `failures`, `schoolsup` i `higher`.

Co można powiedzieć na prezentacji:

**Model rozszerzony daje lekko lepsze dopasowanie, ale kosztem większej liczby zmiennych. Model bazowy jest prostszy i łatwiejszy do interpretacji, natomiast model rozszerzony pokazuje dodatkowo, że `Dalc`, czyli alkohol w dni robocze, może mieć ujemny związek z oceną końcową.**

### Jak czytać współczynniki

W tabeli współczynników są kolumny:

- `coef`: współczynnik regresji,
- `p_value`: istotność danej zmiennej,
- `istotne_0_05`: czy zmienna jest istotna przy poziomie 0.05.

Dodatni `coef` oznacza związek z wyższą przewidywaną oceną `G3`. Ujemny `coef` oznacza związek z niższą przewidywaną oceną `G3`. Interpretujemy to przy założeniu, że pozostałe zmienne są stałe.

### Kodowanie zmiennych kategorycznych

Regresja OLS wymaga danych liczbowych. Zmienne tekstowe/kategoryczne są zakodowane przez `C(...)`, np.:

- `C(schoolsup)`,
- `C(famsup)`,
- `C(paid)`,
- `C(activities)`,
- `C(higher)`.

Współczynnik przy kategorii, np. `C(higher)[T.yes]`, mówi o różnicy względem kategorii bazowej, czyli tutaj względem `no`.

### VIF - współliniowość zmiennych

VIF sprawdza, czy zmienne objaśniające nie powtarzają tej samej informacji.

Jak czytać:

- VIF około 1 oznacza brak problemu,
- VIF powyżej 5 może sugerować problem,
- VIF powyżej 10 to zwykle poważny problem.

W obu modelach VIF-y predyktorów są niskie, głównie około 1-2. To znaczy, że nie ma dużego problemu współliniowości.

`const` może mieć wysoki VIF, ale stałej nie interpretujemy tak jak zwykłej zmiennej.

### Diagnostyka reszt

W outputcie są cztery informacje:

- Shapiro-Wilk - normalność reszt,
- Breusch-Pagan - homoskedastyczność,
- Durbin-Watson - autokorelacja reszt,
- Rainbow - liniowość modelu.

Dla modelu bazowego:

- `Shapiro-Wilk p-value = 0.0000`
- `Breusch-Pagan p-value = 0.0028`
- `Durbin-Watson = 1.8313`
- `Rainbow p-value = 0.0000`

Dla modelu rozszerzonego:

- `Shapiro-Wilk p-value = 0.0000`
- `Breusch-Pagan p-value = 0.0043`
- `Durbin-Watson = 1.8269`
- `Rainbow p-value = 0.0000`

Interpretacja:

- reszty odbiegają od normalności,
- Breusch-Pagan wskazuje na możliwą heteroskedastyczność,
- Durbin-Watson jest blisko 2, więc nie widać dużej autokorelacji,
- Rainbow wskazuje, że model może nie być idealnie liniowy.

Najważniejsze zdanie do obrony:

**Homoskedastyczność sprawdzono testem Breuscha-Pagana. W obu modelach p-value < 0.05, więc mamy podstawy podejrzewać heteroskedastyczność. Dlatego modele można interpretować opisowo, ale przy bardzo ścisłej interpretacji istotności współczynników trzeba zachować ostrożność albo użyć odpornych błędów standardowych.**

### Ograniczenia modeli

- `G3` jest oceną od 0 do 20, więc zmienna jest ograniczona i dyskretna, a nie idealnie ciągła.
- Modele pokazują zależności, ale nie dowodzą przyczynowości.
- Część zmiennych jest porządkowa, np. `studytime`, `traveltime`, `Medu`, `Fedu`.
- Reszty nie spełniają idealnie wszystkich założeń, szczególnie homoskedastyczności.
- Modele nie używają `G1` i `G2`, bo świadomie analizujemy cechy ucznia, a nie wcześniejsze oceny.


## 5. Część TOM / symulacja

### 5.1 Co modelujemy

Modelujemy kolejkę pasażerów do jednego biletomatu na stacji kolejowej.

Sytuacja:

- pasażerowie losowo przychodzą na stację,
- chcą kupić bilet w biletomacie,
- jeśli biletomat jest wolny, obsługa zaczyna się od razu,
- jeśli biletomat jest zajęty, pasażer czeka w kolejce,
- kolejka działa według zasady FIFO.

FIFO oznacza, że pierwszy pasażer w kolejce jest obsługiwany jako pierwszy.

### 5.2 Dlaczego to jest model kolejkowy

Mamy klasyczne elementy systemu obsługi masowej:

- źródło zgłoszeń: pasażerowie,
- zgłoszenie: potrzeba zakupu biletu,
- kanał obsługi: jeden biletomat,
- kolejka: pasażerowie czekający na wolny biletomat,
- dyscyplina kolejki: FIFO,
- charakterystyki systemu: czas oczekiwania, długość kolejki, wykorzystanie biletomatu.

### 5.3 Parametry symulacji

W notebooku przyjęto:

- czas symulacji: 480 minut, czyli 8 godzin,
- liczba powtórzeń: 100,
- średni czas między przyjściami pasażerów: 2.5 minuty,
- minimalny czas obsługi: 0.5 minuty,
- najczęstszy czas obsługi: 1.5 minuty,
- maksymalny czas obsługi: 4 minuty,
- liczba biletomatów: 1.

### 5.4 Dobór rozkładów

#### Przyjścia pasażerów

Odstępy między przyjściami pasażerów losujemy z rozkładu wykładniczego.

Uzasadnienie:

- pasażerowie pojawiają się losowo,
- przyjścia traktujemy jako niezależne,
- rozkład wykładniczy jest klasycznym wyborem dla czasu między kolejnymi zgłoszeniami w prostych modelach kolejkowych.

Najważniejsze zdanie do obrony:

**Rozkład wykładniczy wybrano, ponieważ modelujemy losowe odstępy między niezależnymi przyjściami pasażerów. Jest to standardowe założenie w prostych modelach kolejek.**

#### Czas obsługi

Czas obsługi losujemy z rozkładu trójkątnego.

Uzasadnienie:

- zakup biletu ma naturalne minimum, bo nie da się obsłużyć pasażera natychmiast,
- ma typową wartość, czyli najczęstszy czas zakupu biletu,
- ma też rozsądne maksimum, bo czas obsługi nie powinien rosnąć bez ograniczeń,
- rozkład trójkątny jest dobry, gdy znamy minimum, wartość najbardziej prawdopodobną i maksimum.

Najważniejsze zdanie do obrony:

**Rozkład trójkątny wybrano dla czasu obsługi, ponieważ łatwo opisać minimalny, typowy i maksymalny czas zakupu biletu.**

### 5.5 Na czym polega EDS

EDS to symulacja zdarzeń dyskretnych. Nie przechodzimy przez czas minuta po minucie, tylko przeskakujemy do najbliższego zdarzenia.

W tej symulacji są dwa typy zdarzeń:

- przyjście pasażera,
- zakończenie obsługi pasażera.

Stan systemu w trakcie symulacji:

- aktualny czas,
- czy biletomat jest zajęty,
- kolejka pasażerów,
- czas następnego przyjścia,
- czas następnego zakończenia obsługi,
- zebrane czasy oczekiwania.

### 5.6 Co mierzymy

Wyniki jednej symulacji:

- `served_passengers`: liczba obsłużonych pasażerów,
- `mean_waiting_time`: średni czas oczekiwania pasażera,
- `max_waiting_time`: maksymalny czas oczekiwania,
- `mean_queue_length`: średnia długość kolejki,
- `max_queue_length`: maksymalna długość kolejki,
- `server_utilization`: wykorzystanie biletomatu,
- `passengers_left_in_queue`: liczba osób pozostałych w kolejce na końcu symulacji.

Główną analizowaną charakterystyką jest `mean_waiting_time`, czyli średni czas oczekiwania pasażera.

### 5.7 Wyniki scenariusza bazowego

Dla parametrów z notebooka wyniki ze 100 powtórzeń są następujące:

- średnio obsłużono `188.810` pasażerów,
- odchylenie standardowe liczby obsłużonych pasażerów wyniosło `13.357`,
- średni czas oczekiwania wyniósł `4.027` min,
- odchylenie standardowe średniego czasu oczekiwania wyniosło `1.792` min,
- minimalny średni czas oczekiwania w pojedynczym przebiegu wyniósł `1.317` min,
- maksymalny średni czas oczekiwania w pojedynczym przebiegu wyniósł `10.752` min,
- średnia długość kolejki wyniosła `1.633` osoby,
- średnie maksymalne wydłużenie kolejki w przebiegu wyniosło `8.360` osoby,
- średnie wykorzystanie biletomatu wyniosło `0.789`, czyli około `78.9%`,
- średnio na końcu symulacji zostawało `1.680` pasażera w kolejce.

Jak czytać tabelę `describe()`:

- `count = 100` oznacza, że wykonano 100 powtórzeń symulacji,
- `mean` to średnia wartość z tych 100 powtórzeń,
- `std` to odchylenie standardowe wyników między powtórzeniami,
- `min` i `max` pokazują najlepszy i najgorszy przebieg,
- `25%`, `50%`, `75%` to kwartyle; `50%` to mediana.

Interpretacja:

System jest dość mocno obciążony, ale nie jest skrajnie przeciążony. Jeden biletomat działa w tym scenariuszu sensownie, bo średnia kolejka jest krótka, ale wykorzystanie około 79% oznacza, że nie ma bardzo dużego zapasu przepustowości.

Histogram średniego czasu oczekiwania pokazuje, że większość przebiegów skupia się w okolicach kilku minut oczekiwania. Prawy ogon histogramu oznacza, że czasami trafiają się mniej korzystne przebiegi, gdzie średni czas oczekiwania jest wyraźnie większy.

Najkrótszy wniosek:

**W scenariuszu bazowym pasażer czeka średnio `4.027` minuty, a biletomat jest zajęty przez około `78.9%` czasu. System działa stabilnie, ale przy większym ruchu warto rozważyć drugi biletomat.**

### 5.8 Co można powiedzieć na prezentacji

Model kolejki został zbudowany jako osobna część TOM. Symulacja EDS pozwala sprawdzić zachowanie systemu bez rozwiązywania wzorów analitycznych. Najważniejszą badaną charakterystyką jest średni czas oczekiwania pasażera. Wynik pokazuje, że jeden biletomat wystarcza przy przyjętym natężeniu, ale przy większym ruchu można byłoby rozważyć dodanie drugiego biletomatu.


## 6. Pytania podchwytliwe do obrony

### Dane

**Pytanie:** Co dokładnie oznacza jeden wiersz w danych?  
**Odpowiedź:** Jeden wiersz oznacza jednego ucznia. Kolumny opisują jego sytuację rodzinną, szkolną, styl życia oraz oceny.

**Pytanie:** Czym jest `G3` i dlaczego jest najważniejsze?  
**Odpowiedź:** `G3` to ocena końcowa ucznia w skali 0-20. W projekcie jest główną zmienną wynikową.

**Pytanie:** Dlaczego część zmiennych liczbowych nie jest zwykłą zmienną ilościową?  
**Odpowiedź:** Niektóre liczby oznaczają kategorie uporządkowane, np. `studytime` 1-4 albo `famrel` 1-5.

**Pytanie:** Czy w danych są braki?  
**Odpowiedź:** W podstawowym podsumowaniu sprawdzamy liczbę braków. Dla używanego zbioru nie widać braków w analizowanych kolumnach.

### Hipotezy

**Pytanie:** Dlaczego dla hipotezy 1 użyto testu t Welcha?  
**Odpowiedź:** Porównujemy średnią ocenę `G3` w dwóch niezależnych grupach. Wersja Welcha jest bezpieczna przy nierównych liczebnościach albo wariancjach.

**Pytanie:** Dlaczego dla hipotezy 2 i 4 użyto testu U Manna-Whitneya?  
**Odpowiedź:** Porównywane zmienne są porządkowe. Test Manna-Whitneya nie wymaga normalności rozkładu.

**Pytanie:** Dlaczego dla hipotezy 3 użyto testu chi-kwadrat?  
**Odpowiedź:** Sprawdzamy zależność między dwiema zmiennymi kategorycznymi: wyższe wykształcenie rodzica tak/nie oraz plan studiów tak/nie.

**Pytanie:** Czy istotność statystyczna oznacza silny efekt?  
**Odpowiedź:** Nie zawsze. Istotność mówi, że wynik raczej nie jest przypadkowy, ale siłę efektu trzeba oceniać osobno.

### Regresja

**Pytanie:** Dlaczego regresja klasyczna nie działa bezpośrednio na tekstowych kategoriach?  
**Odpowiedź:** Model OLS wymaga wartości liczbowych. Zmienne tekstowe kodujemy przez `C(zmienna)` albo zmienne zero-jedynkowe.

**Pytanie:** Co oznacza współczynnik regresji?  
**Odpowiedź:** Pokazuje, jak zmienia się przewidywana wartość `G3`, gdy dana zmienna rośnie o 1 jednostkę, przy założeniu że pozostałe zmienne są stałe.

**Pytanie:** Co oznacza `R2`?  
**Odpowiedź:** To część zmienności `G3`, którą wyjaśnia model. Model bazowy wyjaśnia około 26%, a rozszerzony około 29%.

**Pytanie:** Po co liczymy VIF?  
**Odpowiedź:** VIF sprawdza współliniowość zmiennych objaśniających. Niskie VIF-y oznaczają brak dużego problemu współliniowości.

**Pytanie:** Co to jest homoskedastyczność?  
**Odpowiedź:** To założenie, że wariancja reszt jest podobna dla różnych poziomów wartości przewidywanych.

**Pytanie:** Jak sprawdzono homoskedastyczność?  
**Odpowiedź:** Testem Breuscha-Pagana. W modelu bazowym p-value = 0.0028, a w rozszerzonym p-value = 0.0043, więc w obu przypadkach pojawia się problem heteroskedastyczności.


**Pytanie:** Czy modele regresji są przyczynowe?  
**Krótka odpowiedź:** Nie, modele pokazują zależności statystyczne, ale nie dowodzą przyczynowości.  
**Dłuższa odpowiedź:** Regresja pokazuje, które zmienne są powiązane z oceną `G3` przy kontroli pozostałych zmiennych. Nie mamy jednak eksperymentu ani losowego przypisania uczniów do warunków, więc nie można powiedzieć, że dana zmienna na pewno powoduje zmianę oceny. Możemy mówić o związku, a nie o przyczynie.

**Pytanie:** Co zrobić, jeśli pojawia się heteroskedastyczność?  
**Krótka odpowiedź:** Model można interpretować opisowo, ale do ścisłego wnioskowania warto użyć odpornych błędów standardowych.  
**Dłuższa odpowiedź:** Heteroskedastyczność oznacza, że wariancja reszt nie jest stała, więc klasyczne błędy standardowe mogą być mniej wiarygodne. Współczynniki regresji nadal można opisywać, ale ostrożniej interpretujemy ich istotność. Typowym rozwiązaniem jest użycie odpornych błędów standardowych, np. HC3.

**Pytanie:** Czy test chi-kwadrat ma założenia?  
**Krótka odpowiedź:** Tak, najważniejsze są niezależność obserwacji i odpowiednio duże oczekiwane liczebności w tabeli.  
**Dłuższa odpowiedź:** Test chi-kwadrat zakłada, że obserwacje są niezależne, czyli jeden uczeń nie powinien wpływać na wynik drugiego ucznia. Drugi warunek dotyczy oczekiwanych liczebności w komórkach tabeli kontyngencji, które nie powinny być zbyt małe. Jeśli oczekiwane liczebności są bardzo małe, test chi-kwadrat może być mniej wiarygodny.

### TOM

**Pytanie:** Co trzeba uzasadnić przy symulacji kolejki?  
**Odpowiedź:** Rozkłady przyjść i obsługi, liczbę stanowisk, dyscyplinę kolejki FIFO oraz analizowaną charakterystykę, czyli średni czas oczekiwania pasażera.

**Pytanie:** Dlaczego w symulacji można użyć rozkładu wykładniczego?  
**Odpowiedź:** Bo modelujemy losowe odstępy między niezależnymi przyjściami pasażerów. To klasyczne założenie w prostych modelach kolejkowych.



**Pytanie:** Dlaczego czas obsługi ma rozkład trójkątny?  
**Odpowiedź:** Bo dla zakupu biletu można rozsądnie określić minimalny, typowy i maksymalny czas obsługi. Rozkład trójkątny dobrze pasuje do takiej sytuacji.

**Pytanie:** Co oznacza wykorzystanie biletomatu około 78.9%?  
**Odpowiedź:** Oznacza to, że biletomat jest zajęty przez około 78.9% czasu symulacji. System jest mocno używany, ale nie pracuje cały czas na granicy możliwości.

**Pytanie:** Co mówi średni czas oczekiwania 4.027 min?  
**Odpowiedź:** Oznacza to, że w 100 powtórzeniach symulacji pasażer czekał przeciętnie około 4 minuty na rozpoczęcie obsługi przy biletomacie.

**Pytanie:** Jak interpretować histogram średniego czasu oczekiwania?  
**Odpowiedź:** Histogram pokazuje rozrzut średnich czasów oczekiwania z kolejnych powtórzeń symulacji. Większość wyników jest w okolicy kilku minut, ale zdarzają się przebiegi z dłuższym oczekiwaniem.

**Pytanie:** Co może być wynikiem symulacji?  
**Odpowiedź:** Średni czas oczekiwania, średnia długość kolejki, maksymalna długość kolejki, wykorzystanie biletomatu i liczba obsłużonych pasażerów.