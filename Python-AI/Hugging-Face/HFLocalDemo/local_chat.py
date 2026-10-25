import torch
from transformers import AutoTokenizer,AutoModelForCausalLM
# 1. location of the downloaded model
model_path='./models/qwen2.5-0.5b-instruct'
# 2. load the tokenizer from local files
tokenizer=AutoTokenizer.from_pretrained(
    model_path
)
# 3. Load the trained language model from local files
model=AutoModelForCausalLM.from_pretrained(
    model_path
)

# 4. Prepare a prompt using the model's chat format
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python instructor."
    },
    {
        "role": "user",
        "content": "Explain Python functions in simple terms."
    }
]

# 5. Convert messages into model input tokens
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True
)

# 6. Generate a response
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=False
    )

# 7. Decode only the newly generated tokens
new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
response = tokenizer.decode(
    new_tokens,
    skip_special_tokens=True
)

print("\nAI Response:")
print(response)
