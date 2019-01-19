from dash_dagre import DagreD3
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div(id='svg_container', children=[
    DagreD3(
        id="dag",
        nodes={
            '1': {
                'label': 'Node 1',
                'specific_property': 'some specificities',
                'rx': 10,
                'ry': 10,
            },
            '2': {
                'label': 'Node 2',
                'rx': 5,
                'ry': 5,
            },
            '3': {
                'label': 'Node3',
                'rx': 5,
                'ry': 5,
            },
            '4': {
                'label': 'Node 4',
                'rx': 5,
                'ry': 5,
            },
            '5': {
                'label': 'Node 5',
                'rx': 5,
                'ry': 5,
            },
            '6': {
                'label': 'Node 6',
                'rx': 5,
                'ry': 5,
            }
        }
        ,
        edges=[
            ['1', '2', {'curve': 'd3.curveBasis'}],
            ['1', '3', {'curve': 'd3.curveBasis'}],
            ['2', '4', {'curve': 'd3.curveBasis'}],
            ['2', '3', {'curve': 'd3.curveBasis'}],
            ['1', '4', {'curve': 'd3.curveBasis'}],
            ['5', '4', {'curve': 'd3.curveBasis'}],
            ['6', '4', {'curve': 'd3.curveBasis'}],
            ['3', '4', {'curve': 'd3.curveBasis'}]
        ]
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('dag', 'selectedId'),Input('dag', 'selectedNodeProps')]
)
def show_task_info(selectedId, selectedNodeProps):
    if selectedId is not None and selectedNodeProps is not None:
        output_table = selectedNodeProps.get('specific_property', 'out sepcificity')
        s = "You have selected node #{} with {}".format(selectedId, output_table)
        return s

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_serve_dev_bundles=False)
