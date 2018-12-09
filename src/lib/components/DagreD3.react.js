import React, {Component} from 'react';
import PropTypes from 'prop-types'
import * as dagreD3 from 'dagre-d3'
import * as d3 from 'd3'

import isEqual from 'react-fast-compare'

export default class DagreD3 extends Component {
    constructor(props) {
        super(props);
    }

    shouldComponentUpdate(nextProps, nextState) {
        return !isEqual(this.props.data.nodes, nextProps.data.nodes) ||
            !isEqual(this.props.data.edges, nextProps.data.edges) ||
            !isEqual(this.props.zoom, nextProps.zoom)
    }

    componentDidMount() {
        this.renderDag();
    }

    componentDidUpdate() {
        this.renderDag();
    }

    renderDag() {
         const {id, setProps} = this.props;

        let g = new dagreD3.graphlib.Graph().setGraph({});

        for (let [id, node] of Object.entries(this.props.data.nodes))
            g.setNode(id, node);

        for (let edge of this.props.data.edges){
            if(edge[2].curve && edge[2].curve == 'd3.curveBasis')
                edge[2].curve = d3.curveBasis
            g.setEdge(edge[0], edge[1], edge[2]); // from, to, props
        }

        // Set up an SVG group so that we can translate the final graph.
        let svg = d3.select(this.nodeTree);
        let inner = d3.select(this.nodeTreeGroup);

        // set up zoom support
        if (this.props.interactive) {
            let zoom = d3.zoom().on("zoom",
                () => inner.attr("transform", d3.event.transform));
            svg.call(zoom);
        }

        // Create the renderer
        let render = new dagreD3.render();

        // set up custom shape renderers
        if (this.props.shapeRenderers)
            for (let [shape, renderer] of Object.entries(this.props.shapeRenderers))
                render.shapes()[shape] = renderer;

        // Run the renderer. This is what draws the final graph.
        render(inner, g);


        // TODO add padding?
        if (this.props.fit) {
            let {height: gHeight, width: gWidth} = g.graph();
            let {height, width} = this.nodeTree.getBBox();
            let transX = width - gWidth;
            let transY = height - gHeight;
            svg.attr("height", height);
            svg.attr("width", width);
            inner.attr("transform", d3.zoomIdentity.translate(transX, transY))
        }

        svg.selectAll('.dagre-d3 .node').on('click',
                id => {
                    setProps({selectedId: id})
                    setProps({selectedNodeProps: this.props.data.nodes[id]})
                });
    }

    render() {
        return (
            <svg className='dagre-d3' ref={(r) => {this.nodeTree = r}}
                 width={this.props.height}
                 height={this.props.width}>

                <g ref={(r) => {this.nodeTreeGroup = r}}/>
            </svg>
        );
    }
}


DagreD3.defaultProps = {
    height: "1",
    width: "1",
    // width and height are defaulted to 1 due to a FireFox bug(?) If set to 0, it complains.
    fit: true,
    interactive: true,
    data: {
        'nodes': {},
        'edges': []
    }
};

DagreD3.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,
        /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,
    /*
    data: {
        'nodes': {},
        'edges': []
    }
    */
    data: PropTypes.object.isRequired,

    interactive: PropTypes.bool,
    fit: PropTypes.bool,
    height: PropTypes.string,
    width: PropTypes.string,
    shapeRenderers: PropTypes.objectOf(PropTypes.func),
    onNodeClick: PropTypes.func,
    selectedId: PropTypes.string,
    selectedNodeProps: PropTypes.object,
};
