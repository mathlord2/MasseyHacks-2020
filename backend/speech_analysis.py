from parselmouth.praat import run_file
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import numpy as np
import pathlib, os

# dir = pathlib.Path(__file__).parent.absolute() not a string, doesn't work
dir = os.path.dirname(__file__)

# print(dir) should print the directory of "backend"

file_praat = os.path.join(dir, "praatfile.praat") # For Borna
# file_praat = os.path.join(dir, "praatfile.praat")

def analyze_speech(wav_filename):
    sound_path = os.path.join(dir, wav_filename)
    print("sound path: %s"%sound_path)
    print("dir: %s"%dir)
    print("praat file: %s"%file_praat)

    # where sound_path is the absolute path to the file, file_praat is the absolute path to the praat file,
    # and dir is the absolute path to 
    info = run_file(file_praat, -20, 2, 0.3, "yes", sound_path, dir, 80, 400, 0.01, capture_output=True)[1].split()
        
    return {
        "syllable_count": int(info[0]),
        "pause_count": int(info[1]),
        "speech_rate": float(info[2]), # in syllables/second of total duration
        "articulation_rate": float(info[3]), # in syllables/second of speech duration
        "speaking_duration": float(info[4]), # in seconds of speech duration, excluding pauses
        "total_duration": float(info[5]), # in seconds of speech duration, including pauses
        "balance": float(info[6]), # ratio of speaking to non-speaking duration
        "f0_mean": float(info[7]), # In Hz, global mean of fundamental frequency distribution
        "f0_std": float(info[8]), # In Hz, global standard deviation of fundamental frequency distribution
        "f0_median": float(info[9]), # In Hz, global median of fundamental frequency distribution
        "f0_min": float(info[10]), # In Hz, global minimum of fundamental frequency distribution
        "f0_max": float(info[11]), # In Hz, global maximum of fundamental frequency distribution
        "f0_first_quartile": float(info[12]), # In Hz, global first quartile of fundamental frequency distribution
        "f0_third_quartile": float(info[13]), # In Hz, global third quartile of fundamental frequency distribution
        "pronounciation_score": 10*np.mean(np.array(binom.rvs(n=10,p=float(info[14]),size=10000))) # pronounciation posterior probability percent (idk)
    }


# print(analyze_speech("recordings/recording-1.wav"))