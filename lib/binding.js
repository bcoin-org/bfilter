/*!
 * bfilter
 * Copyright (c) 2017, Christopher Jeffrey (MIT License).
 * https://github.com/bcoin-org/bfilter
 */

'use strict';

if (process.env.BFILTER_BACKEND && process.env.BFILTER_BACKEND !== 'native')
  throw new Error('Non-native backend selected.');

const binding = require('bindings')('bfilter');

exports.murmur3 = {
  sum: binding.murmur3_sum,
  tweak: binding.murmur3_tweak
};
