const rawData = [
    ['AA', 'AB', 67],
    ['AB', 'AC', 298],
    ['AB', 'AL', 244],
    ['AC', 'AD', 186],
    ['AC', 'AK', 140],
    ['AD', 'AE', 142],
    ['AD', 'AJ', 158],
    ['AE', 'AF', 326],
    ['AE', 'AI', 134],
    ['AF', 'AG', 474],
    ['AF', 'AH', 150],
    ['AG', 'AH', 128],
    ['AG', 'AR', 156],
    ['AH', 'AI', 138],
    ['AH', 'AQ', 152],
    ['AI', 'AJ', 94],
    ['AI', 'AP', 36],
    ['AJ', 'AK', 156],
    ['AJ', 'AO', 162],
    ['AK', 'AL', 118],
    ['AK', 'AN', 30],
    ['AL', 'AM', 124],
    ['AM', 'AN', 108],
    ['AM', 'AX', 122],
    ['AN', 'AO', 204],
    ['AN', 'AW', 92],
    ['AO', 'AP', 112],
    ['AO', 'AV', 130],
    ['AP', 'AQ', 246],
    ['AP', 'AU', 148],
    ['AQ', 'AR', 100],
    ['AQ', 'AT', 48],
    ['AR', 'AS', 198],
    ['AS', 'AT', 202],
    ['AS', 'BE', 46],
    ['AT', 'AU', 154],
    ['AT', 'BD', 174],
    ['AU', 'AV', 34],
    ['AU', 'BC', 118],
    ['AV', 'AW', 190],
    ['AV', 'BA', 58],
    ['AW', 'AX', 78],
    ['AW', 'AZ', 100],
    ['AX', 'AY', 212],
    ['AY', 'AZ', 158],
    ['AY', 'BJ', 468],
    ['AZ', 'BA', 156],
    ['AZ', 'BJ', 218],
    ['BA', 'BC', 78],
    ['BA', 'BI', 214],
    ['BC', 'BD', 98],
    ['BC', 'BH', 166],
    ['BD', 'BE', 214],
    ['BD', 'BG', 302],
    ['BE', 'BF', 264],
    ['BF', 'BG', 136],
    ['BF', 'ZZ', 22],
    ['BG', 'BH', 166],
    ['BH', 'BI', 162],
    ['BI', 'BJ', 88],
]

function parseData(rawData) {
    let nodes = new Set();
    let edges = [];

    rawData.forEach(parts => {
        let from = parts[0];
        let to = parts[1];
        let weight = parseInt(parts[2]);

        // Add nodes to set (unique values only)
        nodes.add(from);
        nodes.add(to);

        // Add edge
        edges.push({from, to, label: weight.toString(), value: weight});
    });

    // Convert nodes set to array of objects
    let nodesArray = Array.from(nodes).map(node => ({id: node, label: node}));

    return {nodes: nodesArray, edges};
}

let {nodes, edges} = parseData(rawData);
nodes = new vis.DataSet(nodes);
edges = new vis.DataSet(edges);
let nodeSelectedEdgesCount = new Map();

// Create a network
const container = document.getElementById('mynetwork');
const data = {nodes: nodes, edges: edges};
const options = {
    physics: false, // Disable physics for static graph
    interaction: {
        selectConnectedEdges: false
    }
};
const network = new vis.Network(container, data, options);

// Global score variable and selected edges set
let totalScore = 0;
let selectedEdges = new Set();

// Handling click event on edges
network.on("selectEdge", function (params) {
    if (params.edges.length === 1) {
        const edgeId = params.edges[0];
        const edge = edges.get(edgeId);

        // Toggle highlight and update score
        if (selectedEdges.has(edgeId)) {
            // Edge is already selected, unselect it
            unhighlightEdge(edgeId);
            updateScore(-edge.value); // Subtract the value from score
            selectedEdges.delete(edgeId); // Remove from the set
        } else {
            // Edge is not selected, select it
            highlightEdge(edgeId);
            updateScore(edge.value); // Add the value to score
            selectedEdges.add(edgeId); // Add to the set
        }

        // After updating selected edges, update node colors
        updateNodeColors();
    }
});

// Function to highlight the edge
function highlightEdge(edgeId) {
    edges.update({id: edgeId, color: {color:'red'}});
}

// Function to unhighlight the edge
function unhighlightEdge(edgeId) {
    edges.update({id: edgeId, color: {inherit: 'from'}}); // Resetting to default color
}

// Updating score function
function updateScore(value) {
    totalScore += value;
    document.getElementById('score').innerText = totalScore;
}

// Prevent the default context menu from appearing on right click
container.addEventListener('contextmenu', function (event) {
    event.preventDefault();
}, false);

// Handling right-click event on edges to remove them
network.on("oncontext", function (params) {
    // Prevent the browser's context menu from appearing
    params.event.preventDefault();

    // Identify if an edge was clicked
    const edgeId = this.getEdgeAt(params.pointer.DOM);

    // If an edge is clicked, remove it
    if (edgeId) {
        removeEdge(edgeId);
    }

    // After removing an edge, update node colors
    updateNodeColors();
});

// Function to remove edge
function removeEdge(edgeId) {
    // Remove from the vis DataSet
    edges.remove({id: edgeId});

    // Update the score and selected edges if this edge was highlighted
    if (selectedEdges.has(edgeId)) {
        const edge = edges.get(edgeId);
        updateScore(-edge.value); // Subtract the value from the score
        selectedEdges.delete(edgeId); // Remove from the set of selected edges
    }
}

// Function to update node colors
function updateNodeColors() {
    // Reset all counts to zero initially
    nodeSelectedEdgesCount.clear();
    nodes.forEach((node) => {
        nodeSelectedEdgesCount.set(node.id, 0);
    });

    // Count the number of selected edges for each node
    selectedEdges.forEach(edgeId => {
        const edge = edges.get(edgeId);
        nodeSelectedEdgesCount.set(edge.from, (nodeSelectedEdgesCount.get(edge.from) || 0) + 1);
        nodeSelectedEdgesCount.set(edge.to, (nodeSelectedEdgesCount.get(edge.to) || 0) + 1);
    });

    // Update the node color based on the count
    nodeSelectedEdgesCount.forEach((count, nodeId) => {
        if (count === 2) {
            nodes.update({id: nodeId, color: {background: 'green'}});
        } else {
            nodes.update({id: nodeId, color: {background: 'lightgray'}}); // default color or whatever it was initially
        }
    });
}