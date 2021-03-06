# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Actions for interacting with the host system."""

import logging
from glazier.lib.actions.base import BaseAction
from glazier.lib.actions.base import RestartEvent
from glazier.lib.actions.base import ShutdownEvent
from glazier.lib.actions.base import ValidationError


class _PowerAction(BaseAction):

  def Validate(self):
    self._TypeValidator(self._args, list)
    if len(self._args) not in [1, 2]:
      raise ValidationError('Invalid args length: %s' % self._args)
    if not isinstance(self._args[0], str) and not isinstance(self._args[0],
                                                             int):
      raise ValidationError('Invalid argument type: %s' % self._args[0])
    if len(self._args) > 1 and not isinstance(self._args[1], str):
      raise ValidationError('Invalid argument type: %s' % self._args[1])


class Reboot(_PowerAction):
  """Perform a host reboot."""

  def Run(self):
    timeout = str(self._args[0])
    reason = 'unspecified'
    if len(self._args) > 1:
      reason = str(self._args[1])
    logging.info('Rebooting with a timeout of %s and a reason of %s', timeout,
                 reason)
    raise RestartEvent(reason, timeout=timeout)


class Shutdown(_PowerAction):
  """Perform a host shutdown."""

  def Run(self):
    timeout = str(self._args[0])
    reason = 'unspecified'
    if len(self._args) > 1:
      reason = str(self._args[1])
    logging.info('Shutting down with a timeout of %s and a reason of %s',
                 timeout, reason)
    raise ShutdownEvent(reason, timeout=timeout)
