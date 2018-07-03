import twitterpastcrawler
import os, errno
from sys import argv 
"""
command:
	$ python crawling_twitter.py <HashTag> <OutputDirectory>
example:
	$ python crawling_twitter.py dating data/
"""

def mkdir(directory):
	try:
		os.makedirs(directory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

def main(sys_args):
	hashtag, output_dir = sys_args[1], sys_args[2]

	mkdir(output_dir)
	output_file = '{}{}.csv'.format(output_dir, hashtag)

	print("Crawling #{} from twitter to {}...".format(hashtag, output_file))

	crawler = twitterpastcrawler.TwitterCrawler(
		query="#"+hashtag, # searches for tweets that respond to the query, "#haiku"
		output_file=output_file # outputs results to haiku.csv
		)

	crawler.crawl() # commences the crawl


if __name__ == "__main__":
	main(argv)
