import os
import shutil
import taglib


def update_metadata(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, 165):  # change  this to the number of files in your folder + 1
        input_file = os.path.join(input_folder, f"{i}.wav")
        output_file = os.path.join(output_folder, f"{i}.wav")

        if os.path.exists(input_file):
            with taglib.File(input_file) as audio:
                audio.tags["TITLE"] = [f"{i}"]
                audio.tags["TRACKNUMBER"] = [f"{i}"]

                # Save updated WAV file
                audio.save()

            shutil.copy2(input_file, output_file)

            print(
                f"Updated metadata for {i}.wav: title='{i}', track number={i}")  # Update the print statement as well
        else:
            print(f"File {i}.wav not found.")


if __name__ == "__main__":
    input_folder = "/wav"  # your path
    output_folder = "/wavout"  # your path
    update_metadata(input_folder, output_folder)