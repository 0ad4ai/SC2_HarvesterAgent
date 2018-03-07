# screen size and minimap size have to be the same to work
SCREEN_SIZE_X = 32
SCREEN_SIZE_Y = 32
MINIMAP_SIZE_X = SCREEN_SIZE_X
MINIMAP_SIZE_Y = SCREEN_SIZE_Y
NUM_ACTIONS = 15
NON_SPATIAL_FEATURES = 6 + 6 + NUM_ACTIONS
MINIMAP_FEATURES = 2
SCREEN_FEATURES = 3

DISCOUNT_FACTOR = 0.99
EXPLORATION_RATE = 0.3
LEARNING_RATE = 10e-3
EPSILON = 0.05

NUM_BATCHES = 20
PARALLEL_THREADS = 16
MAX_STEPS_TOTAL = 600 * 10**6 # TODO: check if it really exits (e.g. after 100 steps)
CHECKPOINT = 100
SAVE_PATH = './saved_checkpoints/'
LOG_PATH = './logs/'
DETAILED_LOGS = 10 # detailed logs are kept for top 10 episodes for minerals and gas, as well as for the last 10 episodes
RENDER = False
SHOW_PROGRESS = True
