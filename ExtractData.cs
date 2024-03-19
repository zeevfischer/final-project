//author: zeev fischer 
/*
this is a data extraction class
it creats the file data4.json
the data here is a json file the data corresponds to the MyBone, SerializableFinger, and PalmArm classes created in HandData.cs file
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
using System.Linq;
using System.Text.Json;
using Palmmedia.ReportGenerator.Core.Common;
using System;
using System.Timers;

public class ExtractData : MonoBehaviour
{
    // the device itself
    public LeapProvider leapProvider;
    string filePath = "data4.json";
    bool isRunning = false;
    const float timerInterval = 10f;
    bool timer_on = false;
    float timer = 0f;



    // Start is called before the first frame update
    private void Start()
    {
        // Uncomment the following lines if you want to delete the file on start
        if (File.Exists(filePath))
        {
            File.Delete(filePath);
        }
    }
    // Update is called once per frame
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            isRunning = true;
        }
        else if (Input.GetKeyDown(KeyCode.S))
        {
            isRunning = false;
        }
        else if (Input.GetKeyDown(KeyCode.T))
        {
            isRunning = true;
            timer_on = true;
            timer = 0f;
        }

        if (isRunning)
        {
            if (timer_on)
            {
                timer += Time.deltaTime;
                if (timer >= timerInterval)
                {
                    isRunning = false;
                    timer = 0f; // Reset timer
                }
                ExtractHandData();
            }
            else
            {
                ExtractHandData();
            }
        }
    }

    private void ExtractHandData()
    {
        List<string> handDataList = new List<string>();

        foreach (Hand hand in leapProvider.CurrentFrame.Hands)
        {
            PalmArm palmArmData = new PalmArm();
            palmArmData.frameId = leapProvider.CurrentFrame.Id;
            palmArmData.PalmPosition = hand.PalmPosition;
            palmArmData.PalmVelocity = hand.PalmVelocity;
            palmArmData.WristPosition = hand.WristPosition;
            palmArmData.ElbowPosition = hand.Arm.ElbowPosition;

            foreach (Finger finger in hand.Fingers)
            {
                SerializableFinger serializableFinger = new SerializableFinger
                {
                    Direction = finger.Direction,
                    TipPosition = finger.TipPosition
                };

                for (int i = 0; i < 4; i++)
                {
                    MyBone myBone = new MyBone
                    {
                        Width = finger.bones[i].Width,
                        Length = finger.bones[i].Length,
                        Center = finger.bones[i].Center,
                        NextJoint = finger.bones[i].NextJoint,
                        PrevJoint = finger.bones[i].PrevJoint
                    };

                    serializableFinger.Bones.Add(myBone);
                }

                palmArmData.fingers.Add(serializableFinger);
            }

            string jsonString = JsonUtility.ToJson(palmArmData);
            handDataList.Add(jsonString);
        }

        File.AppendAllLines(filePath, handDataList);
    }
}
