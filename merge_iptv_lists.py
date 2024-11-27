import requests


def merge_iptv_lists(remote_url, second_file, output_file):
    # Download the remote file
    response = requests.get(remote_url)
    if response.status_code == 200:
        remote_list = response.text
    else:
        raise Exception(f"Failed to download remote file: {remote_url}")

    # Download Second file
    response = requests.get(second_file)
    if response.status_code == 200:
        local_list = response.text
    else:
        raise Exception(f"Failed to download remote file: {second_file}")

    # Read the local file
    #  with open(second_file, "r") as f1:
    #     local_list = f1.read()

    # Merge and write to output file
    with open(output_file, "w") as f3:
        f3.write(remote_list)
        f3.write(local_list)


if __name__ == "__main__":
    remote_url = "https://raw.githubusercontent.com/josxha/german-tv-m3u/refs/heads/main/german-tv.m3u"
    second_file = "https://raw.githubusercontent.com/guenes/iptv/refs/heads/master/streams/tr.m3u"  # Replace
    output_file = "detr.m3u"
    merge_iptv_lists(remote_url, second_file, output_file)
