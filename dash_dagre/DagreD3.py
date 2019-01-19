# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DagreD3(Component):
    """A DagreD3 component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- nodes (dict; optional)
- edges (list; optional)
- interactive (boolean; optional)
- fit (boolean; optional)
- height (string; optional)
- width (string; optional)
- shapeRenderers (dict with strings as keys and values of type ; optional)
- selectedId (string; optional)
- selectedNodeProps (dict; optional)

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, nodes=Component.UNDEFINED, edges=Component.UNDEFINED, interactive=Component.UNDEFINED, fit=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, shapeRenderers=Component.UNDEFINED, onNodeClick=Component.UNDEFINED, selectedId=Component.UNDEFINED, selectedNodeProps=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'nodes', 'edges', 'interactive', 'fit', 'height', 'width', 'shapeRenderers', 'selectedId', 'selectedNodeProps']
        self._type = 'DagreD3'
        self._namespace = 'dash_dagre'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'nodes', 'edges', 'interactive', 'fit', 'height', 'width', 'shapeRenderers', 'selectedId', 'selectedNodeProps']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DagreD3, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DagreD3(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DagreD3(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
