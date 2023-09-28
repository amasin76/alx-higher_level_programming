#!/bin/bash
# Sends a JSON POST request
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
