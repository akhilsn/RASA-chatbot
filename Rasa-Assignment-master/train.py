config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"
print(config, training_files, domain, output)
import re

import rasa
import warnings
warnings.filterwarnings("ignore")

model_path = rasa.train(domain, config, [training_files], output, fixed_model_name='custom_nlu')
print(model_path)


# with open('./lookup_tables/location.txt', encoding='utf-8', errors='ignore') as f:
#     list_locations= f.read().lower().splitlines()
#
# print(list_locations)
# # rasa shell --debug --model ./models/custom_nlu.tar.gz  --endpoint endpoints.yml
# # rasa run --enable-api -m ./models/custom_nlu.tar.gz  --endpoint endpoints.yml
# # rasa run actions
# # rasa shell --model ./models/custom_nlu.tar.gz  --endpoint endpoints.yml
