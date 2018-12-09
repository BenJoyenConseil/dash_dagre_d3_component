/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { DagreD3 } from '../lib';
import '../../dash_dagre/style.css';

class App extends Component {

    constructor() {
        super();
        this.state = {
                nodes: {
                    '1': {
                        label: 'Node 1'
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
                    ['1', '2', {}],
                    ['1', '3', {}],
                    ['2', '4', {}],
                    ['2', '3', {}],
                    ['1', '4', {}],
                    ['5', '4', {}],
                    ['6', '4', {}],
                    ['3', '4', {}]
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
