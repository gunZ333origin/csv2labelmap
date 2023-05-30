"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python csv_to_labelmap.py --csv_input=data/train_labels.csv  --output_path=data/train.pbtxt
  # Create test data:
  python csv_to_labelmap.py --csv_input=data/test_labels.csv  --output_path=data/test.pbtxt
"""
import tensorflow as tf
import pandas as pd

flags = tf.compat.v1.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output pbtxt file')

FLAGS = flags.FLAGS


def main(_):
    df = pd.read_csv(FLAGS.csv_input)
    # print(df)
    lbls = df["label"].unique()
    cats = df["category"]
    # print(cats)

    label_maps = ""
    it = 0
    for i in range(len(df)):
        label_maps += """
item {
    id: """ + str(i) + """
    name: '""" + str(lbls[i]) + """'
    category: '""" + str(cats[i]) + """'
}
        """
        it += 1

    with open(FLAGS.output_path, "w") as pbfile:
        pbfile.write(label_maps)
        print('Labelmaps generated!')


if __name__ == '__main__':
    tf.compat.v1.app.run()
