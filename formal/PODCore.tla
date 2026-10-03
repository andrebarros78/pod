------------------------------ MODULE PODCore ------------------------------
EXTENDS Naturals, Integers

CONSTANTS Workers, MaxGeneration, MaxStaleAttempts, MaxWrites

MissionStates == {
  "CREATED", "READY", "RUNNING", "VALIDATING", "MISSION_PROVEN",
  "BLOCKED_EXTERNAL", "CANCELLED", "FAILED_UNRECOVERABLE"
}

VARIABLES missionState,
          validated,
          currentLease,
          generation,
          fencingToken,
          resourceVersion,
          staleAttempts,
          deniedStaleWrites

vars == <<missionState, validated, currentLease, generation, fencingToken,
          resourceVersion, staleAttempts, deniedStaleWrites>>

Init ==
  /\ missionState = "CREATED"
  /\ validated = FALSE
  /\ currentLease = "NONE"
  /\ generation = 0
  /\ fencingToken = 0
  /\ resourceVersion = 0
  /\ staleAttempts = 0
  /\ deniedStaleWrites = 0

Prepare ==
  /\ missionState = "CREATED"
  /\ missionState' = "READY"
  /\ UNCHANGED <<validated, currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

Start ==
  /\ missionState = "READY"
  /\ missionState' = "RUNNING"
  /\ UNCHANGED <<validated, currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

Validate ==
  /\ missionState = "RUNNING"
  /\ missionState' = "VALIDATING"
  /\ validated' = TRUE
  /\ UNCHANGED <<currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

Prove ==
  /\ missionState = "VALIDATING"
  /\ validated = TRUE
  /\ missionState' = "MISSION_PROVEN"
  /\ UNCHANGED <<validated, currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

BlockExternal ==
  /\ missionState \in {"CREATED", "READY", "RUNNING", "VALIDATING"}
  /\ missionState' = "BLOCKED_EXTERNAL"
  /\ UNCHANGED <<validated, currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

Cancel ==
  /\ missionState # "MISSION_PROVEN"
  /\ missionState' = "CANCELLED"
  /\ UNCHANGED <<validated, currentLease, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

AcquireLease(w) ==
  /\ w \in Workers
  /\ currentLease = "NONE"
  /\ generation < MaxGeneration
  /\ currentLease' = w
  /\ generation' = generation + 1
  /\ fencingToken' = fencingToken + 1
  /\ UNCHANGED <<missionState, validated, resourceVersion,
                 staleAttempts, deniedStaleWrites>>

ReleaseLease(w) ==
  /\ w \in Workers
  /\ currentLease = w
  /\ currentLease' = "NONE"
  /\ UNCHANGED <<missionState, validated, generation, fencingToken,
                 resourceVersion, staleAttempts, deniedStaleWrites>>

AuthorizedWrite(w) ==
  /\ w \in Workers
  /\ currentLease = w
  /\ resourceVersion < MaxWrites
  /\ resourceVersion' = resourceVersion + 1
  /\ UNCHANGED <<missionState, validated, currentLease, generation,
                 fencingToken, staleAttempts, deniedStaleWrites>>

StaleWriteAttempt(w, token) ==
  /\ w \in Workers
  /\ token \in 0..MaxGeneration
  /\ token < fencingToken
  /\ staleAttempts < MaxStaleAttempts
  /\ staleAttempts' = staleAttempts + 1
  /\ deniedStaleWrites' = deniedStaleWrites + 1
  /\ UNCHANGED <<missionState, validated, currentLease, generation,
                 fencingToken, resourceVersion>>

Next ==
  \/ Prepare
  \/ Start
  \/ Validate
  \/ Prove
  \/ BlockExternal
  \/ Cancel
  \/ \E w \in Workers: AcquireLease(w)
  \/ \E w \in Workers: ReleaseLease(w)
  \/ \E w \in Workers: AuthorizedWrite(w)
  \/ \E w \in Workers, token \in 0..MaxGeneration: StaleWriteAttempt(w, token)

Spec == Init /\ [][Next]_vars

TypeOK ==
  /\ missionState \in MissionStates
  /\ validated \in BOOLEAN
  /\ currentLease \in Workers \cup {"NONE"}
  /\ generation \in 0..MaxGeneration
  /\ fencingToken \in 0..MaxGeneration
  /\ resourceVersion \in 0..MaxWrites
  /\ staleAttempts \in 0..MaxStaleAttempts
  /\ deniedStaleWrites \in 0..MaxStaleAttempts

MissionProvenRequiresValidation ==
  missionState = "MISSION_PROVEN" => validated = TRUE

FencingMonotonicModel == fencingToken = generation

StaleWritesAreDenied == staleAttempts = deniedStaleWrites

NoTwoLeaseHolders == currentLease \in Workers \cup {"NONE"}

=============================================================================
