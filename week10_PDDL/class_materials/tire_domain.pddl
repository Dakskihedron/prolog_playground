(define (domain tire)
  (:requirements :strips)
  (:predicates
   (at ?thing ?place) (tire ?tr) 
  )
  (:constants Flat Spare Axle Trunk Ground)
  (:action remove  
    :parameters (?obj ?loc)
    :precondition (at ?obj ?loc)
    :effect (and (not (at ?obj ?loc)) (at ?obj Ground))
  )
  (:action puton
    :parameters (?tr)
    :precondition (and (tire ?tr) (at ?tr Ground) (not (at Flat Axle)))
    :effect (and (not (at ?tr Ground)) (at ?tr Axle))
  )
  (:action leave
    :parameters ()
    :effect (and (not (at Spare Ground)) (not (at Spare Axle)) (not (at Spare Trunk)) 
                 (not (at Flat Axle))  (not (at Flat Ground))  (not (at Flat Trunk))
            )
  )
)

