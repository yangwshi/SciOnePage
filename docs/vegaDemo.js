"use strict";     // the code should be executed in "strict mode".
                  // With strict mode, you can not, for example, use undeclared variables

const options = {
  config: {
    // Vega-Lite default configuration
  },
  init: (view) => {
    // initialize tooltip handler
    view.tooltip(new vegaTooltip.Handler().call);
  },
  view: {
    // view constructor options
    // remove the loader if you don't want to default to vega-datasets!
    //   loader: vega.loader({
    //     baseURL: "",
    //   }),
    renderer: "canvas",
  },
};

vl.register(vega, vegaLite, options);

vl.markBar()
.data("https://cse442-22w.github.io/Web-Publishing-Example/sunshine.csv")
.encode(
    vl.x().fieldN('month').sort('none'),
    vl.y().fieldQ('sunshine'),
    vl.color().fieldN('city').title('Cities'),
)
.width(450)
.height(450)
.render()
.then(viewElement => {
  // render returns a promise to a DOM element containing the chart
  // viewElement.value contains the Vega View object instance
  document.getElementById('view').appendChild(viewElement);
});