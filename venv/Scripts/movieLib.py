import random

movieList = ["bodyMovies_000.mp4",
"bodyMovies_001.avi",
"bodyMovies_001_01.avi",
"bodyMovies_002.avi",
"bodyMovies_003.avi",
"bodyMovies_004.avi",
"bodyMovies_005.avi",
"bodyMovies_006.avi",
"bodyMovies_007.avi",
"bodyMovies_008.avi",
"bodyMovies_009.avi",
"bodyMovies_010.avi"
]

def main():
    return ( "bodyMovies\\" + random.choice(movieList))


if __name__ == '__main__':
    main()