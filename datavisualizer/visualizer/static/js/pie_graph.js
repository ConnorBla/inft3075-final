// Handle the click event for the 'Update Chart' button
document.getElementById('update-graph').addEventListener('click', function () {
    // Gather all label and value pairs from the input fields
    const labels = [];
    const values = [];
    const headers = []

    const title = document.getElementById('title_label').value.trim() || 'Pie Chart'
    headers.push(title)
    // Get each row in the table
    const rows = document.querySelectorAll('#input-table tbody tr');
    rows.forEach(row => {
        const label = row.querySelector('.label').value.trim();
        const value = parseFloat(row.querySelector('.value').value.trim());
        if (label && !isNaN(value)) {  
            labels.push(label);
            values.push(value);
        }
    });


    fetch('/update_pie_graph/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            labels: labels,
            sizes: values,
            headers: headers
        })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update the image source with the new pie chart image
            document.getElementById('pie-graph').src = 'data:image/png;base64,' + data.plot_image;
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('add-row').addEventListener('click', function () {
    const tableBody = document.querySelector('#input-table tbody');
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td><input type="text" class="label" placeholder="Enter label"></td>
        <td><input type="number" class="value" placeholder="Enter value"></td>
    `;
    tableBody.appendChild(newRow);
});

document.getElementById('download-btn').addEventListener('click', function () {
    const graph = document.getElementById('pie-graph');
    const link = document.createElement('a');
    const title = document.getElementById('title_label').value || "pie-chart"
    link.href = graph.src;  //image source
    link.download = title;  //file name 
    link.click();           //trigger the download 
});