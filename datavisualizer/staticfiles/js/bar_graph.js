document.getElementById('update-graph').addEventListener('click', function () {
    const labels = [];
    const values = [];
    const headers = [];

    const title = document.getElementById('title_label').value.trim() || 'Line Graph';
    const xLabel = document.getElementById('x_axis_label').value.trim() || 'X-Axis';
    const yLabel = document.getElementById('y_axis_label').value.trim() || 'Y-Axis';

    headers.push(title, xLabel, yLabel);

    const rows = document.querySelectorAll('#input-table tbody tr');

    rows.forEach(row => {
        const label = row.querySelector('.label').value.trim();
        const value = parseFloat(row.querySelector('.value').value.trim());
        if (label && !isNaN(value)) {  
            labels.push(label);
            values.push(value);
        }
    });

    fetch('/update_bar_graph/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            labels: labels,
            values: values,
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
            document.getElementById('bar-graph').src = 'data:image/png;base64,' + data.plot_image;
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
    const graph = document.getElementById('bar-graph');
    const link = document.createElement('a');
    const title = document.getElementById('title_label').value || "bar-graph"
    link.href = graph.src;  //image source
    link.download = title;  //file name 
    link.click();           //trigger the download
});