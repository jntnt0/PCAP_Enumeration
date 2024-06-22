import plotly.graph_objects as go

def plot_ips(ips):
    src_ips = [src for src, dst in ips]
    dst_ips = [dst for src, dst in ips]

    fig = go.Figure(data=[go.Scatter(x=src_ips, y=dst_ips, mode='markers')])
    fig.update_layout(title='Source vs Destination IPs', xaxis_title='Source IP', yaxis_title='Destination IP')
    fig.show()
