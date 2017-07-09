# coding=utf-8
from __future__ import unicode_literals
from AngelHack.AngelHack import settings
from lxml import html
from six import print_
import requests
import asana
import sys, os
import http.client
import json


class AsanaAuth:

    @staticmethod
    def clientauth():
        """

        :return:
        """
        client = asana.Client.oauth(
            client_id=settings.ASANA_CLIENT_ID,
            client_secret=settings.ASANA_CLIENT_SECRET,
            redirect_uri=settings.ASANA_OAUTH_REDIRECT_URI,
        )
        print_("authorized =", client.session.authorized)
        (url, state) = client.session.authorization_url()
        try:
            # in a web app you'd redirect the user to this URL when they take action to
            # login with Asana or connect their account to Asana
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print_("Open the following URL in a browser to authorize:")
            print_(url)
            print(e)

        print_("Copy and paste the returned code from the browser and press enter:")
        code = sys.stdin.readline().strip()
        # exchange the code for a bearer token


        token = client.session.fetch_token(code=code)

        print_("token=", json.dumps(token))
        print_("authorized=", client.session.authorized)
        print_("me=", client.users.me())

        # normally you'd persist this token somewhere
        os.environ['ASANA_TOKEN'] = json.dumps(token)  # (see below)

    if 'ASANA_TOKEN' in os.environ:
        # create a client with your OAuth client ID and a previously obtained bearer token
        client = asana.Client.oauth(
            client_id=os.environ['ASANA_CLIENT_ID'],
            token=json.loads(os.environ['ASANA_TOKEN'])
        )
        print_("authorized=", client.session.authorized)
        print_("me=", client.users.me())

    if 'ASANA_ACCESS_TOKEN' in os.environ:
        # create a client with a Personal Access Token
        client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
        me = client.users.me()
        print_("me=" + json.dumps(me, indent=2))

        # find your "Personal Projects" workspace
        personal_projects = next(workspace for workspace in me['workspaces'] if workspace['name'] == 'Personal Projects')
        projects = client.projects.find_by_workspace(personal_projects['id'], iterator_type=None)
        print_("personal projects=" + json.dumps(projects, indent=2))

        # create a "demo project" if it doesn't exist
        try:
            project = next(project for project in projects if project['name'] == 'demo project')
        except Exception as e:
            print_("creating 'demo project'")
            project = client.projects.create_in_workspace(personal_projects['id'], {'name': 'demo project'})
        print_("project=", project)

        # start streaming modifications to the demo project.
        # make some changes in Asana to see this working
        print_("starting streaming events for " + project['name'])
        for event in client.events.get_iterator({'resource': project['id']}):
            print_("event", event)


class TeamViewer():
    strClientId = '119295-Ynu7oSEM16okHcWBzvXb'
    strClientSecret = ' XSUrd9iaykqVKVKEbG96'
    apiVersion = "v1"
    tvApiBaseUrl = "webapi.teamviewer.com"
    tvApiPort = 443

    currentPath = os.path.abspath(os.path.dirname(sys.argv[0]))

    def RequestOAuthAccessToken(strClientId, strClientSecret, strAuthorizationCode):
        print("")
        print("Get token...")
        print("Request [POST] /api/" + apiVersion + "/oauth2/token")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()

            request = conn.putrequest('POST', '/api/' + apiVersion + '/oauth2/token')

            payload = "grant_type=authorization_code&code=" + strAuthorizationCode + "&client_id=" + strClientId + "&client_secret=" + strClientSecret

            headers = {}
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            headers['Content-Length'] = "%d" % len(payload)
            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            print("Payload :" + payload)
            conn.send(payload)

            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if (statusCode != 200):
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            jsonResp = json.loads(resp.read())
            result = jsonResp["access_token"]

            print("Token received.")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    def PingAPI(accessToken):

        print("")
        print("Ping API...")
        print("Request [GET] /api/" + apiVersion + "/ping")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()

            request = conn.putrequest('GET', '/api/' + apiVersion + '/ping')

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()
            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 200:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result
            jsonResp = json.loads(resp.read())
            tokenValue = jsonResp["token_valid"]
            if tokenValue:
                print("Ping: Token is valid")
                result = True
            else:
                result = False

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False
        return result

    # get all users of a company with all available fields
    def GetAllUsersAPI(accessToken):
        print("")
        print("Get all users...")
        print("Request [GET] /api/" + apiVersion + "/users?full_list=true")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()

            request = conn.putrequest('GET', '/api/' + apiVersion + '/users?full_list=true')

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            conn.send("")
            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 200:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            result = json.loads(resp.read())
            result = result["users"]

            print("Request ok!")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    # get a single company user, identified by email
    def GetUserByMail(accessToken, strMail):
        print("")
        print("Get single user by mail (" + strMail + ")")
        print("Request [GET] /api/" + apiVersion + "/users?email=" + strMail + "&full_list=true")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()

            request = conn.putrequest('GET', '/api/' + apiVersion + '/users?email=' + strMail + '&full_list=true')

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            conn.send("")

            # Check response
            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 200:
                print("nexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            result = json.loads(resp.read())
            result = result["users"]

            print("Request ok!")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    # Updates a single company user:
    #   Field values in dictUser will be used to update the given user id (updateUserId)
    #   if email should be updated, the dict must declare a column "newEmail" with the new email value
    def UpdateUser(accessToken, updateUserId, dictUser):
        print("")
        print("Updating user [" + dictUser["email"] + "]")
        print("Request [PUT] /api/" + apiVersion + "/users/" + str(updateUserId))
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()
            request = conn.putrequest('PUT', '/api/' + apiVersion + '/users/' + str(updateUserId))

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            headers['Content-Type'] = 'application/json; charset=utf-8'

            # define update fields
            updatePayload = {}

            # name parameter
            if ("name" in dictUser and len(dictUser["name"]) > 0):
                updatePayload["name"] = dictUser["name"]

            # password parameter
            if ("password" in dictUser and len(dictUser["password"]) > 5):
                updatePayload["password"] = dictUser["password"]

                # permission parameter
            if ("permissions" in dictUser and len(dictUser["permissions"]) > 0):
                updatePayload["permissions"] = dictUser["permissions"]

            # email parameter (column newEmail must exist in csv)
            if ("newMail" in dictUser and len(dictUser["newEmail"]) > 5):
                updatePayload["email"] = dictUser["newEmail"]

                # active parameter (assume every user to be updated is also active per default)
            if ("active" in dictUser and len(dictUser["active"]) > 0):
                updatePayload["active"] = Str2Bool(str(dictUser["active"]))
            else:
                updatePayload["active"] = True

            jsonPayload = json.dumps(updatePayload)

            headers['Content-Length'] = "%d" % len(jsonPayload)

            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            print("Payload: " + jsonPayload)
            conn.send(jsonPayload)

            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode == 204:
                print("User updated.")
                result = True
            else:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    # Creates a single company user:
    #   Field values in dictUser will be used to create the given user.
    #   Defaults for some missing fields (permissions, password, language) must be provided.
    def CreateUser(accessToken, dictUser, defaultUserPermissions, defaultUserLanguage, defaultUserPassword):
        print("")
        print("Creating user [" + dictUser["email"] + "]")
        print("Request [POST] /api/" + apiVersion + "/users")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()
            request = conn.putrequest('POST', '/api/' + apiVersion + '/users')

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            headers['Content-Type'] = 'application/json; charset=utf-8'

            # define fields
            createPayload = {}

            # name parameter
            if "name" in dictUser and len(dictUser["name"]) > 0:
                createPayload["name"] = dictUser["name"]
            else:
                print("Field [name] is missing. Can't create user.")
                return False

            # email parameter (field [newMail] must exist for this to work)
            if "email" in dictUser and len(dictUser["email"]) > 5:
                createPayload["email"] = dictUser["email"]
            else:
                print("Field [email] is missing. Can't create user.")
                return False

            # password parameter
            if "password" in dictUser and len(dictUser["password"]) > 5:
                createPayload["password"] = dictUser["password"]
            else:  # use defaultUserPassword parameter
                createPayload["password"] = defaultUserPassword

            # permission parameter
            if "permissions" in dictUser and len(dictUser["permissions"]) > 0:
                createPayload["permissions"] = dictUser["permissions"]
            else:  # use defaultUserPermissions parameter
                createPayload["permissions"] = defaultUserPermissions

            # language parameter
            if "language" in dictUser and len(dictUser["language"]) > 0:
                createPayload["language"] = dictUser["language"]
            else:  # use defaultUserLanguage parameter
                createPayload["language"] = defaultUserLanguage

            jsonPayload = json.dumps(createPayload)

            headers['Content-Length'] = "%d" % len(jsonPayload)

            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            print("Payload :" + jsonPayload)
            conn.send(jsonPayload)

            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 200:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            print("Request ok!")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    # Deactivates a single company user:
    def DeactivateUser(accessToken, userId):
        print("")
        print("Deactivating user [" + str(userId) + "]")
        print("Request [PUT] /api/" + apiVersion + "/users/" + str(userId))
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()
            request = conn.putrequest('PUT', '/api/' + apiVersion + '/users/' + str(userId))

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            headers['Content-Type'] = 'application/json; charset=utf-8'

            # define update fields
            updatePayload = {}

            updatePayload["active"] = False

            jsonPayload = json.dumps(updatePayload)

            headers['Content-Length'] = "%d" % len(jsonPayload)

            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            print("Payload :" + jsonPayload)
            conn.send(jsonPayload)

            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 204:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            print("Request ok!")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return result

    # get all connections of a company with all available fields
    def GetAllConnectionsAPI(accessToken):
        print("")
        print("Get all connections...")
        print("Request [GET] /api/" + apiVersion + "/reports/connections")
        result = False

        try:
            conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
            conn.connect()

            request = conn.putrequest('GET', '/api/' + apiVersion + '/reports/connections')

            headers = {}
            headers['Authorization'] = 'Bearer ' + accessToken
            for k in headers:
                conn.putheader(k, headers[k])
            conn.endheaders()

            conn.send("")
            resp = conn.getresponse()
            statusStr = resp.reason
            statusCode = resp.status

            print(statusCode, statusStr)

            if statusCode != 200:
                print("Unexpected response code. Received content was:")
                print(resp.read())
                result = False
                return result

            result = json.loads(resp.read())

            if 'next_offset' in result:
                moreConnections = GetMoreConnectionsAPI(accessToken, result)
                return moreConnections

            if 'records' in result:
                storedConnections = {}
                moreConnections = result["records"]
                storedConnections["Connections %d" % 0] = moreConnections

            print("Request ok!")

        except Exception as e:
            print("Request failed! The error was: ", e)
            result = False

        return storedConnections

    def GetMoreConnectionsAPI(self, strAccessToken, connectObj):
        result = connectObj
        accessToken = strAccessToken

        storedConnections = {}
        moreConnUrl = ""
        i = int(0)

        # as long as result have item next, loop
        while 'next_offset' in result:
            print("More connections found ...")
            # store more connections in dict
            if 'records' in result:
                moreConnections = result["records"]
                storedConnections["Connections %d" % i] = moreConnections
                moreConnUrl = '?offset_id=' + result["next_offset"]

            try:
                conn = http.client.HTTPSConnection(tvApiBaseUrl, tvApiPort)
                conn.connect()

                request = conn.putrequest('GET', '/api/' + apiVersion + '/reports/connections' + moreConnUrl)

                headers = {}
                headers['Authorization'] = 'Bearer ' + accessToken
                for k in headers:
                    conn.putheader(k, headers[k])
                conn.endheaders()

                conn.send("")
                resp = conn.getresponse()
                statusStr = resp.reason
                statusCode = resp.status

                print(statusCode, statusStr)

                if statusCode != 200:
                    print("Unexpected response code. Received content was:")
                    print(resp.read())
                    result = False
                    return result

                result = json.loads(resp.read())
                i +=1
            except:
                print('error/exception')

        # writes the last connections in the dictionary
        if 'records' in result:
            moreConnections = result["records"]
            storedConnections["Connections %d" % i] = moreConnections

        return storedConnections

    def Str2Bool(self, str):
        return str.lower() in ("true", "1", "t")