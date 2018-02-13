#!/bin/bash

gitBranch = $1

git add --all
git commit -m "Updated url/description"
git push origin $gitBranch
