
export function delay(t: number) {
  return new Promise(resolve => setTimeout(resolve, t*1000.0));
}
