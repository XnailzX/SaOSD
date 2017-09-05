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

"""Store points in time to be used for metrics."""

import datetime


class Timers(object):
  """Store named time elements."""

  def __init__(self):
    self._time_store = {}

  def Get(self, name):
    """Get the stored value of a single timer.

    Args:
      name: The name of the timer being requested.

    Returns:
      A specific named datetime value if stored, or None
    """
    if name in self._time_store:
      return self._time_store[name]
    return None

  def GetAll(self):
    """Get the dictionary of all stored timers.

    Returns:
      A dictionary of all stored timer names and values.
    """
    return self._time_store

  def Now(self):
    """Get the current time using the default timer method.

    Returns:
      A datetime object.
    """
    return datetime.datetime.utcnow()

  def Set(self, name, at_time=None):
    """Set a timer at a specific time.

    Defaults to the current time in UTC.

    Args:
      name: Name of the timer being set.
      at_time: A predetermined time value to store.
    """
    if at_time:
      self._time_store[name] = at_time
    else:
      self._time_store[name] = self.Now()
