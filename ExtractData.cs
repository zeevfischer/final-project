//author: zeev fischer 
/*
this is a data extraction class
it creats the file data4.json
the data here is a json file the data corresponds to the MyBone, SerializableFinger, and PalmArm classes any change needs to be across all files!!
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using Leap;
using Leap.Unity;
using TMPro;
using UnityEditor;
using UnityEngine.UIElements;
using UnityEngine.Playables;
using System;
using System.Linq;
using System.Text.Json;
using Palmmedia.ReportGenerator.Core.Common;

public class ExtractData : MonoBehaviour
{
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
        public Vector3 Direction;
        public Vector3 TipPosition;
        public List<MyBone> Bones = new List<MyBone>();
    }

    [System.Serializable]
    public class PalmArm
    {
        public long frameId;
        public List<SerializableFinger> fingers = new List<SerializableFinger>();
        public Vector3 PalmPosition; // The center position of the palm.
        public Vector3 PalmVelocity; // The rate of change of the palm position.
        public Vector3 WristPosition; // The position of the wrist of this hand.
        public Vector3 ElbowPosition;
    }

    // the device itself
    public LeapProvider leapProvider;
    string filePath = "data4.json";

    // Start is called before the first frame update
    private void Start()
    {
        // Uncomment the following lines if you want to delete the file on start
        // if (File.Exists(filePath))
        // {
        //     File.Delete(filePath);
        // }
    }

    // Update is called once per frame
    private void Update()
    {
        // Create a list to store the data for all fingers and palms
        List<string> handDataList = new List<string>();

        for (int i = 0; i < leapProvider.CurrentFrame.Hands.Count(); i++)
        {
            // run over all hands
            Hand cur = leapProvider.CurrentFrame.Hands[i];

            PalmArm palmArmData = new PalmArm();
            palmArmData.frameId = leapProvider.CurrentFrame.Id;
            palmArmData.PalmPosition = cur.PalmPosition;
            palmArmData.PalmVelocity = cur.PalmVelocity;
            palmArmData.WristPosition = cur.WristPosition;
            palmArmData.ElbowPosition = cur.Arm.ElbowPosition;

            for (int j = 0; j < cur.Fingers.Count(); j++)
            {
                Finger curfinger = cur.Fingers[j];
                SerializableFinger serializableFinger = new SerializableFinger
                {
                    Direction = curfinger.Direction,
                    TipPosition = curfinger.TipPosition
                };

                for (int x = 0; x < 4; x++)
                {
                    MyBone myBone = new MyBone
                    {
                        Width = curfinger.bones[x].Width,
                        Length = curfinger.bones[x].Length,
                        Center = curfinger.bones[x].Center,
                        NextJoint = curfinger.bones[x].NextJoint,
                        PrevJoint = curfinger.bones[x].PrevJoint
                    };

                    serializableFinger.Bones.Add(myBone);
                }

                palmArmData.fingers.Add(serializableFinger);
            }

            // Convert PalmArm to JSON string and add to the list
            string jsonString = JsonUtility.ToJson(palmArmData);
            handDataList.Add(jsonString);
        }

        // Write all hand data to the file outside the loop
        File.AppendAllLines(filePath, handDataList);
    }
}
