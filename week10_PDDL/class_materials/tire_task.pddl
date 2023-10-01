(define (problem tire1)
  (:domain tire)
  (:objects tr)
  
  (:init (tire Flat) (tire Spare) (at Flat Axle) (at Spare Trunk)
  )
  (:goal (at Spare Axle)
  )
)