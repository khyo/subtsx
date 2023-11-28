const { $ } = voby


export function Widget() {
  const value = $(0x45)
  
  return (
    <>
      <h1>Widget</h1>
      <p style="color: red">{value}</p>
    </>
  );
}
