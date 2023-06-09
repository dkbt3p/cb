import yt_dlp, os, argparse

parser = argparse.ArgumentParser(description="Config and username parser for ctbrec.")
parser.add_argument("-u", "--username", help="Provide an username from the commandline.", required=False, type=str, default=None)
parser.add_argument("-p", "--path", help="Provide a path for the downloads. (Current parent directory by default)", required=False, type=str, default=os.getcwd())
parser.add_argument("-c", "--cookie", "--cookiefile", help="Provide a name for a cookiefile. (`cb-cookie.txt` by default)", required=False, type=str, default=None)
parser.add_argument("-v", "--verbose", help="Print yt-dlp debugging information.", required=False, const=True, default=False, action="store_const")
parser.add_argument("-q", "--quiet", help="Do not print yt-dlp messages.", required=False, const=True, default=False, action="store_const")
args = parser.parse_args()

def main():
    print(args.path)
    if args.username is not None:
        username = args.username
    else:
        username = str.lower(input("Username: "))

        os.system("title " + username)
        
    # Download options / flags
    downloadOptions = {
        "cookiefile": "cb-cookies.txt",
        "quiet": False,
        "verbose": False,
        "nopart": True,
        "outtmpl": "%(epoch>%Y-%m-%d)s/%(id)s/%(id)s %(epoch>%Y-%m-%d %H-%M)s.%(ext)s"
        # example path: G:\ctbrec\{username}\{username} {YYYY-MM-DD HH-MM}
    }
    if os.path.isdir(args.path) == False: # Check if the given directory exists
        os.mkdir(args.path) # If not, make the directory.
    os.chdir(args.path) # Then change directory, to the given directory
    if args.cookie is not None: # Check if a cookie arg is given
        downloadOptions["cookiefile"] = args.cookie # If T, set the yt-dlp flag
    if args.verbose is True: # Check if a verbose arg is given
        downloadOptions["verbose"] = True # If T, set the yt-dlp flag
    if args.quiet is True: # Check if a quiet arg is given
        downloadOptions["quiet"] = True # If T, set the yt-dko flag

    # Download the stream
    with yt_dlp.YoutubeDL(downloadOptions) as ydl:
        ydl.download("https://chaturbate.com/"+username+"/")

if __name__ == "__main__":
    main()
