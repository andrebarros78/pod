------------------------------ MODULE PODCore ------------------------------
EXTENDS Naturals, Integers, FiniteSets

CONSTANTS Workers, MaxGeneration, MaxStaleAttempts, MaxWrites

MissionStates == {
  "CREATED", "READY", "RUNNING", "VALIDATING", "MISSION_PROVEN",
  "BLOCKED_EXTERNAL", "CANCELLED", "FAILED_UNRECOVERABLE"
}

VARIABLES missionState,
          evidenceComplete,
          acceptancePass,
          regressionPass,
          checkpointPresent,
          securityGatePass,
          privacyGateApplicable,
          privacyGatePass,
          sensitiveDataGateApplicable,
          sensitiveDataGatePass,
          recoveryPass,
          donorDecouplingPass,
          projectIsolationPass,
          proofVerdictFresh,
          currentLease,
          generation,
          fencingToken,
          workerToken,
          resourceVersion,
          staleAttempts,
          deniedStaleWrites

vars == <<
  missionState,
  evidenceComplete,
  acceptancePass,
  regressionPass,
  checkpointPresent,
  securityGatePass,
  privacyGateApplicable,
  privacyGatePass,
  sensitiveDataGateApplicable,
  sensitiveDataGatePass,
  recoveryPass,
  donorDecouplingPass,
  projectIsolationPass,
  proofVerdictFresh,
  currentLease,
  generation,
  fencingToken,
  workerToken,
  resourceVersion,
  staleAttempts,
  deniedStaleWrites
>>

Init ==
  /\ missionState = "CREATED"
  /\ evidenceComplete = FALSE
  /\ acceptancePass = FALSE
  /\ regressionPass = FALSE
  /\ checkpointPresent = FALSE
  /\ securityGatePass = FALSE
  /\ privacyGateApplicable = FALSE
  /\ privacyGatePass = FALSE
  /\ sensitiveDataGateApplicable = FALSE
  /\ sensitiveDataGatePass = FALSE
  /\ recoveryPass = FALSE
  /\ donorDecouplingPass = FALSE
  /\ projectIsolationPass = FALSE
  /\ proofVerdictFresh = FALSE
  /\ currentLease = "NONE"
  /\ generation = 0
  /\ fencingToken = 0
  /\ workerToken = [w \in Workers |-> 0]
  /\ resourceVersion = 0
  /\ staleAttempts = 0
  /\ deniedStaleWrites = 0

Prepare ==
  /\ missionState = "CREATED"
  /\ missionState' = "READY"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

Start ==
  /\ missionState = "READY"
  /\ missionState' = "RUNNING"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

RecordEvidence ==
  /\ missionState = "RUNNING"
  /\ ~evidenceComplete
  /\ evidenceComplete' = TRUE
  /\ UNCHANGED << missionState, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassAcceptance ==
  /\ missionState = "RUNNING"
  /\ ~acceptancePass
  /\ acceptancePass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassRegression ==
  /\ missionState = "RUNNING"
  /\ ~regressionPass
  /\ regressionPass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

CreateCheckpoint ==
  /\ missionState = "RUNNING"
  /\ ~checkpointPresent
  /\ checkpointPresent' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassSecurity ==
  /\ missionState = "RUNNING"
  /\ ~securityGatePass
  /\ securityGatePass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

RequirePrivacy ==
  /\ missionState = "RUNNING"
  /\ ~privacyGateApplicable
  /\ privacyGateApplicable' = TRUE
  /\ privacyGatePass' = FALSE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassPrivacy ==
  /\ missionState = "RUNNING"
  /\ privacyGateApplicable
  /\ ~privacyGatePass
  /\ privacyGatePass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

RequireSensitiveDataGate ==
  /\ missionState = "RUNNING"
  /\ ~sensitiveDataGateApplicable
  /\ sensitiveDataGateApplicable' = TRUE
  /\ sensitiveDataGatePass' = FALSE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      recoveryPass, donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassSensitiveDataGate ==
  /\ missionState = "RUNNING"
  /\ sensitiveDataGateApplicable
  /\ ~sensitiveDataGatePass
  /\ sensitiveDataGatePass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, recoveryPass, donorDecouplingPass,
      projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassRecovery ==
  /\ missionState = "RUNNING"
  /\ ~recoveryPass
  /\ recoveryPass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, donorDecouplingPass,
      projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassDonorDecoupling ==
  /\ missionState = "RUNNING"
  /\ ~donorDecouplingPass
  /\ donorDecouplingPass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

PassProjectIsolation ==
  /\ missionState = "RUNNING"
  /\ ~projectIsolationPass
  /\ projectIsolationPass' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

ProofPrerequisites ==
  /\ evidenceComplete
  /\ acceptancePass
  /\ regressionPass
  /\ checkpointPresent
  /\ securityGatePass
  /\ recoveryPass
  /\ donorDecouplingPass
  /\ projectIsolationPass
  /\ (~privacyGateApplicable \/ privacyGatePass)
  /\ (~sensitiveDataGateApplicable \/ sensitiveDataGatePass)

EnterValidation ==
  /\ missionState = "RUNNING"
  /\ ProofPrerequisites
  /\ missionState' = "VALIDATING"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

IssueFreshVerdict ==
  /\ missionState = "VALIDATING"
  /\ ProofPrerequisites
  /\ ~proofVerdictFresh
  /\ proofVerdictFresh' = TRUE
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

Prove ==
  /\ missionState = "VALIDATING"
  /\ ProofPrerequisites
  /\ proofVerdictFresh
  /\ missionState' = "MISSION_PROVEN"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

BlockExternal ==
  /\ missionState \in {"CREATED", "READY", "RUNNING", "VALIDATING"}
  /\ missionState' = "BLOCKED_EXTERNAL"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

Cancel ==
  /\ missionState # "MISSION_PROVEN"
  /\ missionState' = "CANCELLED"
  /\ UNCHANGED << evidenceComplete, acceptancePass, regressionPass, checkpointPresent,
      securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

AcquireLease(w) ==
  /\ w \in Workers
  /\ currentLease = "NONE"
  /\ generation < MaxGeneration
  /\ currentLease' = w
  /\ generation' = generation + 1
  /\ fencingToken' = fencingToken + 1
  /\ workerToken' = [workerToken EXCEPT ![w] = fencingToken + 1]
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      resourceVersion, staleAttempts, deniedStaleWrites >>

ReleaseLease(w) ==
  /\ w \in Workers
  /\ currentLease = w
  /\ currentLease' = "NONE"
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      generation, fencingToken, workerToken,
      resourceVersion, staleAttempts, deniedStaleWrites >>

AuthorizedWrite(w) ==
  /\ w \in Workers
  /\ currentLease = w
  /\ workerToken[w] = fencingToken
  /\ resourceVersion < MaxWrites
  /\ resourceVersion' = resourceVersion + 1
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken,
      staleAttempts, deniedStaleWrites >>

StaleWriteAttempt(w) ==
  /\ w \in Workers
  /\ workerToken[w] < fencingToken
  /\ staleAttempts < MaxStaleAttempts
  /\ staleAttempts' = staleAttempts + 1
  /\ deniedStaleWrites' = deniedStaleWrites + 1
  /\ UNCHANGED << missionState, evidenceComplete, acceptancePass, regressionPass,
      checkpointPresent, securityGatePass, privacyGateApplicable, privacyGatePass,
      sensitiveDataGateApplicable, sensitiveDataGatePass, recoveryPass,
      donorDecouplingPass, projectIsolationPass, proofVerdictFresh,
      currentLease, generation, fencingToken, workerToken, resourceVersion >>

Next ==
  \/ Prepare
  \/ Start
  \/ RecordEvidence
  \/ PassAcceptance
  \/ PassRegression
  \/ CreateCheckpoint
  \/ PassSecurity
  \/ RequirePrivacy
  \/ PassPrivacy
  \/ RequireSensitiveDataGate
  \/ PassSensitiveDataGate
  \/ PassRecovery
  \/ PassDonorDecoupling
  \/ PassProjectIsolation
  \/ EnterValidation
  \/ IssueFreshVerdict
  \/ Prove
  \/ BlockExternal
  \/ Cancel
  \/ \E w \in Workers: AcquireLease(w)
  \/ \E w \in Workers: ReleaseLease(w)
  \/ \E w \in Workers: AuthorizedWrite(w)
  \/ \E w \in Workers: StaleWriteAttempt(w)

Spec == Init /\ [][Next]_vars

AuthorizedWorkers ==
  {w \in Workers : currentLease = w /\ workerToken[w] = fencingToken}

TypeOK ==
  /\ missionState \in MissionStates
  /\ evidenceComplete \in BOOLEAN
  /\ acceptancePass \in BOOLEAN
  /\ regressionPass \in BOOLEAN
  /\ checkpointPresent \in BOOLEAN
  /\ securityGatePass \in BOOLEAN
  /\ privacyGateApplicable \in BOOLEAN
  /\ privacyGatePass \in BOOLEAN
  /\ sensitiveDataGateApplicable \in BOOLEAN
  /\ sensitiveDataGatePass \in BOOLEAN
  /\ recoveryPass \in BOOLEAN
  /\ donorDecouplingPass \in BOOLEAN
  /\ projectIsolationPass \in BOOLEAN
  /\ proofVerdictFresh \in BOOLEAN
  /\ currentLease \in Workers \cup {"NONE"}
  /\ generation \in 0..MaxGeneration
  /\ fencingToken \in 0..MaxGeneration
  /\ workerToken \in [Workers -> 0..MaxGeneration]
  /\ resourceVersion \in 0..MaxWrites
  /\ staleAttempts \in 0..MaxStaleAttempts
  /\ deniedStaleWrites \in 0..MaxStaleAttempts

MissionProvenRequiresCompleteProof ==
  missionState = "MISSION_PROVEN" =>
    /\ ProofPrerequisites
    /\ proofVerdictFresh

PrivacyCannotBeBypassedWhenApplicable ==
  missionState = "MISSION_PROVEN" =>
    (~privacyGateApplicable \/ privacyGatePass)

SensitiveDataGateCannotBeBypassedWhenApplicable ==
  missionState = "MISSION_PROVEN" =>
    (~sensitiveDataGateApplicable \/ sensitiveDataGatePass)

FencingTokenTracksGeneration ==
  fencingToken = generation

AtMostOneAuthorizedWriter ==
  Cardinality(AuthorizedWorkers) <= 1

StaleWritesAreDenied ==
  staleAttempts = deniedStaleWrites

=============================================================================
