# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AllotaxonometerForAll(Component):
    """An AllotaxonometerForAll component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- data (list; optional):
    The allotaxonometer data. Should have the form:
    `[{\"x1\":0,\"y1\":0,\"coord_on_diag\":0,\"cos_dist\":0,\"rank\":\"(1,
    1)\",\"rank_L\":[1,1],\"rank_R\":[1,1],\"value\":1,\"types\":\"Mary\",\"which_sys\":\"right\"}...]`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'allotaxonometer_for_all'
    _type = 'AllotaxonometerForAll'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AllotaxonometerForAll, self).__init__(**args)
