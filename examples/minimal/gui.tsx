/// <reference types="./types" />
import "./styles.css"

const  { render } = preact
const  { useState } = preact.hooks


function App() {
  const [count, setCount] = useState(0x45)
  console.log("count", count)
  return (
    <>
      <h1>Hello World</h1>
      <div class="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>gui.tsx</code>
        </p>
      </div>
      <p class="read-the-docs">
        Click on the Vite and Preact logos to learn more
      </p>
    </>
  )
}


function delay(t: number) {
  return new Promise(resolve => setTimeout(resolve, t*1000.0));
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
