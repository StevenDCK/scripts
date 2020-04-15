#!/bin/bash
declare -a g_WeightFileNameSet=(
MBperson_final.weights
MBperson_345028.weights
MBperson_320004.weights
)
g_CfgFileName=/home/dbs/mycfg/MBperson.cfg
g_WorkDirectory=/home/dbs/darknetwwd/darknet/build
g_LogFilePath=/home/dbs/logfile/evaluate
g_WeigthFilePath=/home/dbs/modelMB

g_Option="detector recallm"
g_SrcDataConfigerPath=/home1/wiwide_data/train_image
declare -a g_SrcDataSet=(
testPerson.txt
)

g_ResultFileName=$g_LogFilePath/../result_MBperson_30.txt
g_GPUIndex=1
g_Thresh=0.3

function calculateRecallAndPrecesion()
{
 EXE=$g_WorkDirectory/darknet
 WeightName=${g_WeightFileNameSet[$1]}
 WeightFileName=$g_WeigthFilePath/$WeightName
 SrcData=$g_SrcDataConfigerPath/${g_SrcDataSet[$2]}
 echo "$EXE $g_Option $SrcData $g_CfgFileName -i $g_GPUIndex $WeightFileName -thresh $g_Thresh  2>>$3" >>$3
 $EXE $g_Option $SrcData $g_CfgFileName -i $g_GPUIndex $WeightFileName -thresh $g_Thresh  2>>$3
 echo "" >>$3
}

function evaluateModel()
{
	WeightName=${g_WeightFileNameSet[$1]}
	WeightFileName=$g_WeigthFilePath/$WeightName
	echo "The evaluating results about the model of $WeightFileName" >> $g_ResultFileName 
	for((i=0;i<${#g_SrcDataSet[@]};i++))
	do
		LogFileName="$g_LogFilePath/evaluate_${WeightName%.*}_${g_SrcDataSet[$i]}"		
		calculateRecallAndPrecesion $1 $i $LogFileName
		echo "The result from data of ${g_SrcDataSet[$i]}"  >> $g_ResultFileName
		grep -a Recall $LogFileName  | tail -n 1 >> $g_ResultFileName 	
		echo "" >> $g_ResultFileName
	done

	echo "The last results are saved in file of $g_ResultFileName"
	echo ""  >> $g_ResultFileName
	echo ""  >> $g_ResultFileName
}

cd $g_WorkDirectory
for((k=0;k<${#g_WeightFileNameSet[@]};k++))
do
	evaluateModel $k
done
