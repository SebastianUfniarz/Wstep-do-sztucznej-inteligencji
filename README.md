"zad.1"

import numpy as np

import matplotlib.pyplot as plt

srednia = 1  
odchylenie_standardowe = 3  
rozmiar = 10000 

dane = np.random.normal(średnia, odchylenie_standardowe, rozmiar)

plt.hist(dane, bins=50, color='blue', edgecolor='black', alpha=0.7)

plt.title('Histogram')

plt.xlabel('Wartość')

plt.ylabel('Częstość')

plt.grid(True)

plt.show()

---------------------------------------------------------------------------------------------------

"zad.2"

data = np.genfromtxt('wine.data', delimiter=',')

odmiana = data[:, 0]

zmienne = data[:, 1:]

min_values = np.min(zmienne, axis=0)

max_values = np.max(zmienne, axis=0)

mean_values = np.mean(zmienne, axis=0)

median_values = np.median(zmienne, axis=0)

std_deviation = np.std(zmienne, axis=0)

for i in range(13):

    print(f'Zmienna {i+1}:')
    
    print(f'  Wartość minimalna: {min_values[i]}')
    
    print(f'  Wartość maksymalna: {max_values[i]}')
    
    print(f'  Średnia: {mean_values[i]}')
    
    print(f'  Mediana: {median_values[i]}')
    
    print(f'  Odchylenie standardowe: {std_deviation[i]}')
    
    print()

---------------------------------------------------------------------------------------------
"zad.3"

data = np.genfromtxt('wine.data', delimiter=',')

odmiana_1 = data[data[:, 0] == 1]

zmienne_ciagle = odmiana_1[:, 1:]

srednie_zmiennych = np.mean(zmienne_ciagle, axis=0)

print("Średnie zmiennych ciągłych dla win odmiany 1:")

for i, srednia in enumerate(srednie_zmiennych):

    print(f'Zmienna {i+1}: {srednia}')

----------------------------------------------------------------------------------------------

"zad.4"

data = np.genfromtxt('wine.data', delimiter=',')

zawartosc_alkoholu = data[:, 1]

plt.hist(zawartosc_alkoholu, bins=20, color='blue', edgecolor='black', alpha=0.7)

plt.title('Histogram zawartości alkoholu w winach')

plt.xlabel('Zawartość alkoholu')

plt.ylabel('Częstość')

plt.grid(True)

plt.show()

---------------------------------------------------------------------------------

"zad.5"

data = np.genfromtxt('wine.data', delimiter=',')

zawartosc_alkoholu = data[:, 1]

odmiana_1 = zawartosc_alkoholu[data[:, 0] == 1]

odmiana_2 = zawartosc_alkoholu[data[:, 0] == 2]

odmiana_3 = zawartosc_alkoholu[data[:, 0] == 3]

plt.figure(figsize=(10, 6))

plt.hist([odmiana_1, odmiana_2, odmiana_3], bins=20, color=['blue', 'red', 'green'], alpha=0.7, label=['Odmiana 1', 'Odmiana 2', 'Odmiana 3'])

plt.title('Histogram zawartości alkoholu w winach dla każdej odmiany')

plt.xlabel('Zawartość alkoholu')

plt.ylabel('Częstość')

plt.legend()

plt.grid(True)

plt.show()

---------------------------------------------------------------------------------

"zad.6"

data = np.genfromtxt('wine.data', delimiter=',')

liczebnosc_odmian = np.bincount(data[:, 0].astype(int))

odmiany = ['Odmiana 1', 'Odmiana 2', 'Odmiana 3']

plt.figure(figsize=(8, 6))

plt.bar(odmiany, liczebnosc_odmian[1:], color='skyblue')

plt.title('Liczebność win każdej z 3 odmian')

plt.xlabel('Odmiana wina')

plt.ylabel('Liczebność')

plt.grid(axis='y')

plt.show()

---------------------------------------------------------------------------------

"zad.7"

data = np.genfromtxt('wine.data', delimiter=',')

zmienna_1 = data[:, 1]

zmienna_2 = data[:, 2]

plt.figure(figsize=(8, 6))

plt.scatter(zmienna_1, zmienna_2, color='skyblue', alpha=0.7)

plt.title('Zawartość alkoholu vs Kwas winowy')

plt.xlabel('Zawartość alkoholu')

plt.ylabel('Kwas winowy')

plt.grid(True)

plt.show()

---------------------------------------------------------------------------------

"zad.8"

data = np.genfromtxt('wine.data', delimiter=',')

zmienna_1 = data[:, 1]  # Zawartość alkoholu

zmienna_2 = data[:, 2]  # Kwas winowy

odmiana_wina = data[:, 0]

plt.figure(figsize=(10, 8))

for odmiana in np.unique(odmiana_wina):

    plt.scatter(zmienna_1[odmiana_wina == odmiana], zmienna_2[odmiana_wina == odmiana], label=f'Odmiana {int(odmiana)}')


plt.title('Wykres rozrzutu: Zawartość alkoholu vs. Kwas winowy z oznaczeniem odmian wina')

plt.xlabel('Zawartość alkoholu')

plt.ylabel('Kwas winowy')

plt.legend()

plt.grid(True)

plt.show()

---------------------------------------------------------------------------------

zad.9

Jak załadować plik, w którym każda odmiana wina ma inny separator? Tzn. zamiast , będzie np.: ; Tab lub :.?

Wystarczy data = np.genfromtxt('wine.data', delimiter=',') i delimiter zmienić na odpowiedni znak


