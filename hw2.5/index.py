import os
import subprocess
import time


def files_manager():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    sources_directory = os.path.join(current_directory, 'Source')
    files = os.listdir(sources_directory)

    for file in files:
        basename = os.path.basename(file)
        source_filename = os.path.join(sources_directory, basename)
        results_directory = os.path.join(current_directory, 'Results')
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)
        new_filename = os.path.join(results_directory, basename)
        yield [source_filename, new_filename]


def resize(src, dst):
    print('Start resizing %s' % os.path.basename(src))
    try:
        subprocess.run('imagick %s -resize 200 %s' % (src, dst))
    except Exception as e:
        subprocess.run('magick %s -resize 200 %s' % (src, dst))  # для windows версии
    print('Resized image %s' % os.path.basename(src))


def run():
    for paths_pair in files_manager():
        resize(*paths_pair)


def run_multi_processed():
    from multiprocessing import Pool
    i = 0
    with Pool(processes=4) as pool:
        i += 1
        print('Running pool item number %d' % i)
        res = pool.starmap(resize, [f for f in files_manager()])


def run_with_time_counter(fn):
    start = time.time()
    fn()
    end = time.time()
    elapsed = end - start
    print('Total elapsed time: %f' % elapsed)
    print()


if __name__ == '__main__':
    print('Run simple resize:')
    run_with_time_counter(run)
    
    print('Run multi processed resize:')
    run_with_time_counter(run_multi_processed)
