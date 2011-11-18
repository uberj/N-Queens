#!/bin/bash

# call do_homework()

do_homework(){
    for i in 1 2 3 4 5 6 7 8 9
    do
        python nqueens.py "$i"
    done
}

speak_to_ta(){
    echo "Hello Nels (White Knight) Oscar."
    echo "This is a \"concise report\"."
    echo "============================="
}

explain_homework(){
    echo "What follows is the number of unique solutions to the N-Queens problem calculated"
    echo "for a N X N board. N starts at 1 and goes up to 9."
    echo
    echo "Enjoy the show! (This report was brought to you by BASH)."
    echo
}

speak_to_ta
explain_homework
do_homework

