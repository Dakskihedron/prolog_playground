(define (problem bwtask1) (:domain blocks_world) (:objects a b c) 
	(:init
		(on-table b) (on c a) (on-table a) (clear b) (clear c)
	)
	(:goal (and
		(on a b) (on b c))
	)
)