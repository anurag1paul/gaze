#!/bin/sh

ps -ef | grep "joint_attention" | grep -v grep | awk '{print $2}' | xargs kill -15
