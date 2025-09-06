#!/bin/bash
# Get all repos you own
#
# gh auth login
gh repo list gmweinberg --limit 1000 --json name -q '.[].name' > repos.txt

# Loop through and list open issues + PRs
while read repo; do
  echo "=== $repo ==="
  gh issue list --repo gmweinberg/$repo --state open
  gh pr list --repo gmweinberg/$repo --state open
done < repos.txt

