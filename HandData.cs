using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class MyBone
{
    public float Width;
    public float Length;
    public Vector3 Center;
    public Vector3 NextJoint;
    public Vector3 PrevJoint;
}

[System.Serializable]
public class SerializableFinger
{
    public long frameId;
    public Vector3 Direction;
    public Vector3 TipPosition;
    public List<MyBone> Bones = new List<MyBone>();
}

[System.Serializable]
public class PalmArm
{
    public List<SerializableFinger> fingers = new List<SerializableFinger>();
    public Vector3 PalmPosition;
    public Vector3 PalmVelocity;
    public Vector3 WristPosition;
}