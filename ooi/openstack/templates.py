# -*- coding: utf-8 -*-

# Copyright 2015 Spanish National Research Council
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ooi.occi.core import attribute
from ooi.occi.core import mixin
from ooi.occi.infrastructure import templates
from ooi.openstack import helpers


class OpenStackOSTemplate(mixin.Mixin):
    scheme = helpers.build_scheme("template/os")

    def __init__(self, uuid, name):
        super(OpenStackOSTemplate, self).__init__(
            OpenStackOSTemplate.scheme,
            uuid,
            name,
            related=[templates.os_tpl])


class OpenStackResourceTemplate(mixin.Mixin):
    scheme = helpers.build_scheme("template/resource")

    def __init__(self, id, name, cores, memory, disk, ephemeral=0, swap=0):
        attrs = [
            attribute.InmutableAttribute("occi.compute.cores", cores),
            attribute.InmutableAttribute("occi.compute.memory", memory),
            attribute.InmutableAttribute("occi.compute.disk", disk),
            attribute.InmutableAttribute("occi.compute.ephemeral", ephemeral),
            attribute.InmutableAttribute("occi.compute.swap", swap),
            attribute.InmutableAttribute("org.openstack.flavor.name", name)
        ]

        attrs = attribute.AttributeCollection({a.name: a for a in attrs})

        super(OpenStackResourceTemplate, self).__init__(
            OpenStackResourceTemplate.scheme,
            id,
            "Flavor: %s" % name,
            related=[templates.resource_tpl],
            attributes=attrs)

    @property
    def cores(self):
        return self.attributes["occi.compute.cores"].value

    @property
    def memory(self):
        return self.attributes["occi.compute.memory"].value

    @property
    def disk(self):
        return self.attributes["occi.compute.disk"].value

    @property
    def ephemeral(self):
        return self.attributes["occi.compute.ephemeral"].value

    @property
    def swap(self):
        return self.attributes["occi.compute.swap"].value

    @property
    def name(self):
        return self.attributes["org.openstack.flavor.name"].value
