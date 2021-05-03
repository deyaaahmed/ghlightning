#!/usr/bin/env python3
# Will Being Coded By: Nader.
"""
A Python module whose function is to extract the information of github users
download their photos, get a lot of information about the country of any user
on github, know a number of his followers, download his followers pictures
and many, many advantages that you can try!
########################
Was Developed By: Nader.
########################
"""
import os
from urllib.request import urlretrieve
import pathlib
import countryinfo
import requests.exceptions
from requests import get


class Github:
    """ Pass a Github username to the object of this class to begin collect information!"""

    def __init__(self, username):
        self.username = username

        self.__headersDic = {
            "Authorization": "token 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"
        }

        self.__resp = get(f"https://api.github.com/users/{self.username}", headers=self.__headersDic).json()

        try:
            self.userId = self.__resp["id"]
        except:
            self.userId = None
        try:
            self.fullName = self.__resp["name"]
        except:
            self.fullName = None

        try:
            self.countryName = str(self.__resp["location"]).split(",")[1].strip()
        except Exception as e:
            self.countryName = None

        try:
            get(f"https://www.github.com/{self.username}")
        except requests.exceptions.ConnectionError:
            print("username is NOT invalid.")

        if self.username.strip() == "":
            print("Github username must NOT be empty.")

        try:
            self.email = self.__resp["email"]
        except:
            self.email = None
        try:
            self.followers = self.__resp["followers"]
        except:
            self.followers = None
        try:
            self.following = self.__resp["following"]
        except:
            self.following = None
        try:
            self.repos = self.__resp["public_repos"]
        except:
            self.repos = None

        self.CURRENT_PATH = os.getcwd()

    def __createPathAndEnterIn(self, Path):
        if not os.path.exists(Path):
            os.mkdir(Path)
        os.chdir(Path)

    def fetchInfo(self) -> tuple:
        """ Method For Collecting All user info such as his followers number, email, full name and more """
        res = self.__resp  # API request.
        # ################################################# Begin User Info
        # ##################################################

        """ ############# """

        """ For Test """
        # def info(query):
        #     return res[query]

        """ ############# """
        userInfo = {}  # Dictionary to store user info.
        """

        user_id = res["id"]
        profile_pic = res["avatar_url"]
        followers_url = res["followers_url"]
        following_url = res["following_url"]
        repos_url = res["repos_url"]
        length_of_repos = len(repos_url)
        name = res["name"]
        company = res["company"]
        blog = res["blog"]
        location = res["location"]
        email = res["email"]
        hireable = res["hireable"]
        bio = res["bio"]
        twitter_username = res["twitter_username"]
        puplic_repos = res["public_repos"]
        followes = res["followers"]
        following = res["following"]
        created_at = res["created_at"]
        last_Update = res["updated_at"]

        """
        """
        userInfo.update({
            "user_id": user_id,
            "profile_pic": profile_pic,
            "followers_url": followers_url,
            "following_url": following_url,
            "repos_url": repos_url,
            "length_of_repos": length_of_repos,
            "name": name,
            "company": company,
            "blog": blog,
            "location": location,
            "email": email,
            "hireable": hireable,
            "bio": bio,
            "twitter_username": twitter_username,
            "puplic_repos": puplic_repos,
            "followes": followes,
            "following": following,
            "created_at": created_at,
            "last_Update": last_Update
        }) """  # Append data to userInfo Dictionary.

        ############################################## End User Info ##############################################
        return res

    def countryInfo(self):
        """ A simple function to collect information about any country """
        if self.countryName is None:
            return None
        try:
            country = countryinfo.CountryInfo(self.countryName)
            countryInfo = country.info()
        except:
            return None
        return countryInfo

    current_path = os.getcwd()

    def downloadProfilePic(self, Path=current_path):
        """ Method for downloading specific  profile picture of Github user or Id
         You can specify the path for downloading the picture, default is current path.
         """
        if not os.path.exists(Path):
            os.mkdir(Path)

        os.chdir(Path)

        picUrl = f"https://avatars.githubusercontent.com/u/{self.__resp['id']}?v=4"  # The profile pic of the
        # object or instance.
        picName = self.username + ".jpeg"

        # if not os.path.isfile(os.path.join(os.path.abspath(Path), picName)):
        if not pathlib.Path(picName).exists():
            urlretrieve(picUrl, picName)
            """
            print(pathlib.Path(picName))
            print(pathlib.Path(picName).exists())
            """
        else:
            pass
        os.chdir(self.CURRENT_PATH)

        return os.path.abspath(os.path.join(Path, picName))

    """
    # def downloadAllProfPics(self, path=current_path):
    #     Method for downloading specific number of profile pictures of Github users 
    #     # if not os.path.exists(path):
    #     #     os.mkdir(path)
    #     #
    #     # os.chdir(path)
    #
    #     pass
    """

    def getProfileById(self, UserId: str) -> str:
        """ Method that gets the user link profile by his Github id """
        api = f"https://api.github.com/user/{UserId}"  # API for return user info by ID.
        profileLink = get(api).json()["html_url"]
        return profileLink

    def fetch(self):
        """ Method For Collecting All user info such as his followers number, email, full name and more """
        api = f"https://api.github.com/users/{self.username}"

        token = "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"

        headersDic = {
            "Authorization": f"token {token}"
        }
        resp = get(api, headers=headersDic).json()
        return resp

    def getFollowersProfiles(self) -> list:
        """ Simple method for fetching followers urls """
        followersProfiles = []
        followersProfilesResponse = get(self.__resp["followers_url"]).json()
        for item in followersProfilesResponse:
            followersProfiles.append(item["html_url"])
        return followersProfiles

    def getFollowingProfilesPics(self) -> list:
        """ Get All Following Pictures """

        followingProfilesPicsList = []

        followersProfilesPicsRespone = get(f"https://api.github.com/users/{self.username}/following",
                                           headers=self.__headersDic).json()

        """ Fetching Profiles Pictures """
        for item in followersProfilesPicsRespone:
            followingProfilesPicsList.append(item["avatar_url"])

        return followingProfilesPicsList

    def getFollowersProfilesPics(self) -> list:
        """ Get All Followers Pictures """
        followersProfilesPicsList = []

        followersProfilesPicsRespone = get(f"https://api.github.com/users/{self.username}/followers",
                                           headers=self.__headersDic).json()

        """ Fetching Profiles Pictures """
        for item in followersProfilesPicsRespone:
            followersProfilesPicsList.append(item["avatar_url"])

        return followersProfilesPicsList

    def downloadFollowersPics(self, Path=current_path):
        """ Method for downloading followers profile photos  """

        self.__createPathAndEnterIn(Path)

        followersProfilesPicsList = self.getFollowersProfilesPics()

        """ Downloading Profiles Pictures """
        for imageLink in followersProfilesPicsList:
            imgName = (str(imageLink).split("/")[-1])[:-4] + ".jpeg"
            if not pathlib.Path(imgName).exists():
                urlretrieve(imageLink, imgName)
            else:
                # print(f"image {imgName} is already exists")
                pass
        os.chdir(self.CURRENT_PATH)

    def downloadFollowingPics(self, Path=current_path):
        """ Method for downloading following profile photos  """
        self.__createPathAndEnterIn(Path)

        followingsProfilesPicsList = self.getFollowingProfilesPics()

        """ Downloading Profiles Pictures """
        for imageLink in followingsProfilesPicsList:
            imgName = (str(imageLink).split("/")[-1])[:-4] + ".jpeg"
            if not pathlib.Path(imgName).exists():
                urlretrieve(imageLink, imgName)
            else:
                # print(f"image {imgName} is already exists")
                pass
        os.chdir(self.CURRENT_PATH)

    def __path__(self):
        return os.path.abspath(__file__)

    def getFollowersEmails(self) -> list:
        followersEmails = []
        for followerData in get(self.__resp["followers_url"], headers=self.__headersDic).json():
            try:
                followersEmails.append(get(followerData["url"], headers=self.__headersDic).json()["email"])
                # print(followerData["login"]["email"])
                # print(get(followerData["url"]).json()["email"])
            except:
                pass
        return followersEmails

    def getFollowingEmails(self) -> list:
        followingEmails = []
        for followingData in get(self.__resp["following_url"], headers=self.__headersDic).json():
            try:
                followingEmails.append(get(followingData["url"], headers=self.__headersDic).json()["email"])
                # print(get(followingData["url"]).json()["email"])
                # print(followingData)
            except:
                pass
        return followingEmails


"""    
################################################## Begin User Info ##################################################

"""  # For Test """
# def info(query):
#     return res[query]


# USER_ID = res["id"]
# PROFILE_PIC = res["avatar_url"]
# FOLLOWERS_URL = res["followers_url"]
# FOLLOWING_URL = res["following_url"]
# REPOS_URL = res["repos_url"]
# LENGTH_OF_REPOS = len(REPOS_URL)
# NAME = res["name"]
# COMPANY = res["company"]
# BLOG = res["blog"]
# LOCATION = res["location"]
# EMAIL = res["email"]
# HIREABLE = res["hireable"]
# BIO = res["bio"]
# TWITTER_USERNAME = res["twitter_username"]
# PUPLIC_REPOS = res["public_repos"]
# FOLLOWES = res["followers"]
# FOLLOWING = res["following"]
# CREATED_AT = res["created_at"]
# LAST_UPDATE = res["updated_at"]

################################################## End User Info ##################################################

# print(USER_ID)
# print(PROFILE_PIC)
# print(FOLLOWERS_URL)
# print(FOLLOWING_URL)
# print(REPOS_URL)
# print(LENGTH_OF_REPOS)
# print(NAME)
# print(COMPANY)
# print(BLOG)
# print(LOCATION)
# print(EMAIL)
# print(HIREABLE)
# print(BIO)
# print(TWITTER_USERNAME)
# print(PUPLIC_REPOS)
# print(FOLLOWES)
# print(FOLLOWING)
# print(CREATED_AT)
# print(LAST_UPDATE)"""
