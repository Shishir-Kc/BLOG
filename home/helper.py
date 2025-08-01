from supabase import create_client
from decouple import config
import uuid

SUPABASE_URL = config('SUPABASE_URL')
SUPABASE_KEY = config('SUPABASE_KEY')


supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)


def upload_image_to_supabase(file_obj):
    ext = file_obj.name.split('.')[-1]
    unique_name = f"{uuid.uuid4()}.{ext}"
    file_data = file_obj.read()

    response = supabase_client.storage.from_("user-content").upload(unique_name, file_data)
    
    print("Response from Supabase upload:", response)  # debug output

    if hasattr(response, 'error') and response.error is not None:
        raise Exception(f"Supabase upload error: {response.error.message}")
    
    public_url = f"{SUPABASE_URL}/storage/v1/object/public/user-content/{unique_name}"
    return public_url
