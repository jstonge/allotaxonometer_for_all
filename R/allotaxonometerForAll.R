# AUTO GENERATED FILE - DO NOT EDIT

#' @export
allotaxonometerForAll <- function(id=NULL, data=NULL) {
    
    props <- list(id=id, data=data)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AllotaxonometerForAll',
        namespace = 'allotaxonometer_for_all',
        propNames = c('id', 'data'),
        package = 'allotaxonometerForAll'
        )

    structure(component, class = c('dash_component', 'list'))
}
