package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		_, err := fmt.Fprintln(w, "Hello World!")
		if err != nil {
			panic(err)
		}
	})
	log.Fatalf("error: %s", http.ListenAndServe(":8080", nil))
}
