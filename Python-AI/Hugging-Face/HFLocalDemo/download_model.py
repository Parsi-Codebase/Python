from huggingface_hub import snapshot_download
model_id='Qwen/Qwen2.5-0.5B-Instruct'
local_model_path=snapshot_download(
    repo_id=model_id,
    local_dir='./models/qwen2.5-0.5b-instruct'
)
print('Model Downloaded Successfully!!')
print('Local model path:',local_model_path)