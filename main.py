import args
import merge_csv

size = merge_csv.merge_csv(args.directory, args.output, args.separator)

if (size < 0.1):
    print("done")
else:
    print("done, " + args.output + " is " + str(size) + " GB")