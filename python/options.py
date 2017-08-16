import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file',type=str, nargs='+')
parser.add_argument('--OutputName',action="store",dest="OutputName",type=str,default="Myconfig",help="Set Output file name, default is: Myconfig")
parser.add_argument('--SelectSheetNum',action="store",dest="SelectSheetNum",type=int,default=0,help="Select the Excel sheet for reading, default is: 0")
parser.add_argument('--SelectColumnX',action="store",dest="SelectColumnX",type=int,default=0,help= "Select Column number for X data, default value is 0")
parser.add_argument('--SelectColumnY',action="store",dest="SelectColumnY",type=int,default=0,help= "Select Column number for Y data, default value is 0")
parser.add_argument('--SelectRowStart',action="store",dest="SelectRowStart",type=int,default=1,help= "Select the first Row for reading, default is 1")
parser.add_argument('--SelectRowEnd',action="store",dest="SelectRowEnd",type=int,default=61,help= "Select the last Row for reading, default is 61")
parser.add_argument('--AxisNDiv',action="store",dest="AxisNDiv",type=str,default="508,510",help="Set Axis Ndivisions X,Y (default is: 508,510)")
parser.add_argument('--CanvDim',action="store",dest="CanvDim",type=str,default="1000,1000",help="Set Canvas Dimensions X,Y (default is: 1000,1000)")
parser.add_argument('--CanvDrawOpt',action="store",dest="CanvDrawOpt",type=str,default="APE1",help="Set Draw Option (default is: APE1)")
parser.add_argument('--CanvGridXY',action="store",dest="CanvGridXY",type=str,default="false,false",help="Set GridXY option (default: false,false)")
parser.add_argument('--LatexLine',action="store",dest="LatexLine",type=str,default="0.62,0.86, #splitline{LS2}{Detector~Production}",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--LatexLine1',action="store",dest="LatexLine1",type=str,default="0.62,0.27, Gas~=~CO_{2}",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--LatexLine2',action="store",dest="LatexLine2",type=str,default="",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--LatexLine3',action="store",dest="LatexLine3",type=str,default="",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--LatexLine4',action="store",dest="LatexLine4",type=str,default="",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--LatexLine5',action="store",dest="LatexLine5",type=str,default="",help= "Add Latex line, example: 0.62,0.86, #splitline{LS2}{Detector~Production}")
parser.add_argument('--CanvLegDimX',action="store",dest="CanvLegDimX",type=str,default="0.20,0.60",help="Set X Legend Dimensions") 
parser.add_argument('--CanvLegDimY',action="store",dest="CanvLegDimY",type=str,default="0.56,0.92",help="Set Y Legend Dimensions") 
parser.add_argument('--CanvLegDraw',action="store",dest="CanvLegDraw",type=str,default="true",help="Set Legend Draw Option (dedault: true)") 
parser.add_argument('--CanvLogXY',action="store",dest="CanvLogXY",type=str,default="false,false",help="Set Canvas LogXY options (default: false,false)") 
parser.add_argument('--CanvLogoPos',action="store",dest="CanvLogoPos",type=str,default="0",help="Set Logo Position (Default: 0 , Other Options: 11, 22, 33") 
parser.add_argument('--CanvLogoPrelim',action="store",dest="CanvLogoPrelim",type=str,default="true",help="Set Logo Preliminary true or false (default is true)") 
parser.add_argument('--CanvMarginTop',action="store",dest="CanvMarginTop",type=str,default="0.08",help="Set Canvas Margin Top (default is 0.08)") 
parser.add_argument('--CanvMarginBot',action="store",dest="CanvMarginBot",type=str,default="0.14",help="Set Canvas Margin Bottom (default is 0.14)") 
parser.add_argument('--CanvMarginLf',action="store",dest="CanvMarginLf",type=str,default="0.16",help="Set Canvas Margin Left (default is 0.16)") 	
parser.add_argument('--CanvMarginRt',action="store",dest="CanvMarginRt",type=str,default="0.06",help="Set Canvas Margin Right (default is 0.06)") 
parser.add_argument('--CanvPlotType',action="store",dest="CanvPlotType",type=str,default="TGraphErrors",help="Set the Canvas Plot type (default is TGraphErrors)") 
parser.add_argument('--CanvTitleX',action="store",dest="CanvTitleX",type=str,default="Divider Current #left(#muA#right)",help="Set Xaxis title, default is: Divider Current #left(#muA#right)")
parser.add_argument('--CanvTitleY',action="store",dest="CanvTitleY",type=str,default="Applied Voltage #left(kV#right)",help="Set Yaxis title, default is: Applied Voltage #left(kV#right)")
parser.add_argument('--CanvRangeX',action="store",dest="CanvRangeX",type=str,default="0,1000",help="Set the X-Range of the Canvas (default is 0,1000)") 
parser.add_argument('--CanvRangeY',action="store",dest="CanvRangeY",type=str,default="0,7",help="Set the Y-Range of the Canvas (default is 0,7)") 
parser.add_argument('--CanvTitleOffsetX',action="store",dest="CanvTitleOffsetX",type=str,default="1.0",help="Set the X-Offset of the Canvas Title (default is 1.0)") 
parser.add_argument('--CanvTitleOffsetY',action="store",dest="CanvTitleOffsetY",type=str,default="0.8",help="Set the Y-offset of the Canvas Title (default is 0.8)") 
parser.add_argument('--CanvName',action="store",dest="CanvName",type=str,default="LS2_Detectors",help="Set Canvas Name, Default is: LS2_Detectors")
parser.add_argument('--YaxisScale',dest="YaxisScale",action="store",type=str, default="false",help="If YaxisScale option is true the Y axis is plotted in kUnit. Default is: False")
parser.add_argument('--SetErrX',action="store",dest="SetErrX",type=str,default="false",help="Set ErrX option True or False , Default is: False")
parser.add_argument('--SetErrY',action="store",dest="SetErrY",type=str,default="false",help="Set ErrY option True or False , Default is: False")
parser.add_argument('--SelectColumnErrX',action="store",dest="SelectColumnErrX",type=int,default=0,help="If SetErrX=True choose the Column for XError, Default is: 0")
parser.add_argument('--SelectColumnErrY',action="store",dest="SelectColumnErrY",type=int,default=0,help="If SetErrY=True choose the Column for YError, Default is: 0")
parser.add_argument('--PlotLineSize',action="store",dest="PlotLineSize",type=str,default="1",help="Set Plot Line Size (default is: 1)")
parser.add_argument('--PlotLineStyle',action="store",dest="PlotLineStyle",type=str,default="1",help="Set Plot Line Style (default is: 1)")
parser.add_argument('--PlotMarkerSize',action="store",dest="PlotMarkerSize",type=str,default="0.8",help="Set Plot Marker Size (default is: 0.8)")
parser.add_argument('--Fit',action="store",dest="Fit",type=str,default="false",help="if true the header parameters for the fit are created")
parser.add_argument('--FitFormula',action="store",dest="FitFormula",type=str,default="[0]",help="Set the fit formula e.g. [0]*x^2+[1]")
parser.add_argument('--FitLineSize',action="store",dest="FitLineSize",type=str,default="1",help="Set Fit Line Size, default is: 1")
parser.add_argument('--FitLineStyle',action="store",dest="FitLineStyle",type=str,default="1",help="Set Fit Line Style, default is: 1")
parser.add_argument('--FitOption',action="store",dest="FitOption",type=str,default="R",help="Set Fit Option, default is: R")
parser.add_argument('--FitParamIGuess',action="store",dest="FitParamIGuess",type=str,default="0",help="Set Fit Parameters initial values")
parser.add_argument('--FitPerform',action="store",dest="FitPerform",type=str,default="true",help="if true (default) perform a fit to the TObject defined in the [BEGIN_PLOT]header this [BEGIN_FIT] header is found in")
parser.add_argument('--FitRange',action="store",dest="FitRange",type=str,default="0,1",help="Set the Fit range, default is 0,1")