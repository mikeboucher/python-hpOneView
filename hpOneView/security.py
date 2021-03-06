# -*- coding: utf-8 -*-

"""
security.py
~~~~~~~~~~~~

This module implements Settings HP OneView REST API
"""

__title__ = 'security'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright 2012-2014 Hewlett-Packard Development ' \
                ' Company, L.P.'
__license__ = 'MIT'
__status__ = 'Development'

###
# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from hpOneView.common import *
from hpOneView.connection import *
from hpOneView.activity import *
from hpOneView.exceptions import *


class security(object):

    def __init__(self, con):
        self._con = con

    ###########################################################################
    # User management and Roles
    ###########################################################################
    def get_users(self):
        global uri
        body = self._con.get(uri['users'])
        return get_members(body)

    def get_user(self, user):
        global uri
        body = self._con.get(uri['users'] + '/' + user)
        return body

    def get_user_roles(self, user):
        global uri
        body = self._con.get(uri['userRole'] + '/' + user)
        return get_members(body)

    def set_user_roles(self, user, roles):
        global uri
        request = []
        for role in roles:
            req = {'type': 'RoleNameDtoV2', 'roleName': role}
            request.append(req)
        task, body = self._con.put(uri['users'] + '/' + user +
                             '/roles?multiResource=true', request)
        return body

    def set_user_role(self, user, role):
        global uri
        request = {'type': 'RoleNameDtoV2', 'roleName': role}
        task, body = self._con.put(uri['users'] + '/' + user +
                             '/roles?multiResource=true', [request])
        return body

    def create_user(self, name, password, enabled=True, fullName='',
                    emailAddress='', officePhone='', mobilePhone='',
                    roles=['Infrastructure administrator']):
        global uri
        usr = make_user_dict(name, password, enabled, fullName,
                             emailAddress, officePhone, mobilePhone,
                             roles)
        task, body = self._con.post(uri['users'], usr)
        return body

    def delete_user(self, user):
        global uri
        task, body = self._con.delete(uri['users'] + '/' + user)
        return body

    def update_user(self, updateUser):
        global uri
        task, body = self._con.put(uri['users'], updateUser)
        return body

    def get_roles(self):
        global uri
        body = self._con.get(uri['roles'])
        return get_members(body)

    ###########################################################################
    # Certificates
    ###########################################################################
    def get_certs(self):
        global uri
        body = self._con.get(uri['certificates'])
        return body

    def get_cert_https(self):
        global uri
        body = self._con.get(uri['cert-https'])
        return body

    def get_cert_ca(self):
        global uri
        body = self._con.get(uri['ca'])
        return body

    def get_cert_ca_crl(self):
        global uri
        body = self._con.get(uri['crl'])
        return body

    def gen_rabbitmq_ca(self):
        global uri
        request = {'type': 'RabbitMqClientCert', 'commonName': 'default'}
        task, body = self._con.post(uri['rabbitmq'], request)
        return body

    def get_rabbitmq_kp(self, alias='default'):
        global uri
        body = self._con.get(uri['rabbitmq-kp'] + '/' + alias)
        return body

    def get_rabbitmq_ca(self, alias='default'):
        global uri
        body = self._con.get(uri['rabbitmq'] + '/' + alias)
        return body

    def get_active_user_sessions(self):
        global uri
        body = self._con.get(uri['activeSessions'])
        return body

    def get_category_actions(self):
        global uri
        body = self._con.get(uri['category-actions'])
        return body

    def get_role_category_actions(self):
        global uri
        body = self._con.get(uri['role-category-actions'])
        return body



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
