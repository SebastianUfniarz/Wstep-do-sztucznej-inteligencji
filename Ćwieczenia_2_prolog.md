## ZAD2.
Załóżmy, że w pewnej bazie zdefiniowano wyłącznie predykaty: rodzic oraz mężczyzna. Załóżmy
ponadto, że zakresem rozważań jest zbiór osób – jako dodatkowy, trzeci predykat. Opierając się na
tych trzech predyklatach zdefiniuj w języku Prolog kolejno każdą z poniższych reguł:
1. kobieta(X)
2. ojciec(X,Y) – X jest ojcem Y
3. matka(X,Y) – X jest matką Y
4. corka(X,Y) – X jest córką Y
5. brat_rodzony(X,Y) – X jest rodzonym bratem Y
6. brat_przyrodni(X,Y) – X jest przyrodnim bratem Y
7. kuzyn(X,Y) – X jest kuzynem Y
8. dziadek_od_strony_ojca(X,Y) – X jest dziadkiem od strony ojca dla Y
9. dziadek_od_strony_matki(X,Y) – X jest dziadkiem od strony matki dla Y
10. dziadek(X,Y) – X jest dziadkiem Y
11. babcia(X,Y) – X jest babcią Y
12. wnuczka(X,Y) – Y jest wnuczką X
13. przodek_do2pokolenia_wstecz(X,Y) – X jest przodkiem Y do drugiego pokolenia wstecz
14. przodek_do3pokolenia_wstecz(X,Y) - X jest przodkiem Y do trzeciego pokolenia wstecz
Podczas tworzenia reguł nie można korzystać z definicji reguł, które nie zostały jeszcze w bazie
podane. Oznacza to, że np.:
- definiując regułę kobieta możemy korzystać wyłącznie z predykatów osoba, mezczyzna, rodzic;
- definiując regułę ojciec możemy korzystać wyłącznie z predykatów osoba, mezczyzna, rodzic
oraz reguły kobieta;
- definiując regułę matka możemy korzystać wyłącznie z predykatów osoba, mezczyzna, rodzic
oraz reguł kobieta, ojciec;
itd.
--------------------------------------------------------------------------------------------
kobieta(X) :- 
    osoba(X), 
    \+ mezczyzna(X).

ojciec(X, Y) :- 
    mezczyzna(X), 
    rodzic(X, Y).

matka(X, Y) :-
    kobieta(X),
    rodzic(X, Y).

corka(X, Y) :- 
    kobieta(X), 
    matka(Y, X).

brat_rodzony(X, Y) :- 
    mezczyzna(X),
    matka(M, X), 
    matka(M, Y), 
    X \= Y.

brat_przyrodni(X, Y) :-
   mezczyzna(X), <br />	
   ( <br />	
       (   % Jeśli X ma wspólnego ojca i różne matki <br />	
           ojciec(Ojciec, X), ojciec(Ojciec, Y), <br />	
           matka(MatkaX, X), matka(MatkaY, Y), <br />	
           X \= Y, MatkaX \= MatkaY <br />	
       ); <br />	
       (   % Jeśli X ma wspólną matkę i różnych ojców <br />	
           matka(Matka, X), matka(Matka, Y), <br />	
           ojciec(OjciecX, X), ojciec(OjciecY, Y), <br />	 
           X \= Y, OjciecX \= OjciecY <br />	
       ) <br />	
   ).
   
kuzyn(X, Y) :-
    rodzic(RodzicX, X),
    rodzic(RodzicY, Y),
    ((brat_rodzony(RodzicX, RodzicY), X \= Y);
    (brat_rodzony(RodzicY, RodzicX), X \= Y)).

dziadek_od_strony_ojca(X, Y) :-
    mezczyzna(X),
    rodzic(Ojciec, Y),
    rodzic(X, Ojciec),
    mezczyzna(Ojciec).

dziadek_od_strony_matki(X, Y) :-
    mezczyzna(X),
    rodzic(Matka, Y),
    rodzic(X, Matka),
    kobieta(Matka).

dziadek(X, Y) :-
    dziadek_od_strony_ojca(X, Y);
    dziadek_od_strony_matki(X, Y).

babcia(X, Y) :-
    rodzic(RodzicY, Y),
    matka(X, RodzicY).

wnuczka(X, Y) :-
    kobieta(Y),
    rodzic(X, RodzicX),
    rodzic(RodzicX, Y).

przodek_do2pokolenia_wstecz(X, Y) :-
    dziadek(Y, X);
    babcia(Y, X),
    X \= Y.

przodek_do3pokolenia_wstecz(X, Y) :-
    (rodzic(Z, X), przodek_do2pokolenia_wstecz(Z, Y)),
    X \= Y.
