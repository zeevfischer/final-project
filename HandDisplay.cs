//author: zeev fischer 
/*
this calss will read a json file note the json file coresponds to the classes Mybone and SerializableFinger all changes need to be compateble 
even in the calss cylinderFinger
it will worck only after pressing "q" !!
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
using System.Threading;

public class testreading : MonoBehaviour
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
        public Vector3 PalmPosition; //The center position of the palm.
        public Vector3 PalmVelocity; //The rate of change of the palm position.
        public Vector3 WristPosition; //The position of the wrist of this hand.
    }

    string filePath = "data4.json";

    private void ClearCylinders()
    {
        // Destroy old cylinders from the previous frame
        foreach (var cylinder in cylinders)
        {
            Destroy(cylinder);
        }

        // Clear the list
        cylinders.Clear();
    }

    private void ClearPalmAndWrist()
    {
        // Destroy the palm position object
        GameObject palmObject = GameObject.Find("PalmPosition");
        if (palmObject != null)
        {
            Destroy(palmObject);
        }

        // Destroy the wrist position object
        GameObject wristObject = GameObject.Find("WristPosition");
        if (wristObject != null)
        {
            Destroy(wristObject);
        }
    }

    // Start is called before the first frame update
    IEnumerator Start()
    {
        while (true)
        {
            if (Input.GetKey(KeyCode.Q))
            {
                // Read the JSON file
                string[] jsonLines = File.ReadAllLines(filePath);
                long frameid = -1;

                // Iterate through each line in the file
                foreach (string jsonLine in jsonLines)
                {
                    // Deserialize the JSON data into PalmArm
                    PalmArm palmArmData = JsonUtility.FromJson<PalmArm>(jsonLine);

                    if (frameid == -1)
                    {
                        frameid = palmArmData.frameId;
                    }

                    if (frameid != -1 && frameid != palmArmData.frameId)
                    {
                        yield return new WaitForSeconds(0.05f);

                        // Clear cylinders
                        ClearCylinders();

                        // Clear PalmPosition and WristPosition
                        ClearPalmAndWrist();

                        frameid = palmArmData.frameId;
                    }

                    // Draw spheres for PalmPosition and WristPosition
                    DrawPalmAndWrist(palmArmData.PalmPosition, palmArmData.WristPosition, 0.05f);

                    // Iterate through each finger in the palm
                    foreach (SerializableFinger finger in palmArmData.fingers)
                    {
                        // Iterate through each bone in the finger
                        foreach (MyBone bone in finger.Bones)
                        {
                            // Call DrawCylinder function with bone data
                            DrawCylinder(bone.PrevJoint, bone.NextJoint, bone.Width);
                        }
                    }
                }

                // Delete the last hand
                ClearCylinders();
                ClearPalmAndWrist();
            }

            yield return null;
        }
    }

    private List<GameObject> cylinders = new List<GameObject>();
    private void DrawCylinder(Vector3 start, Vector3 end, float width)
    {
        // Calculate the position of the cylinder
        Vector3 position = (start + end) / 2f;

        // Calculate the rotation of the cylinder to face the direction from start to end
        Quaternion rotation = Quaternion.FromToRotation(Vector3.up, end - start);

        // Create a GameObject for the cylinder
        GameObject cylinder = GameObject.CreatePrimitive(PrimitiveType.Cylinder);

        // Set the position and rotation of the cylinder
        cylinder.transform.position = position;
        cylinder.transform.rotation = rotation;

        // Scale the cylinder
        float distance = Vector3.Distance(start, end);
        cylinder.transform.localScale = new Vector3(width, distance / 2f, width);

        cylinders.Add(cylinder);
    }

    private void DrawPalmAndWrist(Vector3 palmPosition, Vector3 wristPosition, float radius)
    {
        // Draw the palm position as a sphere
        GameObject palmObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        palmObject.name = "PalmPosition";
        palmObject.transform.position = palmPosition;
        palmObject.transform.localScale = new Vector3(radius * 2, radius * 2, radius * 2);

        // Draw the wrist position as a sphere
        GameObject wristObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        wristObject.name = "WristPosition";
        wristObject.transform.position = wristPosition;
        wristObject.transform.localScale = new Vector3(radius * 2, radius * 2, radius * 2);
    }

    // Update is called once per frame
    void Update()
    {

    }
}
