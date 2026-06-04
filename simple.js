if (performance.memory) { console.log("Used JS Heap Size:", performance.memory.usedJSHeapSize); console.log("Total JS Heap Size:", performance.memory.totalJSHeapSize); console.log("JS Heap Size Limit:", performance.memory.jsHeapSizeLimit);
} else { console.log("Memory API not supported."); }

const memoryStore = {};
memoryStore.username = "Marvel Manuza Gulane && coderlava / Coderlava && Grace Manuza Gulane ";
memoryStore.age = 25;
console.log(memoryStore);

const data = [];

setInterval(() => {
  data.push(new Array(100000).fill("memory"));
  console.log(`Stored arrays: ${data.length}`);
}, 1000);

function randomHex(length = 8) {
  const chars = "0123456789abcdef";
  let result = "";

  for (let i = 0; i < length; i++) {
    result += chars[Math.floor(Math.random() * chars.length)];
  }

  return result;
}

function textToHex(text) {
  return Array.from(new TextEncoder().encode(text))
    .map(byte => byte.toString(16).padStart(2, "0"))
    .join("");
}

console.log(textToHex("Hello"));
// 48656c6c6f

function generateHexCode(bytes) {
  return bytes
    .map(byte => `0x${byte.toString(16).padStart(2, "0")}`)
    .join(", ");
}

const data = [72, 101, 108, 108, 111];
console.log(generateHexCode(data));

// 0x48, 0x65, 0x6c, 0x6c, 0x6f

function toHexLiteral(num) {
  return "0x" + num.toString(16).toUpperCase();
}

console.log(toHexLiteral(255));
// 0xFF

console.log(randomHex());     // e.g. "7fa2c4d1"
console.log(randomHex(16));   // e.g. "b93ef0c1a27d4e88"

const code = String(Math.floor(Math.random() * 1000)).padStart(3, '0');
console.log(code);
