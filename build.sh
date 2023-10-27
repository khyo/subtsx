#!/bin/bash

cd examples/gui
./dist/esbuild ./index.tsx  --sourcemap --outfile=dist/out.js --jsx-factory=h --tree-shaking=false --bundle --jsx-fragment=Fragment
