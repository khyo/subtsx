/// <reference types="./types" />
import "./styles.css"

const { $, $$, render } = voby

function App() {
  const value = $(0)
  const increment = () => value(v => v + 1);
  const decrement = () => value(v => v - 1);

  return (
    <>
      <h1>Counter</h1>
      <p>{value}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </>
  );
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
