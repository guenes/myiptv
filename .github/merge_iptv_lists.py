import requests


def merge_iptv_lists(remote_url, local_file, output_file):
    # Download the remote file
    response = requests.get(remote_url)
    if response.status_code == 200:
        remote_list = response.text
    else:
        raise Exception(f"Failed to download remote file: {remote_url}")

    # Read the local file
    with open(local_file, "r") as f1:
        local_list = f1.read()

    # Merge and write to output file
    with open(output_file, "w") as f3:
        f3.write(remote_list)
        f3.write(local_list)


if __name__ == "__main__":
    remote_url = "https://raw.githubusercontent.com/josxha/german-tv-m3u/refs/heads/main/german-tv.m3u"
    local_file = "https://raw.githubusercontent.com/guenes/iptv/refs/heads/master/streams/tr.m3u"  # Replace
    output_file = "detr.m3u"
    merge_iptv_lists(remote_url, local_file, output_file)
