#!/bin/bash

rm -f Gemfile.lock
gem cleanup
bundle clean --force
bundle install
bundle exec jekyll serve --trace #--watch --drafts --config _config.yml,_config_dev.yml