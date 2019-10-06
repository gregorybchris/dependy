export class Simulation {
    constructor(graph) {
        this.graph = graph

        this.svg = d3.select("svg")
        this.width = +this.svg.attr("width")
        this.height = +this.svg.attr("height")

        this.color = d3.scaleOrdinal(d3.schemeCategory20)

        this.simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id).strength(0.05))
            .force("charge", d3.forceManyBody(-10))
            .force("center", d3.forceCenter(this.width / 2, this.height / 2))

        this.addSVGDefs()
        this.simulation.tick(1000)
        this.simulation.velocityDecay(0.3)
    }

    addSVGDefs() {
        // this.svg.append('defs').append('marker')
        //     .attrs({
        //         'id': 'arrowhead',
        //         'viewBox': '-0 -5 10 10',
        //         'refX': 13,
        //         'refY': 0,
        //         'orient': 'auto',
        //         'markerWidth': 13,
        //         'markerHeight': 13,
        //         'xoverflow':' visible'
        //     })
        //     .append('svg:path')
        //     .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        //     .attr('fill', '#999')
        //     .style('stroke', 'none');
    }

    simulate() {
        let link = this.svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(this.graph.links)
            .enter().append("line")
            .attr("stroke-width", d => Math.sqrt(d.value))
            // .attr('marker-end', 'url(#arrowhead)')

        let node = this.svg.append("g")
            .attr("class", "nodes")
            .selectAll("g")
            .data(this.graph.nodes)
            .enter().append("g")

        let circles = node.append("circle")
            .attr("r", 5)
            .attr("fill", d => this.color(d.group))
            .call(d3.drag()
            .on("start", this.dragStarted)
            .on("drag", this.dragged)
            .on("end", this.dragEnded))

        let lables = node.append("text")
            .text(d => d.id)
            .attr('x', 9)
            .attr('y', 4)

        node.append("title")
            .text(d => d.id)

        this.simulation
            .nodes(this.graph.nodes)
            .on("tick", this.getTicked(link, node))

        this.simulation.force("link")
            .links(this.graph.links)
    }

    getTicked(link, node) {
        return () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y)
            node.attr("transform", d => `translate(${d.x},${d.y})`)
        }
    }

    dragStarted(d) {
        if (!d3.event.active)
            simulation.alphaTarget(0.3).restart()
        d.fx = d.x
        d.fy = d.y
    }

    dragged(d) {
        d.fx = d3.event.x
        d.fy = d3.event.y
    }

    dragEnded(d) {
        if (!d3.event.active)
            this.simulation.alphaTarget(0)
        d.fx = null
        d.fy = null
    }
}
