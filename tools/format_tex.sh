#!/bin/bash

format_latex() {
    if [ ! -f "$1" ]; then
        exit 1
    fi

    if [[ ! $1 == *.tex ]]; then
        exit 1
    fi

    latexindent -l=localSettings.yaml -w -m -s $1
}

for i in $@; do
	format_latex $i
done
