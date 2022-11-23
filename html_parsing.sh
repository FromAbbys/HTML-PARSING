#!/bin/bash
#

echo "######################################################################"
echo "|                                                                    |"
echo "|                         HTML PARSING                               |"
echo "|                                                                    |"
echo "######################################################################"


TEMP=$1
echo "Welcome to the HTML Parsing"

grabing_index(){
        echo
        wget -q $TEMP 
        cat index.html | grep "href" | egrep "http|https" | cut -d "/" -f3 | cut -d '"' -f1 > urls && rm -f index.html
        echo "URLS ENCONTRADAS NO $TEMP:"
        cat urls
}

lookup(){
        echo 
        echo "Os endereços IPS referentes aos enderecos encontrados sao os seguintes:\n"
        for X in `cat urls`
        do
                host $X
        done
        rm -f urls
}

grabing_index
lookup
