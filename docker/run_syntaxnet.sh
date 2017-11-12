#!/usr/bin/env bash

docker run -p 9000:9000 -v models:/models -d mitoai/syntaxnet
