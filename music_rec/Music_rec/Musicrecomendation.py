import pandas as pd
import numpy as np

# no double printing
Dataset=pd.read_csv(r"Datasets/high_popularity_spotify_data.csv")
allgenre=['pop','rock','hip-hop','latin','electronic','gaming']
Dataset=Dataset[Dataset['playlist_genre'].isin(allgenre)]
allsubgenre=['modern','throwback','sof','classic','chill','global']
Dataset=Dataset[Dataset['playlist_subgenre'].isin(allsubgenre)]
# print((Dataset.value_counts('playlist_subgenre'),Dataset.value_counts('playlist_genre')))

Dataset.fillna("NO DATA",inplace=True,axis=0)
# print(Dataset.value_counts('playlist_subgenre'))
# print(Dataset.value_counts('playlist_genre'))
# allcoloums=Dataset.columns
# print(Dataset.columns)
allcoloums=np.array(Dataset.columns)
# print(allcoloums)
"""'energy' 'tempo' 'danceability' 'playlist_genre' 'loudness' 'liveness'
 'valence' 'track_artist' 'time_signature' 'speechiness'
 'track_popularity' 'track_href' 'uri' 'track_album_name' 'playlist_name'
 'analysis_url' 'track_id' 'track_name' 'track_album_release_date'
 'instrumentalness' 'track_album_id' 'mode' 'key' 'duration_ms'
 'acousticness' 'id' 'playlist_subgenre' 'type' 'playlist_id'"""
reqcoloums=['track_album_release_date','track_name','playlist_genre','track_popularity',
                  'playlist_subgenre','danceability','loudness','liveness','time_signature',
                     ]
Dataset=Dataset[reqcoloums]
start_date = '2000-01-01'
end_date = '2024-12-31'

Dataset=Dataset[
    (Dataset['track_album_release_date'] >= start_date) & 
    (Dataset['track_album_release_date'] <= end_date)
]
# Spotifydata=np.array(Dataset['track_popularity'])
def userdata():
    # user_profiles = pd.DataFrame([
    # {
    #     'user_id': 1,
    #     'preferred_genre': 'pop',
    #     'preferred_subgenre': 'dance-pop',
    #     'min_popularity': 80,
    #     'max_popularity': 95,
    #     'release_start': '2015-01-01',
    #     'release_end': '2025-12-31',
    #     'likes_danceable': True,
    #     'max_loudness': -4.5
    # },
    # {
    #     'user_id': 2,
    #     'preferred_genre': 'rock',
    #     'preferred_subgenre': 'alternative',
    #     'min_popularity': 70,
    #     'max_popularity': 90,
    #     'release_start': '2010-01-01',
    #     'release_end': '2023-12-31',
    #     'likes_danceable': False,
    #     'max_loudness': -5.5
    # },
    # {
    #     'user_id': 3,
    #     'preferred_genre': 'hip-hop',
    #     'preferred_subgenre': 'alternative',  # ignore subgenre
    #     'min_popularity': 75,
    #     'max_popularity': 100,
    #     'release_start': '2018-01-01',
    #     'release_end': '2025-12-31',
    #     'likes_danceable': True,
    #     'max_loudness': -3.5
    # }
    # ])
    user_profiles=pd.read_csv(r"Datasets/user_profiles_50.csv")
    user_profiles['max_loudness']=user_profiles['max_loudness']
    # print("user")
    # print(user_profiles['max_loudness'])
    return user_profiles
def userdata_numeric():
    user_profiles = userdata()  # your existing function
    df = user_profiles

    # Extract numeric features
    numeric_features = df[['min_popularity','max_popularity','likes_danceable','max_loudness'
                        #    ,'release_start','release_end'
                        ]].copy()
                         
    # print(type(numeric_features))
    numeric_features['likes_danceable'] = numeric_features['likes_danceable'].astype(int)  # convert bool to int
    # print(type(numeric_features))
    # print(numeric_features.columns)
    numeric_array = numeric_features.to_numpy()
    return numeric_array

reqcoloums=['track_popularity','danceability','loudness','playlist_genre',
                  'playlist_subgenre'
                     ]

user_data=userdata()
# print(user_data['preferred_genre'][1])
UserData_array = userdata_numeric()
# print(Dataset.columns)
Spotifydata_mod=np.array((Dataset['track_popularity'],Dataset['loudness']
                     ,Dataset['danceability']))
Spotifydata_category=np.array((Dataset['playlist_genre'],Dataset['playlist_subgenre']))

required_data_spotify=Dataset[reqcoloums]

# print(required_data_spotify.columns)

user_category=np.array((user_data['preferred_genre'],user_data['preferred_subgenre']))
# print(user_category[1])
# print(Spotifydata_category[1])
# Index(['track_album_release_date', 'track_name', 'playlist_genre',
#        'track_popularity', 'playlist_subgenre', 'danceability', 'loudness',
#        'liveness', 'time_signature'],
#       dtype='object') spotify data
#'min_popularity','max_popularity','likes_danceable','max_loudness'userdata

# for spotify data =track_popularity,,loudness,dancablity

class MusicRecomendationData:
    def __init__(self,user_no):
        self.user_no=user_no
        self.filtering_data_spotify()
        # self.filtering_data_spotify()
        self.filtering_data_user()
        self.spotify_datamodifier()
        self.user_datamodifier()
        self.stuff(user_no)
    def user_datamodifier(self):
        # 'min_popularity','max_popularity','likes_danceable','max_loudness'
        #       0               1               2               3
       self.user_popularity= (((UserData_array[:,0])+(UserData_array[:,1]))/2)
       self.user_loudness=((UserData_array[:,3]))
       self.user_dancable=((UserData_array[:,2]))
       self.user_genre=user_category[0]
       self.user_subgenre = user_category[1]
    def spotify_datamodifier(self):
        #track_popularity,,     loudness,     dancablity
        #   0                       1                2
        self.spotify_popularity=Spotifydata_mod[0]
        self.spotify_loudness=Spotifydata_mod[1]
        self.spotify_dancable=Spotifydata_mod[2]
        self.spotify_genre=Spotifydata_category[0]
        self.spotify_subgenre=Spotifydata_category[1]
        # print("LOUDENSS")
        # print(self.spotify_loudness)
        # print(self.varation_user)
    #all the accesing is done for now 
    def filtering_data_spotify(self):
        #my formula is =max of the array-mean of the array-standard devation=varation
        self.user_datamodifier()
        self.spotify_datamodifier()
        varation_popularity=self.spotify_popularity.max()-self.spotify_popularity.mean()
        varation_popularity=varation_popularity-self.spotify_popularity.std()
        varation_dancable=self.spotify_dancable.max()-self.spotify_dancable.mean()
        varation_dancable=varation_dancable-self.spotify_dancable.std()
        varation_loudness=self.spotify_loudness.max()-self.spotify_loudness.mean()
        varation_loudness=varation_loudness-self.spotify_loudness.std()
        self.varation_spotify=np.array((varation_popularity,varation_dancable,varation_loudness))
        # print(self.varation_spotify)
        return self.varation_spotify
    def filtering_data_user(self):
        varation_popularity_user=self.user_popularity.max()-self.user_popularity.mean()
        varation_popularity_user=varation_popularity_user-self.user_popularity.std()
        varation_dancable_user=self.user_dancable.max()-self.user_dancable.mean()
        varation_dancable_user=varation_dancable_user-self.user_dancable.std()
        varation_loudness_user=self.user_loudness.max()-self.user_loudness.mean()
        varation_loudness_user=varation_loudness_user-self.user_loudness.std()
        self.varation_user=np.array((varation_popularity_user,varation_dancable_user,varation_loudness_user))
        # print(self.varation_user)
        return self.varation_user
    def arrangedata_spotify(self):
        #popularity,dancable,loudness
        user=self.filtering_data_user()
        spotify=self.filtering_data_spotify()
        #i need to sort the spotify data first according to the genre
        #so that it will be easy for me to compare
        self.spotify_genre=required_data_spotify
        
        self.all_unique_genres = np.unique(self.user_genre)
        self.all_unique_subgenres = np.unique(self.user_subgenre)
        coloums_finaldata = np.unique(np.concatenate((self.user_genre, self.user_subgenre)))
        mask = np.isin(self.spotify_genre, coloums_finaldata)
        self.spotify_genre=self.spotify_genre[mask]
        # print(self.spotify_genre)
        return self.spotify_genre


    def stuff(self,user_no):
        
        # self.spotify_data=self.spotify_genre
        self.user_data=self.user_genre#This varaible stores all the playlist 
        self.user_subgenre=self.user_subgenre
        self.varation_user_data=self.filtering_data_user()
        self.varation_spotify_data=self.filtering_data_spotify()
        self.Comparring_data()
        self.algo_ranging(user_no)
        self.perfoming_filterantion(user_no)
        self.data_manuplating(user_no)
        # print(self.user_data)
        # print(self.spotify_genre)    
    def Comparring_data(self):
        
        self.pop_data=required_data_spotify[(required_data_spotify['playlist_genre']=='pop')]
        self.rock_data=required_data_spotify[(required_data_spotify['playlist_genre']=='rock')]
        self.hip_hop_data=required_data_spotify[(required_data_spotify['playlist_genre']=='hip-hop')]
        # print(self.user_data)
    def algo_ranging(self,user_no):
            # for i in range(len(self.varation_spotify_data)):         
            #     range_varation=np.array(((self.user_popularity[i])+self.varation_spotify_data[i]))
            self.range_varation_popularity=(((self.user_popularity[user_no])+self.varation_spotify_data[0]),
                                            ((self.user_popularity[user_no])-self.varation_spotify_data[0]))
            
            self.range_varation_loudness=(((self.user_loudness[user_no])+self.varation_spotify_data[2]),
                                            ((self.user_loudness[user_no])-self.varation_spotify_data[2]))
            self.range_varation_dancablity=(((self.user_dancable[user_no])+self.varation_spotify_data[1]),
                                            ((self.user_dancable[user_no])-self.varation_spotify_data[1]))
            self.range_all=((self.range_varation_popularity),( self.range_varation_loudness),( self.range_varation_dancablity))
            self.range_all=np.array( self.range_all)
            return self.range_all
                        # required_data_spotify
    def perfoming_filterantion(self,user_no):
                
               high_pop,low_pop=self.range_varation_popularity
               high_loud,low_loud=self.range_varation_loudness
               high_dance,low_dance=self.range_varation_dancablity
               single_user = user_data.iloc[user_no]
            #    print("Low:", low_dance, "High:", high_dance)
               self.Sorting_data=Dataset[(Dataset['playlist_genre']==single_user['preferred_genre'])]
               
               self.Sorting_data_pop=self.Sorting_data[
                   (self.Sorting_data['track_popularity']<=high_pop)&(self.Sorting_data['track_popularity']>=low_pop)
               ]
               self.Sorting_data_loud=self.Sorting_data[
                   (self.Sorting_data['loudness']>=low_loud) &(self.Sorting_data['loudness']<=high_loud)
               ]
               self.Sorting_data_dance=self.Sorting_data[
                  (self.Sorting_data['danceability']>=low_dance) &(self.Sorting_data['danceability']<=high_dance)
               ]
               self.sorted_data=self.Sorting_data[
    (self.Sorting_data['track_popularity'] >= low_pop) & (self.Sorting_data['track_popularity'] <= high_pop) &
    (self.Sorting_data['loudness'] >= low_loud) & (self.Sorting_data['loudness'] <= high_loud)
]
               
            #    print(Dataset.columns)
               self.sorted_data=(self.Sorting_data_pop, self.Sorting_data_loud,self.Sorting_data_dance)
            #    print(something[1])
            #    print((self.Sorting_data_pop.shape),(self.Sorting_data_loud.shape),(self.Sorting_data_dance.shape))
               return self.sorted_data
            #i have sorted all the data now it is time for extracting the songs
    def data_manuplating(self,user_no):
            user_filter_data=self.perfoming_filterantion(user_no)
            single_user = user_data.iloc[user_no]
            self.filtered_data = self.Sorting_data#this give mutilple recomadation , 
            
            self.filtered_data=self.filtered_data[(self.filtered_data['track_popularity']<(single_user['max_popularity']))
                                        
                                        ]
            
            # print(self.filtered_data)
            return self.filtered_data
 
#tbh i have just done the data so far , so now i need to comeup with a clearcut algorithim             
class Algorithm:
    def __init__(self,user_no):
        self.user_no=user_no
        self.md=MusicRecomendationData(self.user_no)
        self.algo_ranging()
        self.perfoming_filterantion(self.user_no)
        self.data_manuplating(self.user_no)
        self.algo_making(self.user_no)
        self.mod_data = self.final_data.copy()
        # self.retrevingdata(self.user_no)
        # self.Scraping_data(self.user_no)
        # print(self.filtered_data)
    def algo_ranging(self):
            # for i in range(len(self.varation_spotify_data)):         
            #     range_varation=np.array(((self.user_popularity[i])+self.varation_spotify_data[i]))
            self.range_varation_popularity=(((self.md.user_popularity[self.user_no])+self.md.varation_spotify_data[0]),
                                            ((self.md.user_popularity[self.user_no])-self.md.varation_spotify_data[0]))
            
            self.range_varation_loudness=(((self.md.user_loudness[self.user_no])+self.md.varation_spotify_data[2]),
                                            ((self.md.user_loudness[self.user_no])-self.md.varation_spotify_data[2]))
            self.range_varation_dancablity=(((self.md.user_dancable[self.user_no])+self.md.varation_spotify_data[1]),
                                            ((self.md.user_dancable[self.user_no])-self.md.varation_spotify_data[1]))
            self.range_all=((self.range_varation_popularity),( self.range_varation_loudness),( self.range_varation_dancablity))
            self.range_all=np.array( self.range_all)
            return self.range_all
                        # required_data_spotify
    def perfoming_filterantion(self,user_no):
                
               high_pop,low_pop=self.range_varation_popularity
               high_loud,low_loud=self.range_varation_loudness
               high_dance,low_dance=self.range_varation_dancablity
               single_user = user_data.iloc[self.user_no]
            #    print("Low:", low_dance, "High:", high_dance)
               self.Sorting_data=Dataset[(Dataset['playlist_genre']==single_user['preferred_genre'])]
               
               self.Sorting_data_pop=self.Sorting_data[
                   (self.Sorting_data['track_popularity']<=high_pop)&(self.Sorting_data['track_popularity']>=low_pop)
               ]
               self.Sorting_data_loud=self.Sorting_data[
                   (self.Sorting_data['loudness']>=low_loud) &(self.Sorting_data['loudness']<=high_loud)
               ]
               self.Sorting_data_dance=self.Sorting_data[
                  (self.Sorting_data['danceability']>=low_dance) &(self.Sorting_data['danceability']<=high_dance)
               ]
               self.sorted_data=self.Sorting_data[
    (self.Sorting_data['track_popularity'] >= low_pop) & (self.Sorting_data['track_popularity'] <= high_pop) &
    (self.Sorting_data['loudness'] >= low_loud) & (self.Sorting_data['loudness'] <= high_loud)
]
               
            #    print(Dataset.columns)
               self.sorted_data=(self.Sorting_data_pop, self.Sorting_data_loud,self.Sorting_data_dance)
            #    print(something[1])
            #    print((self.Sorting_data_pop.shape),(self.Sorting_data_loud.shape),(self.Sorting_data_dance.shape))
               return self.sorted_data
            #i have sorted all the data now it is time for extracting the songs
    def data_manuplating(self,user_no):
            user_filter_data=self.perfoming_filterantion(self.user_no)
            single_user = user_data.iloc[self.user_no]
            self.filtered_data = self.Sorting_data#this give mutilple recomadation , 
            
            self.filtered_data=self.filtered_data[(((self.filtered_data['track_popularity'])<(single_user['max_popularity'])) 
                                               &    ((self.filtered_data['track_popularity'])>(single_user['min_popularity']))
            )
                                        ]
            
            # print(self.filtered_data)
            return self.filtered_data
    def algo_making(self,user_no):
        self. final_data=self.data_manuplating(self.user_no).copy()
        self.user_property=[self.md.user_popularity[self.user_no],self.md.user_loudness[self.user_no],
                       self.md.user_dancable[self.user_no]]
        self.data_property=['track_popularity','loudness','danceability']
        self.user_dates=( pd.to_datetime(user_data['release_start'][self.user_no], errors='coerce'),
                     pd.to_datetime(user_data['release_end'][self.user_no], errors='coerce'))
        self.final_data['track_album_release_date']=pd.to_datetime(self.final_data['track_album_release_date']
                                                      , errors='coerce'        )
        
    def perofoming_algo(self,user_no,year):
        if year < 1950 or year > 2025:  # <-- base condition (adjust as needed)
            # print("Year out of valid range. Stopping recursion.")
            self.mod_data =self.final_data
            self.retrevingdata(self.user_no)
       
        spanyears= pd.DateOffset(years=year)
        self.mod_data=self.final_data[(self.final_data['track_album_release_date']>=(self.user_dates[0]
                                                                      - spanyears))&
               (self.final_data['track_album_release_date']<=(self.user_dates[1]+ spanyears))             ]
        # i perfomed one layer of data
        if year <= 0:
            self.retrevingdata(self.user_no) 
       
        if(self.mod_data.shape[0]==0):
            self.perofoming_algo(self.user_no,year=year-1)
            
        elif(self.mod_data.shape[0]==1):
            
            print(self.mod_data['track_name'])
            return self.mod_data['track_name']
            
        else:
            # print("going")
            self.retrevingdata(self.user_no)   
            pass
        
    def retrevingdata(self,user_no):
        tolorence=0
        step=0.1
        data=self.mod_data.copy()
        # print(data.shape)
        checking_change=self.mod_data.shape[0]
        
        z=(self.user_property,self.data_property)
        while((data.shape[0]>1 ) and (tolorence <=30)):
           
            data=self.mod_data[(self.mod_data['track_popularity']>=(self.user_property[0]+tolorence))
                           ]
            tolorence += step
        
        # print(data)
        if(data.shape[0]!=1):
            data=self.mod_data.copy()
            return self.Scraping_data(data,1)
            
        else:
            print(data['track_name'])  
            return data['track_name']
            

    def Scraping_data(self,data,value):
        if (value>4):
            return "NO DATA"
        returining_data=None
    
        # print(data)
        match value:
            case 1:
                tolorence=0
                step=0.1
                while((data.shape[0]>1 ) and (tolorence <=30)):
           
                    data=self.mod_data[(self.mod_data['track_popularity']>=(self.user_property[0]+tolorence))
                           ]
                    tolorence += step
                if(data.shape[0]!=1):
                    # print("MOVING")
                    data=self.mod_data.copy()
                    return self.Scraping_data(data,value=value+1)
                else:
                    print(data['track_name']) 
                    returining_data=data['track_name']
                    return returining_data
            case 2:
                tolorence=0
                step=0.1
                while((data.shape[0]>1 ) and (tolorence <=30)):
           
                    data=self.mod_data[(self.mod_data['track_popularity']<=(self.user_property[0]-tolorence))
                           ]
                    tolorence += step
                if(data.shape[0]!=1):
                    # print("MOVING")
                    data=self.mod_data.copy()
                    return self.Scraping_data(data,value=value+1)
                else:
                    print(data['track_name'])
                    returining_data=data['track_name']
                    return  returining_data
            case 3:
                #default popularity song
                if(data.shape[0]>=1):
                    print(f"{(data['track_name'].iloc[0])} ")
                    returining_data=data['track_name'].iloc[0]#code
                    return returining_data
                # self.Scraping_data(data,value=value+1) 
            case 4:
                closest_idx = (self.mod_data['track_popularity'] - self.user_property[0]).abs().idxmin()
                closest_song = self.mod_data.loc[closest_idx, 'track_name']
                closest_pop = self.mod_data.loc[closest_idx, 'track_popularity']
                print(f"🎧 No perfect match, but you might like '{closest_song}' (popularity: {closest_pop})")
                return closest_song
        
def collectinguser_data():
    skip=[16,36]
    
    collection_data=[]
    for i in range(user_data.shape[0]):
        if (i+1 in skip):
            continue 
        algo=Algorithm(i)
        collection_data.append(algo.retrevingdata(i))
        
    return collection_data
listing=collectinguser_data()

# print(listing[0])

# skip=[16,36]
# for i in range(user_data.shape[0]):
#     if (i+1 in skip):
#         continue
#     user=i
#     print(f"USER{i+1}")
#     algo=Algorithm(user)
    




