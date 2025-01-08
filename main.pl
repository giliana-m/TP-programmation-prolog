homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
homme(tom).
femme(marie).
femme(sophie).
femme(anne).


parent(pierre, paul).
parent(marie, paul).
parent(louis, pierre).
parent(marc, sophie).
parent(jacques, marc).

frere_soeur(anne, paul).
frere_soeur(tom, paul).


pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

a_enfant(X) :- parent(X, _). 

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

 
frere(X, Y) :- homme(X), frere_soeur(X, Y).
soeur(X, Y) :- femme(X), frere_soeur(X, Y).

a_frere_soeur(Y) :- frere(X, Y); soeur(X,Y).

:- initialization(main).

main :-
    (   pere(pierre, paul), write('Pierre est le père de Paul.'), nl, % Qui est le père de Paul ?
        mere(marie, paul), write('Marie est la mère de Paul.'), nl,  % Qui est la mère de Paul ?
        parent(marc, sophie), write('Marc est le parent de Sophie.'), nl,  % Marc est-il le parent de Sophie ?
        pere(jacques, marc), write('Jacques est le père de Marc'), nl, % Qui est le père de Marc ?
        a_enfant(marc), write('Marc a des enfants'), nl, % Est-ce que Marc a des enfants ?
        grandparent(X, paul), write(X), write(' est le grandparent de Paul'), nl, % Qui est le grand père de Paul ?
        grandparent(jacques, sophie), write('jacques est le grandparent de Sophie'), nl, % Jacques est-il le grand-parent de Sophie ?
        a_frere_soeur(paul), write('Paul a des frères et soeurs'), nl % Paul a-t-il des frères ou des sœurs ?
    ).
