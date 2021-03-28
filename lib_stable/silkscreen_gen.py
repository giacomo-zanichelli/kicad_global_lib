
def main():
    for n in range(20):
        x = 1.27 + 2.54*n
        print('(fp_line (start {:.2f} -1.27) (end {:.2f} 1.27) (layer F.SilkS) (width 0.12))'.format(x, x))


if __name__ == '__main__':
    main()
