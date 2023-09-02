#!/bin/bash
#takesURL, sends arequest, displays the size of the body
curl -s "$1" | wc -c
