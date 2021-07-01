"""A video player class."""

from video_library import VideoLibrary
from random import randint
import re

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._titl=[]
        self._vid_id=[]
        self._tag=[]
        self._state=[]
        self._j=0
        self._playlist={}
        self._flag=[]
        self._reason=[]
        self._c=0
        
        self._video_library = VideoLibrary()
        self._data=(self._video_library.get_all_videos())
        for i in range(0,len(self._data)):
           
            self._titl.append(getattr(self._data[i],'title'))
            self._vid_id.append(getattr(self._data[i],'video_id'))
            self._tag.append(getattr(self._data[i],'tags'))
            self._flag.append(0)
            self._reason.append("")
    def number_of_videos(self):
        num_videos = len(self._data)
        print(f"{num_videos} videos in the library")
        
        
        
    def show_all_videos(self):
        """Returns all videos."""
        vid=(self._video_library.get_all_videos())
        print("Here's a list of all available videos:")
        for i in range(0,len(vid)):
            print(" "+self._titl[i]+"  ("+self._vid_id[i]+")", end=" ")
            if self._reason[j]!="":
                                print(list(self._tag[ind]),end=" ")
                                print("FLAGGED (reason:"+self._reason[j]+")")
            else:
                                print(list(self._tag[ind]))
                      
            
            
               

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
    
        if video_id in self._vid_id:
            self._vid=self._vid_id.index(video_id)
       
            if self._flag[self._vid]!=1:
                if len(self._state)==0:
                    self._state.append(self._titl[self._vid])
                    print("Playing video: "+self._state[0])
                else:
                   print("Stopping video: "+self._state[0])
                   self._state.pop()
                   self._state.append(self._titl[self._vid])
                   print("Playing video: "+self._state[0])
            else:
                print("Cannot play video: Video is flagged (reason:"+self._reason[self._vid]+")")
        else:
            print("Cannot play video: video does not exist")
        
           

    def stop_video(self):
        """Stops the current video."""
        if len(self._state)==0:
            print("Cannot stop video: No video is currently playing")
            
        else:
            print("Stopping video: "+self._state[0])
            self._state.pop()
            self._j=0

    def play_random_video(self):
        """Plays a random video from the video library."""
        i=randint(0,4)
        for k in range(0,len(self._data)):
            if self._flag[k]==1:
                self._c=self._c+1
        if self._c== len(self._data):
            print("No videos available")
        else:
            if self._flag[i]!=1:
                if len(self._state)==0:
                    self._state.append(self._titl[i])
                    print("Playing video: "+self._state[0])
                else:
                    print("Stopping video: "+self._state[0])
                    self._state.pop()
                    self._state.append(self._titl[i])
                    print("Playing video: "+self._state[0])
            else:
                print("Cannot play video: Video is flagged (reason:"+self._reason[self._vid]+")")
                

         

    def pause_video(self):
        """Pauses the current video."""
        
        if len(self._state)!=0 and self._j==0:
           print("Pausing Video: "+self._state[0])
           self._j+=1
        elif self._j==1:
           print("Video already paused: "+self._state[0])
        else:
            print("Cannot pause: No video is playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._j==1 and len(self._state)!=0:
             print("Continuing video: "+self._state[0])
             self._j=0
        elif (len(self._state)!=0 and self._j==0):
             print("Cannot continue video: Video is not paused")
        else:
             print("Cannot continue video: No video is playing")
             

    def show_playing(self):
        
        """Displays video currently playing."""
        if (len(self._state)!=0 and self._j==1):
             print("Currently playing : "+self._titl[self._vid]+"  ("+self._vid_id[self._vid]+")", end=" ")
             print(list(self._tag[self._vid]+"-PAUSED"))
             
        elif (len(self._state)!=0 and self._j==0):
             print("Currently playing : "+self._titl[self._vid]+"  ("+self._vid_id[self._vid]+")", end=" ")
             print( list(self._tag[self._vid]))
        else:
             print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        if len(self._playlist)==0:
            
            self._playlist[playlist_name]=list()
            print("Succesfully Created playlist :"+playlist_name)
        else:
            for i in self._playlist:
                if i.lower()== playlist_name.lower():
                    print("Cannot create playlist: A playlist with the same name already exist")
                else:
                   
                    self._playlist[playlist_name]=list()
                    print("Succesfully Created playlist :"+playlist_name)
                    

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if video_id in self._vid_id and playlist_name in self._playlist.keys():
            ind=self._vid_id.index(video_id)
            if self._flag[ind]!=1:
                if len(self._playlist[playlist_name])==0:
                    self._playlist[playlist_name].append(self._titl[ind])
                    print("Added video to "+playlist_name+":"+self._titl[ind])
                    self._playlist[playlist_name]
                elif self._titl[ind] in self._playlist[playlist_name]:
                    print("Cannot add video to "+playlist_name+": Video already added")
                else:
                    self._playlist[playlist_name].append(self._titl[ind])
                    print("Added video to "+playlist_name+":"+self._titl[ind])
            else:
                print("Cannot play video: Video is flagged (reason:"+self._reason[ind]+")")
        elif video_id not in self._vid_id:
            print("Cannot add video to "+playlist_name+": Video does not exist")
        else:
            print("Cannot add video to "+playlist_name+": Playlist does not exist")
                
    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlist)==0:
            print("No playlist exist yet")
        else:
            print("Showing all playlists")
            for i in self._playlist.keys():
                print(i)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlist.keys():
            print("Cannot show playlist "+playlist_name+": Playlist does not exist") 
        else:
            for i in self._playlist.keys():
                if i ==playlist_name:
                    print("Showing playlist: "+playlist_name, end=" ")
                    if len(i)==1:
                        print("("+len(i)+" video)")
                    else:
                        print("("+len(i)+" videos)")
                    if(len(i)==0):
                        print("No videos here yet")
                    else:
                        for j in range(len(self._playlist)):
                            ind=self._titl.index(self._playlist[j])
                            print(" "+self._titl[ind]+"  ("+self._vid_id[ind]+")", end=" ")
                            
                            if self._reason[j]!="":
                                print(list(self._tag[ind]),end=" ")
                                print("FLAGGED (reason:"+self._reason[j]+")")
                            else:
                                print(list(self._tag[ind]))
                        
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name not in self._playlist.keys():
                print("Cannot remove video from "+playlist_name+": Playlist does not exist")
        else:
            if video_id not in self._vid_id:
                print("Cannot remove video from "+playlist_name+": Video does not exist")
            else:
                ind=self._vid_id.index(video_id)
                if self._titl[ind] not in self._playlist:
                    print("Cannot remove video from "+playlist_name+": Video is not in playlist")
                else:
                    self._playlist[playlist_name].remove(self._titl[ind])
                    print("Removed video from "+playlist_name+": "+self._titl[ind])
        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlist.keys():
                print("Cannot clear playlist "+playlist_name+": Playlist does not exist")
        else:
            self._playlist[playlist_name]=[]
            print("Successfully removed all videos from "+playlist_name)
        #print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlist.keys():
                print("Cannot delete playlist "+playlist_name+": Playlist does not exist")
        else:
            del self._playlist[playlist_name]
            print("Deleted playlist: "+playlist_name)
        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        
        k=1
        t=[]
        for i in range(0,len(self._data)):
            
                if re.search(search_term,self._vid_id[i]):
                    t.append(i)
        if len(t)!=0:
            print("Here are the results for: "+ search_term)
            for i in t:
                if self._flag[i]!=1:
                    print(k,")"+self._titl[i]+"  ("+self._vid_id[i]+")", end=" ")
                    print( list(self._tag[i]))
                    k+=1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            command = (input("If your answer is not a valid number, we will assume it's a no."))
            if command.isnumeric():
                self.play_video(self._vid_id[t[int(command)-1]])
            
        else:
                print("No search results for "+search_term)
                
                  
            

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        k=1
        t=[]
        for i in range(0,len(self._data)):
            
                if (video_tag in self._tag[i]):
                    t.append(i)
        if len(t)!=0:
            print("Here are the results for: "+ video_tag)
            for i in t:
                if self._flag[i]!=1:
                    print(k,")"+self._titl[i]+"  ("+self._vid_id[i]+")", end=" ")
                    print( list(self._tag[i]))
                    k+=1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            command = (input("If your answer is not a valid number, we will assume it's a no."))
            if command.isnumeric():
                self.play_video(self._vid_id[t[int(command)-1]])
            
        else:
                print("No search results for "+video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        if video_id in self._vid_id:
                       ind=self._vid_id.index(video_id)
                       self._reason[ind]=(flag_reason)
        else:
            print("Cannot flag video: Video does not exist")
            return(0)
                       
        if self._flag[ind]==0 and video_id in self._vid_id:
                       if len(self._state)!=0:
                           print("Stopping video: "+self._state[0])
                           self._state.pop()
                
                       self._flag[ind]=1
                       print("Succesfully flagged: "+self._titl[ind],end=" ")
                       if flag_reason!="":
                           print("(reason: "+flag_reason+")")
                       else:
                           print("(reason: Not supplied)")
        else:
            print("Cannot flag video: video already flagged")
        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if video_id  in self._vid_id:
            ind=self._vid_id.index(video_id)
            if self._flag[ind]==1:
                print("Succesfully removed flag from video:"+self._titl[ind])
                self._flag[ind]=0
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            
            print("Cannot remove flag from video: Video does not exist")
        
       # print("allow_video needs implementation")
