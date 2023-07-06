import allotaxonometer_for_all
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

sample_data = [
    {"x1":0,"y1":0,"coord_on_diag":0,"cos_dist":0,"rank":"(1, 1)","rank_L":[1,1],"rank_R":[1,1],"value":1,"types":"Mary","which_sys":"right"},
    {"x1":4,"y1":4,"coord_on_diag":4,"cos_dist":0,"rank":"(2, 2)","rank_L":[2,2],"rank_R":[2,2],"value":1,"types":"Anna","which_sys":"right"},
    {"x1":7,"y1":7,"coord_on_diag":7,"cos_dist":0,"rank":"(3, 3)","rank_L":[3,3],"rank_R":[3,3],"value":1,"types":"Emma","which_sys":"right"},
    {"x1":9,"y1":9,"coord_on_diag":9,"cos_dist":0,"rank":"(4, 4)","rank_L":[4,4],"rank_R":[4,4],"value":1,"types":"Elizabeth","which_sys":"right"},
    {"x1":11,"y1":10,"coord_on_diag":10.5,"cos_dist":1,"rank":"(5, 6)","rank_L":[5,5],"rank_R":[6,6],"value":1,"types":"Minnie","which_sys":"left"},
    {"x1":10,"y1":11,"coord_on_diag":10.5,"cos_dist":1,"rank":"(6, 5)","rank_L":[6,6],"rank_R":[5,5],"value":1,"types":"Margaret","which_sys":"right"},
    {"x1":14,"y1":12,"coord_on_diag":13,"cos_dist":4,"rank":"(7, 9)","rank_L":[7,7],"rank_R":[9,9],"value":1,"types":"Ida","which_sys":"left"},
    {"x1":15,"y1":13,"coord_on_diag":14,"cos_dist":4,"rank":"(8, 11)","rank_L":[8,8],"rank_R":[11,11],"value":1,"types":"Alice","which_sys":"left"},
    {"x1":13,"y1":14,"coord_on_diag":13.5,"cos_dist":1,"rank":"(9, 8)","rank_L":[9,9],"rank_R":[8,8],"value":1,"types":"Bertha","which_sys":"right"},
    {"x1":15,"y1":15,"coord_on_diag":15,"cos_dist":0,"rank":"(11, 10)","rank_L":[11,11],"rank_R":[10,10],"value":1,"types":"Annie","which_sys":"right"}
]

app.layout = html.Div([
    allotaxonometer_for_all.AllotaxonometerForAll(
        id='input', data=sample_data
    ),
    html.Div(id='output')
])


@callback(Output('output', 'children'), Input('input', 'value'))
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
