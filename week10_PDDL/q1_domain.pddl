(define (domain delivery2)
    (:requirements :strips)

    (:predicates
        (at ?thing ?place)
        (plane ?pl)
        (airport ?a)
        (in ?thing ?place)
        (cargo ?thing)
    )
    (:action load
        :parameters (?c ?p ?a)
        :precondition (and (at ?c ?a) (at ?p ?a) (cargo ?c) (plane ?p) (airport ?a))
        :effect (and (in ?c ?p) (not (at ?c ?a)))
    )

    (:action unload
        :parameters (?c ?p ?a)
        :precondition (and (in ?c ?p) (at ?p ?a) (cargo ?c) (plane ?p) (airport ?a))
        :effect (and (at ?c ?a) (not (in ?c ?p)))
    )

    (:action fly
        :parameters (?p ?from ?to)
        :precondition (and (at ?p ?from) (plane ?p) (airport ?from) (airport ?to))
        :effect (and (not (at ?p ?from)) (at ?p ?to))
    )
)