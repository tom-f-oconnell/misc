#!/usr/bin/env python3

import numpy as np


def main():
    np.random.seed(1)
    img = np.random.randn(*(256, 256))

    imgs = [img]
    def check_no_duplicates_and_add(new_img):
        for i, im in enumerate(imgs):
            if np.array_equal(new_img, im):
                raise ValueError(f'new image was duplicate of one in list ({i})'
                )
        imgs.append(new_img)


    print('\nAdding 90 degree rotations:')
    for n_rotations in range(1, 4):
        print(f'rotating 90 degrees {n_rotations} times')
        rotated = np.rot90(img, k=n_rotations)
        check_no_duplicates_and_add(rotated)
    print(f'{len(imgs)} total images now')


    print('\nAdding LR flips:')
    imgs_flipped_lr = []
    for im in imgs:
        lr_flipped = np.fliplr(im)
        imgs_flipped_lr.append(lr_flipped)

    for i, im in enumerate(imgs_flipped_lr):
        print(f'adding LR flip of previous img {i}')
        check_no_duplicates_and_add(im)
    print(f'{len(imgs)} total images now')


    print('\nAdding UD flips:')
    imgs_flipped_ud = []
    for im in imgs:
        ud_flipped = np.flipud(im)
        imgs_flipped_ud.append(ud_flipped)

    for i, im in enumerate(imgs_flipped_ud):
        try:
            check_no_duplicates_and_add(im)
            print(f'adding UD flip of previous img {i}')
        except ValueError as e:
            print(f'did not add: {e}')
    print(f'{len(imgs)} total images now')

    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()

