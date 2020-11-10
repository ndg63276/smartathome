#!/bin/bash

aws s3 sync . s3://smartathome.co.uk/ --exclude ".git*" --exclude "scripts/*" --exclude "*/images/*" --exclude "*/scripts/*" --exclude "*/.git*" --exclude "*json"
