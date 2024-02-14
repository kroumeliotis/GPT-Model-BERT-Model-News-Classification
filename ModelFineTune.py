from DBmethods import DBmethods
from LLAMAmethods import LLAMAmethods
# from GPTmethods import GPTmethods

"""
Create the json files
"""
DB = DBmethods()
# print(DB.create_jsonl('gpt', 'train'))
# print(DB.create_jsonl('gpt', 'validation'))
# print(DB.create_jsonl('llama', 'train'))
# print(DB.create_jsonl('llama', 'validation'))
# exit()
"""
Train Llama 2 Model
"""
destination = "kroumeliotis/ecommerce-reviews50"  # Which is the new model you created in replicate?
train_data = "https://acloud.gr/ai/50/ft_train_dataset_llama.jsonl"  # Where the training data are hosted?
version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"  # Which version of Llama you want to train?
LLAMA = LLAMAmethods(model_id=version)  # Instantiate the LLAMAmethods class
print(LLAMA.llama_train(destination, train_data))  # Run the train
"""
Run Llama 2 Trained Model
DO NOT USE IT! JUST AN EXAMPLE
"""
# LLAMA = LLAMAmethods(model_id="kroumeliotis/sentiment:df179eef934e986eb88d513262e5e25831d9df89369e42afac7cddbc0358d2af")
# print(LLAMA.llama_ratings(["theres cheaper ones with better fans it has extremely low fan speed does heat tho", "works fine good purchase experience works fine good purchase experience"]))


"""
Upload Dataset for GPT Fine-tuning
SOS Now you can upload the training dataset along with validation using OpenAI's graphical interface
"""
# GPT = GPTmethods()

# Upload train-data-gpt-50.jsonl file
# file_id = GPT.upload_file(dataset="datasets/train-data-gpt-50.jsonl").id
# print(file_id)

# Upload train-data-gpt-100.jsonl file
# file_id = GPT.upload_file(dataset="datasets/train-data-gpt-100.jsonl").id
# print(file_id)
"""
Train GPT Model
"""
# Train GPT Model using the train-data-gpt-50.jsonl
# file_id = "file-j8qxeLfVbyU3fb86Q6F7VmC3"
# train_id = GPT.train_gpt(file_id).id
# print(train_id)

# Train GPT Model using the train-data-gpt-100.jsonl
# file_id = "file-4DeHbaacd2bDZTcYTaY9fnPt"
# train_id = GPT.train_gpt(file_id).id
# print(train_id)

"""
Run GPT Trained Model
DO NOT USE IT! JUST AN EXAMPLE
"""
# GPT = GPTmethods()  # Get the fine-tuned model from https://platform.openai.com/finetune
# print(GPT.gpt_ratings(['works fine good purchase experience works fine good purchase experience', 'they work until they dont my husband tried making cinnamon rolls using this mat within 5 min of it being put in the preheated 375 degree oven it started smoking and melting never had a mat like this melt since it was a two pack i threw the other one away just to be safe wont buy again obviously not heat safe like they state less than a year old and they wont give me my money back but offered to send me new ones ummm no thanks not going to risk burning my house down again', 'my pizza tastes like silicone i want to like this product because of how to clean it is however my pizza tasted a taste that wont go away like silicone and my apartment smells like burnt plastic i followed the instructions in the package and washed the pad before using it maybe my bad experience is because it was my first time using the pad but i shouldnt have to destroy a pizza because of a poorly designed product i rarely write reviews but the lingering taste in my mouth says i had to stop what i was doing to let everyone know to choose something else', 'my go to items when bakingcooking i love these these are my go tos and i am always excited to use these they are a better alternative than having to measure out parchment paper or tinfoil it saves me time and money it can be hard to wash but usually i leave in the pan and wash both at the same time so im not splashing myself around with water i would say to test batches when first cooking or baking because you may have to cook in the oven a little longer than usual a definite 1010 for me', 'what is this i purchased these for 2 purposes12 for baking and 12 for wax melts i used the first one in a wax melt warmer the photo shows the result they do not leak it is not wax this is what i believe is the breaking down of whatever these are made with although it comes off easily enough i feel very uneasy about using them i would never use them for baking the description does not state 100 silicone my bad i guess i am very disappointed and would never trust them to bake in is there anything leaching into the air']))

