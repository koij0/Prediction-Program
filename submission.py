# Koi Johnson
# CSCI 128 - Section I
# Create Project


# Function 1 : alter songs
def alterSongs(songs, artist, artist_list):
    song_list = []
    for i in range(len(artist_list)):
        if artist_list[i] == artist:
            song_list.append(songs[i]) 
    return song_list
                           
# Function 2 : alter streams
def alterStreams(streams, artist, artist_list):
    stream_list = []
    for i in range(len(artist_list)):
        if artist_list[i] == artist:
            if streams[i] == "" or streams[i] is None:
                streams[i] = 0
            stream_list.append(int(streams[i])) 
    return stream_list

# Function 3 : alter regions
def alterRegions(region, artist, artist_list):
    regions_list = []
    for i in range(len(artist_list)):
        if artist_list[i] == artist:
            regions_list.append(region[i]) 
    return regions_list

# Function 4 : find top songs
def topSongs(songs, streams, setlist_length):
    if setlist_length > len(songs):
        return "ERROR"
    else:
        setlist = []
        while len(setlist) < setlist_length:
            if len(streams) == 0:
                return "ERROR"
            else:
                highest_stream = streams[0]
                for i in range(len(songs)):
                    if streams[i] >= highest_stream:
                        highest_stream = streams[i]
                        top_song = songs[i]
                        idx = i
                if top_song not in setlist:
                    setlist.append(top_song)
                del songs[idx]
                del streams[idx] 
             
        return setlist


# Function 5 : find top locations
def topLocations(streams, region, tourlist_length):
    if tourlist_length > len(region):
        return "ERROR"
    else:
        tourlist =[]
        while len(tourlist) < tourlist_length:
            if len(streams) == 0:
                return "ERROR"
            else:
                max_streams = streams[0]
                for j in range(len(region)):
                    if streams[j] >= max_streams:
                        max_streams = streams[j]
                        location = region[j]
                        idx = j
                if location != "Global":
                    if location not in tourlist:        
                        tourlist.append(location)
                del streams[idx]
                del region[idx]

        return tourlist


# main code
if __name__ == "__main__":

# artist input
    artist = input("Artist: ")

# read file
    with open("/Users/emmajohnson/Desktop/ARCHIVES/CSCI_128/Code/Create_Project/spotify_fixed_data.csv", "r") as music_data:

    # organize data from file
        songs = []
        streams = []
        artist_list = []
        region = []
        for line in music_data:
            line = line.strip()
            line = line.split("~")
            songs.append(line[1])
            streams.append((line[2]))
            artist_list.append(line[0])
            region.append(line[3])

    if artist not in artist_list:
         print("Artist not Found")
        
    else: 
        # calls
        song = alterSongs(songs, artist, artist_list)
        stream = alterStreams(streams, artist, artist_list)
        stream2 = stream.copy()
        regions = alterRegions(region, artist, artist_list)
        setlist_length = int(input("Setlist Length? "))
        setlist = str(topSongs(song, stream, setlist_length))
        if setlist == "ERROR":
            print("ERROR SETLIST_LENGTH EXCEEDS SONGS AVAILABLE")
        else:
            tourlist_length = int(input("Tourlist Length? "))
            tourlist = str(topLocations(stream2, regions, tourlist_length))
            if tourlist == "ERROR":
                print("ERROR TOURLIST_LENGTH EXCEEDS LOCATIONS AVAILABLE")
            if setlist != "ERROR" and tourlist != "ERROR":
            # Output
                with open(f"{artist}_TOURLIST_AND_SETLIST.txt", "w") as new_file:
                    new_file.write(f"Setlist: {setlist} \nTourlist: {tourlist}")
                    print(f"Setlist and Tourlist stored in {artist}_TOURLIST_AND_SETLIST.txt file")

        

 


