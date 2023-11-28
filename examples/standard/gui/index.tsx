import "./styles.css"

import { Widget } from './widget'
import { delay } from './lib'
const { $, $$, render } = voby



function App() {
  const count = $(0x45)
  console.log("count", count())
  return (
    <>
      <h1>Hello World</h1>
      <a>ASDF</a>
      <button onClick={() => count((count) => count + 1)}>
        count is {count}
      </button>
      <p>
        Edit <code>gui/index.tsx</code>
      </p>
      <Widget />
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
