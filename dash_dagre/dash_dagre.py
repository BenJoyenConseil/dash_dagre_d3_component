# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class dash_dagre(Component):
    """A dash_dagre component.


Keyword arguments:
- nodes (dict; required)
- edges (list; required)
- interactive (boolean; optional)
- fit (boolean; optional)
- height (string; optional)
- width (string; optional)
- shapeRenderers (dict with strings as keys and values of type ; optional)

Available events: """
    @_explicitize_args
    def __init__(self, nodes=Component.REQUIRED, edges=Component.REQUIRED, interactive=Component.UNDEFINED, fit=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, shapeRenderers=Component.UNDEFINED, onNodeClick=Component.UNDEFINED, **kwargs):
        self._prop_names = ['nodes', 'edges', 'interactive', 'fit', 'height', 'width', 'shapeRenderers']
        self._type = 'dash_dagre'
        self._namespace = 'dash_dagre'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['nodes', 'edges', 'interactive', 'fit', 'height', 'width', 'shapeRenderers']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['nodes', 'edges']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(dash_dagre, self).__init__(**args)

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
            return ('dash_dagre(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'dash_dagre(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
