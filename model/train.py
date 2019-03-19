import argparse
import model


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # parser.add_argument('--model', type=str) #required = True
    parser.add_argument('--batch_size', type=int,
                        help='Batch size for model', default=32)
    parser.add_argument('--num_epochs', type=int,
                        help='Number of epochs', default=10)
    parser.add_argument('--debug', type=bool,
                        help='If true, train on small dataset(for testing)', default=False)
    parser.add_argument('--input_shape', nargs='+' ,type=int,
                        help='Height, width, channel size')

    # args = parser.parse_args()
    # if args.model == "Blur":
    #     print("Blur")
    # if args.model == "Noise":
    #     print("Noise")
