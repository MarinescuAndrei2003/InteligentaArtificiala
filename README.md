# Traveling Salesman Problem Solver

## Problem Statement
The Traveling Salesman Problem (TSP) involves finding the shortest possible route that visits each city exactly once and returns to the origin city. This project provides implementations for various strategies to solve TSP, focusing on minimizing the longest distance between consecutive cities.
## Requirements

This project includes implementations for the following strategies:
- Exhaustive strategies
  - Depth-First Search
  - Least-Cost (Uniform cost) Search
- Heuristic strategy
  - A* Search

For the A* Search strategy, a custom heuristic function and its implementation are provided.

## Pseudocodul Algoritmilor
Pseudocodul detaliat pentru fiecare strategie implementata este furnizat in sectiunile corespunzatoare ale codului.

## Detalii Implementare
Aplicatia pentru rezolvarea Problemei Comerciantului Calator este implementata in Python si include trei algoritmi principali: Cautare in Adancime (DFS), Cautare cu Cost Minim si Cautare A*. Fiecare algoritm si functie utilitara sunt encapsulate in propriul lor modul, permitand flexibilitate in adaugarea sau modificarea algoritmilor si oferind o separare clara a responsabilitatilor.

## Formatul Datelor de Intrare
Datele de intrare pentru aplicatie sunt reprezentate printr-o matrice de adiacenta, unde elementul de pe randul i si coloana j reprezinta distanta intre orasul i si orasul j. Graficul poate fi simetric sau asimetric, in functie de cazul specific.

## Formatul Datelor de Iesire
Iesirea fiecarei functii de rezolvare a Problemei Comerciantului Calator consta in lista care reprezinta traseul optim incepand si terminand la orasul de plecare. Traseul include indicii oraselor vizitate in ordine.

## Lista de Module si Functii
- **dfs.py**: Contine algoritmul de Cautare in Adancime pentru rezolvarea TSP.
- **a_star.py**: Contine algoritmul de cautare A* pentru rezolvarea TSP.
- **least_cost_search.py**: Contine algoritmul de Cautare cu Cost Minim pentru rezolvarea TSP.
- **random_generator.py**: Contine o functie pentru generarea de grafuri TSP aleatorii.
- **main.py**: Scriptul principal pentru testarea si demonstrarea algoritmilor de rezolvare.

## Experimente si Evaluare
Datele de intrare reprezentand distantele dintre orase sunt introduse in cod ca o lista de grafuri. Rezultatul pentru fiecare dintre cele trei functii este o lista care arata traseul cu cel mai mic cost, incepand si terminand in acelasi oras (de exemplu, Bucuresti din tabel). Codul include si o functie pentru generarea unui graf aleatoriu pentru Problema Comerciantului Calator, furnizand date de intrare similare cu exemplul de mai sus.

## Executia Codului
  - Se deschide CMD
  - se tasteaza in consola: python "C:\Desktop\Homework\main.py", Acesta este un exemplu. Nu trebuie neaparat sa fie in Desktop sau in partitia C
## Concluzii
Proiectul a fost unul interesant care a necesitat implementarea unor algoritmi pentru gasirea unui traseu cu cost minim. Python a fost ales ca limbaj de programare datorita lizibilitatii si usurintei de scriere in comparatie cu limbaje precum C++/Java.
