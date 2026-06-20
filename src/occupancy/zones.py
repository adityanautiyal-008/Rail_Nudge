class Zone:
    """
    Represents a rectangular area in the camera view.
    """

    def __init__(self, name, x1, y1, x2, y2):
        """
        Create a new zone.

        Parameters:
            name:
                Name of the zone.

            x1, y1:
                Top-left corner.

            x2, y2:
                Bottom-right corner.
        """

        self.name = name

        # Save the rectangle coordinates
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def contains(self, point):
        """
        Check whether a point lies inside this zone.

        Parameters:
            point:
                A tuple containing (x, y).

        Returns:
            True  -> point is inside the zone.
            False -> point is outside.
        """

        x, y = point

        return (
            self.x1 <= x <= self.x2 and
            self.y1 <= y <= self.y2
        )


    def get_center(self, bbox):
        """
        Calculate the center point of a person's
        bounding box.

        We use the center point to decide whether
        a person is inside a zone.

        bbox format:
        [x1, y1, x2, y2]
        """

        x1, y1, x2, y2 = bbox

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        return (center_x, center_y)