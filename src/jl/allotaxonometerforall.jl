# AUTO GENERATED FILE - DO NOT EDIT

export allotaxonometerforall

"""
    allotaxonometerforall(;kwargs...)

An AllotaxonometerForAll component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (Array; optional): The allotaxonometer data. Should have the form:

  `[{"x1":0,"y1":0,"coord_on_diag":0,"cos_dist":0,"rank":"(1, 1)","rank_L":[1,1],"rank_R":[1,1],"value":1,"types":"Mary","which_sys":"right"}...]`
"""
function allotaxonometerforall(; kwargs...)
        available_props = Symbol[:id, :data]
        wild_props = Symbol[]
        return Component("allotaxonometerforall", "AllotaxonometerForAll", "allotaxonometer_for_all", available_props, wild_props; kwargs...)
end

