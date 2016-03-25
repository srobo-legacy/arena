
from __future__ import print_function

import time

from sr.robot.vision import ( Vision, C500_focal_length,
                              MARKER_TOP, MARKER_BOTTOM, MARKER_SIDE,
                              NET_A, NET_B, NET_C )

from term import print_fail, print_ok

RES = (1280,1024)

def get_net(markers):
    assert markers, "No markers to get the nets of"

    nets = set()
    for m in markers:
        nets.add(m.info.token_net)

    assert None not in nets, "Saw some non-token markers!"

    assert len(nets) == 1, "Saw more than one net: {0}.".format(', '.join(nets))

    return nets.pop()

def get_direction_to_top(marker):
    """Returns the direction from the bottom to the top of token as a
       ``WorldVector``, according to the given marker."""

    assert marker.maker_type == MARKER_SIDE, "Can't deal with top or bottom yet."

vis = Vision("/dev/video0", "../../../libkoki/lib", RES)
vis.camera_focal_length = C500_focal_length

def see():
    return vis.see('dev', 'A', RES, False)

while True:
    markers = see()

    print("I see", len(markers), "markers")

    for m in markers:
        #print(m.centre.polar, m.orientation)
        #print(m.centre.polar)
        print(m.info, m.orientation)

    net = None
    try:
        net = get_net(markers)
    except Exception as e:
        print_fail(e)
    else:
        print_ok(net)

    assert net == NET_C





    time.sleep(0.1)