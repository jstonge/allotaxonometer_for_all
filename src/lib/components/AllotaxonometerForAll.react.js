import React, {Component} from 'react';
import PropTypes from 'prop-types';
import AllotaxD3 from '../d3/allotaxonometer';

export default class AllotaxonometerForAll extends Component {
    componentDidMount() {
        this.allotax = new AllotaxD3(this.el, this.props, figure => {
            const {setProps} = this.props;
            const {selectedPath} = figure;

            if (setProps) { setProps({selectedPath}); }
            else { this.setState({selectedPath}); }
        });
    }

    render() {
         return <div id={this.props.id} ref={el => {this.el = el}} />;
    }
}

AllotaxonometerForAll.defaultProps = {};

AllotaxonometerForAll.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,


    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * The allotaxonometer data. Should have the form:
     *
     *   `[{"x1":0,"y1":0,"coord_on_diag":0,"cos_dist":0,"rank":"(1, 1)","rank_L":[1,1],"rank_R":[1,1],"value":1,"types":"Mary","which_sys":"right"}...]`
     *
     */
    data: PropTypes.array,
};
