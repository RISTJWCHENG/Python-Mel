# Tool: Search And BlendShape For Curves
# Author: RIST JIANWEN CHENG
# Python Version: 3.10.8
# System: Linux
# Support: Updated as MAYA versions
# Creation Date: May 07, 2017
# Updated Date: Sep 27, 2023
# Version: 1.3




class UI_SearchAndBlendShapeForCurves:
    """
    This is a class for UI of 'Search And BlendShape For Curves'.
    """
        
    @classmethod 
    def ui_createWindow(cls, position='default'):   
        """
        Creates the UI for 'Search And BlendShape For Curves'.
        Args:
            position (str or list): Position as a list, e.g., [400, 700]. Defaults to 'default'.
        Returns:
            dict: Global dictionary 'uiSearchAndBlendShapeForCurvesOutputDic'.
        """
        
        import maya.cmds as cmds
        import os 
        import importlib  
        
        global uiSearchAndBlendShapeForCurvesOutputDic
        
        # Variable definitions.                
        variateInheritedList = ['TOOL_PARENT_MAIN_WINDOW']     
        variateNameList = ['Search_And_BlendShape_For_Curves', 'ui_searchAndBlendShapeForCurves_Presets.py'] 
        uiDefaultValueDic = {'om1Value':'is calculated automatically', 'ff1Enable':False,'ff1Value':0.0001, 'ff1Visible':False,'one':True,'multi':False, 'rbSelect':[True, False, False, 210]}
        
        # Locate preset file path.
        scriptPathStr = os.environ['MAYA_SCRIPT_PATH']
        scriptPathList = scriptPathStr.split(':')
        string = 'maya/scripts'
        for scriptPath in scriptPathList:
            if string in scriptPath:
                presetFile = variateNameList[1]
                presetFileName = presetFile.split(".")[0]
                presetFilePath = scriptPath+'/'+presetFile
                break
            else:
                presetFilePath = False
        # Load UI preset values if the file exists.
        if os.access(presetFilePath, os.F_OK):
            uiPreset = __import__(presetFileName)
            importlib.reload(uiPreset)
            uiValueDic = uiPreset.searchAndBlendShapeForCurvesPresetValueDic  
            pathResult = "The UI settings have been retrieved from the presets file: "+presetFilePath
            print(pathResult)
        else:                       
            uiValueDic = uiDefaultValueDic
        
        # Determine window position.
        if position == 'default':   
            if cmds.window(variateInheritedList[0],exists=True) == True:  
                # Retrieve the position of the parent main window.
                nHairSetupUIPosition = cmds.window(variateInheritedList[0],q=True,topLeftCorner=True) 
                # Set window postion of 'Search And BlendShape For Curves'.
                position = [nHairSetupUIPosition[0]+439, nHairSetupUIPosition[1]-382]
            else:
                position = [400,700]
        else:  
            position = position 
            
        # Ensure the 'Search And BlendShape For Curves' window does not already exist.
        windowName = variateNameList[0]                       
        if cmds.window(windowName, exists=True) == True:        
            cmds.deleteUI(windowName)
        if cmds.windowPref(windowName, exists=True):
            cmds.windowPref(windowName, remove=True) 
                    
        # Create window.    
        windowTitle = windowName.replace('_', ' ')      
        #cmds.window(windowName, q=True, widthHeight=True)
        #cmds.window(windowName, q=True, topLeftCorner=True)  
        #cmds.window(variateInheritedList[0], q=True, topLeftCorner=True)
        cmds.window(windowName, title=windowTitle, width=376, height=uiValueDic['rbSelect'][3], topLeftCorner=position, sizeable=False)   
        
        cl1 = cmds.columnLayout(adjustableColumn=True)
        mb1 = cmds.menuBarLayout()    
        m1 = cmds.menu(label='Edit', helpMenu=False)
        mi1 = cmds.menuItem(label='Save Settings', command="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('Save Settings')")
        mi2 = cmds.menuItem(label='Reset Settings', command="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('Reset Settings')")        
        m2 = cmds.menu(label='Help', helpMenu=True )
        mi3 = cmds.menuItem(label="Help on 'Search And BlendShape For Curves'", command="search_and_blendShape_for_curves.CM_searchAndBlendShapeForCurves.cm_openHelpPDF()") 
        mi4 = cmds.menuItem(label='Information', command="search_and_blendShape_for_curves.CM_searchAndBlendShapeForCurves.cm_information()" ) 
        
        cmds.separator(style='in', width=1)
        
        cl2 = cmds.columnLayout(columnAttach=('both', 2), rowSpacing=2, adjustableColumn=True)        
       
        rl1 = cmds.rowLayout(p=cl2, numberOfColumns=2)
        tf1 = cmds.textField(bgc=[0.2, 0.2, 0.2], width=290, editable=False)
        b1 = cmds.button('Base Curves', width=72, height=20, command="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('b1')")
        
        rl2 = cmds.rowLayout(p=cl2,numberOfColumns=2)
        tf2 = cmds.textField(bgc=[0.2, 0.2, 0.2], width=290, editable=False)
        b2 = cmds.button('Target Curves', width=72, height=20, command="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('b2')")
        
        cmds.separator(p=cl2, style='single', horizontal=True)
        
        rl3 = cmds.rowLayout(p=cl2, numberOfColumns=2)        
        om1 = cmds.optionMenu(label='Search radius value :', width=265, changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('om1')")
        mi4 = cmds.menuItem(label='is calculated automatically')
        mi5 = cmds.menuItem(label='is specified manually')
        cmds.optionMenu(om1, e=True, value=uiValueDic['om1Value'], backgroundColor=[0.15,0.2,0.35])
        ff1 = cmds.floatField(enable=uiValueDic['ff1Enable'], width=96, minValue=0.0001, value=uiValueDic['ff1Value'], visible=uiValueDic['ff1Visible'])
        
        cmds.separator(p=cl2, style='single', horizontal=True)
        
        rl4 = cmds.rowLayout(p=cl2, numberOfColumns=3)
        t1 = cmds.text('BlendShape node number : ', width=137)
        cb1 = cmds.checkBox('one', value=uiValueDic['one'], width=110, changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('cb1')")
        cb2 = cmds.checkBox('multi', value=uiValueDic['multi'], width=110, changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('cb2')")
        
        rl5 = cmds.rowLayout(p=cl2, numberOfColumns=3)
        t2 = cmds.text('BlendShape envelope controlled : ')
        rc1 = cmds.radioCollection()
        rb1 = cmds.radioButton(label='by default', select=uiValueDic['rbSelect'][0], changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('rb')")
        rb2 = cmds.radioButton(label='by control attribute', select=uiValueDic['rbSelect'][1], changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('rb')")
        
        rl6 = cmds.rowLayout(p=cl2, numberOfColumns=4, visible=uiValueDic['rbSelect'][2])
        b3 = cmds.button('Select', enable=True, width=47, height=20, command="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('b3')")
        tf3 = cmds.textField(p=rl6, text='', editable=True, width=153)
        om2 = cmds.optionMenu(label='.', enable=True, changeCommand="search_and_blendShape_for_curves.UI_SearchAndBlendShapeForCurves.cm_uiControl('om2')", width=160)
        mi6 = cmds.menuItem(label='Custom Attribute')
        
        cmds.separator(p=cl2, style='single', horizontal=True)
        cb3 = cmds.checkBox(p=cl2, label="Rebuild the target curve if its topology isn't the same as the base curve")
        cmds.separator(p=cl2, style='single', horizontal=True)
        
        rl7 = cmds.rowLayout(p=cl2, numberOfColumns=2)
        b4 = cmds.button('Apply', align='left', width=181, command="search_and_blendShape_for_curves.CM_searchAndBlendShapeForCurves.cm_searchAndBlendShapeForCurves()") 
        b5 = cmds.button('Cancel', align='right', width=181, command="cmds.deleteUI(uiSearchAndBlendShapeForCurvesOutputDic[0])") 
        
        cmds.showWindow(windowName) 
        
        uiSearchAndBlendShapeForCurvesOutputDic = {0:windowName, 1:tf1, 2:tf2, 3:om1, 4:ff1, 5:cb1, 6:cb2, 7:rc1, 8:rb1, 9:rb2, 10:rl6, 11:b3, 12:tf3, 13:om2, 14:mi6, 15:cb3, 16:uiDefaultValueDic, 17:presetFilePath, 18:presetFile}
        
        return uiSearchAndBlendShapeForCurvesOutputDic  


    @staticmethod
    def getSelectedCurveTransforms():
        """
        Return selected NURBS curve transform names.
    
        This method accepts both:
          - NURBS curve transform nodes
          - NURBS curve shape nodes
    
        Any other node type will be rejected.
    
        If the selection contains invalid nodes, a confirmDialog will be shown to the user.
    
        Returns:
            list[str]: A list of curve transform short names. confirmDialog for invalid selections.
        """
        
        import maya.cmds as cmds
        
        # Variable definitions.
        curveTransformList = []
        invalidList = []
        
        # Get selectedObjectList.
        selectedObjectList = cmds.ls(sl=True) or []
    
        if not selectedObjectList:
            cmds.confirmDialog(title="No Selection", message="Nothing is selected.", button=["OK"])
            return []
    
        for obj in selectedObjectList:
            if not cmds.objExists(obj):
                continue
    
            objType = cmds.objectType(obj)
    
            # If a curve SHAPE is selected.
            if objType == "nurbsCurve":
                parent = cmds.listRelatives(obj, parent=True, path=False)[0]
                curveTransformList.append(parent)
                continue
    
            # If a transform is selected.
            if objType == "transform":
                shape = cmds.listRelatives(obj, shapes=True, type="nurbsCurve")
                if shape:
                    curveTransformList.append(obj)
                else:
                    invalidList.append(obj)
                continue
    
            # Anything else is invalid.
            invalidList.append(obj)
    
        # Remove duplicates.
        curveTransformList = list(set(curveTransformList))
    
        # Show invalid selection dialog.
        info1, info2 = '', ''
        if invalidList:
            info1 = "These selected objects are NOT NURBS curves:\n\n"+"\n".join(invalidList)               
        # If result is empty
        if not curveTransformList:
            info2 = "No NURBS curves detected in your selection."
            
        if len(info1+info2) > 0:
            info = f"{info2}\n{info1}\n\nPlease only select NURBS curve transform nodes or NURBS curve shape nodes."  
            cmds.confirmDialog(title="Invalid Selection", message=info, button=["Confirm"]) 
            
        return curveTransformList, invalidList
    
    
    @classmethod
    def cm_uiControl(cls, option):      
        """
        This is a function for controling the controls on the UI. The valid values for the 'option' argument is only valid: 'tf1', 'tf2', 'b1', 'b2', 'b3', 'cb1', 'cb2', 'rb', 'om1', 'om2', 'Save Settings', 'Reset Settings'."
        """     
        
        import maya.cmds as cmds
        import os         
        
        windowName = uiSearchAndBlendShapeForCurvesOutputDic[0]
        tf1 = uiSearchAndBlendShapeForCurvesOutputDic[1]
        tf2 = uiSearchAndBlendShapeForCurvesOutputDic[2]
        om1 = uiSearchAndBlendShapeForCurvesOutputDic[3] 
        ff1 = uiSearchAndBlendShapeForCurvesOutputDic[4]
        cb1 = uiSearchAndBlendShapeForCurvesOutputDic[5]
        cb2 = uiSearchAndBlendShapeForCurvesOutputDic[6]
        rc1 = uiSearchAndBlendShapeForCurvesOutputDic[7] 
        rb1 = uiSearchAndBlendShapeForCurvesOutputDic[8] 
        rb2 = uiSearchAndBlendShapeForCurvesOutputDic[9] 
        rl6 = uiSearchAndBlendShapeForCurvesOutputDic[10]
        tf3 = uiSearchAndBlendShapeForCurvesOutputDic[12]
        om2 = uiSearchAndBlendShapeForCurvesOutputDic[13]
        uiDefaultValueDic = uiSearchAndBlendShapeForCurvesOutputDic[16] 
        presetFilePath = uiSearchAndBlendShapeForCurvesOutputDic[17]
        presetFile = uiSearchAndBlendShapeForCurvesOutputDic[18]  
        
        controlResult = ''
        
        # This is for controling the 'button' of 'b1' and 'b2' on the UI.
        if option == 'b1' or option == 'b2':
            returnValue = UI_SearchAndBlendShapeForCurves.getSelectedCurveTransforms()
            
            if len(returnValue[1]) != 0:
                return
            else:
                curveTransformList = returnValue[0]                 
                # Edit the text field based on the button.
                textValue = ",".join(f"'{x}'" for x in curveTransformList)                                                         
                tf = tf1 if option == 'b1' else tf2
                cmds.textField(tf, e=True, text=textValue)    
            
            controlResult = {option: returnValue}
            
        # This is for controling the 'button' of 'b3' on the UI.  
        elif option == 'b3': 
            selectedControllerList = cmds.ls(selection=True, type='transform')
            if not selectedControllerList:
                info = "Please select an available object."
                cmds.confirmDialog(title='NOTICE', message=info, button=['Confirm'])
                return
            
            selectedController = selectedControllerList[0]
            attrs = cmds.listAttr(selectedController, keyable=True) or []            
            longAttrList = []
            
            for attr in attrs:
                fullAttr = f"{selectedController}.{attr}"
                try:
                    attrType = cmds.getAttr(fullAttr, type=True)            
                    if attrType == "double":
                        longAttrList.append(fullAttr)            
                except:
                    pass 
                               
            if not longAttrList:
                info = "No long-type attributes found in Channel Box."
                cmds.confirmDialog(title='NOTICE', message=info, button=['Confirm'])
                return                  
            else:
                cmds.textField(tf3, e=True, text=selectedController)
                print("Found long-type attributes:")
                for a in longAttrList:
                    print("  -", a) 
                # delete menuItem(s).  
                miList = cmds.optionMenu(om2, q=True, itemListLong=True) 
                if len(miList) == 1:
                    pass
                else:
                    cmds.deleteUI(miList[1:], menuItem=True)
                # create menuItem(s).        
                for longAttr in longAttrList:   
                    attr = longAttr.split('.')[-1]                      
                    cmds.menuItem(p=om2, label=attr) 
                                               
                controlResult = [option, selectedController ,longAttrList]

        # This is for controling the 'checkBox' of 'cb1' and 'cb2' on the UI.
        elif option == 'cb1' or option == 'cb2':
            if option == 'cb1':
                cb1Value = cmds.checkBox(cb1, q=True, value=True)
                cb2Value = not cb1Value
                cmds.checkBox(cb2, e=True, value=cb2Value)
            else:
                cb2Value = cmds.checkBox(cb2, q=True, value=True)
                cb1Value = not cb2Value
                cmds.checkBox(cb1, e=True, value=cb1Value)
                   
            controlResult = [option, {'one':cb1Value, 'multi':cb2Value}]

        # This is for controling the 'radioButton' of 'rb1' and 'rb2' on the UI.
        elif option == 'rb':                                           
            rc1Selected = cmds.radioCollection(rc1, q=True, select=True)
            selectedLabel = cmds.radioButton(rc1Selected, q=True, label=True)
            if selectedLabel == 'by default':
                booleanResult = False
                cmds.window(windowName, e=True, height=210, sizeable=False)
            else:
                booleanResult = True
                cmds.window(windowName, e=True, height=234, sizeable=False)
            
            cmds.rowLayout(rl6, e=True, visible=booleanResult)    
            
            controlResult = [option, selectedLabel]   

        # This is for controling the 'optionMenu' of 'om1' on the UI.  
        elif option == 'om1':                          
            optionMenuValue = cmds.optionMenu(om1, q=True, value=True)
            if optionMenuValue == 'is calculated automatically':
                value = False
            else:
                value = True
                
            cmds.floatField(ff1, e=True, enable=value, visible=value)
            
            controlResult = [option, optionMenuValue]         
            
        # This is for controling the 'optionMenu' of 'om2' on the UI.  
        elif option == 'om2':               
            optionMenuItem = cmds.optionMenu(om2, q=True, value=True)     
            if optionMenuItem == 'Custom Attribute':   
                selectedController = cmds.textField(tf3, q=True, text=True)
                if selectedController == '':
                    message = "There is no controller has been selected."
                    cmds.confirmDialog(title='NOTICE', message=message, button=['Confirm'])
                else:
                    result = cmds.promptDialog(title='create attribute', message ='Create Attibute Name', button = ['Apply','Cancle'], defaultButton='Apply', cancelButton='Cancel', dismissString='Cancel')
                    # If Apply button is pressed, create the new attribute
                    if result == 'Apply':         
                        newAttribute = cmds.promptDialog(query=True, text=True) 
                        cmds.addAttr(selectedController, ln=newAttribute, at='double', min=0, max=1, dv=1, keyable=True)
                        cmds.menuItem(p=om2, label=newAttribute)
                        cmds.optionMenu(om2, e=True, value=newAttribute) 
                        optionMenuItem = newAttribute    
                    else:
                        print ('CANCEL')            
            else:
                pass
            
            controlResult = option+'.'+optionMenuItem   
        
        # This is for controling the 'Save Settings' on the UI.
        elif option == 'Save Settings':     
            # Get the value from the UI.
            optionMenu1Value = cmds.optionMenu(om1, q=True, value=True) 
            floatField1Enable = cmds.floatField(ff1, q=True, enable=True)
            floatField1Value = cmds.floatField(ff1, q=True, value=True)
            floatField1Visible = cmds.floatField(ff1, q=True, visible=True)
            checkBox1Value = cmds.checkBox(cb1, q=True, value=True)
            checkBox2Value = cmds.checkBox(cb2, q=True, value=True)
            rc1Selected = cmds.radioCollection(rc1, q=True, select=True)
            selectedLabel = cmds.radioButton(rc1Selected, q=True, label=True) 
            
            if selectedLabel == 'by default':
                rbSelect = [True, False, False, 167]
            else:
                rbSelect = [False, True, True, 192]
                
            uiValueDic = {'om1Value':optionMenu1Value, 'ff1Enable':floatField1Enable, 'ff1Value':floatField1Value, 'ff1Visible':floatField1Visible, 'one':checkBox1Value, 'multi':checkBox2Value, 'rbSelect':rbSelect}            
            # Save all settings.
            if presetFilePath != False:
                pyFile = open(presetFilePath,"w")
                pyFile.write('searchAndBlendShapeForCurvesPresetValueDic='+str(uiValueDic))
                pyFile.close() 
                print("The preset file have been saved in the directory: "+presetFilePath) 
            else:
                print("Couldn't find the directory for saving the preset file: "+presetFile) 
            
            controlResult = [option, uiValueDic]   
        
        # This is for controling the 'Reset Settings' on the UI.        
        elif option == 'Reset Settings':  
            # Reset all settings.
            uiValueDic = uiDefaultValueDic
            cmds.optionMenu(om1, e=True, value=uiValueDic['om1Value'])
            cmds.floatField(ff1, e=True, enable=uiValueDic['ff1Enable'], value=uiValueDic['ff1Value'], noBackground=False, visible=uiValueDic['ff1Visible'] )  
            cmds.checkBox(cb1, e=True, value=uiValueDic['one'])
            cmds.checkBox(cb2, e=True, value=uiValueDic['multi'])           
            cmds.radioButton(rb1, e=True, select=uiValueDic['rbSelect'][0])
            cmds.radioButton(rb2, e=True, select=uiValueDic['rbSelect'][1])
            cmds.window(uiSearchAndBlendShapeForCurvesOutputDic[0], e=True, height=uiValueDic['rbSelect'][3])
            cmds.rowLayout(uiSearchAndBlendShapeForCurvesOutputDic[10], e=True, visible=uiValueDic['rbSelect'][2])  
              
            if os.path.exists(presetFilePath):
                os.remove(presetFilePath)
                print("All the settings in the UI have been set to their default values.")
            else:
                pass
            
            controlResult = [option, uiValueDic]      
                                                                       
        # Parameter Ivalid.       
        else:
            message = "Parameter Invalid. The valid values for the parameter are: 'tf1', 'tf2', 'b1', 'b2', 'b3', 'cb1', 'cb2', 'rb', 'om1', 'om2', 'Save Settings', 'Reset Settings'."
            controlResult = [option, message] 
            cmds.error(message)
                
        return controlResult


class CM_searchAndBlendShapeForCurves:
    """
    Class for 'Search And BlendShape For Curves'.
    """
    
    @classmethod     
    def cm_information(cls):
        """ 
        This is a function for the information about 'Search And BlendShape For Curves'.
        """ 
        
        import maya.cmds as cmds    
       
        message='Author: RIST JIANWEN CHENG\nPython Version: 3.10.8\nSystem: Linux\nSupport: Updated as MAYA versions\nCreation Date: May 07, 2017\nUpdated Date: Sep 27, 2023\nVersion: 1.3'
        cmds.confirmDialog( title="Information", message=message, messageAlign='right', button=['CLOSE'], dismissString='CLOSE', backgroundColor=[1,1,1,] )
                            
        return message
    
    @classmethod 
    def cm_openHelpPDF(cls):
        """ 
        This is a function for opening the PDF help document about 'Search And BlendShape For Curves'.
        """ 
     
        import webbrowser
        
        url = 'https://pub-be55520ef38745d6bdd2347de9cfa440.r2.dev/Search%20And%20BlendShape%20For%20Curves_Document.pdf'
        webbrowser.open(url)
        
        return url
    
    
    @classmethod 
    def cm_calculateDistanceBetweenObjects(self,a, b):
        """
        Calculates the Euclidean distance between two objects in 3D space. The objects can be points or Maya transform nodes.
        
        Args:
            a (str): The first object, specified by its name in Maya.
            b (str): The second object, specified by its name in Maya.
        
        Returns:
            float: The calculated distance between the two objects.
                    
        Formula:    
            |Distance's ab| = √((aX-bX)^2 + (aY-bY)^2 + (aZ-bZ)^2)
        """
        import maya.cmds as cmds
        import math
        
        # Retrieves the world-space position of an object or point.
        worldPositionList = []
        for obj in [a, b]:
            if '.' in obj:
                worldPosition = cmds.pointPosition(obj, world=True)
            else:
                worldPosition = cmds.xform(obj, query=True, translation=True, worldSpace=True)
            worldPositionList.append(worldPosition)
        
        aPositionX, aPositionY, aPositionZ = worldPositionList[0]
        bPositionX, bPositionY, bPositionZ = worldPositionList[1]
        
        distance = math.sqrt( (aPositionX - bPositionX)**2 + (aPositionY - bPositionY)**2 + (aPositionZ - bPositionZ)**2 )
        
        return distance


  
    
    @classmethod      
    def cm_searchAndBlendShapeForCurves(cls):   
        """
        This function searches for the closest curves and creates blendShapes on them.
        """
        
        import maya.cmds as cmds
        import CFX.Search_And_BlendShape_For_Curves.search_and_blendShape_for_curves as search_and_blendShape_for_curves
        
        # Variable references.
        tf1 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[1]
        tf2 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[2]
        om1 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[3]
        ff1 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[4]
        cb1 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[5]
        rc1 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[7]
        tf3 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[12]
        om2 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[13]
        cb3 = search_and_blendShape_for_curves.uiSearchAndBlendShapeForCurvesOutputDic[15] 
        
        # Gather values from UI elements.        
        tf1Text = cmds.textField(tf1, q=True, text=True)
        tf2Text = cmds.textField(tf2, q=True, text=True)
        optionMenu1Value = cmds.optionMenu(om1, q=True, value=True)
        ff1Value = cmds.floatField(ff1, q=True, value=True)
        cb1Value = cmds.checkBox(cb1, q=True, value=True)
        rc1Selected = cmds.radioCollection(rc1, q=True, select=True)
        rbLabel = cmds.radioButton(rc1Selected, q=True, label=True)
        tf3Text = cmds.textField(tf3, q=True, text=True)
        optionMenu2Value = cmds.optionMenu(om2, q=True, value=True)
        cb3Value = cmds.checkBox(cb3, q=True, value=True) 
        
        # Validate the 'base curves' & 'target curves'.
        baseCurveTransformList = [x.strip("'") for x in tf1Text.split(",")]
        targetCurveTransformList = [x.strip("'") for x in tf2Text.split(",")]
        
        if not baseCurveTransformList[0]:
            print("The first element in baseCurveTransformList is empty.") 
        elif not targetCurveTransformList[0]:
            print("The first element in targetCurveTransformList is empty.")
        else:
            #1. Check whether there are any curves with the same name in baseCurveTransformList and targetCurveTransformList.
            allTransformList = cmds.ls(type="transform") or []
            allCurveTransformList = [i for i in allTransformList if cmds.listRelatives(i, shapes=True, type="nurbsCurve")]  
            allCurveFullPathList = [c for c in allCurveTransformList if '|' in c]      
            checkCurveNameList = baseCurveTransformList + targetCurveTransformList
            checkCurveFullPathList = [c for c in checkCurveNameList if '|' in c]   
            
            sameCurveNameDic ={}
            for checkCurveFullPath in checkCurveFullPathList:
                checkCurveShortName = checkCurveFullPath.split("|")[-1]
                if checkCurveShortName in sameCurveNameDic.keys():
                    continue
                for curveFullPathName in allCurveFullPathList:
                    curveShortName = curveFullPathName.split("|")[-1]
                    if checkCurveShortName == curveShortName:
                        sameCurveNameDic.setdefault(checkCurveShortName, []).append(curveFullPathName)
                                    
            if len(sameCurveNameDic) > 0:
                info = f"The following curves have the same name in the scene: {sameCurveNameDic}"
                cmds.confirmDialog(title='WARNING', message=info, button=['Confirm'])
                print(info)
                return sameCurveNameDic
            else:
                print("There are no curves with the same name in the scene.")             
            #2. Check whether any curve is included in both baseCurveTransformList and targetCurveTransformList.
            commonCurves = list(set(baseCurveTransformList) & set(targetCurveTransformList))
            if commonCurves:
                info = f"These curves appear in both 'base curves' and 'target curves' lists: {commonCurves}"
                cmds.confirmDialog(title='WARNING', message=info, button=['Confirm'])
                print(info)
                return commonCurves
            #3. Check whether more than one curves have the same base point position within either list (baseCurveTransformList / targetCurveTransformList).
            sameBaseCVPositionList = []
            for idx, curveTransformList in enumerate([baseCurveTransformList, targetCurveTransformList]):
                curveBaseCVPositionDic = {} 
                for curveTransform in curveTransformList:
                    curveShape = cmds.listRelatives(curveTransform, shapes=True, type='nurbsCurve')[0]
                    # Get the first CV of the curve in world space.
                    curveBaseCVPosition = cmds.xform(f"{curveShape}.cv[0]", query=True, worldSpace=True, translation=True)
                    # rounding to avoid float precision issues.
                    curveBaseCVPosition = tuple(round(coord, 4) for coord in curveBaseCVPosition) 
                    # Add to dictionary.
                    if curveBaseCVPosition not in curveBaseCVPositionDic:
                        curveBaseCVPositionDic[curveBaseCVPosition] = []
                    curveBaseCVPositionDic[curveBaseCVPosition].append(curveTransform)
                print(f"curveBaseCVPositionDic:\n {curveBaseCVPositionDic}")
                if idx == 0:  
                    baseCurveBaseCVPositionDic = curveBaseCVPositionDic
                else: 
                    targetCurveBaseCVPositionDic = curveBaseCVPositionDic          
            # Check for more than one curve at same position.                                
            for curvePositionDic in [baseCurveBaseCVPositionDic, targetCurveBaseCVPositionDic]:
                for position, curveList in curvePositionDic.items():
                    if len(curveList) > 1:
                        sameBaseCVPositionList.append(curveList)
            # Get the result.
            if len(sameBaseCVPositionList) > 0:
                info = f"There are more than two curves with the same base cv point position: {sameBaseCVPositionList}"
                cmds.confirmDialog(title='WARNING', message=info, button=['Confirm'])
                print(info)    
                return sameBaseCVPositionList  
            #4. Check whether the counts of baseCurveTransformList and targetCurveTransformList match and get resultDic.
            if len(baseCurveTransformList) != len(targetCurveTransformList):
                info1 = f"The count of curves in baseCurveTransformList and targetCurveTransformList is different.\n\nThere are {len(baseCurveTransformList)} base curves and {len(targetCurveTransformList)} target curves.\n\nPlease make sure they have the same number of curves."
                if len(baseCurveTransformList) < len(targetCurveTransformList):
                    info2 = f"\n\nIf you choose 'Continue according to the number of 'base curves'':\nThe process will select {len(baseCurveTransformList)} target curves out of the {len(targetCurveTransformList)} that are closest to the {len(baseCurveTransformList)} base curves."
                    result = cmds.confirmDialog(title='WARNING',message=info1+info2, button=["Continue according to the number of 'base curves'", "Stop Process"], dismissString='Stop Process')
                else:
                    info3 = f"\n\nIf you choose 'Continue according to the number of 'target curves'':\nThe process will select {len(targetCurveTransformList)} base curves out of the {len(baseCurveTransformList)} that are closest to the {len(targetCurveTransformList)} target curves."
                    result = cmds.confirmDialog(title='WARNING',message=info1+info3, button=["Continue according to the number of 'target curves'", "Stop Process"], dismissString='Stop Process')
                #
                if result == 'Stop Process':
                    print(f"\n\n{info1}\n\nUser chose to stop the process.")
                    return        
                elif result == "Continue according to the number of 'base curves'":
                    # Returns a dictionary in the form: {baseCurveTransform: {"closestTarget": targetCurveTransform, "distance": 0.0027}}.
                    resultDic = {}  
                    copyTargetCurveTransformList = targetCurveTransformList.copy()      
                    for baseCurveTransform in baseCurveTransformList:
                        distanceList = []    
                        baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]    
                        for targetCurveTransform in copyTargetCurveTransformList:     
                            targetCurveShape = cmds.listRelatives(targetCurveTransform, shapes=True, type='nurbsCurve')[0]     
                            # Compute distance.
                            distance = cls.cm_calculateDistanceBetweenObjects(f"{baseCurveShape}.cv[0]", f"{targetCurveShape}.cv[0]")       
                            distanceList.append((targetCurveTransform, distance))        
                        # Sort by distance and pick the closest.                
                        distanceList.sort(key=lambda x: (x[1], copyTargetCurveTransformList.index(x[0])))
                        closestTargetCurveTransform, closestDistance = distanceList[0]
                        # Store result.
                        resultDic[baseCurveTransform] = {'closestTarget': closestTargetCurveTransform, 'distance': closestDistance}
                        copyTargetCurveTransformList.remove(closestTargetCurveTransform)    
                    # Regenerate baseCurveTransformList & targetCurveTransformList.
                    baseCurveTransformList = list(resultDic.keys())
                    targetCurveTransformList = [subDic['closestTarget'] for subDic in resultDic.values()]                     
                else:
                    # result == "Continue according to the number of 'target curves'":
                    # Returns a dictionary in the form: {targetCurveTransform: {"closestBase": baseCurveTransform, "distance": 0.0027}}.
                    reverseResultDic = {}      
                    copyBaseCurveTransformList = baseCurveTransformList.copy()  
                    for targetCurveTransform in targetCurveTransformList:
                        distanceList = []    
                        targetCurveShape = cmds.listRelatives(targetCurveTransform, shapes=True, type='nurbsCurve')[0]    
                        for baseCurveTransform in copyBaseCurveTransformList:     
                            baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]     
                            # Compute distance.
                            distance = cls.cm_calculateDistanceBetweenObjects(f"{targetCurveShape}.cv[0]", f"{baseCurveShape}.cv[0]")       
                            distanceList.append((baseCurveTransform, distance))        
                        # Sort by distance and pick the closest.                
                        distanceList.sort(key=lambda x: (x[1], copyBaseCurveTransformList.index(x[0])))
                        closestBaseCurveTransform, closestDistance = distanceList[0]
                        # Store result.
                        reverseResultDic[targetCurveTransform] = {'closestBase': closestBaseCurveTransform, 'distance': closestDistance} 
                        copyBaseCurveTransformList.remove(closestBaseCurveTransform)  
                    # Reverse reverseResultDic.
                    resultDic = {}
                    for key, subDic in reverseResultDic.items():
                        print(key,subDic)
                        newKey = subDic['closestBase']      
                        resultDic[newKey] = {'closestTarget': key, 'distance': subDic['distance']}
                    # Regenerate baseCurveTransformList & targetCurveTransformList.
                    baseCurveTransformList = list(resultDic.keys())
                    targetCurveTransformList = [subDic['closestTarget'] for subDic in resultDic.values()]
   
            else:
                # len(baseCurveTransformList) == len(targetCurveTransformList):                
                # Returns a dictionary in the form: {baseCurveTransform: {"closestTarget": targetCurveTransform, "distance": 0.0027}}.
                resultDic = {}        
                for baseCurveTransform in baseCurveTransformList:
                    distanceList = []    
                    baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]    
                    for targetCurveTransform in targetCurveTransformList:     
                        targetCurveShape = cmds.listRelatives(targetCurveTransform, shapes=True, type='nurbsCurve')[0]     
                        # Compute distance.
                        distance = cls.cm_calculateDistanceBetweenObjects(f"{baseCurveShape}.cv[0]", f"{targetCurveShape}.cv[0]")       
                        distanceList.append((targetCurveTransform, distance))        
                    # Sort by distance and pick the closest.                
                    distanceList.sort(key=lambda x: (x[1], targetCurveTransformList.index(x[0])))
                    closestTarget, closestDistance = distanceList[0]
                    # Store result.
                    resultDic[baseCurveTransform] = {'closestTarget': closestTarget, 'distance': closestDistance}
        
        # Check whether multiple target curves share the same base curve.
        # matchCurveTransformDic = {'curve3':['curve12, 'curve17'], 'curve5':['curve1'], 'curve4':['curve8', 'curve11', 'curve20']}
        # sharedBaseCurveTransformDic = {'curve3':['curve12, 'curve17'], 'curve4':['curve8', 'curve11', 'curve20']} 
        matchCurveTransformDic = {} 
        for baseCurveTransform, value in resultDic.items():
            targetCurveTransform = value['closestTarget']
            matchCurveTransformDic.setdefault(targetCurveTransform, []).append(baseCurveTransform)           
        sharedBaseCurveTransformDic = {k: v for k, v in matchCurveTransformDic.items() if len(v) > 1}
        #
        if len(sharedBaseCurveTransformDic) > 0:
            info1 = f"There are more than two base curves sharing the same target curve:\n{sharedBaseCurveTransformDic}"
            result = cmds.confirmDialog(title='WARNING', message=info1, button=['Continue', 'Cancel'], defaultButton='Continue', cancelButton='Cancel', dismissString='Cancel')
            if result == 'Continue':
                info2 = "If 'Confirm' is clicked, it will automatically assign the closest target curve without sharing."
                result = cmds.confirmDialog(title='WARNING',message=info2,button=['Confirm', 'Cancel'],defaultButton='Continue',cancelButton='Cancel', dismissString='Cancel')
                if result == 'Confirm':
                    copyTargetCurveTransformList = targetCurveTransformList.copy()                    
                    for baseCurveTransform in baseCurveTransformList:
                        distanceList = []    
                        baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]    
                        for copyTargetCurveTransform in copyTargetCurveTransformList:     
                            copyTargetCurveShape = cmds.listRelatives(copyTargetCurveTransform, shapes=True, type='nurbsCurve')[0]     
                            # Compute distance.
                            distance = cls.cm_calculateDistanceBetweenObjects(f"{baseCurveShape}.cv[0]", f"{copyTargetCurveShape}.cv[0]")       
                            distanceList.append((copyTargetCurveTransform, distance))        
                        # Sort by distance and pick the closest.                
                        distanceList.sort(key=lambda x: (x[1], copyTargetCurveTransformList.index(x[0])))
                        closestTargetCurveTransform, closestDistance = distanceList[0]
                        # Store result.
                        resultDic[baseCurveTransform] = {'closestTarget': closestTargetCurveTransform, 'distance': closestDistance}
                        copyTargetCurveTransformList.remove(closestTargetCurveTransform)   
                else:
                    print(f"\n\n{info1}\n\nUser canceled the process.")
                    return
            else:
                print(f"\n\n{info1}\n\nUser canceled the process.")
                return
                                     
        # Check if any distance in resultDic is greater than specifyMaximumRadius.        
        if optionMenu1Value == 'is specified manually':
            specifyMaximumRadius = ff1Value
            hasTooLargeDistancelist = [baseCurve for baseCurve, info in resultDic.items() if info["distance"] > specifyMaximumRadius]
            hasTooLargeDistanceDic = {}            
            for curveName in hasTooLargeDistancelist:
                hasTooLargeDistanceDic[curveName] = resultDic[curveName]['closestTarget']                
            for baseCurveTransform in hasTooLargeDistancelist:
                resultDic.pop(baseCurveTransform, None) 
            
            print(f"\n\nAvailable distances between the 'base curves' and the 'target curves':\n{resultDic}\n\nThe following curves have distances exceeding the limit {specifyMaximumRadius}:\n{hasTooLargeDistanceDic}")

            if len(resultDic) == 0:
                info = f"Cannot find any available closest distance between the 'base curves' and the 'target curves' within the specified search radius of {specifyMaximumRadius}."
                cmds.confirmDialog(title='NOTICE', message=info, button=['Confirm']) 
                print(info)   
                return
            if len(hasTooLargeDistanceDic) > 0:                           
                info = f"Curves with distance exceeding the limit {specifyMaximumRadius}:\n{hasTooLargeDistanceDic}"
                result = cmds.confirmDialog(title='NOTICE', message=info, button=['Stop Process', 'Continue'], defaultButton='Continue', cancelButton='Stop Process', dismissString='Stop Process')
                if result == 'Stop Process':
                    print("\n\nProcess stopped by user.")
                    return
                else:
                    print("\n\nUser chose to continue.")        
        else:
            pass
        
        print("\n."*5, "\nContinue Process","\n."*5)
        print(f"{baseCurveTransformList}\n\n{targetCurveTransformList}\n\n{resultDic}")

        # Check whether the topology between the base curve and the corresponding target curve is the same for making blendShape.
        baseCurveDic = {}
        targetCurveDic = {}
        invalidTopologyCurveDic = {}
        for baseCurveTransform, value in resultDic.items():
            baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]
            baseCurveDic[baseCurveTransform] = [cmds.getAttr(f"{baseCurveShape}.spans"), cmds.getAttr(f"{baseCurveShape}.degree"), cmds.getAttr(f"{baseCurveShape}.form")]
            
            targetCurveTransform = value['closestTarget']
            targetCurveShape = cmds.listRelatives(targetCurveTransform, shapes=True, type='nurbsCurve')[0]
            targetCurveDic[targetCurveTransform] = [cmds.getAttr(f"{targetCurveShape}.spans"), cmds.getAttr(f"{targetCurveShape}.degree"), cmds.getAttr(f"{targetCurveShape}.form")]
            
            if baseCurveDic[baseCurveTransform] != targetCurveDic[targetCurveTransform]:
                invalidTopologyCurveDic[baseCurveTransform] = targetCurveTransform
        
        if len(invalidTopologyCurveDic) == 0:
            pass
        else:       
            if cb3Value == False:
                info = f"Cannot create blendShape because the following 'base curves' and 'target curves' have different topology: {invalidTopologyCurveDic}\n\nIf you insist on creating a blendShape, you can enable “Rebuild the target curve if its topology isn’t the same as the base curve” in the UI."
                cmds.confirmDialog(title='NOTICE', message=info, button=['Confirm']) 
                print(info)   
                return 
            else:
                # Rebuild the curves to ensure they have matching topology. 
                rebuiltTargetCurveTransformList = []
                for baseCurveTransform, targetCurveTransform in invalidTopologyCurveDic.items():
                    baseCurveShape = cmds.listRelatives(baseCurveTransform, shapes=True, type='nurbsCurve')[0]
                    targetCurveShape = cmds.listRelatives(targetCurveTransform, shapes=True, type='nurbsCurve')[0]
        
                    # Get base curve topology
                    spans = cmds.getAttr(f"{baseCurveShape}.spans")
                    degree = cmds.getAttr(f"{baseCurveShape}.degree")
                    form = cmds.getAttr(f"{baseCurveShape}.form")  # 0=open, 1=closed
        
                    # Rebuild target curve
                    targetCurveTransform = cmds.rebuildCurve(targetCurveTransform, ch=False, rpo=True, rt=0, end=1, kr=0, s=spans, d=degree, tol=0.01)[0]
                    if form == 1:
                        cmds.closeCurve(targetCurveTransform, replaceOriginal=True, preserveShape=True)
            
                    rebuiltTargetCurveTransformList.append(targetCurveTransform)
                    
        # Create set for base curves.  
        n=1
        while cmds.objExists('base_curve_set'+str(n)):
            n = n+1
        baseCurveSet= cmds.sets(baseCurveTransformList, name='base_curve_set'+str(n))
        # Create the blendShape envelope attributes.                                 
        if rbLabel == 'by default':
            cmds.addAttr(baseCurveSet, ln="TargetCurveEnvelope", at='double', min=0, max=1, dv=1, keyable=True)
            TargetCurveEnvelope = baseCurveSet+'.TargetCurveEnvelope'
        else:            
            TargetCurveEnvelope = tf3Text+'.'+optionMenu2Value
        
        # Create a blendShape between the 'base curve' and the 'target curve'. 
        if cb1Value == True:
            baseCurveTransformParentGroupDic = {}
            targetCurveTransformParentGroupDic = {}
            baseCurveTransformXGrp = cmds.group(empty=True, name='base_curve_grp')
            targetCurveTransformXGrp = cmds.group(empty=True, name='target_curve_grp')
            for baseCurveTransform, value in resultDic.items():
                targetCurveTransform = value['closestTarget']

                baseCurveTransformParentGroupList = cmds.listRelatives(baseCurveTransform, parent=True, fullPath=True)
                baseCurveTransformParentGroup = baseCurveTransformParentGroupList[0] if baseCurveTransformParentGroupList else None

                targetCurveTransformParentGroupList = cmds.listRelatives(targetCurveTransform, parent=True, fullPath=True)
                targetCurveTransformParentGroup = targetCurveTransformParentGroupList[0] if targetCurveTransformParentGroupList else None
     
                baseCurveTransformParentGroupDic[baseCurveTransform] = baseCurveTransformParentGroup
                targetCurveTransformParentGroupDic[targetCurveTransform] = targetCurveTransformParentGroup
                
                cmds.parent(baseCurveTransform, baseCurveTransformXGrp)
                cmds.parent(targetCurveTransform, targetCurveTransformXGrp)
            blendShapeNode = cmds.blendShape(targetCurveTransformXGrp, baseCurveTransformXGrp, name='targetCurveGrp_bs', before=True, origin='world')[0]
            cmds.setAttr(blendShapeNode+'.target_curve_grp', 1)
            cmds.connectAttr(TargetCurveEnvelope, blendShapeNode+'.envelope', f=True)                    
            for baseCurveTransform, baseCurveTransformParentGroup in baseCurveTransformParentGroupDic.items():
                targetCurveTransform = resultDic[baseCurveTransform]['closestTarget']
                targetCurveTransformParentGroup = targetCurveTransformParentGroupDic[targetCurveTransform]
                
                if baseCurveTransformParentGroup == None:
                    cmds.parent(baseCurveTransform, world=True)
                else:
                    cmds.parent(baseCurveTransform, baseCurveTransformParentGroup)
                    
                if targetCurveTransformParentGroup == None:
                    cmds.parent(targetCurveTransform, world=True)
                else:
                    cmds.parent(targetCurveTransform, targetCurveTransformParentGroup)
                                
            cmds.delete(baseCurveTransformXGrp, targetCurveTransformXGrp)
        else:
            for baseCurveTransform, value in resultDic.items():
                targetCurveTransform = value['closestTarget']
                blendShapeNode = cmds.blendShape(targetCurveTransform, baseCurveTransform, name=targetCurveTransform+'_bs', before=True, origin='world')[0]
                cmds.setAttr(blendShapeNode+'.'+targetCurveTransform, 1)
                cmds.connectAttr(TargetCurveEnvelope, blendShapeNode+'.envelope', f=True)

        return
