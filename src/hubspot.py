from hubspot import HubSpot
from datetime import datetime, timedelta, timezone
from hubspot.crm.objects import PublicObjectSearchRequest
import os


class HubspotClient:
    def __init__(self):
        self.access_token = os.getenv("HUBSPOT_ACCESS_TOKEN")
        self.client = HubSpot(access_token=self.access_token)

    def get_recent_calls(self, limit=3, min_date=None):
        """Get recent calls from HubSpot with pagination support

        Args:
            limit (int): Maximum number of calls to return
            min_date (int): Minimum timestamp in milliseconds to filter from
        """
        all_calls = []
        after = None
        page_size = min(200, limit)

        if min_date:
            utc_min_date = min_date.astimezone(timezone.utc)
            utc_timestamp = int(utc_min_date.timestamp() * 1000)
            filter_timestamp = str(utc_timestamp)
            print(f"Filtering calls after timestamp: {filter_timestamp}")
            print(f"Original min_date: {min_date}")
            print(f"UTC min_date: {utc_min_date}")

        while True:
            try:
                search_request = PublicObjectSearchRequest(
                    filter_groups=[
                        {
                            "filters": [
                                {
                                    "propertyName": "hs_createdate",
                                    "operator": "GTE",
                                    "value": str(
                                        int(
                                            min_date.astimezone(
                                                timezone.utc
                                            ).timestamp()
                                            * 1000
                                        )
                                    )
                                    if min_date
                                    else "0",
                                },
                                {
                                    "propertyName": "hs_call_recording_url",
                                    "operator": "HAS_PROPERTY",
                                },
                            ]
                        }
                    ],
                    sorts=[
                        {
                            "propertyName": "hs_createdate",
                            "direction": "ASCENDING",
                        }
                    ],
                    limit=page_size,
                    after=after,
                    properties=[
                        "hs_call_recording_url",
                        "hs_call_duration",
                        "hs_call_title",
                    ],
                )

                response = self.client.crm.objects.calls.search_api.do_search(
                    public_object_search_request=search_request
                )

                all_calls.extend(response.results)

                if len(all_calls) >= limit:
                    all_calls = all_calls[:limit]
                    break

                if not response.paging or not response.paging.next.after:
                    break

                after = response.paging.next.after

            except Exception as e:
                print(f"Error getting calls from HubSpot: {str(e)}")
                break

        formatted_calls = [
            {
                "id": call.id,
                "recording_url": call.properties.get("hs_call_recording_url"),
                "title": call.properties.get("hs_call_title"),
                "created_date": call.properties.get("hs_createdate"),
            }
            for call in all_calls
        ]

        print(f"Found {len(formatted_calls)} calls")
        if formatted_calls:
            print(f"First call date: {formatted_calls[0]['created_date']}")
        return formatted_calls

    def get_latest_call(self, number=1):
        """Get most recent call from HubSpot with recording URL"""
        try:
            search_request = PublicObjectSearchRequest(
                filter_groups=[
                    {
                        "filters": [
                            {
                                "propertyName": "hs_call_recording_url",
                                "operator": "HAS_PROPERTY",
                            }
                        ]
                    }
                ],
                sorts=[
                    {
                        "propertyName": "hs_createdate",
                        "direction": "DESCENDING",
                    }
                ],
                limit=number,
                properties=[
                    "hs_call_recording_url",
                    "hs_call_duration",
                    "hs_call_title",
                    "hs_createdate",
                ],
            )
            calls = self.client.crm.objects.calls.search_api.do_search(
                public_object_search_request=search_request
            )
            if calls.results:
                formatted_calls = [
                    {
                        "id": call.id,
                        "recording_url": call.properties.get(
                            "hs_call_recording_url"
                        ),
                        "title": call.properties.get("hs_call_title"),
                        "created_date": call.properties.get("hs_createdate"),
                    }
                    for call in calls.results
                ]
                return formatted_calls
            return None
        except Exception as e:
            print(f"Error getting latest call: {str(e)}")
            return None

    def get_call_by_id(self, call_id):
        """Get a specific call from HubSpot by ID"""
        try:
            call = self.client.crm.objects.calls.basic_api.get_by_id(
                call_id,
                properties=[
                    "hs_call_recording_url",
                    "hs_call_duration",
                    "hs_call_title",
                    "hs_createdate",
                ],
            )

            if call:
                return {
                    "id": call.id,
                    "recording_url": call.properties.get(
                        "hs_call_recording_url"
                    ),
                    "title": call.properties.get("hs_call_title"),
                    "created_date": call.properties.get("hs_createdate"),
                }
            return None

        except Exception as e:
            print(f"Error getting call {call_id}: {str(e)}")
            return None
