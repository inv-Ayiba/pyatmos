import os
THISDIR=os.path.dirname(os.path.abspath(__file__))

import pyatmos

OVERALL_RUN = 6
ITERATIONS = 2

atmos = pyatmos.Simulation(
        code_path = '/Users/Will/Documents/FDL/atmos',
        #docker_image="gcr.io/i-agility-205814/pyatmos:co2-photogenic",
        DEBUG=True)

atmos.start()




for it in range(0, ITERATIONS):
    #concentration = base_conc + float(it)/100
    #print('iteration', it, 'concentration', concentration)
    
    args = {
        'save_logfiles' : True,
        'species_concentrations' : {'H2O': 0.2, 'CO2': 0.0004, 'CH4': 1.63e-06, 'O2': 0.2, 'H2': 8.13e-08},
        'max_photochem_iterations' : 10000, 
        'max_clima_steps' : 10, 
        'output_directory' : '/Users/Will/Documents/FDL/results/run_{1}_{0}'.format(it, OVERALL_RUN),
        'run_iteration_call' : it
    }
    if it > 0:
        args['previous_photochem_solution'] = '/Users/Will/Documents/FDL/results/run_{1}_{0}/out.dist'.format(it-1, OVERALL_RUN)
        args['previous_clima_solution'] = '/Users/Will/Documents/FDL/results/run_{1}_{0}/TempOut.dat'.format(it-1, OVERALL_RUN)
        args['species_concentrations'] = {'H2O': 0.1, 'CO2': 0.02, 'CH4': 1.63e-06, 'O2': 0.21, 'H2': 8.13e-08}
    print('running atmos with args:')
    print(args)
    atmos.run(**args)
    print('\n\nNEXT ITERATION..\n\n')


    data = atmos.get_metadata() 
    print(data)
    print('')

atmos.close()
