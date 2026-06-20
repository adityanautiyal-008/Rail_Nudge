class OccupancyCounter:
    """
    Tracks people entering and leaving a zone.
    """

    def __init__(self, zone):
        """
        Create a counter for one zone.

        Parameters:
            zone:
                A Zone object that defines the area.
        """

        # Store the zone we are monitoring
        self.zone = zone

        # Remember whether each track ID was
        # previously inside the zone
        self.person_states = {}

        # Current number of people inside
        self.current_count = 0


    def update(self, tracked_people):
        """
        Update occupancy information using tracked people.

        Parameters:
            tracked_people:
                List from tracker.py containing:
                track_id and bounding box.
        """

        for person in tracked_people:

            # Get the unique person ID
            track_id = person["track_id"]

            # Get the person's bounding box
            bbox = person["bbox"]

            # Find the center of the person
            center = self.zone.get_center(bbox)

            # Check if the person is inside the zone
            is_inside = self.zone.contains(center)


            # If we have never seen this ID before,
            # save its first state
            if track_id not in self.person_states:

                self.person_states[track_id] = is_inside

                if is_inside:
                    self.current_count += 1

                continue


            # Get the previous state
            was_inside = self.person_states[track_id]


            # Person entered the zone
            if not was_inside and is_inside:
                self.current_count += 1
                print(f"ID {track_id} entered {self.zone.name}")


            # Person left the zone
            elif was_inside and not is_inside:
                self.current_count -= 1
                print(f"ID {track_id} left {self.zone.name}")


            # Update the latest state
            self.person_states[track_id] = is_inside


    def get_count(self):
        """
        Return the current occupancy.
        """

        return self.current_count