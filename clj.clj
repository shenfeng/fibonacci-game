(defn f [n]
  (if (> n 1)
    (+ (f (- n 1)) (f (- n 2)))
    1))

;; java -cp ../rssminer/lib/clojure-1.4.0.jar clojure.main clj.clj
(let [start (System/currentTimeMillis)
      result (f 40)]
  (println (- (System/currentTimeMillis) start))
  (println result))
