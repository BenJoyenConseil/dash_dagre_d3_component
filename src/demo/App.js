/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';
import * as d3 from 'd3'

import { DagreD3 } from '../lib';
import '../../dash_dagre/dash_dagre_style.css';

class App extends Component {

    constructor() {
        super();
        this.state = {
            nodes: {
                '1': {
                    label: 'Node 1',
                    output_table: 'table_1'
                },
                '2': {
                    label: 'Node 2'
                },
                '3': {
                    label: 'Node 3'
                },
                '4': {
                    label: 'Node 4'
                },
                '5': {
                    label: 'Node 5'
                },
                '6': {
                    label: 'Node 6'
                }
            },
            edges: [
                ['1', '2', {curve: d3.curveBasis}],
                ['1', '3', {curve: d3.curveBasis}],
                ['2', '4', {curve: d3.curveBasis}],
                ['2', '3', {curve: d3.curveBasis}],
                ['1', '4', {curve: d3.curveBasis}],
                ['5', '4', {curve: d3.curveBasis}],
                ['6', '4', {curve: d3.curveBasis}],
                ['3', '4', {curve: d3.curveBasis}]
            ],
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <DagreD3
                    setProps={this.setProps}
                    {...this.state}
                />
            </div>
        )
    }
}

export default App;
