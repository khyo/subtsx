/// <reference lib="dom" />

import * as _voby from './voby'

declare global {
  const React: any;
  const ipc: Ipc;
  const voby: typeof _voby;
  const h: typeof _voby.h;

  type Handler = (event: string, arg: any) => any

  interface Ipc {
    /** Send one-way event to Superior */
    send(event: string, arg?: any): void
    /** Specify an event handler for one-way event sent from Superior */
    on(event: string, handler: Handler): void
    /** Cancel an event handler and return the handler if one existed */
    cancel(event: string): Handler | null
    /** Ask Superior to perform request with arguments, wait for and return the response */
    ask(req: string, arg?: any, timeout?: number): Promise<any>
  }
}
