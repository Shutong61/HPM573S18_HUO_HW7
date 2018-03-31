import CalibrationClasses as CalibClasses
import CalibrationSettings as CalibSets
import Calibration6 as Calib6
import CalibrationS6 as CalibS6
import scipy.stats as stat

# Problem 1
calibration1 = CalibClasses.Calibration()
calibration1.sample_posterior()
print("Problem 1: The percentage of survival over 5 years", calibration1.get_5yr_survival_percentage())

# Problem 2
print('Problem 2: If the probability of 5-year survival is q.'
      'The number of participants that survived beyond 5 years in a cohort of N participants follows Binomial distribution. The parameter is (K,N,q).')

# Problem 3
prob=stat.binom.pmf(400, 573, 0.5)
print('Problem 2: The likelihood that a clinical study reports 400 of 573 participants survived at the end of the 5-year study period '
      'if 50% of the patients in our simulated cohort survived beyond 5 years is:', prob)

# Problem 4
# create a calibration object
calibration = CalibClasses.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# create the histogram of the resampled mortality probabilities
Fig.graph_histogram(
    observations=calibration.get_mortality_resamples(),
    title='Histogram of Resampled Mortality Probabilities',
    x_label='Mortality Probability',
    y_label='Counts',
    x_range=[CalibSets.POST_L, CalibSets.POST_U])

# Estimate of mortality probability and the posterior interval
print('Problem 4: Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

# Problem 5
# initialize a calibrated model
calibrated_model = CalibClasses.CalibratedModel('CalibrateResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# plot the histogram of mean survival time
Fig.graph_histogram(
    observations = calibrated_model.get_all_mean_survival(),
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count',
    x_range=[10, 20])

# report mean and projection interval
print('Problem 5: Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))

# Problem 6
# If a clinical study that reports 800 of 1146 participants survived at the end of the 5-year study period.
# create a calibration object
calibration6 = Calib6.Calibration()
# sample the posterior of the mortality probability
calibration6.sample_posterior()
# Estimate of mortality probability and the posterior interval
print('Estimate of new mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets6.ALPHA, prec=0),
      calibration6.get_mortality_estimate_credible_interval(CalibSets6.ALPHA, 4))

# initialize a calibrated model
calibrated_model6 = Calib6.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model6.simulate(CalibS6.SIM_POP_SIZE, CalibS6.TIME_STEPS)

# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets6.ALPHA, prec=0),
      calibrated_model6.get_mean_survival_time_proj_interval(CalibS6.ALPHA, deci=4))


