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

