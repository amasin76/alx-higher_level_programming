#!/bin/bash
# Displays the size of the body of the response

URL=$1
curl -s "$URL" | wc -c
