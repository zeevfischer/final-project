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

public class HandDisplay : MonoBehaviour
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
        public Vector3 PalmPosition;//The center position of the palm.
        public Vector3 PalmVelocity;//The rate of change of the palm position.
        public Vector3 WristPosition;//The position of the wrist of this hand.
        public Vector3 ElbowPosition;
    }

    string filePath = "data4.json";   
    // Start is called before the first frame update
    IEnumerator Start()
    {
        while (true)
        {
            if (Input.GetKey(KeyCode.Q))
            // if (true)
            {
                Debug.Log("Pressed 'Q'");
                // Read the JSON file
                string[] jsonLines = File.ReadAllLines(filePath);
                long frameid = -1;
                Debug.Log("frame id first = " + frameid);
                // Iterate through each line in the file
                foreach (string jsonLine in jsonLines)
                {
                    // Deserialize the JSON data into PalmArm
                    PalmArm palmArmData = JsonUtility.FromJson<PalmArm>(jsonLine);
                    Debug.Log("palmarmdata = " + palmArmData);
                    if (frameid == -1)
                    {
                        frameid = palmArmData.frameId;
                    }
                    // Debug.Log("frame id = " + frameid);
                    // Debug.Log("palmArmData.frameId = " + palmArmData.frameId);
                    if (frameid != -1 && frameid != palmArmData.frameId)
                    {
                        float delay = Mathf.Max(0.02f, palmArmData.PalmVelocity.magnitude * Time.deltaTime);
                        // Debug.Log("delayed for: " + delay);
                        yield return new WaitForSeconds(delay);
                        
                        Debug.Log("deleat");
                        ClearCylinders();
                        ClearPalmAndWrist();
                        frameid = palmArmData.frameId;
                    }

                    float radios = 0.03f;
                    // Debug.Log("started creating");
                    DrawPalmAndWrist(palmArmData.PalmPosition, palmArmData.WristPosition, palmArmData.ElbowPosition, radios);

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
                    // Debug.Log("end creation");
                }

                // Delete the last hand
                ClearCylinders();
                ClearPalmAndWrist();
            }

            yield return null;
        }
    }
    private List<GameObject> cylinders = new List<GameObject>();
    private List<GameObject> spheres = new List<GameObject>();
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
        foreach (var sphere in spheres)
        {
            Destroy (sphere);
        }
        spheres.Clear();
    }
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
    private void DrawPalmAndWrist(Vector3 palmPosition, Vector3 wristPosition,Vector3 elbowposition, float ballRadius)
    {
        // Create a GameObject for the palm position
        GameObject palmObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        palmObject.transform.position = palmPosition;
        palmObject.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        palmObject.GetComponent<Renderer>().material.color = Color.green;

        spheres.Add(palmObject);

        // Create a GameObject for the wrist position
        GameObject wristObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        wristObject.transform.position = wristPosition;
        wristObject.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        wristObject.GetComponent<Renderer>().material.color = Color.blue;

        spheres.Add(wristObject);

        // Create a GameObject for the wrist position
        GameObject elbow = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        elbow.transform.position = elbowposition;
        elbow.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        elbow.GetComponent<Renderer>().material.color = Color.grey;

        spheres.Add(elbow);

        // Draw a line between wristObject and elbowObject using LineRenderer
        LineRenderer lineRenderer = wristObject.AddComponent<LineRenderer>();
        lineRenderer.material.color = Color.red;
        lineRenderer.startWidth = 0.02f;
        lineRenderer.endWidth = 0.02f;
        lineRenderer.positionCount = 2;
        lineRenderer.SetPosition(0, wristPosition);
        lineRenderer.SetPosition(1, elbowposition);
    }
    

    // Update is called once per frame
    void Update()
    {
        
    }
}