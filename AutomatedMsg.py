import pywhatkit
import win32clipboard

"""SENDING AUTOMATED WHATSAPP MESSAGE TO A SINGLE CHAT"""
# pywhatkit.sendwhatmsg("+91 7977807180",
#                       "Hello..!",
#                       17,0o2)


"""USING THE LIBRARY TO AUTOMATICALLY PLAY YOUTUBE VIDEOS"""
# # This is to play a youtube video
# pywhatkit.playonyt("https://www.youtube.com/watch?v=wyE9x5HETkY&list=RDCtUIXnJKPgU&index=3")

"""USING THE LIBRARY TO AUTOMATICALLY SEARCH ON SEARCH ENGINE"""
# this is to search on search Engine
# pywhatkit.search("LIONEL MESSI")

"""SENDING A AUTOMATED MESSAGE ON WHATSAPP GROUP"""
# pywhatkit.sendwhatmsg_to_group("DHG53GmzF6bH7KXl54rHJx", "Tumlog mai se koi PTA mai baita tha?", 17, 0o7)


"""SENDING A AUTOMATED IMAGE USING PYWHATKIT

Main: import win32clipboard (pip install pywin32)
don't use \ instead use /
we can also use (r) before starting a string to let know that it is a string
we can also use (\\) before starting a string to let know that it is a string
if you give the boolean value TRUE.. then whatsapp will close immediately after sending the message
So always put FALSE """
#
# pywhatkit.sendwhats_image("+91 7977807180",
#                           "C:/Users/hp/PycharmProjects/Python_mini/Operation_Kingfish_2013_group_crop.png",
#                           "This is a image sent by Pycharm to a whatsapp group",
#                           10, False, 2)
#
# """ Automating messages """

pywhatkit.show_history()