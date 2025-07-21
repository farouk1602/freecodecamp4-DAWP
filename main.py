from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate and save plots
draw_line_plot().savefig('line_plot.png')
draw_bar_plot().savefig('bar_plot.png')
draw_box_plot().savefig('box_plot.png')
