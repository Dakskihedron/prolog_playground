(define (problem q1)
  (:domain delivery2)
  (:objects
    c1 c2 sfo jfk p1 p2
  )
  (:init
    (at c1 sfo)
    (at c2 jfk)
    (at p1 sfo)
    (at p2 jfk)
    (cargo c1)
    (cargo c2)
    (plane p1)
    (plane p2)
    (airport jfk)
    (airport sfo)
  )
  (:goal
    (and
      (at c1 jfk)
      (at c2 sfo)
    )
  )
)