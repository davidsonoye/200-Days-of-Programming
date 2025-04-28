import plotly.graph_objects as go
from ipywidgets import interact, IntSlider, FloatSlider

def simulation(fixed, variable):
    infected = [fixed['initial_infections']]
    new_infections = [fixed['initial_infections']]
    total_infections = fixed['initial_infections']
    
    for t in range(fixed['duration']):
        cur_infections = infected[-1]
        
        # Remove people who are no longer contagious
        if len(new_infections) > fixed['days_spreading']:
            cur_infections -= new_infections[-fixed['days_spreading']-1]
        
        # Set daily contacts
        if t < variable['reduction_day']:
            daily_contacts = fixed['init_contacts']
        else:
            daily_contacts = variable['reduced_daily_contacts']
        
        # Compute new cases
        total_contacts = cur_infections * daily_contacts
        susceptible = fixed['pop'] - total_infections
        risky_contacts = total_contacts * (susceptible / fixed['pop'])
        newly_infected = round(risky_contacts * fixed['contagiousness'])
        
        # Update variables
        new_infections.append(newly_infected)
        total_infections += newly_infected
        infected.append(cur_infections + newly_infected)
    
    return infected

def interactive_simulation(
    initial_infections=10,
    pop=330_000_000,
    duration=180,
    init_contacts=15,
    reduced_daily_contacts=5,
    reduction_day=30,
    contagiousness=0.05,
    days_spreading=14
):
    fixed = {
        'initial_infections': initial_infections,
        'pop': pop,
        'duration': duration,
        'init_contacts': init_contacts,
        'contagiousness': contagiousness,
        'days_spreading': days_spreading
    }
    
    variable = {
        'reduction_day': reduction_day,
        'reduced_daily_contacts': reduced_daily_contacts
    }
    
    infections = simulation(fixed, variable)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(len(infections))),
        y=infections,
        mode='lines',
        name='Active Infections'
    ))
    
    fig.update_layout(
        title='Simulation of COVID-19 Spread in the USA',
        xaxis_title='Days',
        yaxis_title='Active Infections',
        template='plotly_dark'
    )
    
    fig.show()

# Now create sliders for interactivity
interact(
    interactive_simulation,
    initial_infections=IntSlider(min=1, max=1000, step=10, value=10),
    pop=IntSlider(min=10_000_000, max=400_000_000, step=10_000_000, value=330_000_000),
    duration=IntSlider(min=30, max=365, step=10, value=180),
    init_contacts=IntSlider(min=1, max=50, step=1, value=15),
    reduced_daily_contacts=IntSlider(min=1, max=50, step=1, value=5),
    reduction_day=IntSlider(min=0, max=180, step=5, value=30),
    contagiousness=FloatSlider(min=0.01, max=0.2, step=0.01, value=0.05),
    days_spreading=IntSlider(min=5, max=21, step=1, value=14)
)
