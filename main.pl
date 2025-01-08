homme(pierre).
homme(marc).
homme(paul).
femme(marie).
femme(sophie).

parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).

pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

:- initialization(main).

main :-
    (   pere(pierre, paul), write('Pierre est le père de Paul.'), nl, % Qui est le père de Paul ?
        mere(marie, paul), write('Marie est la mère de Paul.'), nl,  % Qui est la mère de Paul ?
        parent(marc, sophie), write('Marc est le parent de Sophie.'), nl  % Marc est-il le parent de Sophie ?
    ).
    
