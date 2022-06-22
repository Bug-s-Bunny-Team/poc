#!/bin/bash

# need to install https://github.com/openapitools/openapi-generator-cli

openapi-generator-cli generate -g markdown -i openapi.yaml
