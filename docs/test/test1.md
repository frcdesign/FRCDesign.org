# Local Storage Test Page 1

## Demo

<input id="textInput" type="text" placeholder="Enter some text here" style="padding:5px; width: 250px;">
<button onclick="saveData()" style="margin-left: 5px;">Save</button>
<button onclick="loadData()">Load</button>
<button onclick="clearData()">Clear</button>

<p id="output" style="margin-top:10px; font-weight:bold;"></p>

---
<script>
// Save data to local storage
function saveData() {
  const value = document.getElementById('textInput').value;
  localStorage.setItem('testData', value);
  document.getElementById('output').innerText = "Saved: " + value;
}

// Load data from local storage
function loadData() {
  const value = localStorage.getItem('testData');
  document.getElementById('output').innerText = value ? "Loaded: " + value : "Nothing saved yet!";
}

// Clear data from local storage
function clearData() {
  localStorage.removeItem('testData');
  document.getElementById('output').innerText = "Cleared storage.";
}

</script>
