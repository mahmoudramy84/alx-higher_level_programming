#!/bin/bash
#takes in a URL as an argument, sends a GET request, displays the body of response
curl "$1" -sH "X-School-User-Id: 98"
