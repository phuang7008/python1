#!/usr/bin/env python3

# this is implemented for a single chromosome
# for handling multiple chromosomes, we need to add extra things in

import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--low_cov_file', required=True)
    parser.add_argument('--map_file', required=True)

    return parser.parse_args()


def main():
    args = create_parser()

    starts1, ends1 = file_reading(args.low_cov_file, 1)
    starts2, ends2 = file_reading(args.map_file, 2)
    all_starts = list(starts1.keys()) + list(starts2.keys())
    all_ends   = list(ends1.keys()) + list(ends2.keys())
    all_vals   = all_starts + all_ends
    all_vals.sort()
    #print(all_vals)

    # now we need to walk through the sorted all_vals list
    counter = 0         # when counter drop to 1, there is an intersect
    prev_start0 = 0     # set when counter from 0 to 1
    prev_start1 = 0
    map_position = 0        # set when val is in starts2 or ends2

    for val in all_vals:

        if val in ends1 or val in ends2:
            counter -= 1

            if counter == 1:
                # the first part of the annotation should come from starts1 or ends1
                # the second part of the annotation should come from starts2 or ends2
                #
                out_string = ""
                if prev_start0 in starts1:
                    out_string = starts1[prev_start0]
                else:
                    out_string = "no annotation for part 1"

                if map_position in ends2:
                    out_string += '\t' + ends2[map_position]
                elif map_position in starts2:
                    out_string += '\t' + starts2[map_position]
                else:
                    out_string += "no annotation for part2"

                print("%s\t%s\t%s" %(prev_start1, val, out_string))
                
            # because bed file starts with 0 (or 0-indxed), so one value will appear in both start and end dict
            # we have to remove those appeas in end position, so the next round, it will be the start position only
            #
            if val in ends1:
                ends1.pop(val, None)
            elif val in ends2:
                ends2.pop(val, None)

            continue
                
        if val in starts1:
            prev_start0 = val
            counter += 1
            prev_start1 = val
        elif val in starts2:
            counter += 1
            prev_start1 = val
        
        if val in ends2 or val in starts2:
            map_position = val


def file_reading(file_in, type_in):
    starts = {}
    ends   = {}

    # now read in low_cov_file
    try:
        with open(file_in, 'r') as fh:
            for line in fh:
                if line.startswith('#'):
                    continue
                
                line = line.rstrip()
                start, end = [0, 0]
                if type_in == 1:
                    chr_id, start, end, length, ave = line.split('\t')
                elif type_in == 2:
                    chr_id, start, end, mappability = line.split('\t')

                starts[int(start)] = line
                ends[int(end)] = line

    except OSError as err:
        print("OSError: {0}".format(err))
    except Exception as err:
        print("Other error happened: {0}".format(err))

    return starts, ends


if __name__ == '__main__':
    main()
