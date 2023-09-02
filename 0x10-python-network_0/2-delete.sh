#!/bin/bash
sends a DELETE request to the URL passed as the first argument, displays the body
curl -s -X DELETE "$1"
