const d3 = require('d3')

export default class AllotaxD3 {
    
    constructor(el, figure, onChange) {
        const self = this;

        const max_rank = d3.max(diamond_dat, (d) => d.rank_L[1]);
        const xyDomain   = [1, 10**Math.ceil(Math.max(Math.log10(max_rank))-1)];
        const xyScale    = d3.scaleLog().domain(xyDomain).range([0, 512])
        const max_xy   = d3.max(diamond_dat, d => d.x1) 
        const max_val  = d3.max(diamond_dat, d => d.value)
        const xy  = d3.scaleBand().domain(d3.range(60)).range([0, 600])
        const color_scale = d3.scaleSequentialLog().domain([max_val, 1]).interpolator(d3.interpolateInferno)


        self.svg = d3.select(el).append('svg');
        self.g = svg.attr("id", "myGraph")   
            .attr('height', 512 + margin.top + margin.bottom)
            .attr('width', 512)
            .attr("viewBox", [0-50, 0, 512 + margin.top+50, 512])
            .append('g');

        svg.selectAll('rect')
            .data(figure.data)
            .enter()
            .append('rect')
            .attr('x', (d) => xy(d.x1))
            .attr('y', (d) => xy(d.y1))
            .attr('width', xy.bandwidth())
            .attr('height', xy.bandwidth())
            .attr('fill', (d) => color_scale(d.value))
            .attr('stroke', 'black')
            .attr('stroke-width', 0.3)

        g.append('g')
         .attr("transform", `translate(0, ${512*canvas_mult_size})`)
         .call(d3.axisBottom(xyScale))
         
        g.append('g').call(d3.axisRight(xyScale));

        self.figure = {};

        self.onChange = onChange;

        self.initialized = false;

        self._promise = Promise.resolve();

        self.update(figure);
    }
}

