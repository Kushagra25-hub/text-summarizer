from huggingface_hub import upload_folder

upload_folder(
    folder_path="saved_summary_model",
    repo_id="kushagra2511/text-summarizer-t5",
    repo_type="model",
)

print("Upload Complete!")