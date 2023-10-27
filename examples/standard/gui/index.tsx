/// <reference types="./types" />
import "./styles.css"

import { delay } from './lib'
const  { render } = preact
const  { useState } = preact.hooks


function App() {
  const [count, setCount] = useState(0x45)
  console.log("count", count)
  return (
    <>
      <h1>Hello World</h1>
      <a>ASDF</a>
      <button onClick={() => setCount((count) => count + 1)}>
        count is {count}
      </button>
      <p>
        Edit <code>gui/index.tsx</code>
      </p>
    </>
  )
}

async function ipcTest() {
  const event = 'js-sourced-event'
  console.log('Sending Python an event', event)
  ipc.send(event)

  ipc.on('long-process', async (e, arg) => {
    await delay(arg)
    return `done with ${e}`
  })
  
  const request: [string, any] = ['ping-python', [1, 2]]
  console.log("Sending Python a request:", request)
  const response = await ipc.ask(...request)
  console.log("Python responded with:", response)
}

function main() {
  render(<App />, document.body)
  ipcTest()
}
main();
