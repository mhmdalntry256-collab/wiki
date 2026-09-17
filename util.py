import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))