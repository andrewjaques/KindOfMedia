Attribute VB_Name = "Module1"
Sub CreateAnalysisSheet()

    'Create worksheet "Analysis" if it doesn't exist.
    Dim wsTest As Worksheet
    Const strSheetName As String = "Analysis"
    Set wsTest = Nothing
    On Error Resume Next
    Set wsTest = ActiveWorkbook.Worksheets(strSheetName)
    On Error GoTo 0
    If wsTest Is Nothing Then
        Worksheets.Add.Name = strSheetName
    End If

    '1. Establish where output goes - Note - this requires a new sheet called Analysis
    Set Analysis = Sheets("Analysis").Range("A1")
    
    '2. Set counter for destination rows
    dindx = 0
    
    '3. Cycle through all sheets
    For Each s In Sheets
    
        '4. Test if current sheet is not "Analysis"
        If s.Name <> "Analysis" Then
        
            '5. True Case: Grab name of sheet and set as Version Under Test (user will need to prep sheet names this way when gathering data)
            versionUnderTest = s.Name
            
            '6. Find 'Test Description' in column C, set as variable rngX
            'IMPORTANT NOTE: If "Test Description" doesn't exist in column C in ANY sheet that isn't called "Analysis", this step will break.
            Dim rngX As Range
            Set rngX = Worksheets(s.Name).Range("C1:C10000").Find("Test Description", lookat:=xlPart)
            
            '7. Set source anchor
            Set srce = s.Range(rngX.Address)
            
            '10. Initialize row counter to 0
            rindx = 0
                
            '11. Loop as long as anchor cell down isn't blank. This stops the loop when there's no more data to be found.
            While srce.Offset(rindx, -1) <> ""
                
                '12. Test if not empty; if not empty populate destination with data
                If srce.Offset(rindx, cindx) <> "" Then
                    
                    '13. True Case: Output as: Test Number, Version Under Test, Test Description, Lipsync (ms), E-E Delay (ms), PSNR Bad Frames, PSNRY Average, PSNRC Average, CSNRY Average, CSNRC Average
                    Analysis.Offset(dindx, 0) = srce.Offset(rindx, -1)
                    If rindx <> 0 Then
                        Analysis.Offset(dindx, 1) = versionUnderTest
                    Else: Analysis.Offset(dindx, 1) = "Version Under Test"
                    End If
                    Analysis.Offset(dindx, 2) = srce.Offset(rindx, 0)
                    Analysis.Offset(dindx, 3) = srce.Offset(rindx, 44)
                    Analysis.Offset(dindx, 4) = srce.Offset(rindx, 48)
                    Analysis.Offset(dindx, 5) = srce.Offset(rindx, 51)
                    Analysis.Offset(dindx, 6) = srce.Offset(rindx, 60)
                    Analysis.Offset(dindx, 7) = srce.Offset(rindx, 63)
                    Analysis.Offset(dindx, 8) = srce.Offset(rindx, 66)
                    Analysis.Offset(dindx, 9) = srce.Offset(rindx, 69)
                    
                    '14. Increment destination counter (Analysis sheet)
                    dindx = dindx + 1
                    
                '15. End if statement from #12
                End If
                
                '16. Increment row index
                rindx = rindx + 1
                
            '17. End while statement from #11
            Wend
            
            '19. End if from #4
            End If
            
        '20. Go to next sheet from For loop in #3
        Next s
    
    
    'PSNR Conditional Formatting
    Dim psnrRange As Range
    Dim psnrColourScale As ColorScale
    Set psnrRange = ThisWorkbook.Sheets("Analysis").Range("G2", "J100000")
    
    'Clear any existing conditional formatting
    psnrRange.FormatConditions.Delete
    
    'Add a three colour scale for PSNR
    Set psnrColourScale = psnrRange.FormatConditions.AddColorScale(ColorScaleType:=3)
    With psnrColourScale
        'Unacceptable PSNR is coloured red
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(248, 105, 107)
            .Type = xlConditionValueNumber
            .Value = 20
        End With
        'Less than desirable PSNR is coloured yellow
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 235, 132)
            .Type = xlConditionValueNumber
            .Value = 30
        End With
        'Good desirable PSNR is coloured green
        With .ColorScaleCriteria(3)
            .FormatColor.Color = RGB(99, 190, 123)
            .Type = xlConditionValueNumber
            .Value = 40
        End With
    End With
    
    
    'Lipsync error Conditional Formatting
    Dim lipsyncRange As Range
    Dim lipsyncColourScale As ColorScale
    Set lipsyncRange = ThisWorkbook.Sheets("Analysis").Range("D2", "D100000")
    
    'Clear any existing conditional formatting
    lipsyncRange.FormatConditions.Delete
    
    'Colour scale colours and conditions
    Set lipsyncColourScale = lipsyncRange.FormatConditions.AddColorScale(ColorScaleType:=3)
    With lipsyncColourScale
        'Critical video-leads-audio lipsync error is coloured orange
        With .ColorScaleCriteria(1)
            .FormatColor.Color = RGB(237, 125, 49)
            .Type = xlConditionValueNumber
            .Value = -30
        End With
        'Desirable, close lipsync error is coloured white
        With .ColorScaleCriteria(2)
            .FormatColor.Color = RGB(255, 255, 255)
            .Type = xlConditionValueNumber
            .Value = 0
        End With
        'Critical audio-leads-video lipsync error is coloured orange
        With .ColorScaleCriteria(3)
            .FormatColor.Color = RGB(237, 125, 49)
            .Type = xlConditionValueNumber
            .Value = 10
        End With
    End With
    
    'Blank cells - indicating silent audio - are coloured blue
    On Error GoTo NoBlanks
    lipsyncRange.SpecialCells(xlCellTypeBlanks).Interior.Color = RGB(0, 176, 240)
NoBlanks:
    Resume Next
    
End Sub
