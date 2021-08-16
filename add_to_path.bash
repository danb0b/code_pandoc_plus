#!/usr/bin/bash

echo "export PATH=\$PATH:$PWD/python/pandoc_plus" >> ~/.bashrc
chmod +x python/pandoc_plus/pandoc-plus
chmod +x python/pandoc_plus/pp-beamer

