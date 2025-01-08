homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(marie).
femme(sophie).


parent(pierre, paul).
parent(marie, paul).
parent(louis, pierre).
parent(marc, sophie).
parent(jacques, marc).


pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

a_enfant(X) :- parent(X, _). 

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

:- initialization(main).

main :-
    (   pere(pierre, paul), write('Pierre est le père de Paul.'), nl, % Qui est le père de Paul ?
        mere(marie, paul), write('Marie est la mère de Paul.'), nl,  % Qui est la mère de Paul ?
        parent(marc, sophie), write('Marc est le parent de Sophie.'), nl,  % Marc est-il le parent de Sophie ?
        pere(jacques, marc), write('Jacques est le père de Marc'), nl, % Qui est le père de Marc ?
        a_enfant(marc), write('Marc a des enfants'), nl, % Est-ce que Marc a des enfants ?
        grandparent(X, paul), write(X), write(' est le grandparent de Paul'), nl, % Qui est le grand père de Paul ?
        grandparent(jacques, sophie), write('jacques est le grandparent de Sophie'), nl % Jacques est-il le grand-parent de Sophie ?
    ).
    
    
