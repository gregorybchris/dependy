let svg = d3.select("svg")
let width = +svg.attr("width")
let height = +svg.attr("height")

let color = d3.scaleOrdinal(d3.schemeCategory20)

let simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(d => d.id))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2))

d3.json("static/data/miserables.json", function(error, graph) {
    if (error)
        throw error

    let link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("stroke-width", d => Math.sqrt(d.value))

    let node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
    
    let circles = node.append("circle")
        .attr("r", 5)
        .attr("fill", d => color(d.group))
        .call(d3.drag()
        .on("start", dragStarted)
        .on("drag", dragged)
        .on("end", dragEnded))

    let lables = node.append("text")
        .text(d => d.id)
        .attr('x', 9)
        .attr('y', 3)

    node.append("title")
        .text(d => d.id)

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked)

    simulation.force("link")
        .links(graph.links)

    function ticked() {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y)
        node.attr("transform", d => `translate(${d.x},${d.y})`)
    }
})

function dragStarted(d) {
    if (!d3.event.active)
        simulation.alphaTarget(0.3).restart()
    d.fx = d.x
    d.fy = d.y
}

function dragged(d) {
    d.fx = d3.event.x
    d.fy = d3.event.y
}

function dragEnded(d) {
    if (!d3.event.active)
        simulation.alphaTarget(0)
    d.fx = null
    d.fy = null
}
