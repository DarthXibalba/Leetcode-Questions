#include <map>

using namespace std;

class Robot {
    virtual bool move();
    virtual void turnLeft();
    virtual void turnRight();
    virtual void clean();
};

class Solution {
public:
    bool roomCleaned = false;
    map<pair<int, int>, bool> room;

    void cleanRoom(Robot& robot)
    {
        mapCell(0, 0, true);
    }

    bool checkIfComplete()
    {
        bool cleaned = false;

        // TODO

        return cleaned;
    }

    void mapCell(int r, int c, bool val)
    {
        pair<int, int> coordinates(r,c);
        this->room.insert(pair<pair<int, int>, bool>(coordinates, val));
        this->roomCleaned = checkIfComplete();
    }

private:
    class RoomSize {
        int leftMin = 0;
        int rightMax = 0;
        int downMin = 0;
        int upMax = 0;
    };
};