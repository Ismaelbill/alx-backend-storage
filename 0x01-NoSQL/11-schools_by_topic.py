#!/usr/bin/env python3
""" Where can I learn Python? """


if __name__ == '__main__':
    def schools_by_topic(mongo_collection, topic):
        """  function that returns the list of
        school having a specific topic """
        return mongo_collection.find({'topic': topic})