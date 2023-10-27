/* Copyright Subinitial LLC, Author: Kyle Howen */
/// <reference types="./electron" />

import path from 'node:path';
import fs from 'node:fs/promises'
import * as esbuild from './esbuild_bundleable'

interface Options {
  esbuild: string
  wd: string
  entry: string
  cache: string
  fresh: boolean
}

export async function main(mainWindow: Electron.BrowserWindow) {
  const opts: Options = JSON.parse(process.argv[3]) 
  await build(mainWindow, opts)
}

async function build(mainWindow: Electron.BrowserWindow, opts: Options) {
  let defaults = path.join(__dirname, '..', 'root')

  let procs: Promise<any>[] = []
  if (opts.fresh) {
    procs.push(
      fs.copyFile(path.join(defaults, 'index.html'), path.join(opts.cache, 'index.html')),
      fs.copyFile(path.join(defaults, 'lib.js'),     path.join(opts.cache, 'lib.js'))
    )
  }
  
  // custom hacked esbuild receives our binpath this way
  process.env.ESBUILD_BINARY_PATH = opts.esbuild
  const outfile = path.join(opts.cache, 'out.js')

  let reloadPlugin = {
    name: 'reloadPlugin',
    setup(build) {
      build.onEnd(result => {
        if (result.errors.length == 0) {
          mainWindow.loadFile(path.join(opts.cache, 'index.html'))
        }
      })
    },
  }

  const ctx = await esbuild.context({
    entryPoints: [opts.entry],
    absWorkingDir: opts.wd,
    outfile,
    bundle: true,
    jsxFactory: 'h',
    jsxFragment: 'Fragment',
    plugins: [reloadPlugin],
  })
  procs.push(ctx.watch())

  await Promise.all(procs)
}
